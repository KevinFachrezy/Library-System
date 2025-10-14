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
        headers = ["Book Id", "Judul", "Tahun Publikasi", "Status"]
        table = [[book["book_id"], book["name"], book["year"], book["status"]] for book in book_list]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    print()



def generateBookId(genre, year):        # Generate Book Function (digunakan untuk proses Create)
    genreCode = genre[:2].upper()
    nextId = len(books.get(genre, [])) + 1
    return f"{nextId:02d}-{genreCode}-{year}"



def addBook():                          # Add Book function (Proses Create) (Function ini khusus untuk user "Librarian")
    while True:
        genre = input("Masukkan genre buku baru:").capitalize()
        
        if not genre.isalpha():
            print("\Genre tidak boleh mengandung angka. Silahkan coba lagi!\n")
            continue
        
        name = input("Masukkan nama buku baru: ").strip().title()
        year = input("Masukkan tahun terbit: ")
        
        if not year.isdigit():
            print("\nTahun terbit harus berupa angka. Silahkan coba lagi!")
            continue
        
        if genre not in books:
            books[genre] = []
            
        duplicate = False
        for book in books[genre]:
            if book["name"].lower() == name.lower():
                print("\nBuku dengan nama tersebut sudah ada dalam genre ini.\n")
                duplicate = True
                break
        
        if duplicate:
            continue
        
        bookId = generateBookId(genre, year)
        books[genre].append({
            "book_id": bookId,
            "name": name,
            "year": int(year),
            "status": "available"
        })
        
        print(f"\nBuku '{name}' berhasil ditambahkan ke genre {genre} dengan id {bookId}!")
        
        
        while True:
            repeat = input("Apakah anda ingin menambahkan buku lain? (ya/tidak): ").strip().lower()
            if repeat != "ya":
                print("\nKembali ke menu ...\n")
                break
            elif repeat == "tidak":
                return
            else:
                print("Input tidak valid. Ketik 'ya' atau 'tidak'\n")



def removeBook():                   # Remove Book function (Proses Delete) (Function ini khusus untuk user "Librarian")
    while True:
        displayBooks()
        name = input("Masukkan nama buku yang ingin dihapus: ")
        
        found = False
        for genre, bookList in books.items():
            for book in bookList:
                if book["name"].lower() == name.lower():
                    bookList.remove(book)
                    print(f"\nBuku '{book['name']}' berhasil dihapus!\n")
                    found = True
                    break            
            if found:
                print("\nBuku tidak ditemukan.\n")
        
        while True:
            repeat = input("Apakah anda ingin menghapus buku lain dari record? (ya/tidak): ").strip().lower()
            if repeat != "ya":
                print("\nKembali ke menu ...\n")
                break
            elif repeat == "tidak":
                return
            else:
                print("Input tidak valid. Ketik 'ya' atau 'tidak'\n")  
            



def borrowBook():                   # Borrow Book function (Proses Update) (Function ini khusus untuk user "visitor")
    while True:
        displayBooks()
        name = input("Masukkan nama buku yang ingin dipinjam: ")
        if name.lower() == "selesai":
            break
        
        found = False
        for genre, bookList in books.items():
            for book in bookList:
                if book["name"].lower() == name.lower():
                    found = True
                    if book["status"] == "available":
                        book["status"] = "not available"
                        borrowedBooks.append(book)
                        print(f"\nBerhasil meminjam buku '{book['name']}'\n")
                        return
                    else:
                        print("\nMaaf, buku tidak tersedia.\n")
                    break
            if found:
                break
        if not found:
            print("\nBuku tidak ditemukan.\n")



def returnBook():
    if not borrowedBooks:
        print("\nAnda belum meminjam buku apapun.\n")
        return
    
    while True:
        print("\n=== Buku Yang Anda Pinjam ===")
        headers = ["Book Id", "Judul", "Tahun Publikasi"]
        table = [[book["book_id"], book["name"], book["year"]] for book in borrowedBooks]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        
        name = input("Masukkan judul buku yang ingin dikembalikan: ").strip()
        
        found = False
        for book in borrowedBooks:
            if book["name"].lower() == name.lower():
                book["status"] = "available"
                borrowedBooks.remove(book)
                print(f"\nBuku '{book['name']}' berhasil dikembalikan!\n")
                found = True
                break
            
        if not found:
            print("\nBuku tidak ditemukan dalam daftar pinjaman buku anda.\n")
            
        if not borrowedBooks:
            print("Anda sudah mengembalikan semua buku.\n")
            break
        
        while True:
            repeat = input("Apakah anda ingin mengembalikan buku lain? (ya/tidak): ").strip().lower()
            if repeat != "ya":
                print("\nKembali ke menu ...\n")
                break
            elif repeat == "tidak":
                return
            else:
                print("Input tidak valid. Ketik 'ya' atau 'tidak'\n")