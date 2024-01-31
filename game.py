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
            

            
    