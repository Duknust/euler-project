#created by duknust
#find in https://github.com/Duknust

count=0
for i in range(1,1001):
  count+=pow(i,i)
  print i

countInString = str(count)
print countInString[len(countInString)-10:]