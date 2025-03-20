class Book:
    def __init__(self, title, author, is_borrowed= False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Đã thêm sách{book.title} - {book.author}")
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Bạn đã mượn sách {title}")
            return
        print(f"Sách {title} không có sẵn hoặc đã được mượn!")
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = False
                print(f"Trả sách {title} thành công")
                return
            print(f"Không tìm thấy sách {title} trong danh sách mượn")
    def list_books(self):
        if not self.books:
            print("Thư viện hiện chưa có sách nào")
            return
        print("Danh sách trong thư viện:")
        for book in self.books:
            status = "Có sẵn" if not book.is_borrowed else "Đã mượn"
            print(f"{book.title} - {book.author} - {status}")
lib = Library()
book1 = Book("Lập trình Python", "Nguyễn Văn A")
book2 = Book("Học Machine Learning", "Trần Văn B")
lib.add_book(book1)
lib.add_book(book2)
lib.list_books()
lib.borrow_book("Python")
lib.return_book("Python")
lib.list_books()
lib.list_books()

