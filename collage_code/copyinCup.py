# sello copy create a new compound obj and then refrence the obj cantain in the original within it ;
# any made in the copy will reflect in the original obj     .copy();
# sello_copy = original.copy()
# deepcopy() :- In deep copy a new compound obj is created and then recisive populate it  woth copies of child obj found in the priginal 

# clear method 
D = {'name' : 'sello' , 'age' : 21 , 'sex' : 'male'};
D.clear();
print(D);

# copy method 
D = {'name' : 'sello' , 'age' : 21 , 'sex' : 'male'};
D_copy = D.copy();
print(D_copy);
print(id(D),id(D_copy));

# get method 
D = {'name' : 'sello' , 'age' : 22 , 'sex' : 'male'};
print(D.get('age'));

# pop method 
D = {'name' : 'sello' , 'age' : 21 , 'sex' : 'male'};
D.pop('age');
print(D);
# popitem method 
D = {'name' : 'sello' , 'age' : 21 , 'sex' : 'male'};
print(D.popitem());
print(D);
