#created by duknust
#find in https://github.com/Duknust

dic = {}

for a in range (2,101):
  for b in range (2,101):
    dic[pow(a,b)] = 1

print len(dic)