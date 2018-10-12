'''
You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c)  in the string.

input:-
  1222311
output:-
  (1, 1) (3, 2) (1, 3) (2, 1)

'''


from itertools import groupby
print([(len(list(c)), int(x)) for x, c in groupby(input())])


'''
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.

For example, input:-
 {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
output:-
 {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

'''


inp={'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
def group_by_owners(files):
    dic={}
    for x,y in files.items():
        # dic=x,y  i dont know exactly here.
        return dic
print(group_by_owners(files))