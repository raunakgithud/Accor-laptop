print("Hello world")

# conditional statements

# if  ifelse  if elif else nested if


if True:
    print("inside code");
print("end");

if False:
    print("in");
print("end");

if (5>3):
    print("5 is greater");

name1 = "Rahul"
name2 = "Rahul"

if(name1 == name2):
    print("Both name are same");

a = 2
b = 3
c = a == b

if(c):
   print("equal");
else:
   print("not equal");


#############################################

total_bill = 699
discount_start_price = 500

if(total_bill >= discount_start_price):
    print("discount available");
else: 
    print("not available");

#====================================================

rice_available = True
wheat_available = False
apple_available = False

if(rice_available):
    print("buy rice");
elif(wheat_available):
    print("buy wheat");
else:
    print("buy apple");

#-------------------------------------------------

gender = "female"
age = 21

if(gender == "male"):
    if(age == 21):
        print("can marry");
    else:
        print("can't marry");
else:
    if(age >= 18):
        print("can marry");
    else:
        print("cant marry");

###----------------------###-----------------###---------

A = 10
B = 20

if(A == B):
    print("both are equal");
elif(A > B):
    print("A is greater");
else:
    print("B is greater");
##-------------------##########------------------------------

# logical operator   AND  OR   NOT

p = True
q = True
r = p and q

print(r);

if p:
    if q:
        print(r);






