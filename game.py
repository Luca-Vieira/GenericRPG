import random

class Attributes:
    def __init__(self, name):
        self.name = name
        self.maxHealth = 0
        self.maxMana = 0
        self.damage = 0
        self.critPercentage = 0
        self.maxDefense = 0
        self.level = 1
        self.evasion = 0
        self.luck = 0
        self.health = 0
        self.mana = 0
        self.defense = 0
        self.isAlive = True
        self.isStun = False
        self.equipment = []
        self.items = []
    
    def setStatus(self):
        self.maxHealth = random.randint(100, 120)
        self.health = self.maxHealth
        self.maxMana = random.randint(30, 50)
        self.mana = self.maxMana
        self.damage = random.randint(20, 30)
        self.critPercentage = random.randint(100, 110) / 100
        self.luck = random.randint(100, 110) / 100
        self.maxDefense = random.randint(50, 70)
        self.defense = self.maxDefense
        self.evasion = random.randint(100, 110) / 100
    
    def mostrar_atributos(self):
        for atributo, valor in self.__dict__.items():
            print(f"{atributo}: {valor}")
    
    def basicAttack(self, enemy):
        trueDamage = self.damage
        print("=------------------------------------------------------------=")
        print(f"{self.name} attacks {enemy.name}.")
        if enemy.evasion >= random.randint(100,200)/100:
            print("+------------------------------------------------------------+")
            return print(f"{self.name} Missed.\n")
        if self.luck  > random.randint(100,200)/100:
           trueDamage = self.damage * self.luck 
           print("+------------------------------------------------------------+")
           print(f"The luck is on {self.name}'s side.")
        if self.critPercentage  > random.randint(100,200)/100:
           trueDamage = trueDamage * self.critPercentage
           print("+------------------------------------------------------------+")
           print(f"{self.name} did critical Damage.")
        enemy.defense = enemy.defense - trueDamage
        if enemy.defense >= 0:
            print("+------------------------------------------------------------+")
            return print(f"{enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
        else:
            enemy.health = enemy.health + enemy.defense
            enemy.defense = 0
            if enemy.health <= 0:
                enemy.isAlive = False
                print("+------------------------------------------------------------+")
                return print(f"{enemy.name} is dead.\n+------------------------------------------------------------+\n{enemy.name}'s Health: 0/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
            else:
                print("+------------------------------------------------------------+")
                return  print(f"{enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")

class Warrior(Attributes):

    def infusedSword(self,enemy):
        self.mana -= 15
        self.critPercentage += 0.03 * self.level
        trueDamage = self.damage + (20 * self.level)
        print("=------------------------------------------------------------=")
        print(f"{self.name} attacks {enemy.name} with an infused blade.")
        if enemy.evasion >= random.randint(100,200)/100:
            print("+------------------------------------------------------------+")
            return print(f"{self.name} Missed.\n")
        if self.luck  > random.randint(100,200)/100:
           trueDamage = self.damage * self.luck 
           print("+------------------------------------------------------------+")
           print(f"The luck is on {self.name}'s side.")
        if self.critPercentage  > random.randint(100,200)/100:
           trueDamage = trueDamage * self.critPercentage
           print("+------------------------------------------------------------+")
           print(f"{self.name} did critical Damage.")
        enemy.defense = enemy.defense - trueDamage
        if enemy.defense >= 0:
            print("+------------------------------------------------------------+")
            return print(f"{enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
        else:
            enemy.health = enemy.health + enemy.defense
            enemy.defense = 0
            if enemy.health <= 0:
                enemy.isAlive = False
                print("+------------------------------------------------------------+")
                return print(f"{enemy.name} is dead.\n+------------------------------------------------------------+\n{enemy.name}'s Health: 0/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
            else:
                print("+------------------------------------------------------------+")
                return  print(f"{enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
        
    def ironSkin(self):
        self.armor += 30 * self.level
        self.mana -= 15
    
    def warCry(self, enemy):
        self.mana -= 20
        enemy.defense -= 10 * self.level
        if enemy.defense < 0:
            enemy.defense = 0
        if self.luck * self.level > random.randint(100,200)/100:
            self.critPercentage += 1.05 * self.level
            enemy.damage -= 5 * self.level
            if enemy.damage < 0:
                enemy.damage = 0
    
    def warGodPrayer(self):
        self.mana -= 40
        self.luck += 0.05 * self.level
        self.health += 20 * self.level
        if self.luck * self.level >  random.randint(100,200)/100:
            self.health += 10 * self.level
    
    def swordFocus(self, enemy):
        self.mana -= 30
        if self.luck + (0.01 * self.level)> enemy.evasion:
            enemy.health -= enemy.health * (0.20/self.level)
            if enemy.health <= 0.01:
                enemy.isAlive = False
            
class Mage(Attributes):
    
    def natureRoots(self, enemy):
        self.mana -= 20
        if self.luck * self.level > enemy.evasion:
            enemy.isStun = True
            if enemy.mana >= 20 * self.level:
                enemy.mana -= 20 * self.level
                               
    def stoneLance(self,enemy):
        self.mana -= 15
        self.critPercentage += 0.03 * self.level
        trueDamage = self.damage + (20 * self.level)
        print("=------------------------------------------------------------=")
        print(f"{self.name} attacks {enemy.name} with an infused blade.")
        if enemy.evasion >= random.randint(100,200)/100:
            print("+------------------------------------------------------------+")
            return print(f"{self.name} Missed.\n")
        if self.luck  > random.randint(100,200)/100:
           trueDamage = self.damage * self.luck 
           print("+------------------------------------------------------------+")
           print(f"The luck is on {self.name}'s side.")
        if self.critPercentage  > random.randint(100,200)/100:
           trueDamage = trueDamage * self.critPercentage
           print("+------------------------------------------------------------+")
           print(f"{self.name} did critical Damage.")
        enemy.defense = enemy.defense - trueDamage
        if enemy.defense >= 0:
            print("+------------------------------------------------------------+")
            return print(f"{enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
        else:
            enemy.health = enemy.health + enemy.defense
            enemy.defense = 0
            if enemy.health <= 0:
                enemy.isAlive = False
                print("+------------------------------------------------------------+")
                return print(f"{enemy.name} is dead.\n+------------------------------------------------------------+\n{enemy.name}'s Health: 0/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
            else:
                print("+------------------------------------------------------------+")
                return  print(f"{enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}\n{enemy.name}'s Defense:  {enemy.defense}/{enemy.maxDefense}\n")
    
    def concentration(self):
        self.mana -= 30
        self.defense += 20 * self.level
        self.maxMana += 25 + int((self.level - 1) * 100)
    
    def eletricShock(self,enemy):
        self.mana -= 40
        enemy.health -= enemy.health * (0.1 / self.level)
        if enemy.health <= 0.01:
                enemy.isAlive = False
    
    def healingSpell(self):
        self.mana -= 20
        self.health += self.maxMana * 0,1 * self.level
        if self.mana > self.maxMana:
            self.mana =  self.maxMana
            

        
                   


if __name__ == "__main__":
    guerreiro1 = Warrior("Carlos stri")
    guerreiro1.setStatus()
    guerreiro2 = Warrior("JP")
    guerreiro2.setStatus()
    
    while guerreiro1.isAlive and guerreiro2.isAlive:
        if guerreiro1.isAlive:    
            guerreiro1.infusedSword(guerreiro2)
        if guerreiro2.isAlive:
            guerreiro2.infusedSword(guerreiro1)
            

            
    