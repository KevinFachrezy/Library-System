# Library System Project

Project Library System adalah sebuah sistem sederhana yang menggambarkan konsep perpustakaan. Dalam sistem ini terdapat dua user yaitu Librarian dan Visitor yang dimana kedua user ini dapat berinteraksi layaknya perpustakaan fisik.

Dalam Sistem Library ini terdapat beberapa bagian penting yaitu:

1. User data : Menyimpan user data termasuk username dan password.
2. books dictionary : Collection data-type untuk menyimpan buku perpustakaan.
3. borrowed books dictionary : Collection data-type untuk menyimpan buku yang dipinjam.
4. library functions : Kumpulan functions yang menjadi inti dari Library System ini.

Library System ini juga menggunakan salah satu python library yaitu **tabulate**.

Tabulate ini digunakan untuk melakukan display table dalam format yang user-friendly.

---

# Penjelasan komponen sistem

---

## 1. User data

User data adalah tempat penyimpanan informasi user. User data ini nanti digunakan untuk mengakses Library System.

```python
users = {
    "visitor": {"username": "visitor", "password": "visit123"},
    "librarian": {"username": "librarian", "password": "lib123"}
}
```

Untuk project ini, user data akan bersifat statik untuk mempermudah penggunaan.

---

## 2. Book Dictionary

Book dictionary adalah sebuah collection data type dictionary yang digunakan untuk menyimpan koleksi buku-buku di dalam perpustakaan.

```python
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
```

Setiap koleksi yang ada di dalam books akan dipisah per genre dari buku tersebut dan memiliki unique identifier yaitu **book_id.**

---

## 3. Borrowed Book Dictionary

Borrowed book adalah sebuah dictionary kosong yang digunakan untuk menyimpan buku yang nantinya akan dipinjam oleh user **visitor**. 

```python
borrowedBooks = []
```

Dictionary ini akan diinisiasi empty.

---

## 4. Functions

Functions adalah core logic dari Library System. Functions mengatur pengolahan data dan interaksi dengan user. Dalam Library System terdapat sepuluh function.

- `displayBook()` ****→ display semua buku yang ada di library
- `generateBookId()` → generate id buku baru
- `addBook()` → menambah buku ke library
- `removeBook()` → delete buku dari library
- `borrowBook()` → meminjam buku dari library
- `viewBorrowBooks()` → melihat buku yang telah dipinjam
- `returnBook()` → mengembalikan buku yang dipinjam
- `login()` → login akses ke dalam Library System
- `logout()` ****→ logout dari system
- `mainMenu()` → menu utama untuk library system

---

# Penjelasan Function

---

## 1. Function `displayBook()`

```python
def displayBooks()
```

Function `displayBooks()` digunakan untuk mendisplay semua buku dalam library. Dalam function ini digunakan For loop untuk melakukan iterasi book dictionary yang nantinya data dari looping akan ditampilkan menggunakan fitur dari `tabulate` 

### displayBook main feature

```python
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
```

Dalam function ini buku akan ditampilkan berdasarkan genre dan **book_id** yang sudah disortir di variable `sortView` yang didalamnya menggunakan lambda function untuk melakukan pengambilan number dari book_id melalui perintah `.split(”-”)`

### Contoh penggunaan

```python
{"book_id": "01-FI-2003", "name": "Kisah Legenda Indonesia", "year": 2003, "status": "available"},
```

Saat menggunakan `.split(”-”)` , book_id akan terpisah menjadi collection type `{”01”, “FI”, “2003”}`. Lalu akan diambil index 0 yaitu **“01”.**

### displayBook empty checker

Dalam function `displayBook()` ada juga fitur cek empty yang berfungsi untuk mengecek genre kosong dalam dictionary **`books`** 

```python
isEmpty = []
    # Looping dictionary books dan add genre yang tidak memiliki book
    for genre, book in books.items():
        if not book:
            isEmpty.append(genre)
    # Loop jika ada genre lain yang kosong
    for genre in isEmpty:
        del books[genre]  
```

- Kode ini akan membuat empty dictionary yang kemudian akan diisi melalui For loop yang mengecek isi dari dictionary `books` .
    - jika tidak ada isi maka akan menambahkan genre kedalam `isEmpty` dan di delete dalam For loop kedua.

---

## 2. Function `generateBookId()`

```python
def generateBookId(genre, year): 
```

Function `generateBookId()` digunakan untuk automasi pembuatan book_id saat penambahan buku. Fungsi ini menggunakan parameter genre dan year yang nantinya akan digunakan dalam pembuatan book_id.

