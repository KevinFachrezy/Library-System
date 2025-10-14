from tabulate import tabulate

# ===== INITIAL BOOK DATA ====
books = {
    "Fiction": [
        {"book_id": "01-FI-2003", "name": "Kisah Legenda Indonesia", "year": 2003, "status": "available"},
        {"book_id": "02-FI-2007", "name": "European Folklore", "year": 2007, "status": "available"},
        {"book_id": "03-FI-2000", "name": "Tales From The Arabian Peninsula", "year": 2000, "status": "not available"},
    ],
    "Educational": [
        {"book_id": "04-ED-2019", "name": "Introduction To Python Programming", "year": 2019, "status": "available"},
        {"book_id": "05-ED-1995", "name": "Programming Fundamentals", "year": 1995, "status": "available"},
    ],
    "Cooking": [
        {"book_id": "06-CO-2010", "name": "100 Resep Tradisional", "year": 2010, "status": "available"},
        {"book_id": "07-CO-2004", "name": "Resep Menu Simple", "year": 2004, "status": "available"},
    ]
}

# ==== BORROWED BOOK TRACKER ====
borrowedBooks = []

# ==== USER DATA ====
users = {
    "visitor": {"username": "visitor", "password": "visit123"},
    "librarian": {"username": "librarian", "password": "lib123"}
}

# ==== PROGRAM FUNCTIONS


def displayBooks():                     # Display All Books
    print("\n=== DAFTAR BUKU ===")
    for genre, book_list in books.items():
        print(f"\n--- {genre.upper()} ---")
        headers = ["Code", "Name", "Year", "Status"]
        table = [[book["code"], book["name"], book["year"], book["status"]] for book in book_list]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    print()



def generateBookId(genre, year):        # Generate Book Code (digunakan untuk proses Create)
    genreCode = genre[:2].upper()
    nextId = len(books.get(genre, [])) + 1
    return f"{nextId:02d}-{genreCode}-{year}"

def borrowBook():
    displayBooks()
    name = input("Masukan nama buku yang ingin dipinjam: ")
    
    for genre, bookList in books.items():
        for book in bookList:
            if book["name"].lower() == name.lower():
                if book["status"] == "available":
                    book["status"] = "not available"
                    borrowedBooks.append(book)
                    print(f"\nBerhasil meminjam buku '{book['name']}'\n")
                    return
                else:
                    print("\nMaaf, buku tidak tersedia.\n")