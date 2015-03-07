#created by duknust
#find in https://github.com/Duknust

mult=1
for i in range(1,101):
  mult*=i
print mult
count=0
for x in str(mult):
  count+=int(x)
print count