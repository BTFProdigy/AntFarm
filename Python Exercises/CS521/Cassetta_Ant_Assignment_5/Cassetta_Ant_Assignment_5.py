import csv
import os
import sqlite3
import collections


class BadData(Exception):
    """This class is an exception used to handle incomplete or corrupt data within imported file"""
    def __init__(self):
        print('Bad data was found')


class UserChoice:
    """This class ask's user for file to load. Parse response. return filename"""
    def __init__(self):
        pass

    def ask_user(self):

        while True:
            try:
                user_file = input('What file do you want to open? "StockValuations" or "MLB2008"')
                user_file = str(user_file).strip('"')
                if user_file == 'StockValuations' or user_file == 'MLB2008':
                    user_choice_ = ('/' + user_file + '.csv')
                    return user_choice_
                elif 'mlb' in user_file:
                    user_choice_ = '/MLB2008.csv'
                    return user_choice_
                elif 'stock' in user_file:
                    user_choice_ = '/StockValuations.csv'
                    return user_choice_
                else:
                    print("I didn't get that")
            except Exception as error:
                print(str(error) + 'file name error')


class PackageHome:
    """Identify package location, confirm resource data directory is present. Return directory path. """
    def __init__(self):
        pass

    def data_resource_file(self):
        self.module_home = os.path.abspath(os.curdir)  # gather file location
        if os.path.exists(self.module_home + '/Data'):
            self.resource_file = os.path.abspath(self.module_home + '/Data')
            return self.resource_file
        else:
            print('Please place the file %s' % self.module_home + '/Data')


class AbstractRecord:
    """Parent class to child records. Takes 1 arg, name as a label to each record."""
    def __init__(self, name_from_child):
        self.name = name_from_child


class BaseballStatRecord(AbstractRecord):
    """Child of AbstractRecord, takes 4 args: player - is passed up to the parent class member name.
    salary - player salary. G - number of games played, AVG - the players batting average.
    This class is not meant to be called directly it is meant to by called by the load method within the
    AbstractCSVReader class or a child of it."""

    def __init__(self,PLAYER, SALARY, G, AVG):
        super().__init__(PLAYER)
        self.salary = '{:.2f}'.format(SALARY)
        self.games_played = G.__str__()
        self.average = '{:.2f}'.format(AVG)

    def __str__(self):
        return ('MLB record ({}, {}, {}, {})').format(self.name, self.salary, self.games_played, self.average)


class StockStatRecord(AbstractRecord):
    """Child of AbstractRecord, takes 8 args: ticker - is passed up to the parent class member name. exchange_country,
    price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio.
    This class is not meant to be called directly it is meant to by called by the load method within the
    AbstractCSVReader class or a child of it."""

    def __init__(self, ticker, exchange_country,
                 price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio):
        super().__init__(ticker)
        self.exchange_country = exchange_country.__str__()
        self.price = '{:.2f}'.format(price)
        self.exchange_rate = '{:.2f}'.format(exchange_rate)
        self.shares_outstanding = '{:.2f}'.format(shares_outstanding)
        self.net_income = '{:.2f}'.format(net_income)
        self.market_value_usd = '{:.2f}'.format(market_value_usd)
        self.pe_ratio = '{:.2f}'.format(pe_ratio)

    def __str__(self):
        return ('Stock record ({}, {}, {}, {}, {}, {}, {}, {})'.format(self.name, self.exchange_country,
                                                                       self.price, self.exchange_rate,
                                                                       self.shares_outstanding, self.net_income,
                                                                       self.market_value_usd, self.pe_ratio))


