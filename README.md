# Library system for Capstone Project 1

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

Kode ini akan membuat empty dictionary yang kemudian akan diisi melalui For loop yang mengecek isi dari dictionary `books` , jika tidak ada isi maka akan menambahkan genre kedalam `isEmpty` dan di delete dalam For loop kedua.

---

## 2. Function `generateBookId()`

```python
def generateBookId(genre, year): 
```

Fungsi ini digunakan untuk automasi pembuatan book_id saat penambahan buku. Fungsi ini menggunakan parameter genre dan year yang nantinya akan digunakan dalam pembuatan book_id.

### generateBookId genre code slicing and find Id

```python
# Kode untuk mencari genreCode (slicing 2 huruf pertama dari genre)
    genreCode = genre[:2].upper()
    bookList = books.get(genre, [])
```

Dalam snippet ini, parameter `genre` akan dislicing dimana dua huruf pertama dalam nama genre akan dimbil dan dikapitalkan. Lalu `bookList`  akan mengambil nama `genre` dan isinya. `bookList` ini nantinya akan digunakan untuk For loop.

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
