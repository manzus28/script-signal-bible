from dataclasses import dataclass

import openpyxl as xl
import cantools as can

from test import get_name_from_CAN0

SIGNAL_BIBLE_FILE = "Signal_Bible_DP17.xlsx"
SIGNAL_SHEET = "Signal_Bible"

# Colonne Excel
NAME_COL = 1
UNIT_COL = 5
MINMAX_COL = 10
OFFSET_COL = 14
SCALE_COL = 15

START_ROW = 4
END_ROW = 526

@dataclass
class SignalData:
    name: str
    scale: float | None
    offset: float | None
    min_value: float | None
    max_value: float | None
    unit: str | None
    source: str | None

def open_signal_bible(file_name, sheet_name):
    wb = xl.load_workbook(file_name)
    ws = wb[sheet_name]
    return ws

def access_signal_name(work_sheet):
    signal_names_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=NAME_COL, max_col=NAME_COL, min_row=START_ROW, max_row=END_ROW):
        for signal_name in signal_cell_tu:
            signal_names_array.append(signal_name.value)
    return signal_names_array

def signal_not_in_sheet(signals_in_bible, signal_name_CAN0):
    for signal_in_CAN in signal_name_CAN0:
        if signal_in_CAN not in signals_in_bible:
            print("not found: " + signal_in_CAN)

def signal_not_in_can(signals_in_bible, signal_name_CAN0):
    for signal_in_sheet in signal_bible_names:
        if signal_in_sheet not in signal_name_CAN0:
            print("not found: " + signal_in_sheet)

def is_equal_or_null(signal_from_CAN, signal_message, signal_sheet_name, signal_sheet_scale, signal_sheet_offset, signal_sheet_min, signal_sheet_max, signal_sheet_source):
    if signal_from_CAN in signal_sheet_name:
        signal_index = signal_sheet_name.index(signal_from_CAN)
        scale = signal_sheet_scale[signal_index]
        if scale != None:
            if signal_message.get_signal_by_name(signal_from_CAN).scale != scale:
               print("wrong scale of " + signal_from_CAN)


# scale + offset + min + max + unità + source
def access_signal_scale(work_sheet):
    signal_scale_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=SCALE_COL, max_col=SCALE_COL, min_row=4, max_row=526):
        for signal_scale in signal_cell_tu:
            signal_scale_array.append(signal_scale.value)
    return signal_scale_array

def access_signal_offset(work_sheet):
    signal_offset_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=OFFSET_COL, max_col=OFFSET_COL, min_row=4, max_row=526):
        for signal_offset in signal_cell_tu:
            signal_offset_array.append(signal_offset.value)
    return signal_offset_array

def access_signal_min_max(work_sheet):
    signal_min_max_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=MINMAX_COL, max_col=MINMAX_COL, min_row=4, max_row=526):
        for signal_min_max in signal_cell_tu:
            signal_min_max_array.append(signal_min_max.value)
    return signal_min_max_array

def access_signal_unit(work_sheet):
    signal_unit_array = []
    for signal_cell_tu in signal_sheet.iter_cols(min_col=UNIT_COL, max_col=UNIT_COL, min_row=4, max_row=526):
        for signal_unit in signal_cell_tu:
            signal_unit_array.append(signal_unit.value)
    return signal_unit_array

if __name__ == '__main__':
    can_database = can.database.load_file('CAN0.dbc')
    signal_sheet = open_signal_bible(SIGNAL_BIBLE_FILE,SIGNAL_SHEET )
    signal_bible_names = access_signal_name(signal_sheet)
    signal_bible_scale = access_signal_scale(signal_sheet)
    signal_bible_offset = access_signal_offset(signal_sheet)
    signal_bible_min_max = access_signal_min_max(signal_sheet)
    signal_bible_unit = access_signal_unit(signal_sheet)
    signal_name_CAN0 = get_name_from_CAN0()
    signal_bible_scale[111] = 100
    is_equal_or_null(signal_name_CAN0[0], can_database.get_message_by_name(signal_name_CAN0[0]), signal_bible_names, signal_bible_scale,None,None,None, None)











