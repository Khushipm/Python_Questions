
x =int(input())
bool_n =str(input())
 
if bool_n=='true' :
    for i in range(0, x+1):
        print("*"*i)
  
if bool_n=='false' :
    for i in range(x, 0 ,-1):
       print("*"*i)
 