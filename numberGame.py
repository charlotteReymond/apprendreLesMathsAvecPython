from random import randint

def numberGame():
   number = randint (1,100)
   print("Je pense à un nombre entre 1 et 100!")
   guess = int(input("Quel est ton présumé résultat? "))
   while guess:
      if guess == number :
         print("Bravo! Le nombre était bien ", number, " !")
      elif number>guess :
         print("NON, le nombre est plus grand...")
      else :
         print("NON, le nombre est plus petit...")
         
      guess = int(input("Quel est ton résultat? "))




def greet() :
   name= input("Quel est ton nom ? ")
   if name == "Charlotte" :
      print("C'est aussi mon nom ! ")
   else :
      print("Hello, " ,name," !")
      

numberGame()
