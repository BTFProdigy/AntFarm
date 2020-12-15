import pandas as pd
import logging
from glob import glob


class TestLabUSReport(object):

    def run(self):
        log.info('running')
        results = test_runner.read_to_dataframe()
        results.to_csv('../results/results_table.csv', sep=',', index=False)

    def read_to_dataframe(self):
        file_list = glob('*.dat')
        file_list.extend(glob('Samples*'))
        log.info(file_list)
        column_list = ['name', 'count', 'mean', 'std', 'min', '50%', '75%', '90%', '95%', 'max']
        results_df = pd.DataFrame(columns=column_list)
        for name in file_list:
            log.debug(name)
            if 'Samples' in str(name):
                raw_data = pd.read_csv(name, delim_whitespace=True, header=None)
                raw_data.astype(float)
                results = raw_data[0].describe(percentiles=[.75, .9, .95]).to_dict()
                results['name'] = name
                log.debug(results)
                results_df = results_df.append(results, ignore_index=True)
            else:
                raw_data = pd.read_csv(name, delim_whitespace=True, na_filter=True)
                raw_data.astype(float)
                log.debug(raw_data)
                results = raw_data['tests'].describe(percentiles=[.75, .9, .95]).to_dict()
                results['name'] = name
                log.debug(results)
                results_df = results_df.append(results, ignore_index=True)

        log.debug(results_df)
        return results_df

    def main(self):
        TestLabUSReport().read_test_data()


if __name__ == '__main__':
    log = logging.getLogger('test_statistics_report')
    log.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('../log/test_statistics_report.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)o - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    log.addHandler(fh)
    log.addHandler(ch)
    log.info('Beginning run of calculations')
    test_runner = TestLabUSReport()
    test_runner.run()
