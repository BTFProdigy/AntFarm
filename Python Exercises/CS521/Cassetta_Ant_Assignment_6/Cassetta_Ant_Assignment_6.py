import os
import csv
import threading
import queue

stocks_rows = queue.Queue(0)
stocks_records = queue.Queue(0)


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


class UserChoice:
    """This class ask's user for file to load. Parse response. return filename"""

    def ask_user(self):

        while True:
            try:
                user_file = input('Do you want to open "StockValuations"? ("yes" or "no")')
                user_file = str(user_file).strip('"')
                if user_file == 'Yes' or user_file == 'yes' or user_file == 'y' or user_file == 'Y':
                    user_choice_ = ('/StockValuations.csv')
                    return user_choice_
                else:
                    print("I didn't get that")
            except Exception as error:
                print(str(error) + 'file name error')


class StockStatRecord():
    """Child of AbstractRecord, takes 8 args: ticker - is passed up to the parent class member name. exchange_country,
    price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio.
    This class is not meant to be called directly it is meant to by called by the load method within the
    AbstractCSVReader class or a child of it."""

    def __init__(self, ticker, exchange_country,
                 price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio):
        self.name = str(ticker)
        self.exchange_country = str(exchange_country)
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


class Runnable:

    def __call__(self, *args, **kwargs):
        print("{} working hard!!".format(id(self)))
        while True:
            try:
                given_row = stocks_rows.get(timeout=1)
                try:
                    if given_row['ticker'] == '' or given_row['exchange_country'] == '' or given_row['price'] == '' \
                            or given_row['price'] == '#DIV/0!' or given_row['exchange_rate'] == '' \
                            or given_row['shares_outstanding'] == '' or given_row['net_income'] == '':
                        raise Exception
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

                            stocks_records.put(StockStatRecord(ticker, exchange_country, price, ExchangeRate,
                                                               SharesOutstanding, NetIncome, calc_market_value_usd,
                                                               pe_ratio))
                        except Exception as error:
                            print(error)
                except Exception as error:
                    print(error)
            except queue.Empty:
                break



class FastStocksCSVReader:
    # TODO: step 4 and substeps (Convert StockCSVReader to threaded format)
    def __init__(self, csv_path):
        try:
            if os.path.exists(csv_path):
                print("Data file located.")
            else:
                raise Exception
        except Exception as error:
            print(error)

    def load(self, file_source):
            try:
                with open(file_source, 'r', newline='') as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        try:
                            stocks_rows.put(row)
                        except Exception:
                            pass
                        # finally:
                        #     csv_file.close()
            except Exception as error:
                print('broke')
                print(error)

            threads = []
            for num in range(4):
                num = threading.Thread(target=Runnable())
                num.start()
                threads.append(num)

            for index in threads:
                index.join()

            out_list = []
            while stocks_records.empty() is False:
                out_list.append(stocks_records.get())
            return out_list

FileLocation = PackageHome.DataFile(PackageHome)
UserFileChoice = UserChoice.ask_user(UserChoice)
full_file_path = FileLocation + UserFileChoice
print(UserFileChoice)
data_recived = FastStocksCSVReader(full_file_path).load(full_file_path)

for record in data_recived:
    print(record)