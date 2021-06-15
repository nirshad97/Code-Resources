import sqlite3


def create_table():
    table_query = """
    CREATE TABLE "Seat" (
        "seat_id" TEXT,
        "taken" INTEGER,
        "price" REAL
    );
    """

    connection = sqlite3.connect("cinema.db")
    connection.execute(table_query)
    connection.commit()
    connection.close()


def insert_record():

    insert_query = """
    INSERT INTO "Seat" ("seat_id", "taken", "price")  
    VALUES ("A1", "0", "90"),
        ("A2", "1", "190"),
        ("A3", "0", "100")              
    """

    connection = sqlite3.connect("cinema.db")
    connection.execute(insert_query)
    connection.commit()
    connection.close()


def select_all():
    select_all_query = """
    SELECT * FROM "Seat"
    """

    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(select_all_query)
    result = cursor.fetchall()
    connection.close()
    return result


def select_specific():
    select_specific_query = """
    SELECT "seat_id", "price" FROM "Seat"
    """

    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(select_specific_query)
    result = cursor.fetchall()
    connection.close()
    return result


def conditional_select():
    conditional_select_query = """
    SELECT "seat_id", "price" FROM "Seat" WHERE "price" >= 100
    """

    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(conditional_select_query)
    result = cursor.fetchall()
    connection.close()
    return result


def update_value(occupied, seat_id):
    # Dynamically update values
    update_query = """
    UPDATE "Seat" SET "taken"=? WHERE "seat_id" = ?
    """

    connection = sqlite3.connect('cinema.db')
    connection.execute(update_query, [occupied, seat_id])
    connection.commit()
    connection.close()


def delete_value():
    delete_query = """
    DELETE FROM "Seat" WHERE "seat_id" = "A3"
    """
    connection = sqlite3.connect('cinema.db')
    connection.execute(delete_query)
    connection.commit()
    connection.close()


insert_record()

print(select_specific())
print(conditional_select())
update_value(occupied=0, seat_id="A2")
print(select_all())
delete_value()
