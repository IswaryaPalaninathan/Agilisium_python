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
''' 
