import openpyxl as xl
import cantools as can

from test import get_name_from_CAN0

SIGNAL_BIBLE_FILE = "Signal_Bible_DP17.xlsx"
SIGNAL_SHEET = "Signal_Bible"



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def open_signal_bible(file_name, sheet_name):
    wb = xl.load_workbook(file_name)
    ws = wb[sheet_name]
    return ws

def access_signal_name(work_sheet):
    signal_names_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=1, max_col=1, min_row=4, max_row=526):
        for signal_name in signal_cell_tu:
            signal_names_array.append(signal_name.value)
    return signal_names_array

# inizio + lunghezza + scale + offset + min + max + unità + source






if __name__ == '__main__':
    signal_sheet = open_signal_bible(SIGNAL_BIBLE_FILE,SIGNAL_SHEET )
    signal_bible_names = access_signal_name(signal_sheet)
    signal_name_CAN0 = get_name_from_CAN0()
    for signal_in_CAN in signal_name_CAN0:
        if signal_in_CAN not in signal_bible_names:
            print("not found: " + signal_in_CAN)






