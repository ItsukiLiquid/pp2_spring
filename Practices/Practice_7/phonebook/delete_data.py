import psycopg2
from config import load_config

def delete_contact(first_name, number):
    config = load_config()
    if first_name and number == None:
        sql = """
            delete from contacts where contact_first_name=%s
        """
    else:
        sql = """
            delete from contacts where contact_number=%s
        """
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                if first_name and number == None:
                    cursor.execute(sql, (first_name,))
                    deleted_row_count = cursor.rowcount
                    if deleted_row_count == 0:
                        print("[Error] No contact deleted. Please ensure you've typed the data correct!")
                    else:
                        print(f"[Success] Successfully deleted row with first name '{first_name}'")
                else:
                    cursor.execute(sql, (number,))
                    deleted_row_count = cursor.rowcount
                    if deleted_row_count == 0:
                        print("[Error] No contact deleted. Please ensure you've typed the data correct!")
                    else:
                        print(f"[Success] Successfully deleted row with number '{number}'")
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()
        print(error)