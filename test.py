import cantools



class SignalData:
    name: str
    scale: float | None
    offset: float | None
    min_value: float | None
    max_value: float | None
    unit: str | None
    source: str | None


db = cantools.database.load_file('CAN0.dbc')

def get_from_CAN0():
    signal_data_arr = []

    for msg in db.messages:
        # message_names.append(msg.name)
        for signal in msg.signals:
            current_signal = SignalData()
            current_signal.name = signal.name
            current_signal.scale = signal.scale
            current_signal.offset = signal.offset
            current_signal.min_value = signal.minimum
            current_signal.max_value = signal.maximum
            current_signal.unit = signal.unit
            current_signal.source = signal.receivers
            signal_data_arr.append(current_signal)
    return signal_data_arr