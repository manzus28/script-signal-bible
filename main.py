import openpyxl as xl
import cantools as can

import test
from test import get_name_from_CAN0

SIGNAL_BIBLE_FILE = "Signal_Bible_DP17.xlsx"
SIGNAL_SHEET = "Signal_Bible"

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
def access_signal_scale(work_sheet):
    signal_scale_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=15, max_col=15, min_row=4, max_row=526):
        for signal_scale in signal_cell_tu:
            signal_scale_array.append(signal_scale.value)
    return signal_scale_array

def access_signal_offset(work_sheet):
    signal_offset_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=14, max_col=14, min_row=4, max_row=526):
        for signal_offset in signal_cell_tu:
            signal_offset_array.append(signal_offset.value)
    return signal_offset_array

def access_signal_min_max(work_sheet):
    signal_min_max_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=10, max_col=10, min_row=4, max_row=526):
        for signal_min_max in signal_cell_tu:
            signal_min_max_array.append(signal_min_max.value)
    return signal_min_max_array

def access_signal_unit(work_sheet):
    signal_unit_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=5, max_col=5, min_row=4, max_row=526):
        for signal_unit in signal_cell_tu:
            signal_unit_array.append(signal_unit.value)
    return signal_unit_array

if __name__ == '__main__':
    signal_sheet = open_signal_bible(SIGNAL_BIBLE_FILE,SIGNAL_SHEET )
    signal_bible_names = access_signal_name(signal_sheet)
    signal_bible_scale = access_signal_scale(signal_sheet)
    signal_bible_offset = access_signal_offset(signal_sheet)
    signal_bible_min_max = access_signal_min_max(signal_sheet)
    signal_bible_unit = access_signal_unit(signal_sheet)

    for signal_scale in signal_bible_scale:
        print(signal_scale)
    signal_name_CAN0 = get_name_from_CAN0()
    






