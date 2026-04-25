import cantools


db = cantools.database.load_file('CAN0.dbc')

def get_name_from_CAN0():
# message_names = []
    signal_names = []

    for msg in db.messages:
        # message_names.append(msg.name)
        for signal in msg.signals:
            signal_names.append(signal.name)
    return signal_names