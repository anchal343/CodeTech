import datetime

class LibraryItem:
    def __init__(self, item_id, title, author, category):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author} ({self.category})"

class Library:
    def __init__(self):
        self.items = {}
        self.fines = {}
        self.checkout_period = 14  # days

    def add_item(self, item_id, title, author, category):
        if item_id in self.items:
            print("Item with this ID already exists.")
        else:
            self.items[item_id] = LibraryItem(item_id, title, author, category)
            print("Item added successfully.")

    def checkout_item(self, item_id, member_id):
        if item_id in self.items:
            item = self.items[item_id]
            if not item.is_checked_out:
                item.is_checked_out = True
                item.due_date = datetime.date.today() + datetime.timedelta(days=self.checkout_period)
                self.fines[member_id] = 0  # Initialize fines for the member
                print(f"Item checked out successfully. Due date is {item.due_date}.")
            else:
                print("Item is already checked out.")
        else:
            print("Item not found.")

    def return_item(self, item_id, member_id):
        if item_id in self.items:
            item = self.items[item_id]
            if item.is_checked_out:
                item.is_checked_out = False
                if datetime.date.today() > item.due_date:
                    overdue_days = (datetime.date.today() - item.due_date).days
                    self.fines[member_id] += overdue_days * 1  # $1 fine per overdue day
                    print(f"Item returned. Overdue fine is ${overdue_days}.")
                else:
                    print("Item returned on time.")
                item.due_date = None
            else:
                print("Item is not checked out.")
        else:
            print("Item not found.")

    def search_items(self, query, search_type="title"):
        results = []
        for item in self.items.values():
            if (search_type == "title" and query.lower() in item.title.lower()) or \
               (search_type == "author" and query.lower() in item.author.lower()) or \
               (search_type == "category" and query.lower() in item.category.lower()):
                results.append(item)
        return results

    def get_fines(self, member_id):
        return self.fines.get(member_id, 0)

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add new item")
        print("2. Check out item")
        print("3. Return item")
        print("4. Search items")
        print("5. View fines")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            item_id = input("Enter item ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            library.add_item(item_id, title, author, category)
        elif choice == "2":
            item_id = input("Enter item ID: ")
            member_id = input("Enter member ID: ")
            library.checkout_item(item_id, member_id)
        elif choice == "3":
            item_id = input("Enter item ID: ")
            member_id = input("Enter member ID: ")
            library.return_item(item_id, member_id)
        elif choice == "4":
            query = input("Enter search query: ")
            search_type = input("Search by (title/author/category): ")
            results = library.search_items(query, search_type)
            for item in results:
                print(item)
        elif choice == "5":
            member_id = input("Enter member ID: ")
            fines = library.get_fines(member_id)
            print(f"Total fines: ${fines}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
