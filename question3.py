n=int(input("Enter number:"))
even_count=0
odd_count=0
for i in range(1,11):
    res=n*i
    if res%2==0:
        print(n,"x",i,"=",res,"-Even")
        even_count+=1
    else:
        print(n,"x",i,"=",res,"-Odd")
        odd_count+=1
print(f"Even Result: {even_count}")
print(f"Odd Result: {odd_count}")
