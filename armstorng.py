# 125  sabka cube or fer unke cube ka sum 
n = int(input("Enter a number : "))
sum = 0
temp = n 
while(n>0):
    sum =sum+(n%10)*(n%10)*(n%10)
    n//=10

if temp==sum :
    print("Given number is armstorng number ")
else : 
    print("Given number is not armstorng ");


print("Sum of digits = ",sum);
 