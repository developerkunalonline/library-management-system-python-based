import mysql
from book import Book, create_book, TABLE_NAME, create_book_table, print_header
NUMBER_OF_RECORDS_PER_PAGE = 10


def add_book(database, cursor):
    book = create_book()
    query = "insert into {0}(title,author,topic,available) values('{1}','{2}','{3}',{4})".\
            format(TABLE_NAME, book.title, book.author, book.topic, book.available)
    try:
        cursor.execute(query)
        database.commit()
    except mysql.connector.Error as err:
        create_book_table(database)
        cursor.execute(query)
        database.commit()
    print("Operation Successful")


def show_record(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        record = records[0]
        book = Book().create_from_record(record)
        book.print_full()
        return book
    except mysql.connector.Error as err:
        print(err)


def show_records(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        print_header()
        for record in records:
            book = Book().create_from_record(record)
            book.print_all()
        return records
    except mysql.connector.Error as err:
        print(err)


def get_and_print_book_by_id(cursor):
    book_id = int(input("Enter the book id: "))
    query = "select * from {0} where id={1}".format(TABLE_NAME, book_id)
    book = show_record(cursor, query)
    return book


def edit_by_book_id(database, cursor):
    book = get_and_print_book_by_id(cursor)
    if book is not None:
        query = "update {0} set".format(TABLE_NAME)
        print("Input new values (leave blank to keep previous value)")
        title = input("Enter new book title: ")
        if len(title) > 0:
            query += " title='{0}',".format(title)
        author = input("Enter new author: ")
        if len(author) > 0:
            query += " author='{0}',".format(author)
        topic = input("Enter new topic: ")
        if len(topic) > 0:
            query += " topic='{0}',".format(topic)
        query = query[0:-1] + " where id={0}".format(book.book_id)
        confirm = input("Confirm Update (Y/N): ").lower()
        if confirm == 'y':
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def change_book_status(database, cursor, book_id, available):
    query = "update {0} set available={1} where id={2}".format(TABLE_NAME, available, book_id)
    cursor.execute(query)
    database.commit()


def delete_by_book_id(database, cursor):
    book = get_and_print_book_by_id(cursor)
    if book is not None:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME, book.book_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def book_menu(database, cursor):
    while True:
        print()
        print("============================")
        print("==========Books Department=========")
        print("============================")
        print()

        print("1. Add new book")
        print("2. Get book details by book id")
        print("3. Search a book by title or topic")
        print("4. Edit Book details")
        print("5. Delete Book")
        print("6. View all Books")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book(database, cursor)
        elif choice == 2:
            get_and_print_book_by_id(cursor)
        elif choice == 3:
            topic = input("Enter a part of the book title or topic: ")
            query = "select * from {0} where title like '%{1}%' or topic like '%{1}%'".format(TABLE_NAME, topic)
            show_records(cursor, query)
        elif choice == 4:
            edit_by_book_id(database, cursor)
        elif choice == 5:
            delete_by_book_id(database, cursor)
        elif choice == 6:
            query = "select * from {0}".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