### generateBookId genre code slicing and find Id

```python
# Kode untuk mencari genreCode (slicing 2 huruf pertama dari genre)
    genreCode = genre[:2].upper()
    bookList = books.get(genre, [])
```

Dalam snippet ini, 

- parameter `genre` akan dislicing dimana dua huruf pertama dalam nama genre akan dimbil dan dikapitalkan. Lalu `bookList`  akan mengambil nama `genre` dan isinya.
    - `bookList` ini nantinya akan digunakan untuk For loop.

```python
# Kode untuk mencari book id
    existingId = [int(book["book_id"].split("-")[0]) for book in bookList]
```

Setelah slicing dan pembuatan bookList, `existingId` akan digunakan untuk mencari book_id dengan cara membuat dictionary yang berisi angka id dari For loop `book` dalam `bookList` .

### generateBookId bookId checking

```python
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
```

- Kode ini digunakan untuk mengecek Id buku. Jika `existingId` **kosong**, maka akan membuat `nextId` 1.
- Jika function menemukan existingId maka akan dilakukan pencarian `possibleId` menggunakan `set` dengan `range 1 sampai maxId +2` .
    - Dari hasil tersebut, `missingId` akan dicari dengan cara melakukan pengurangan set `possibleId` dengan `existingId`
    - Hasil dari pengurangan set akan dijadikan list dan disorting. Lalu `nextId` akan menjadi **index 0** dari `missingId`.
- Setelah mendapatkan `nextId`, fungsi If digunakan untuk mengecek apakah ada duplikasi dari Id. Jika ada `nextId` menjadi 1 lebih dari `existingId`.
    - Jika `nextId` sama dengan 0 maka `nextId` akan diubah menjadi 1 untuk menghindari kode buku 00.

### generateBookId return bookId

```python
# return id dengan format nextId-kode genre-tahun   
    return f"{nextId:02d}-{genreCode}-{year}"
```

Function akan diakhiri dengan return format `nextId`-genre-tahun.

## 3. Function `addBook()`

```python
def addBook():
```

Function `addBook()` adalah function khusus untuk user librarian yang digunakan untuk menambah buku kedalam `books` dictionary.

### addBook main feature

```python
genre = input("Masukkan genre buku baru:").title()
        
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
```

- User akan diminta untuk menginput `genre` buku yang dimana genre tidak bisa mengandung angka
    - Jika genre yang diinput belum ada maka function akan membuat genre baru.
- Kemudian user menginput judul buku yang akan ada dalam variabel `name` dan tahun terbit dalam `year`
    - Year harus berupa angka, jika tidak maka loop akan mengulang.

### addBook cek duplicate

```python
duplicate = False
        for book in books[genre]:
            if book["name"].lower() == name.lower():
                print("\nBuku dengan nama tersebut sudah ada dalam genre ini.\n")
                duplicate = True
                break
        
        if duplicate:
            continue
```

Setelah input informasi buku, akan ada pengecekan duplikasi judul dimana judul buku yang diinput akan dicek dengan nama buku dalam `books` dictionary.

- Jika duplikasi ditemukan, akan break loop dan kembali ke menu utama.

### addBook add buku baru ke `books` dictionary

```python
bookId = generateBookId(genre, year)
        books[genre].append({
            "book_id": bookId,
            "name": name,
            "year": int(year),
            "status": "available"
        })
        
        print(f"\nBuku '{name}' berhasil ditambahkan ke genre {genre} dengan id {bookId}!")
```

- Setelah pengecekan berhasil, function `generateBookId()` akan dipanggil dengan parameter `genre` dan `year` yang telah diinput sebelumnya.
- Buku baru kemudian di `append` ke dalam dictionary `books`.
- Pesan berhasil akan diprint setelah proses append.

### addBook repeat addition

```python
while True:
            repeat = input("Apakah anda ingin menambahkan buku lain? (ya/tidak): ").strip().lower()
            if repeat == "ya":
                break
            elif repeat == "tidak":
                print("\nKembali ke menu ...\n")
                return
            else:
                print("Input tidak valid. Ketik 'ya' atau 'tidak'\n")
```

Setelah buku berhasil diinput, pesan konfirmasi akan muncul.

- User harus menginput antara “ya” atau “tidak”. Jika user input “ya”, proses input buku akan berulang. Jika “tidak”, user akan kembali ke menu utama.
- Jika user menginput selain “ya” atau “tidak”, loop konfirmasi akan berulang.

---

## 4. Function `removeBook()`

