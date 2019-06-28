import random

class Player:
  def __init__(self, name, playerType, gender):
    self.name = name
    self.playerType = playerType
    self.gender = gender
    self.offensiveStrength = 35
    self.defensiveStrength = 35
    # self.experience = 1
    self.hitPoints = 90
    self.alive = True
    
    if self.playerType == "sorcerer":
      self.offensiveStrength += 20
    if self.playerType == "mage":
      self.defensiveStrength += 20
      
    if self.gender == "male":
      self.pronoun = "He is"
    if self.gender == "female":
      self.pronoun = "She is"
    if self.gender == "neutral":
      self.pronoun = "They are"
    
    # print("You created a new player named %s!  %s is a %s. %s ready to kick some monster-butt!" % (self.name, self.name, self.playerType, self.pronoun))
    


class Enemy:
  def __init__(self, enemyNumber, name, offensiveStrength, defensiveStrength, hitPoints):
    self.enemyNumber = enemyNumber + 1
    self.name = name
    self.offensiveStrength = offensiveStrength
    self.defensiveStrength = defensiveStrength
    self.hitPoints = hitPoints
    self.alive = True


def createEnemies():
  enemyNames = ["Armored Knight", "Axe Knight", "Blue Dragon", "Demon Knight", "Drakee", "Drakeema", "Droll", "Drollmagi", "Druin", "Druinlord", "Ghost", "Goldman", "Golem", "Green Dragon", "Knight", "Magician", "Magidrakee", "Magiwyvern", "Metal Scorpion", "Metal Slime", "Poltergeist", "Red Dragon", "Red Slime", "Scorpion", "Skeleton", "Slime", "Stoneman", "Warlock", "Werewolf", "Wizard", "Wolf", "Wolflord", "Wraith", "Wraith Knight", "Wyvern"]
  enemiesList = []
  enemiesBasicList = []
  enemiesDict = {}
  enemiesAlive = 0
  # enemyStringInfo = []
  for newEnemyNumber in range(7):
    randomName = random.choice(enemyNames)
    enemyNames.remove(randomName)
    enemyOffense = random.randint(35,85)
    enemyDefense = random.randint(25,75)
    enemyHitPoints = random.randint(40,90)
    enemiesList.append(Enemy(newEnemyNumber, randomName, enemyOffense, enemyDefense, enemyHitPoints))
    enemiesAlive += 1
    
  for enemy in enemiesList:
      if (enemy.alive == True):
        enemiesDict[enemy.name] = [enemy.offensiveStrength, enemy.defensiveStrength, enemy.hitPoints]
        enemiesBasicList.append([enemy.name, enemy.offensiveStrength, enemy.defensiveStrength, enemy.hitPoints, enemy.alive])
        
        # enemyStringInfo.append(str(enemy.enemyNumber) + ". " + enemy.name + " ... Offense: " + str(enemy.offensiveStrength) + " ... Defense: " + str(enemy.defensiveStrength) + " ... Hit Points: " + str(enemy.hitPoints))
  # print(enemiesBasicList)
  return enemiesBasicList
    


dictOfPlayers = {}

def makePlayer(formInfo):
  player = Player(formInfo["firstName"], formInfo["wizard"], formInfo["gender"])
  print(vars(player))
  playerName = formInfo["firstName"]
  if playerName not in dictOfPlayers:
    # print(formInfo)
    enemies = createEnemies()
    dictOfPlayers[formInfo["firstName"]] = [formInfo["wizard"], formInfo["gender"], enemies, vars(player)]
    


def calcPlayerStrike(playerOffense, enemyDefense, enemyHitPoints):
  effectiveOffense = playerOffense - enemyDefense
  calcRandomRange = random.randint(-8, 20)
  effectiveOffense = effectiveOffense + calcRandomRange
  if effectiveOffense > 0:
    newHitPointNumber = enemyHitPoints - effectiveOffense
  else:
    newHitPointNumber = enemyHitPoints
  return newHitPointNumber
  
def calcEnemyStrike(enemyOffense, playerDefense, playerHitPoints):
  effectiveOffense = enemyOffense - playerDefense
  calcRandomRange = random.randint(-8, 20)
  effectiveOffense = effectiveOffense + calcRandomRange
  if effectiveOffense > 0:
    newHitPointNumber = playerHitPoints - effectiveOffense
  else:
    newHitPointNumber = playerHitPoints
  return newHitPointNumber
  
  
def checkIfPlayerAlive(player):
  if player[3]["hitPoints"] > 0:
    print("PLAYER ALIVE")
    return True
  else:
    print("PLAYER DEAD")
    dictOfPlayers[player[3]["name"]][3]["alive"] = False
    return False
    
def checkIfEnemyAlive(player, enemyNumber):
  if player[2][enemyNumber][3] > 0:
    print("ENEMY ALIVE")
    return True
  else:
    print("ENEMY DEAD")
    dictOfPlayers[player[3]["name"]][2][enemyNumber][4] = False
    return False
    
def hitPointBoost(player):
  if player[3]["hitPoints"] < 65:
    player[3]["hitPoints"] += 30
    return True
    
def strengthBoost(player):
  # dictOfPlayers[player[3]["offensiveStrength"]] += 7
  # dictOfPlayers[player[3]["defensiveStrength"]] += 7
  print("BOOST!")
  dictOfPlayers[player[3]["name"]][3]["offensiveStrength"] += 7
  dictOfPlayers[player[3]["name"]][3]["defensiveStrength"] += 7