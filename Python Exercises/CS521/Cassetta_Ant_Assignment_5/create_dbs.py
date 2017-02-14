import sqlite3
import collections

def create_baseball_db(database='baseball_stats.db'):
    '''1. baseball_conn connects to a database
    2. baseball_cursor points to the beginning of the database'''

    baseball_conn = sqlite3.connect(database)
    baseball_cursor = baseball_conn.cursor()
    return baseball_conn, baseball_cursor

conn_to_baseball, cursor_baseball = create_baseball_db()


def create_baseball_table(a_table_name='baseball_stats', a_connection=conn_to_baseball, a_cursor=cursor_baseball):
    '''create_db: A table named a_table_name is in the database with
    connection a_connection
    create_baseball_table: Table a_table_name has a_num_fields fields named 's1', 's2, ...
    '''

    # creation_str is the creation string for Post1 and 2
    creation_str = ('CREATE TABLE IF NOT EXISTS ' + a_table_name +
                    ' (player_name TEXT, salary REAL, games_played REAL, average REAL)')

    # Post1, 2 and a trace is on the monitor
    print(creation_str)
    a_cursor.execute(creation_str)
    a_connection.commit()  # save changes
    print('table ' + a_table_name + ' created')

create_baseball_table()


def create_stock_db(database='stock_stats.db'):
    '''1. baseball_conn connects to a database
    2. baseball_cursor points to the beginning of the database'''

    stock_conn = sqlite3.connect(database)
    stock_cursor = stock_conn.cursor()
    return stock_conn, stock_cursor

conn_to_stock, cursor_stock = create_stock_db()


def create_stock_table(a_table_name='stock_stats', a_connection=conn_to_stock, a_cursor=cursor_stock):
    '''create_db: A table named a_table_name is in the database with
    connection a_connection
    create_baseball_table: Table a_table_name has a_num_fields fields named 's1', 's2, ...
    '''

    # creation_str is the creation string for Post1 and 2
    creation_str = ('CREATE TABLE IF NOT EXISTS ' + a_table_name +
                    '(ticker TEXT, country TEXT, price REAL, exchange_rate REAL,' +
                    'shares_outstanding REAL, net_income REAL, market_value REAL, pe_ratio REAL)')

    # Post1, 2 and a trace is on the monitor
    print(creation_str)
    a_cursor.execute(creation_str)
    a_connection.commit()  # save changes
    print('table ' + a_table_name + ' created')

create_stock_table()

cursor_baseball.close()
conn_to_baseball.close()
cursor_stock.close()
conn_to_stock.close()