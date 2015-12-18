import sys
import json
from configs import *


def write_logfile(events):
    with open(JSON_LOG_OUTPUT_FILE, 'w') as outfile:
        json.dump(events, outfile, indent=4, sort_keys=True)


def generate_logs_from_rabbitmq():
    pass


def generate_logs_from_sample_data():
    with open(SAMPLE_DATA_INPUT_FILE, 'r') as infile:
        events = []
        for line in infile.readlines():
            # Sanitize the data
            new_data = line.replace('\\', '')
            data = new_data.replace('null', '\"NULL\"')
            new_data = data.split('", "oslo.version":')[0]

            try:
                new_data_json = json.loads(new_data)
            except:
                sys.exit("Failed sanitizing data to json")
            events.append(new_data_json)

    write_logfile(events)


def app():
    print "Running notifications app..."

    # App logic runs here
    generate_logs_from_sample_data()
    generate_logs_from_rabbitmq()
