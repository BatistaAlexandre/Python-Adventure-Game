import time 

#Objects to be grabbed
sword = 0
flower = 0

required = ("\nUse one of the options above!\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  answer_A = ["ROCK", "Rock", "rock", "rOCK"]
  answer_B = ["WAIT", "Wait", "wait", "wAIT"]
  answer_C = ["RUN", "Run", "run", "rUN"]
 

  print ("After an accident at sea with a strong storm"
  ", you fall off your hiatus and wake up on a beach in the morning"
   "with a huge headache and very disoriented."
  " You struggle to understand where you are and what happened,"
  "but you are interrupted when you hear something coming out of the water and coming towards you."
  "A tipe of sea monster is running towards you. You will :")
  time.sleep(1)
  print ("""  >> TO GRAB A NEARBY ROCK AND THROW IT AT THE MONSTER: TIPE (ROCK)     
   >> TO LIE DOWN AND WAIT TO BE ATTACKED: TIPE (WAIT)
   >> TO RUN: TIPE (RUN)""")   # It was easier to put the variables A, B and C, but they are related to complete words.
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock():
  answer_A = ["RUN", "Run", "run", "rUN"] 
  answer_B = ["ROCK", "Rock", "rock", "rOCK"]
  answer_C = ["CAVE", "Cave", "cave", "cAVE"]

  print ("\nThe moster is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  >> TO RUN: TIPE (RUN)
  >> TO THROW ANOTHER ROCK: TIPE (ROCK)
  >> TO RUN TOWARDS A NEARBY CAVE: TIPE (CAVE)""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "monsters head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  answer_A = ["HIDE", "Hide", "hide", "hIDE"] 
  answer_B = ["FIGHT", "Fight", "fight", "fIGHT"]
  answer_C = ["RUN", "Run", "run", "rUN"]
  yes = ["Y", "y", "yes" "YES"]
  no = ["N", "n", "no"]

  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Yes/Not ?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  >> TO HIDE IN SILENCE TIPE (HIDE)
  >> TO FIGHT TIPE (FIGHT)
  >> TO RUN: TIPE (RUN)""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? But what if"
    " the monster can see in the dark?, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the monster, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the monster "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the monster enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the monster turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  answer_A = ["HIDE", "Hide", "hide", "hIDE"] 
  answer_B = ["FIGHT", "Fight", "fight", "fIGHT"]
  answer_C = ["TOWN", "Town", "town", "tOWN"]

  print ("\nYou run as quickly as possible, but the monster's "
  "speed is too great. You will:")
  time.sleep(1)
  print (""">> TO HIDE BEHIND BOULDER: TIPE (HIDE)
  >> TO FIGHT THE MONSTER: TIPE (FIGHT)
  >> TO RUN TOWARDS AN ABANDONED TOWN: TIPE (TOWN)""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an monster. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  yes = ["Y", "y", "yes" "YES"]
  no = ["N", "n", "no"]

  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the monster to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Yes/Not")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending monster.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the monster. It does! The monster was"
    " looking at you with love in his eyes. "
    
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()