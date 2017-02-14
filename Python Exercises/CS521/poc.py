import sqlite3
import collections
import Cassetta_Ant_Assignment_4 as a4


class AbstractDAO:
    def __init__(self, database):
        self.db_name = database

    def insert_records(self, records):
        raise NotImplementedError

    def select_all(self):
        raise NotImplementedError

    def connect(self, db_name):
        return sqlite3.connect(db_name)


class BaseballStatsDAO(AbstractDAO):
    def __init__(self, database):
        super().__init__(database)

    def insert_records(self, records):
        self.connection = self.connect(self.db_name)
        self.cursor = self.connection.cursor()
        for row in records:
            self.cursor.execute('INSERT INTO baseball_stats VALUES( ?, ?, ?, ?)', (row.name, row.games_played,
                                                                                   row.average, row.salary))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def select_all(self):
        self.connection = self.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.baseball_deque = collections.deque()
        self.cursor.execute("SELECT player_name, games_played, average, salary FROM baseball_stats;")

        for row in self.cursor.fetchall():
            new_class = a4.BaseballStatRecord(row[0], row[1], row[2], row[3])
            self.baseball_deque.append(new_class)
        self.cursor.close()
        self.connection.close()
        return self.baseball_deque


class StockStatDOA(AbstractDAO):
    def __init__(self, database):
        super().__init__(database)

    def insert_records(self, records):
        self.connection = self.connect(self.db_name)
        self.cursor = self.connection.cursor()
        for row in records:
            self.cursor.execute('INSERT INTO stock_stats VALUES(?,?,?,?,?,?,?,?)',(row.name, row.exchange_country,
                                                                                   row.price, row.exchange_rate,
                                                                                   row.shares_outstanding,
                                                                                   row.net_income,
                                                                                   row.market_value_usd, row.pe_ratio))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def select_all(self):
        self.connection = self.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.stock_deque = collections.deque()
        self.cursor.execute("SELECT ticker, country, price, exchange_rate, shares_outstanding, net_income,"
                            " market_value, pe_ratio FROM stock_stats;")

        for row in self.cursor.fetchall():
            new_class = a4.StockStatRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            self.stock_deque.append(new_class)
        self.cursor.close()
        self.connection.close()
        return self.stock_deque


stocks_from_csv = a4.loader()
stocks_data = StockStatDOA('stock_stats.db')
stocks_data.insert_records(stocks_from_csv)
stock_deck = stocks_data.select_all()
#  for i in stock_deck: print(i)


mlb_from_csv = a4.loader()
mlb_data =BaseballStatsDAO('baseball_stats.db')
mlb_data.insert_records(mlb_from_csv)
mlb_deck = mlb_data.select_all()
#  for i in mlb_deck: print(i)

stocks_dict = {}
for row in stock_deck:
    stocks_dict[row.exchange_country] = stocks_dict[row.exchange_country].appened([row.name, row.price,
                                                                                   row.exchange_rate,
                                                                                   row.shares_outstanding,
                                                                                   row.net_income,
                                                                                   row.market_value_usd,
                                                                                   row.pe_ratio])
print(stocks_dict)