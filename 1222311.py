mystring = '12223112'
mystring = input("Enter any text or number sequence: ")
count = 0
flag = 0
mylist = []

for i in range(0,len(mystring)):
  if flag != 0:
    flag = flag - 1
    #print(flag)
  else:
    count = 0
    for j in range(i,len(mystring)):
      if mystring[i] == mystring[j]:
        count = count + 1
      else:
        break
    flag = count -1
    mylist.append((mystring[i],count))
print(mylist)
