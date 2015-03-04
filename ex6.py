#created by duknust
#find in https://github.com/Duknust

sumNormal = 0
sumSquares = 0
squaresSum = 0

for i in range (0,101):
  sumSquares+=i*i
  sumNormal+=i

squaresSum = sumNormal*sumNormal
result = squaresSum-sumSquares

print result

