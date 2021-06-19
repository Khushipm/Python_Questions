num = 18
x = 9
while (x>=0) :

 num1 = int(input())
 x=x-1

 if num1>num :
     print("You entered a greater value")
 
 elif num1<num :
     print("You entered a smaller value")
 
 elif num1==num :
     print("You guessed the correct value in ", 9-x, " moves ")
     break
     
  
 print("Number of guesses left: ", x)
    
print("Number of guesses finished: GAME OVER !")