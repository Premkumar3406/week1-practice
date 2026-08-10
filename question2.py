customer_name=input("Enter your name:")
age=int(input("Enter your age:"))
tickets=int(input("Enter number of tickets:"))
if 0<=age<=12:
    rate=120*tickets
elif 12<=age<=59:
    rate=200*tickets
else:
    rate=150*tickets
if tickets>=5:
    discount=0.10*rate
    total=rate-discount
print(f"Customer Name: {customer_name}")
print(f"Age: {age}")
print(f"Number of tickets: {tickets}")
print(f"Total before discount:{rate}")
print(f"Discount:{discount}")
print(f"Final Amount:{total}")