'''A valid postal code  have to fullfil both below requirements:

 must be a number in the range from 100000  to 999999  inclusive.
 must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
'''

def postalcodeValidate(postalcode):   
    
    pcStr=str(postalcode)
    count=0
    i=0
    j=2
    print("hi")
    ##for i,j in range(0,len(pcStr),range(2,len(pcStr)):
    while i < len(pcStr) and j < len(pcStr): 
    ##while i in range(0,len(pcStr)) and j in range(2,len(pcStr)): 
        print("pcSi"+pcStr[i])
        print("pcSj"+pcStr[j])
        if pcStr[i]== pcStr[j]:
            print("if")
            count+= 1  
        i+=1
        j+=1
                         
    print(count)
    if count ==1 or count ==0 :
        print("valid Postal code 2")  
    else:
        print("Please Enter a valid code, Your code should not contain more than one alternating repeating digit")  
    if postalcode <= 999999 and postalcode >=100000 :
        print("Valid postal code 1")
    else:
        print("Please Enter a valid code, your code should be in the range of 100000 to 999999")         
        
postalcodeValidate(int(input("Enter your postalcode:")))  