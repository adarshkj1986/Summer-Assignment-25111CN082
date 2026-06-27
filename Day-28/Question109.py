library=[]
print("____welcome to library management system____")
while True:
    print("1. add a book")
    print("2. view all books")
    print("3.search for a book")
    print("4.exit")
    ch=input("enter the choices(1-4)")
    if ch=="1":
        title=input("enter book title:")
        author=input("enter the author name:")
        year=input("enter publication year:")
        book={"title":title,"author":author,"year":year}
        library.append(book)
        print("book added successfully")
    elif ch=="2":
        if not library:
            print("the library  is empty")
        else:
            for i,book in enumerate(library,1):
                print(f"{i}. title:{book["title"]},author: {book["author"]},year:{book["year"]}")
    elif ch=="3":
        search_title=input("enter the title of book to search:")
        found=False
        for book in library:
            if book["title"].lower()==search_title.lower():
                print(f" found:{book["title"]} by {book["author"]} ({book["year"]})")
                found=True
                break
        if not found:
            print("book not found")
    elif ch=="4":
        print("exiting the program")
        break
    else:
        print("invalid")