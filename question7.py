values=[10,10,20,20,20,30,10,10,40]
res=[]
previous=None
for num in values:
    if num!=previous:
        res.append(num)
        previous=num
print(res)
 

    