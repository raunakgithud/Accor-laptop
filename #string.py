#string

Str = "nrupul"
N = len(Str)
count = 0
while(count<=N-1):
      if(count%2 == 0):
            print(Str[count])
            
      
      count += 1

print("----------------------------------")      
string = "Samanthaexaminedtheletterandfounditcontainedahiddenmessage"
vowel_lower = "aeiou"
Vowel_upper = "AEIOU"
n = len(string)
count = 0 
for i in range(n):
    if (vowel_lower.count(string[i])==0):
      if(Vowel_upper.count(string[i])==0):
        count += 1
  
print(count)

#def Solve(n):
   #n = 97420 # Write code here
   #
   #target = 420
   #if(str(n).count(str(target)) >= 1):
   #  print("Caught")
   #else:
   #  print("Escaped")

#Solve(n=32045420)
print("-----------------------------------------")
n = 87642030
print(str(n))
target = 420
if(str(n).count(str(target))>= 1):
    print("caught")
else:
    print("Escaped")

print("-------------")  

print("Python"[0])
print("-----------------")

s = "Hello"
print(s[-1])
print("--------------------------")
s = "python"
print(s[1:4])
print(s.split())
print("-------------------------------------")
s1 = "how are you."
s2 = "I am fine"

print(s1,end="")
print(s2)

print(s1,end="\n")
print(s2)





           