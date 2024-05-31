s = 'Prince is my frd......';
s1= 'hello'
t= 'LALIT';
p= 'hello11111'
print(s);
print(s*2);
print(s1+s);
print('_'.join(s1));
# upper case
print(s1.upper());
print(t.isupper());

# Lower case 
print(t.lower());
print(t.casefold());
print(s1.islower());
# all chateretr is upper case ..................
print("\n");

print(s1.capitalize());
# checked string having any numirecie valve inside the string 
print(t.isalpha());
# check having a ding in a string 

print(p.isdigit());

print(p.count('lo'));

print(p.lstrip());
print(s1.rstrip());
print(s.strip());