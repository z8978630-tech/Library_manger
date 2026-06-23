class Library():
    def __init__(self,books=None):
        if books is None:
            self.books=[]
        else:
            self.books=books
    def add_book(self, title):
        if  title not in self.books:
            self.books.append(title)
            print(f"book {title} added")
        else:
            print(f"book {title} is exist")
    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f"book {title} removed")
        else:
              print(f"book {title} not found")
    def show_books(self):
        if not self.books:
            print("libaray ids empty")
        else:
            print("list books")
            for book in self.books:
                print(f"-{book}")

def main():
    lib=Library()
    while True:
        print("1.add book")
        print("2.Remove book")
        print("3.show all books")
        print("4.exit")
        choice=input("choice an option (1-4):").strip()
        if choice =="1":
            title=input("enter book title:")
            if title:
                lib.add_book(title)
            else:
                print("title cannot be empty")
        elif choice=="2":
            title=input("enter book title to remove:")
            if title:
                lib.remove_book(title)
            else:
                print("title can not be empty")
        elif choice=="3":
            lib.show_books()
        elif choice=="4":
            print("bye")
            break
        else:
            print(f"invalid option! please choice 1-4")
if __name__=="__main__":
    main()    

