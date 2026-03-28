import psycopg2
from config import load_config

def update_contact(contact_change_attribute, contact_new_info, contact_number, contact_first_name):
    config = load_config()
    updated_row_count = 0

    if contact_number and contact_first_name == None:
        sql = f"""
            update contacts 
            set {contact_change_attribute}='{contact_new_info}'
            where contact_number='{contact_number}'
        """
    else:
        sql = f"""
            update contacts 
            set {contact_change_attribute}='{contact_new_info}'
            where contact_first_name='{contact_first_name}'
        """
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, None)
                updated_row_count = cursor.rowcount
            conn.commit()
            if updated_row_count == 0:
                print("[Error] There is no row updated. Make sure you have inputted the data correctly!")
            else:
                print(f"[Success] The update operation have completed successfully: attribute {contact_change_attribute}'s value -> {contact_new_info}")
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback() # transaction method
        print(error)
    finally:
        return updated_row_count