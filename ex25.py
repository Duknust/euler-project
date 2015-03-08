#created by duknust
#find in https://github.com/Duknust

seq = [1,1]
numbOfSeq=2
stop = False
while(not stop):
  numbOfSeq+=1
  tmp = seq[0]+seq[1]
  seq[0]=seq[1]
  seq[1]=tmp
  if(len(str(tmp))==1000):
    stop=True

print numbOfSeq