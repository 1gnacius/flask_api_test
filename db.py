# db.py

from datetime import datetime

import psycopg2

from config import DATABASE


def get_db_connection():
    conn = psycopg2.connect(**DATABASE)
    return conn

def get_all_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return items

def get_all_machine_pulses():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM machine_pulse;')
    machine_pulses = cur.fetchall()
    cur.close()
    conn.close()
    return machine_pulses

def create_item(name, description):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id;', (name, description))
    item_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return item_id

def execute_machine_pulse(ip, executed_at, machine_id):
    conn = get_db_connection()
    cur = conn.cursor()
    executed_at_str  = datetime.strptime(executed_at, "%Y-%m-%dT%H:%M:%S.%f")
    try:
        cur.execute("INSERT INTO machine_pulse (ip, executed_at, machine_id) VALUES (%s, %s, %s) RETURNING id;", (ip, executed_at_str, machine_id))
        conn.commit()
        machine_pulse_id = cur.fetchone()[0]
        print('Pulse succefully executed.')
    except psycopg2.Error as e:
        conn.rollback()
        print(f'Error executing pulse: {e}')
        raise
    finally:
        cur.close()
        conn.close()
    
    return machine_pulse_id
