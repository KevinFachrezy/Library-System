from tabulate import tabulate

# ===== INITIAL BOOK DATA ====
books = {
    "Fiction": [
        {"book_id": "01-FI-2003", "name": "Kisah Legenda Indonesia", "year": 2003, "status": "available"},
        {"book_id": "02-FI-2007", "name": "European Folklore", "year": 2007, "status": "available"},
        {"book_id": "03-FI-2000", "name": "Tales From The Arabian Peninsula", "year": 2000, "status": "not available"},
    ],
    "Educational": [
        {"book_id": "01-ED-2019", "name": "Introduction To Python Programming", "year": 2019, "status": "available"},
        {"book_id": "02-ED-1995", "name": "Programming Fundamentals", "year": 1995, "status": "available"},
    ],
    "Cooking": [
        {"book_id": "01-CO-2010", "name": "100 Resep Tradisional", "year": 2010, "status": "available"},
        {"book_id": "02-CO-2004", "name": "Resep Menu Simple", "year": 2004, "status": "available"},
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
    # Cek apakah isi dalam genre kosong
    isEmpty = []
    # Looping dictionary books dan add genre yang tidak memiliki book
    for genre, book in books.items():
        if not book:
            isEmpty.append(genre)
    # Loop jika ada genre lain yang kosong
    for genre in isEmpty:
        del books[genre]  
    
    
    print("\n=== DAFTAR BUKU ===")
    for genre, bookList in books.items():
        print(f"\n--- {genre.upper()} ---")
        
        # Kode untuk sort based on book id
        sortView = sorted(
            bookList, 
            key = lambda book: int(book["book_id"].split("-")[0])
            )
        # Kode untuk display book dengan fungsi built-in tabulate
        headers = ["Book Id", "Judul", "Tahun Publikasi", "Status"]
        table = [[book["book_id"], book["name"], book["year"], book["status"]] for book in sortView]
        print(tabulate(table, headers=headers, tablefmt="grid"))



def generateBookId(genre, year):        # Generate Book Function (digunakan untuk proses Create)
    # Kode untuk mencari genreCode (slicing 2 huruf pertama dari genre)
    genreCode = genre[:2].upper()
    bookList = books.get(genre, [])
    
    # Kode untuk mencari book id
    existingId = [int(book["book_id"].split("-")[0]) for book in bookList]
    
    # Kode If jika tidak ada book (untuk buku baru), else cari id yang missing dari sorted id
    if not existingId:
        nextId = 1
    else:
        maxId = max(existingId)
        possibleId = set(range(1, maxId + 2))
        missingId = sorted(list(possibleId - set(existingId)))
        nextId = missingId[0]
        
    if nextId in existingId: # if untuk mengecek duplikat id
        nextId = max(existingId) + 1
    elif nextId == 0: # elif untuk mencegah id 00
        nextId = 1
    
    # return id dengan format nextId-kode genre-tahun   
    return f"{nextId:02d}-{genreCode}-{year}"



def addBook():                          # Add Book function (Proses Create) (Function ini khusus untuk user "Librarian")
    while True:
        genre = input("Masukkan genre buku baru:").capitalize()
        
        if not genre.isalpha():
            print("\nGenre tidak boleh mengandung angka. Silahkan coba lagi!\n")
            continue
        
        name = input("Masukkan nama buku baru: ").strip().title()
        year = input("Masukkan tahun terbit: ")
        
        if not year.isdigit():
            print("\nTahun terbit harus berupa angka. Silahkan coba lagi!")
            continue
        
        # If genre tidak ada dalam dictionary, akan membuat genre baru
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
            if repeat == "ya":
                break
            elif repeat == "tidak":
                print("\nKembali ke menu ...\n")
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
                break
        
        if not found:    
            print("\nBuku tidak ditemukan.\n")
        
        while True:
            repeat = input("Apakah anda ingin menghapus buku lain dari record? (ya/tidak): ").strip().lower()
            if repeat == "ya":
                break
            elif repeat == "tidak":
                print("\nKembali ke menu ...\n")
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



def viewBorrowedBooks():            # View Borrow Book function (Proses Read) (Function ini khusus untuk user "visitor")
    if not borrowedBooks:
        print("\nAnda belum meminjam buku apapun.\n")
    else:
        print("\n=== Buku Yang Anda Pinjam ===")
        headers = ["Book Id", "Judul", "Tahun Publikasi"]
        table = [[book["book_id"], book["name"], book["year"]] for book in borrowedBooks]
        print(tabulate(table, headers=headers, tablefmt="grid"))


def returnBook():                   # Return Book function (Proses Update) (Function ini khusus untuk user "visitor")
    while True:     
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
            if repeat == "ya":
                break
            elif repeat == "tidak":
                print("\nKembali ke menu ...\n")
                return
            else:
                print("Input tidak valid. Ketik 'ya' atau 'tidak'\n")



def login():
    username = ""
    password = ""
    for i in range(3):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in users and users[username]["password"] == password:
            print(f"\nLogin berhasil! selamat datang di sistem perpustakaan, {username.capitalize()}")
            return username
        else:
            print("Username atau password salah.\n")
    print("Gagal login setelah 3 kali percobaan.")



def logout():
    print("Kembali ke halaman login ...\n")
    return None



                    
def mainMenu():
    user = None
        
    while True:
        if user == None:
            user = login()
            
        if user == "visitor":
            print("\n === MENU VISITOR ===")
            print("1. Lihat daftar buku")
            print("2. Pinjam Buku")
            print("3. Kembalikan Buku")
            print("4. Lihat buku yang dipinjam")
            print("5. Logout")
            print("6. Keluar")
            pilih = input("Pilih menu: ")
            
            if pilih == "1":
                displayBooks()
            elif pilih == "2":
                borrowBook()
            elif pilih == "3":
                returnBook()
            elif pilih == "4":
                viewBorrowedBooks()
            elif pilih == "5":
                user = logout()
            elif pilih == "6":
                print("\nTerima kasih telah menggunakan sistem perpustakaan.\n")
                break
            else:
                print("\nPilihan tidak valid. Silahkan input pilihan yang sesuai menu.\n")
        
        elif user == "librarian":
            print("\n === MENU LIBRARIAN ===")
            print("1. Lihat daftar buku")
            print("2. Tambah Buku")
            print("3. Hapus Buku")
            print("4. Logout")
            print("5. Keluar")
            pilih = input("Pilih menu: ")
            
            if pilih == "1":
                displayBooks()
            elif pilih == "2":
                addBook()
            elif pilih == "3":
                removeBook()
            elif pilih == "4":
                user = logout()
            elif pilih == "5":
                print("\nTerima kasih telah menggunakan sistem perpustakaan.\n")
                break
            else:
                print("\nPilihan tidak valid. Silahkan input pilihan yang sesuai menu.\n")
                
                
                
# ==== PROGRAM INITIATE
mainMenu()