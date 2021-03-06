from turtle import *
speed(0)

def carré(longueurCarré=100) :
      for i in range(4) :
            forward(longueurCarré)
            right(90)

            
def triangle(longueurTriangle=100) :
      for i in range(3) :
            forward(longueurTriangle)
            right(120)


def polygone(nbrCote=4) :
      for i in range(nbrCote) :
            forward(100)
            right(360/nbrCote)


def star(longueurEtoile=100) :
      for i in range(5) :
            forward(longueurEtoile)
            right(504)
      



      
longueurcarré = 5
for i in range(150) :
      
      star(longueurcarré)
      right(5)
      longueurcarré += 5
