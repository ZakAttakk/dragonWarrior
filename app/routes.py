from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/rules', methods = ["GET", "POST"])
def showRules():
    if request.method == "GET":
        return "Please use the form."
    else:
        # return "Got it."
        # userdata = request.form
        userData = formopener.dict_from(request.form)
        # print(userData)
        model.makePlayer(userData);
        # return "Got it"
        global name
        name = userData["firstName"]
        wizard = userData["wizard"].capitalize()
        enemies = model.createEnemies()
        return render_template("rules.html", name = name, wizard = wizard)
    
    
@app.route('/enemies', methods = ["GET", "POST"])
def getEnemies():
    if request.method == "GET":
        return "Please use the form."
    else:
        playerId = request.args.get("id")
        player = model.dictOfPlayers[playerId]
        hitPointBoost = model.hitPointBoost(player);
        # model.strengthBoost(player)
        
        # print(player)
        return render_template("enemies.html", enemies = player[2], name = playerId, player = player, hitPointBoost = hitPointBoost)
        

@app.route('/enemy', methods = ["GET", "POST"])
def showEnemy():
    playerId = request.args.get('id')
    player = model.dictOfPlayers[playerId]
    playerStats = player[3]
    print(player)
    enemyNumber = int(request.args.get('number'))
    enemy = player[2][enemyNumber]
    enemyFileName = player[2][enemyNumber][0].replace(" ", "_")
    
    playerAlive = model.checkIfPlayerAlive(player)
    enemyAlive = model.checkIfEnemyAlive(player, enemyNumber)
    

    
    oldEnemyHitPoints = enemy[3]
    if enemyAlive and playerAlive:
        newEnemyHitPoints = model.calcPlayerStrike(playerStats["offensiveStrength"], enemy[2], enemy[3])
    else:
        newEnemyHitPoints = oldEnemyHitPoints
    model.dictOfPlayers[playerId][2][enemyNumber][3] = newEnemyHitPoints
    
    playerAlive = model.checkIfPlayerAlive(player)
    enemyAlive = model.checkIfEnemyAlive(player, enemyNumber)
    
    # print(enemyAlive)
    if not enemyAlive:
        print("PLAYER BOOST!")
        model.strengthBoost(player)
    
    oldPlayerHitPoints = playerStats["hitPoints"]
    if playerAlive and enemyAlive:
        newPlayerHitPoints = model.calcEnemyStrike(enemy[1], playerStats["defensiveStrength"], playerStats["hitPoints"])
    else:
        newPlayerHitPoints = oldPlayerHitPoints
    model.dictOfPlayers[playerId][3]["hitPoints"] = newPlayerHitPoints 
    
    playerAlive = model.checkIfPlayerAlive(player)
    enemyAlive = model.checkIfEnemyAlive(player, enemyNumber)
        
    enemyHitPointDifference = oldEnemyHitPoints - newEnemyHitPoints
    playerHitPointDifference = oldPlayerHitPoints - newPlayerHitPoints
    
    
    # print("PLAYER STATS: ", playerStats)
    # print("ENEMY:", enemy)
    # print("OLD ENEMY HIT POINTS:", oldEnemyHitPoints)
    # print("NEW ENEMY HIT POINTS:", newEnemyHitPoints)
    
    # print("OLD PLAYER HIT POINTS:", oldPlayerHitPoints)
    # print("NEW PLAYER HIT POINTS:", newPlayerHitPoints)
    
    
    return render_template("enemy.html", enemy = enemy, enemyFileName = enemyFileName, enemyNumber = enemyNumber, playerStats = playerStats, newEnemyHitPoints = newEnemyHitPoints, newPlayerHitPoints = newPlayerHitPoints, enemyHitPointDifference = enemyHitPointDifference, playerHitPointDifference = playerHitPointDifference, playerAlive = playerAlive, enemyAlive = enemyAlive, name = playerId)
    
@app.route('/fight', methods = ["GET", "POST"])
def fight():
    print("fight")
    
@app.route('/run', methods = ["GET", "POST"])
def run():
    print("run")