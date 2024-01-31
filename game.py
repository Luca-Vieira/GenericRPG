import random

class Attributes:
    def __init__(self, name, maxHealth, maxMana, damage, critPercentage, maxDefense, skill, level, evasion):
        self.name = name
        self.maxHealth = maxHealth
        self.maxMana = maxMana
        self.damage = damage
        self.critPercentage = critPercentage
        self.maxDefense = maxDefense
        self.skill = skill
        self.level = level
        self.evasion = evasion

class Enemy(Attributes):
    def __init__(self, name, health, maxHealth, mana, maxMana, damage, critPercentage, defense, maxDefense, level, skill, evasion, isAlive):
        super().__init__(name, maxHealth, maxMana, damage, critPercentage, maxDefense, skill, level, evasion)
        self.health = health
        self.mana = mana
        self.defense = defense
        self.skills = skill
        self.isAlive = isAlive
    
    def basicEnemyAttack(self, player):
        trueDamage = self.damage
        print("=------------------------------------------------------------=")
        print("The monster attacks you.")
        if player.evasion >= random.randint(100,200)/100:
            print("+------------------------------------------------------------+")
            return print("The monster missed.\n")
        if self.critPercentage  > random.randint(100,200)/100:
           trueDamage = trueDamage * self.critPercentage
           print("+------------------------------------------------------------+")
           print("You received critical damage.")
        player.defense = player.defense - trueDamage
        if player.defense >= 0:
            print("+------------------------------------------------------------+")
            return print(f"Your health: {player.health}/{player.maxHealth}\nYour Defense:  {player.defense}/{player.maxDefense}\n")
        else:
            player.health = player.health + player.defense
            player.defense = 0
            if player.health <= 0:
                player.isAlive = False
                print("+------------------------------------------------------------+")
                return print(f"You are dead.\n+------------------------------------------------------------+\nYour health: 0/{player.maxHealth}\nYour Defense:  {player.defense}/{player.maxDefense}\n")
            else:
                print("+------------------------------------------------------------+")
                return  print(f"Your health: {player.health}/{player.maxHealth}\nYour Defense:  {player.defense}/{player.maxDefense}\n")

    
class Player(Attributes):
    def __init__(self, name, health, maxHealth, mana, maxMana, damage, critPercentage, luck, defense, maxDefense, level, class_, equipment, skill, evasion, isAlive):
        super().__init__(name, maxHealth, maxMana, damage, critPercentage, maxDefense, skill, level, evasion)
        self.class_ = class_
        self.health = health
        self.mana = mana
        self.luck = luck
        self.defense = defense
        self.equipment = equipment
        self.isAlive = isAlive

    def basicPlayerAttack(self, enemy: Enemy):
        trueDamage = self.damage
        print("=------------------------------------------------------------=")
        print("You attack the monster.")
        if enemy.evasion >= random.randint(100,200)/100:
            print("+------------------------------------------------------------+")
            return print("You Missed\n")
        if self.luck  > random.randint(100,200)/100:
           trueDamage = self.damage * self.luck 
           print("+------------------------------------------------------------+")
           print("The luck is on your side")
        if self.critPercentage  > random.randint(100,200)/100:
           trueDamage = trueDamage * self.critPercentage
           print("+------------------------------------------------------------+")
           print("You got a critical hit")
        enemy.defense = enemy.defense - trueDamage
        if enemy.defense >= 0:
            print("+------------------------------------------------------------+")
            return print(f"Enemy Health: {enemy.health}/{enemy.maxHealth}\nEnemy Defense:  {enemy.defense}/{enemy.maxDefense}\n")
        else:
            enemy.health = enemy.health + enemy.defense
            enemy.defense = 0
            if enemy.health <= 0:
                enemy.isAlive = False
                print("+------------------------------------------------------------+")
                return print(f"The enemy is dead.\n+------------------------------------------------------------+\nEnemy Health: 0/{enemy.maxHealth}\nEnemy Defense:  {enemy.defense}/{enemy.maxDefense}\n")
            else:
                print("+------------------------------------------------------------+")
                return  print(f"Enemy Health: {enemy.health}/{enemy.maxHealth}\nEnemy Defense:  {enemy.defense}/{enemy.maxDefense}\n")
        
        
                   


if __name__ == "__main__":
    player = Player("carlos",100,100,100,100,50,1.4,1.11,50,50,1,"Guerreiro",[],[],1.1, True)
    inimigo = Enemy("goblin", 100, 100, 100, 100, 50, 1.4, 50, 50, 1, [], 1.1, True)
    
    
    while player.isAlive and inimigo.isAlive:
        if player.isAlive:    
            player.basicPlayerAttack(inimigo)
        if inimigo.isAlive:
            inimigo.basicEnemyAttack(player)
            
    