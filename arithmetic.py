def average(a,b) :
   return(a + b) / 2
            


def mySum(number) :
   running_sum = 0
   for a in range(number+1) :
      running_sum += a
   print(running_sum)



def mySum2(number):
   running_sum = 0
   for i in range(number+1) :
      running_sum += i**2 +1

   return(running_sum)


def average2(liste) :
   return(sum(liste)/len(liste))


def squareRoot(num=9,low=2,high=5) :
   average(low,high)
   for i in range(20) :
      guess = average(low,high)
      if guess**2 == num :
         print(guess)
      elif guess**2 >  num : 
         high = guess
      else :
         low=guess
   print(guess)

squareRoot(2,1,2)

