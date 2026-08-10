hours=int(input("Enter parking hours:"))
if 0<=hours<=2:
    charge=30*hours
elif 3<=hours<=5:
    charge=25*hours
else :
    charge=20*hours
print(f"Parking charge:{charge}")
if  charge>150:
    service=20
else:
    service=0
final=service+charge
print(f"Service charge:{service}")
print(f"Final charge:{final}")
