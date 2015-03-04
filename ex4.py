#created by duknust
#find in https://github.com/Duknust

palindrome = 0
stop = False
i = 999
j = 999

for i in range (0,999):
  for j in range (0,999):
    tmp = (999-i)*(999-j)
    toPali = str(tmp)
    if (toPali == toPali[::-1]):
      if (palindrome < tmp):
        palindrome = tmp
    
print palindrome

