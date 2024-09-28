import json
import re

def parse_changes(record):
    return record.split('\n')

def parse_date_and_change(record):
    # return record.split(' UTC: ')
    return re.split(r' UTC: | PDT: ', record)

with open('wp_cl_person.json') as input_changes:
    data = json.load(input_changes)

output_events = open("person_chages.json", "w")

for i in data:
    person = i['person_id']
    change = i['change_record']
    changes = parse_changes(change)
    for item in changes:
        if item != '':
            date_and_change = parse_date_and_change(item)
            date = date_and_change[0]
            single_change = date_and_change[1]
            event_type_id = 0
            if single_change == 'Initial Change Record':
                event_type_id = 2
            record = {"event_type_id": event_type_id, "person_id": person, "event_date": date, "extra_info": single_change}
            print(record)
            # output_events.write(str(record))
            # json.dump(record, output_events)

output_events.close()
