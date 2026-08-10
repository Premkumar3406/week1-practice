expenses=[250,1200,450,800,150,2000,350]
total=sum(expenses)
average=total/len(expenses)
highest=max(expenses)
lowest=min(expenses)
print(f"Total Expenses:{total}")
print(f"Average Expenses:{average:.2f}")
print(f"Highest Expenses:{highest}")
print(f"Lowest Expenses:{lowest}")
count=0
b_count=0
for i in expenses:
    if i>500:
        count+=1
    else:
        b_count+=1
print(f"Number of Expenses Above 500: {count}")
print(f"Number of Expenses Below 500: {b_count}")

print("Expenses Above Average:")
for i in expenses:
    if i>average:
        print(i)