'''
You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c)  in the string.

input:-
  1222311
output:-
  (1, 1) (3, 2) (1, 3) (2, 1)

SOLUTION:
---------
'''
inp=raw_input("Enter the string:")
l1=list(inp)
t=()
nl=[]
cnt=0
for i in range(len(l1)):
    if i == (len(l1)-1):
        cnt+=1
        t=(cnt,l1[i])
        nl.append(t)
    else:
        if l1[i]==l1[i+1]:
            cnt+=1
        else:
            cnt+=1
            t=(cnt,l1[i])
            nl.append(t)
            cnt=0
print "The output is ", nl
