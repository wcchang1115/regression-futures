import logging
import argparse
import csv
from position import Position
from position_type import PositionType
from report import Report
from strategy import strategy_init, regression_strategy, regression_strategy_ma
import config

def main():
    init_logger()
    config.init()
    arg_parser = init_arg_parse()

    regression(arg_parser)

def init_logger():
    LOG_FORMAT = '%(filename)s [%(levelname)s] - %(funcName)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    logging.debug('logger init finished')

def init_arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="specify the MA strategy", action="store_true")
    parser.add_argument("filename", help="specify the regression file in current directory")
    return parser

def regression(arg_parser):
    long_position = Position(PositionType.LONG)
    short_position = Position(PositionType.SHORT)
    report = Report()

    args = arg_parser.parse_args()
    filename = args.filename
    logging.debug('regression file name is {file_name}'.format(file_name=filename))
    
    strategy_init()

    with open(filename, 'r', newline='', encoding='utf-8-sig') as option_file:
        reader = csv.DictReader(option_file)
        logging.debug(reader.fieldnames)
        next(reader)
        
        if args.m:
            output_file = filename.split(".")[0] + "_result_ma.csv"
        else:
            output_file = filename.split(".")[0] + "_result.csv"

        logging.debug('result file name is {file_name}'.format(file_name=output_file))
        
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as result_csv:
            fieldnames = ['時間', '收盤價', '總和', 'SMA20', 'SMA60', 
                '持有多單', '持有空單', '多單成本', '空單成本', '多單出場', '空單出場', 
                '資金', '進場數', '勝數', '敗數']
            writer = csv.DictWriter(result_csv, delimiter=',', fieldnames=fieldnames)
            writer.writeheader() 
            
            for row in reader:
                if args.m:
                    regression_strategy_ma(
                        row, long_position, short_position, report)
                else:
                    regression_strategy(row, long_position, short_position, report)

                writer.writerow({'時間': row['時間'], '收盤價': row['收盤價'], 
                    '總和': row['總和'], 'SMA20': row['SMA20'], 'SMA60': row['SMA60'],
                    '持有多單': long_position.get_number(), '持有空單': short_position.get_number(), 
                    '多單成本': long_position.get_average_point(), '空單成本': short_position.get_average_point(), 
                    '多單出場': report.get_long_position_gain_point(), '空單出場': report.get_short_position_gain_point(), '資金': config.funds,
                    '進場數': report.get_num_open(), '勝數': report.get_num_win(), '敗數': report.get_num_lose()})



if __name__ == "__main__":
    main()