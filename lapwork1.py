#1
celsius=int(input("enter the temperature in celsius: "));
Fahrenheit= (celsius*(9/5)+32);
print(celsius, "(C) = ", Fahrenheit," (F)");
#2
radius = int(input("enter circle radius: "));
circle_area = (radius**2)*3.14;
print("circle area is: ", + circle_area);
#3
import math;
a=[0,0];
b=[1,1];
print(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2));
#4
def divisor(number):
    ans=[];
    for i in range(1,number+1):
        if (number%i==0):
            ans.append(i);
    return ans;
a=divisor(10);
print(a);
#5
def draw(m,n):
    for i in range(m):
        if(i==0 or i==m-1):
            for i in range(n):
                print("*", end =" ");
            print();
        else:
            for i in range(n):
                if (i ==0 or i ==n-1):
                    print("*", end=" ");
                else:
                    print(" ", end =" ");
            print();
draw(50,50);
#6
def extract_even(list):
    even_list=[];
    for i in range(len(list)):
        if(list[i]%2==0):
            even_list.append(list[i]);
    return even_list;
integer_list=[1,4,5,-1,10];
integer_list=extract_even(integer_list);
print(integer_list);
#7
def extract_even(list):
    even_list=[];
    for i in range(len(list)):
        if(list[i]%2==0):
            even_list.append(list[i]);
    return even_list;
integer_list=[1,4,5,-1,10];
integer_list=extract_even(integer_list);
print(integer_list);
#8
def factorial(number):
    if number <0:
        print("error");
    else:
        ans =1;
        for i in range(1,number+1):
            ans *= i;
    print(ans);
factorial(3);
#9
number=int(input("enter a number: "));
sum=0;
for i in range(1,number):
    if(number%i==0):
        sum +=i;
if(sum == number):
    print("Yes");
else:
    print("No");
#10
number = int(input("enter an integer number: "));

for i in range(2,number+1):
    if(number%i==0):
        break
#11
range1 = range(0,7);
for i in range1:
    print(i, end=" ");
print('\n');
range2 = range(1,11,3);
for v in range2:
    print(v, end=" ");
print("\n");
range3 = range(5,0,-1);
for i in range3:
    print(i, end=" ");
print('\n');
range4 = range(6,-3,-2);
for d in range4:
    print(d, end=" ");
#12
def remove_dollar_sign (s):
    return s.replace('$',''); 
string = input("enter a string: ");
clean_string=remove_dollar_sign(string);
print(clean_string);