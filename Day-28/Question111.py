total_seats=10
booked_seats=0
ticket_price=100.0
print("____welcome to ticket booking system____")
while True:
    print("1. book a ticket")
    print("2.checking the balance present")
    print("3.exit")
    ch=input("enter the choices from(1-3)")
    if ch=="1":
        if booked_seats<total_seats:
            num_tickets=int(input("total tickets you want:"))
            if num_tickets>0 and (booked_seats+num_tickets)<=total_seats:
                total_cost=num_tickets*ticket_price
                booked_seats+=num_tickets
                print(f"successfully booked{num_tickets}.ticket(s).")
                print(f"total cost:${total_cost:.2f}")
            else:
                print("not enough seats available")
        else:
            print("sorry")
    elif ch=="2":
        print(f"total seats:{total_seats}")
        print(f"seats booked:{booked_seats}")
        print(f"seats remaining:{total_seats-booked_seats}")
    elif ch=="3":
        break
    else:
        print("invalid")