class AbstarctCSVReader:
    """This is a parent class. This class hold the methods to load and record data from a CSV.
     The row_to_record method is meant to be overridden by each  child.
     The load method reads each row of the CSV and passes that data to the row_to_record method which will parse
     and validate the data, if the data row can not be validated it will be skipped.
     load will return a list of the class instances."""

    def __init__(self, csv_path):
        try:
            if os.path.exists(csv_path):
                print("Data file located.\n")
            else:
                raise BadData
        except Exception as error:
            print(error)

    def row_to_record(self, given_row):
        raise NotImplementedError

    def load(self, file_source):
        instance_list = []
        try:
            with open(file_source, 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    try:
                        new_object = self.row_to_record(row)
                        if new_object is not None:
                            instance_list.append(new_object)
                        else:
                            pass
                    except Exception:
                        pass
        except Exception:
            print('broke in the abstract')
        finally:
            csv_file.close()
            return instance_list


class BaseballCSVReader(AbstarctCSVReader):
    """Child class of AbstractCSVReader. This class hold the methods to load and record data from a CSV.
         The load method reads each row of the CSV and passes 4 specific args* to the row_to_record method.
         row_to_record validates the data and creates an instance of the record by calling BaseballStatRecord,
         this instance is returned to the load method.
         Should the data fail validation the load method will skip that row. the returned instances are appended
         to a list and returned to the main.
         *args(PLAYER- player name, SALARY-  player salary G- Games played, AVG- Batting average)"""

    def __init__(self, csv_path):
        super().__init__(csv_path)

    def row_to_record(self, given_row):
        try:
            if given_row['PLAYER'] == '' or given_row['SALARY'] == '' or given_row['G'] == '' or given_row['AVG'] == '':
                raise BadData()
            else:
                try:
                    player_name = given_row['PLAYER']
                    player_salary = float(given_row['SALARY'])
                    player_games = float(given_row['G'])
                    player_average = float(given_row['AVG'])

                    return BaseballStatRecord(player_name, player_salary, player_games, player_average)
                except Exception as error:
                    print(error)
        except Exception as error:
            print(error)


class StocksCSVReader(AbstarctCSVReader):
    """Child class of AbstractCSVReader. This class hold the methods to load and record data from a CSV.
             The load method reads each row of the CSV and passes 8 specific args* to the row_to_record method.
             row_to_record validates the data and creates an instance of the record by calling StockStatRecord,
             this instance is returned to the load method.
             Should the data fail validation the load method will skip that row. The returned instances are appended
             to a list and returned to the main.
             *args(ticker, exchange_country, price, ExchangeRate, SharesOutstanding, NetIncome,
             calc_market_value_usd, pe_ratio - price to earning ratio)"""

    def __init__(self, csv_path):
            super().__init__(csv_path)

    def row_to_record(self, given_row):
        try:
            if given_row['ticker'] == '' or given_row['exchange_country'] == '' or given_row['price'] == '' \
                or given_row['price'] == '#DIV/0!' or given_row['exchange_rate'] == ''\
                    or given_row['shares_outstanding'] == '' or given_row['net_income'] == '':
                raise BadData
            else:
                try:
                    ticker = given_row['ticker']
                    exchange_country = given_row['exchange_country']
                    price = float(given_row['price'])
                    ExchangeRate = float(given_row['exchange_rate'])
                    SharesOutstanding = float(given_row['shares_outstanding'])
                    NetIncome = float(given_row['net_income'])

                    calc_market_value_usd = price * ExchangeRate * SharesOutstanding
                    pe_ratio = price * SharesOutstanding / NetIncome

                    return StockStatRecord(ticker, exchange_country, price, ExchangeRate, SharesOutstanding,
                                                       NetIncome, calc_market_value_usd, pe_ratio)
                except Exception as error:
                    print(error)
        except Exception as error:
            print(error)


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
            self.cursor.execute('INSERT INTO baseball_stats VALUES( ?, ?, ?, ?)', (row.name, row.salary,
                                                                                   row.games_played, row.average))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def select_all(self):
        self.connection = self.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.baseball_deque = collections.deque()
        self.cursor.execute("SELECT player_name, salary, games_played, average  FROM baseball_stats;")

        for row in self.cursor.fetchall():
            new_class = BaseballStatRecord(row[0], row[1], row[2], row[3])
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
            new_class = StockStatRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            self.stock_deque.append(new_class)
        self.cursor.close()
        self.connection.close()
        return self.stock_deque


def loader():
    try:
        FileLocation = PackageHome.data_resource_file(PackageHome)
        #print(FileLocation)
        UserFileChoice = UserChoice.ask_user(UserChoice)
        print(UserFileChoice)

        if UserFileChoice == '/StockValuations.csv':
            Stock_chosen = StocksCSVReader(FileLocation + UserFileChoice)
            CSVStockData = Stock_chosen.load(FileLocation + UserFileChoice)

            stocks_data = StockStatDOA('stock_stats.db')
            stocks_data.insert_records(CSVStockData)
            stock_deque = stocks_data.select_all()

            stock_dict = collections.defaultdict(list)

            for row in stock_deque:
                if row.exchange_country in stock_dict.keys():
                    stock_dict[row.exchange_country].append([row.name])
                else:
                    stock_dict[row.exchange_country] = ([row.name])

            for key in stock_dict:
                print('The key is: {} with count: {}\n'.format(str(key), str(len(stock_dict[key]))))

        elif UserFileChoice == '/MLB2008.csv':
            Stock_chosen = BaseballCSVReader(FileLocation + UserFileChoice)
            CSVMLBData = Stock_chosen.load(FileLocation + UserFileChoice)

            mlb_data = BaseballStatsDAO('baseball_stats.db')
            mlb_data.insert_records(CSVMLBData)
            mlb_deque = mlb_data.select_all()

            mlb_dict = collections.defaultdict(list)
            for row in mlb_deque:
                if row.name not in mlb_dict.keys():
                    mlb_dict[row.name] = ([row.salary, row.average])
                else:
                    pass

            player_salary_list = []
            for player, value in mlb_dict.items():
                player_salary_list.append(float(value[0]))
            salary_total = sum(player_salary_list)
            salary_avg = round(salary_total / float(len(player_salary_list)), 3)

            print('\nNumber of MLB players {}, MLB average salary ${}\n'.format(len(player_salary_list), salary_avg))
            for player in mlb_dict:
                print('Player: {}, {} by player batting average: {}\n'
                      .format(player, salary_avg, round((salary_avg * float(mlb_dict[player][1])), 3)))


    except Exception as error:
        print(error)


print('Which would you like to load first?')
loader()

print('Now load your second option.')
loader()