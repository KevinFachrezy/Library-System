Library system for Capstone Project 1

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

- displayBook() → display semua buku yang ada di library
- generatedBookId() → generate id buku baru
- addBook() → menambah buku ke library
- removeBook() → delete buku dari library
- borrowBook() → meminjam buku dari library
- viewBorrowBooks() → melihat buku yang telah dipinjam
- returnBook() → mengembalikan buku yang dipinjam
- login() → login akses ke dalam Library System
- logout() → logout dari system
- mainMenu() → menu utama untuk library system

---
