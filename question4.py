s=input()
uc=0
lc=0
dig=0
spec=0
sc=0
for ch in s:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
    elif ch.isdigit():
        dig+=1
    elif ch.isspace():
        spec+=1
    else:
        sc+=1
       
print(f"Uppercase: {uc}")
print(f"Lowercase: {lc}")
print(f"Digits: {dig}")
print(f"Spaces: {spec}")
print(f"Other Characters: {sc}")


        
