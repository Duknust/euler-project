#created by duknust
#find in https://github.com/Duknust

def isprime(n):
  n = abs(int(n))
  if n < 2:
    return False
  if n == 2:
    return True
  if not n & 1:
    return False
  for x in range(3, int(n**0.5)+1, 2):
    if n % x == 0:
      return False
  return True

inMove = True
i = 1
counter = 0

while (inMove):
  if isprime(i):
    counter+=1
  if counter==10001:
    inMove=False
  i+=1

print i

