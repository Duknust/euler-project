#created by duknust
#find in https://github.com/Duknust

sum = 0
fib = [1,2]
tmp = -1
terminate = False
while(not terminate):
  if(fib[0] % 2 == 0):
    sum+=fib[0]
  tmp = fib[0]
  fib[0]=fib[1]
  fib[1]+=tmp 
  if(fib[0]>4000000):
    terminate = True
print sum