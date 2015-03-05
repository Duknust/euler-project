#created by duknust
#find in https://github.com/Duknust

def findOne():
  for i in range (0,1000):
    for j in range (i+1,1000):
      for k in range (j+1,1000):
        if i+j+k==1000 and i*i+j*j==k*k:
          return i*j*k

print findOne()