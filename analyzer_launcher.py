import sys
import math
import json
from datetime import datetime
from time import sleep
from queue import Queue
from threading import Thread
from decimal import Decimal

def get_data():
    with open('events.txt', 'r') as reader:
        for event in reader:
            event_data, event_time = parse_raw_data(event)
            q.put({'data': event_data, 'time': event_time})


def processing_data():
    sleep(0.5)
    dataset = []

    while True:
        while len(dataset) < setup['slice_size']:
            dataset.append(q.get())

        total_score = sum(list(map(lambda field_config: field_processing(dataset, field_config), setup['fields'])))
        detector = ('Normal', 'Attack!')[total_score > setup['attack_score']]

        print(f'Total score: {total_score}; [{detector}]')
        sleep(0.1)
        dataset = dataset[setup['step_size']:]

        if q.empty():
            sys.exit()
        q.task_done()


def field_processing(dataset, field_config):
    if field_config['score'] == 0:
        return 0

    data_collection = list(map(lambda event: int(event['data'][field_config['name']]), dataset))
    probability = calculate_distribution(data_collection)

    cached_value = store.get(field_config['name'])
    entropy_value = entropy(probability, cached_value) if cached_value else 0
    store[field_config['name']] = probability

    attack_detector = (0, float(field_config['score']))[abs(entropy_value) > field_config['threshold']]
    print(f"{field_config['name']}: {entropy_value}; {probability}; [{attack_detector}]; {data_collection}")
    return attack_detector


def average(collection):
    return sum(collection) / len(collection)


def entropy(current_value, previous_value):
    return Decimal(previous_value) * Decimal(math.log(previous_value / current_value))


def calculate_distribution(collection):
    current_value = collection[-1]
    estimated_value = average(collection)
    distribution = (Decimal(math.e) ** Decimal(estimated_value * -1)) * (Decimal(estimated_value) ** Decimal(current_value)) / math.factorial(
        current_value)

    return distribution


def parse_raw_data(event):
    raw_data, raw_time = event.split(';')
    time = datetime.strptime(raw_time[1:-1], '%c')
    raw_data = raw_data[1:-1].split(', ')
    data = {
        'package_signature': ''.join(map(lambda symbol: symbol[2], raw_data[:4])),
        'package_type': raw_data[5],
        'data_section_length': raw_data[5],
        'checksum': raw_data[6],
        'telemetry_receiver': raw_data[7],
        'uav_status': raw_data[8],
        'battery_voltage': raw_data[9],
        'current_ampere': raw_data[10],
        'flight_time': raw_data[11],
        'height': raw_data[12],
        'pitch': raw_data[13],
        'roll': raw_data[14],
        'yawing': raw_data[15],
        'horizontal_speed': raw_data[16],
        'vertical_speed': raw_data[17],
        'number_of_satellites': raw_data[18],
        'gps_quality': raw_data[19],
        'transmitter_signal_strength': raw_data[20],
        'gas_level': raw_data[21],
        'battery_level': raw_data[22],
        'current_consumption': raw_data[23],
        'power_consumption': raw_data[24],
        'vibration_level': raw_data[25],
        'gps_accuracy': raw_data[26],
        'uav_latitude': raw_data[27],
        'uav_longitude': raw_data[28],
        'take_off_longitude': raw_data[29],
        'take_off_latitude': raw_data[30]}
    return [data, time]


if __name__ == '__main__':
    q = Queue()
    store = {}
    setup_file = open('config.json')
    setup = json.load(setup_file)

    Thread(target=get_data).start()
    Thread(target=processing_data).start()

    setup_file.close()
