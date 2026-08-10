seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
seat_no=int(input("Enter seat number:"))
if seats[seat_no]=="Available":
    print("Seat booked successfully")
    seats[seat_no]="Booked"
else:
    print("Seat is already booked.")


total=len(seats)
booked=seats.count("Booked")
available=total-booked
print(f"Total seats: {total}")
print(f"Booked seats: {booked}")
print(f"Available seats: {available}")
