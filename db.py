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

def execute_session(ip, executed_at, machine_id, execution_log):

    conn = get_db_connection()
    cur = conn.cursor()
    executed_at_str  = datetime.strptime(executed_at, "%Y-%m-%dT%H:%M:%S.%f")
    try:
        cur.execute("INSERT INTO session_execution (ip, executed_at, machine_id, execution_log) VALUES (%s, %s, %s, %s) RETURNING id;", (ip, executed_at_str, machine_id, execution_log))
        conn.commit()
        session_execution_id = cur.fetchone()[0]
        print('Pulse succefully executed.')
    except psycopg2.Error as e:
        conn.rollback()
        print(f'Error executing pulse: {e}')
        raise
    finally:
        cur.close()
        conn.close()
    
    return session_execution_id

def create_task(task_name, task_metadata):
    
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO task (task_name, task_metadata) VALUES (%s, %s) RETURNING id;", (task_name, task_metadata))
        conn.commit()
        session_execution_id = cur.fetchone()[0]
        print('Pulse succefully executed.')
    except psycopg2.Error as e:
        conn.rollback()
        print(f'Error executing pulse: {e}')
        raise
    finally:
        cur.close()
        conn.close()
    
    return session_execution_id

def get_all_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, task_metadata FROM task;')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    print(tasks)
    return tasks

def get_task(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, task_metadata FROM task WHERE id = %s;',(id,))
    task = cur.fetchone()
    cur.close()
    conn.close()
    return task

def get_session_config(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT task_metadata FROM session_config WHERE id = %s;',(id,))
    session_config = cur.fetchone()
    cur.close()
    conn.close()
    return session_config

def get_all_sessions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, task_metadata FROM session_config')
    sessions = cur.fetchall()
    cur.close()
    conn.close()
    return sessions

def get_task_schedule(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT task_id, task_schedule FROM task_schedule WHERE task_id = %s;',(task_id,))
    task_schedule = cur.fetchone()
    cur.close()
    conn.close()
    return task_schedule