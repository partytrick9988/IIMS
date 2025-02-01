class Library_item :
    def __init__(self, title , author):
        self.title = title
        self.author = author

    def details(self):
        return f"Title : {self.title} , Author : {self.author}"

class Book(Library_item) :
    def __init__(self, title, author , pages):
        super().__init__(title, author)
        self.pages = pages
    def details(self) :
        return f"Book: {super().details()} , pages : {self.pages}."

class DVD(Library_item) :
    def __init__(self, title, author ,duration ):
        super().__init__(title, author)
        self.duration = duration
    def details(self) :
        return f"DVD: {super().details()} , duration : {self.duration}."

class Magazine(Library_item) :
    def __init__(self, title, author , issue):
        super().__init__(title, author)
        self.issue = issue 
    def details(self) :
        return f"Magazine: {super().details()} , issue : {self.issue}."


def menu():

    library = []
    while True:
        print("1.Add Book.")
        print("2.Add DVD.")
        print("3.Add Magazine.")
        print("4.View")
        print("5.Exit")

        ch = input("Enter task:")
        if ch == "1":
            title = input("Enter Title: ")
            author = input("Enter Author:")
            pages = int(input("Enter num of pages:"))
            library.append(Book(title , author , pages))
        elif ch == "2":
            title = input("Enter Title: ")
            author = input("Enter Author:")
            duration = int(input("Enter Duration (min):"))
            library.append(DVD(title , author , duration))
        elif ch == "3":
            title = input("Enter Title: ")
            author = input("Enter Author:")
            issue = int(input("Enter Issue:"))
            library.append(Magazine(title , author , issue))
        elif ch == "4" :
            if not library:
                print("No item in the library.")
                continue
            for item in library:
                print(item.details())
        elif ch == "5" :
            quit()

menu()
        
        