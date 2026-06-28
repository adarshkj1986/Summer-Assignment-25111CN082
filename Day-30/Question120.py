def add_book(inventory):
    title=input("enter book title:")
    inventory[title]="available"
    print(f"{title} has been added")
def borrow_book(inventory):
    title=input("enter the title to be borrow:")
    if title in inventory:
        if inventory[title]=="available":
            inventory[title]="checked out"
            print(f"ypu have successfully borrowed {title}")
        else:
            print(f"sorry")
    else:
        print("book not found")
def return_books(inventory):
    title=input("enter the title to return:")
    if title in inventory:
        inventory[title]="available"
        print(f"{title} has been added")
    else:
        print("book not found")
def show_inventory(inventory):
    for title,status in inventory.items():
        print(f"{title}:{status}")
def main():
    library_books={}
    while True:
        print("1. add books")
        print("2. borrow book")
        print("3. return book")
        print("4. view all books")
        print("5. exit")
        ch=input("enter the choices from(1-5)")
        if ch=="1": 
            add_book(library_books)
        elif ch=="2":
            borrow_book(library_books)
        elif ch=="3": 
            return_books(library_books)
        elif ch=="4":
            show_inventory(library_books)
        elif ch=="5":
            break
        else:
            print("invalid")
main()