```python
def removeBook():
```

Function `removeBook()` adalah function khusus user type Librarian yang digunakan untuk menghapus buku dari `books` dictionary.

### removeBook main feature

```python
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
```

- Function `displayBooks()` akan dipanggil untuk referensi user.
- User diminta untuk input judul buku yang mau dihapus.
- For loop akan diiterasi untuk mencari judul buku di dalam `books` dictionary.
    - Jika judul buku ditemukan, loop akan di break.

---

## 5. Function `borrowBook()`

```python
def borrowBook():
```

Function `borrowBook()` adalah function khusus user type Visitor yang digunakan untuk meminjam buku dari `books` dictionary.

### borrowBook input book

```python
displayBooks()
        name = input("Masukkan nama buku yang ingin dipinjam: (tulis 'selesai' untuk kembali ke menu)")
        if name.lower() == "selesai":
            break
```

- User diminta untuk menginput judul buku yang mau dipinjam
    - User bisa input “selesai” jika ingin kembali ke menu.

### borrowBook main feature

```python
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
```

- For loop akan dilakukan untuk mencari buku dalam `books` dictionary sesuai dengan judul yang diinput.
- Jika status buku “available”, buku akan di append ke dictionary `borrowedBooks`.
    - Jika status “unavailable” function akan print “Maaf, buku tidak tersedia”.

---

## 6. Function `viewBorrowedBooks()`

```python
def viewBorrowedBooks():
```

Function `viewBorrowedBooks()` adalah function khusus user type Visitor yang digunakan untuk melihat buku yang telah dipinjam.

### viewBorrowedBooks main feature

```python
if not borrowedBooks:
        print("\nAnda belum meminjam buku apapun.\n")
    else:
        print("\n=== Buku Yang Anda Pinjam ===")
        headers = ["Book Id", "Judul", "Tahun Publikasi"]
        table = [[book["book_id"], book["name"], book["year"]] for book in borrowedBooks]
        print(tabulate(table, headers=headers, tablefmt="grid"))
```

- Function akan mengecek apakah list `borrowedBooks` memiliki isi buku.
- Jika buku ditemukan dalam list, function akan iterasi buku dari `borrowedBooks`

---

## 7. Function `returnBook()`

```python
def returnBook():
```

Function `returnBook()` adalah function khusus user type Visitor yang digunakan untuk mengembalikan buku yang dipinjam.

### returnBook main feature

```python
viewBorrowedBooks()     
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
```

- Function akan memanggil `viewBorrowedBooks()` untuk referensi user.
- User diminta input judul buku yang ingin dikembalikan.
- Function akan melakukan For loop untuk mencari judul buku didalam `borrowBooks` list.
    - Jika judul buku sesuai dengan input, status buku akan diubah menjadi available dan dihapus dari `borrowedBooks` list.

---

## 8. Function `login()`

```python
def login():
```

Function `login()` adalah function umum yang digunakan oleh semua user type untuk mengakses Library System.

### login main feature

```python
		username = None
    password = None
    for i in range(3):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in users and users[username]["password"] == password:
            print(f"\nLogin berhasil! selamat datang di sistem perpustakaan, {username.capitalize()}")
            return username
        else:
            print("Username atau password salah.\n")
    print("Gagal login setelah 3 kali percobaan.")
```

- Username dan password di set none
- User diminta input username dan password
    - User hanya diberi maksimal attempt tiga kali, jika lebih dari tiga kali attempt sistem akan terminate otomatis.
    - Jika username atau password salah, function akan iterasi ulang.
    - Jika login berhasil, function akan return `username` yang nanti akan digunakan di function `mainMenu()`.

---

## 9. Function `logout()`

```python
def logout():
```

Function `logout()` adalah function umum yang digunakan oleh semua user type untuk kembali ke halaman login.

### logout main feature

```python
print("Kembali ke halaman login ...\n")
    return None
```

- Function akan mengembalikan None yang nantinya akan digunakan dalam `mainMenu` function untuk reset user.

---

## 10. Function `mainMenu()`

```python
def mainMenu():
```

Function `mainMenu()` adalah function utama dari Library System dimana user bisa berinteraksi dengan sistem.

### mainMenu main feature

```python
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
```

- `User` akan diset default sebagai `None`.
- Kondisi If akan otomatis terpenuhi dan menampilkan prompt dari `login()` function.
- Setelah login `user` akan terset menjadi username pengguna (antara “visitor” atau “librarian”.
- Function akan menampilkan menu pilihan berdasarkan value`user`.
