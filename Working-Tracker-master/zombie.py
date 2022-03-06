
import sqlite3

sqlite3.connect('ZombieTracker2.db')
conn = sqlite3.connect('ZombieTracker2.db')
cursor = conn.cursor()



# cursor.execute("""SELECT name FROM "ZombieTracker2.db" WHERE type='table' AND name='ZombieTracker' """)


print(" Successfully Connected to table")
   

# Zombie_name = input("Enter zombies name:\n")
# Zombie_age = input("Zombies age:\n")
# Zombie_type = input("Zombies type:\n")
# Zombie_location = input("Zombies location:\n")
# Zombie_specialty = input("Zombies specailty:\n")
# Eat_brains = input("Yes or No:\n")

Zombie_name = input('Enter zombies name:\n')
Zombie_age = input('Zombies age:\n')
Zombie_type = input('Zombies type:\n')
Zombie_location = input('Zombies location:\n')
Zombie_specialty = input('Zombies specailty:\n')
Eat_brains = input('Yes or No:\n')



# params = (Zombie_name, Zombie_age, Zombie_type, Zombie_location, Zombie_specialty, Eat_brains)

# cursor.execute("""INSERT INTO ZombieTracker(Name,Age,Type,Location,Specialty,Brains)\
# VALUES('Zombie_name', 'Zombie_age', 'Zombie_type', 'Zombie_location', 'Zombie_specialty', 'Eat_brains')""")

cursor.execute("""
INSERT INTO ZombieTracker(Name, Age, Type, Location, Specialty, Brains)
VALUES (?,?,?,?,?,?)
""", (Zombie_name, Zombie_age, Zombie_type, Zombie_location, Zombie_specialty, Eat_brains))




print("Data Successfully documented!!")

conn.commit()
