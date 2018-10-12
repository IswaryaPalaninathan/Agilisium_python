'''
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.

For example, input:-
 {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
output:-
 {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.'''
 
def group_by_owners(d):
    print(d)
    resultdic={}
    tempfiles=[]
    for f, o in d.items():
        if o in resultdic:
            existingfile=resultdic[o]
            tempfiles.append(existingfile)
            if resultdic[o]!=f:
                tempfiles.append(f)
                print("tf")
                print(tempfiles)
                resultdic[o]=tempfiles
        if o not in resultdic:
                resultdic[o]=f    
    print(resultdic)   
        
d= {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}    
group_by_owners(d)
