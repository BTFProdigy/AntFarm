import csv
import os


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

    def DataFile(self):
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
        self.salary = '{:,.2f}'.format(SALARY)
        self.games_played = G.__str__()
        self.average = '{:,.2f}'.format(AVG)

    def __str__(self):
        return ('MLB stat record (Player Name: {},'
                ' Salary: {}, Number of games played: {},'
                ' Batting average: {})').format(self.name, self.salary, self.games_played, self.average)


class StockStatRecord(AbstractRecord):
    """Child of AbstractRecord, takes 8 args: ticker - is passed up to the parent class member name. exchange_country,
    price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio.
    This class is not meant to be called directly it is meant to by called by the load method within the
    AbstractCSVReader class or a child of it."""

    def __init__(self, ticker, exchange_country,
                 price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio):
        super().__init__(ticker)
        self.exchange_country = exchange_country.__str__()
        self.price = '{:,.2f}'.format(price)
        self.exchange_rate = '{:,.2f}'.format(exchange_rate)
        self.shares_outstanding = '{:,.2f}'.format(shares_outstanding)
        self.net_income = '{:,.2f}'.format(net_income)
        self.market_value_usd = '{:,.2f}'.format(market_value_usd)
        self.pe_ratio = '{:,.2f}'.format(pe_ratio)

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
                print("Data file located.")
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
            return instance_list
            csv_file.close()


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


def loader():
    is_load = None
    while is_load != 'no':
        try:
            FileLocation = PackageHome.DataFile(PackageHome)
            print(FileLocation)
            UserFileChoice = UserChoice.ask_user(UserChoice)
            print(UserFileChoice)

            if UserFileChoice == '/StockValuations.csv':
                Stock_chosen = StocksCSVReader(FileLocation + UserFileChoice)
                StockData = Stock_chosen.load(FileLocation + UserFileChoice)
                for i in StockData:
                    print(i)
            elif UserFileChoice == '/MLB2008.csv':
                Stock_chosen = BaseballCSVReader(FileLocation + UserFileChoice)
                StockData = Stock_chosen.load(FileLocation + UserFileChoice)
                for i in StockData:
                    print(i)
        finally:
            for i in StockData:
                print(i)
        is_load = None  # reset
        while 'yes' != is_load and 'no' != is_load:
            is_load = input('\nDo you want to load more data? ("yes" or "no"):')
            try:
                is_load = is_load.lower()
            except:
                is_load = None
            if 'yes' != is_load and 'no' != is_load:
                print("I'm sorry I didn't get that.")
    print('See you next time. Bye!')

loader()