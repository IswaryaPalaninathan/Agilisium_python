'''
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.

For example, input:-
 {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
output:-
 {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

SOLUTION:
---------
'''
d={}
d1={}
while True:
    ip=raw_input("Enter options \n1.add \n2.display \n3.quit:")
    if ip=="1":
        fname=raw_input("Enter file name:")
        author=raw_input("Enter author name:")
        d[fname]=author
        print "The output is ", d
    elif ip=="2":
        g=d.values()
        o=d.keys()
        for v in d.values():
            c=[]
            for i in range(len(g)):
                if v==g[i]:
                    c.append(o[i])
                    d1[g[i]]=c
        print "The output is ", d1
    elif ip=="3":
        print "GoodBye!!"
        break
        
        
def myfunc():
    final_dict = {}
    dict1 = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    values_set = set()
    for i in dict1.values():
        values_set.add(i)
    #print(values_set)
    
    for j in values_set:
        final_dict[j] = []
        for k,v in dict1.items():
            if v==j:
                #print("inside if")
                #print(j,k)
                final_dict[j].append(k)
    print(final_dict)
 
