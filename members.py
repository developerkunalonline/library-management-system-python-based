from datetime import datetime

import mysql

from member import Member, create_member, TABLE_NAME, create_members_table, print_header, MEMBERSHIP_PERIOD
NUMBER_OF_RECORDS_PER_PAGE = 10


def add_member(database, cursor):
    member = create_member()
    confirm = input("Complete the operation? (Y/N) ").lower()
    if confirm == 'y':
        query = "insert into {0}(name, address, phone, joining,valid_till) values('{1}','{2}','{3}','{4}','{5}')". \
            format(TABLE_NAME, member.name, member.address, member.phone,
                   member.joining_date.strftime("%Y-%m-%d %H:%M:%S"),
                   member.valid_till.strftime("%Y-%m-%d %H:%M:%S"))
        try:
            cursor.execute(query)
            database.commit()
        except mysql.connector.Error:
            create_members_table(database)
            cursor.execute(query)
            database.commit()
        print("Operation Successful")
    else:
        print("Operation Canceled")


def show_records(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        print_header()
        for record in records:
            member = Member().create_from_record(record)
            member.print_all()
        return records
    except mysql.connector.Error as err:
        print(err)


def show_record(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        record = records[0]
        member = Member().create_from_record(record)
        member.print_full()
        return member
    except mysql.connector.Error as err:
        print(err)


def get_and_print_member_by_id(cursor):
    member_id = input("Enter the member id: ")
    query = "select * from {0} where id = {1}".format(TABLE_NAME, member_id)
    member = show_record(cursor, query)
    return member


def extend_membership_by_id(database, cursor):
    member = get_and_print_member_by_id(cursor)
    if member is not None:
        query = "update {0} set valid_till = date_add(valid_till, INTERVAL {1} MONTH) where id={2}"\
            .format(TABLE_NAME,MEMBERSHIP_PERIOD,member.member_id)
        confirm = input("Confirm Update (Y/N): ").lower()
        if confirm == 'y':
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def edit_by_member_by_id(database, cursor):
    member = get_and_print_member_by_id(cursor)
    if member is not None:
        query = "update {0} set".format(TABLE_NAME)
        print("Input new values (leave blank to keep previous value)")
        name = input("Enter new name: ")
        if len(name) > 0:
            query += " name='{0}',".format(name)
        address = input("Enter new address: ")
        if len(address) > 0:
            query += " address='{0}',".format(address)
        phone = input("Enter phone number: ")
        if len(phone) > 0:
            query += " phone='{0}',".format(phone)
        query = query[0:-1] + " where id={0}".format(member.member_id)
        confirm = input("Confirm Update (Y/N): ").lower()
        if confirm == 'y':
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def delete_by_member_id(database, cursor):
    member = get_and_print_member_by_id(cursor)
    if member is not None:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME, member.member_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def member_menu(database, cursor):
    while True:
        print()
        print("==============================")
        print("==========Member Department=========")
        print("==============================")
        print()
        print("1. New Member")
        print("2. Show Member Details by name")
        print("3. Show Member details by member id")
        print("4. Show Member details by address")
        print("5. Show Member details by phone number")
        print("6. Extend Membership")
        print("7. Edit Member Details")
        print("8. Delete Member record")
        print("9. View all customers")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_member(database, cursor)
        elif choice == 2:
            name = input("Enter the name: ").lower()
            query = "select * from {0} where name like '%{1}%'".format(TABLE_NAME, name)
            show_records(cursor, query)
        elif choice == 3:
            get_and_print_member_by_id(cursor)
        elif choice == 4:
            address = input("Enter the address: ").lower()
            query = "select * from {0} where address like '%{1}%'".format(TABLE_NAME, address)
            show_records(cursor, query)
        elif choice == 5:
            phone = input("Enter the phone number: ")
            query = "select * from {0} where phone like '%{1}%'".format(TABLE_NAME, phone)
            show_records(cursor, query)
        elif choice == 6:
            extend_membership_by_id(database, cursor)
        elif choice == 7:
            edit_by_member_by_id(database, cursor)
        elif choice == 8:
            delete_by_member_id(database, cursor)
        elif choice == 9:
            query = "select * from {0}".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
