import logging as lg
import re
import openpyxl as xl


if __name__ == '__main__':
    print()

    lg.basicConfig(level=lg.ERROR, filename='logging.log', format='%(asctime)s:%(levelname)s:%(message)s')

    lg.debug('debug1')
    lg.critical('critical1')
    lg.warning('warning1')
    lg.error('error1')

    wb = xl.Workbook()
    ws = wb.active

    try:
        x = 1 / 0
    except Exception as e:
        lg.error("An error occurred: %s", str(e))

    symbols = ['%', '#', '$', '*', '@']

    for idx, symbol in enumerate(symbols, start=1):
        ws.cell(row=1, column=idx, value=symbol)


    def process_log_file(log_filename):
        try:
            # קריאת קובץ הלוג
            with open(log_filename, 'r') as file:
                log_content = file.read()

            # חיפוש מספרים וסימונים בקובץ הלוג
            for match in re.finditer(r'[0-9]+', log_content):
                start, end = match.span()
                found_symbols = {symbol: [] for symbol in symbols}

                for symbol in symbols:
                    symbol_index = log_content.find(symbol, start, end)
                    if symbol_index != -1:
                        found_symbols[symbol].append(symbol_index)

                # רישום המיקומים בעמודות המתאימות בקובץ האקסל
                for symbol, indices in found_symbols.items():
                    if indices:
                        column_index = symbols.index(symbol) + 1
                        for idx in indices:
                            ws.append([None] * (column_index - 1) + [idx])
                            print(f'Found {symbol} at index {idx}')

        except Exception as e:
            lg.error(f'Failed to process log file: {e}')


    # קריאת קובץ הלוג ועיבודו
    process_log_file('logging.log')

    # שמירת קובץ האקסל
    wb.save('output.xlsx')