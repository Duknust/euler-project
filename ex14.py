#created by duknust
#find in https://github.com/Duknust

number=1000001
stop = False
stop2 = False
maximum = 0
while(not stop):
    number-=1
    stop2 = False
    internalNumber = number
    sequence = 0
    while (not stop2):
        if internalNumber==1:
            stop2=True
        else:
            if internalNumber%2==0:
                internalNumber=internalNumber/2
                sequence+=1
            else:
                internalNumber=3*internalNumber+1
                sequence+=1
    if sequence>maximum:
        maximum=sequence
        maximumNumber=number
    if(number==1):
        stop=True
    print number

print maximumNumber