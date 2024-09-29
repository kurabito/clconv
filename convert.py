import json
import re

def parse_changes(record):
    return record.split('\n')

def parse_date_and_change(record):
    # return record.split(' UTC: ')
    return re.split(r' UTC: | PDT: ', record)

with open('wp_cl_person.json') as input_changes:
    data = json.load(input_changes)

output_events = open("person_changes.json", "w", encoding='utf-8')

# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

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
            entity_id = 0
            data_name = None
            old_value = None
            new_value = None
            extra_info = single_change

            # Profile created
            if single_change == 'Initial Change Record':
                event_type_id = 2
                entity_id = person
            # Hub owner or delegate change
            if single_change.startswith('Made 30'):
                entity_id = single_change[5:10]
                if single_change.endswith('owner'):
                    event_type_id = 8
                    data_name = 'owner'
                    new_value = person
                else:
                    event_type_id = 9
                    data_name = 'delegate'
                    new_value = person
                extra_info = person + ' ' + single_change
            # Profile updated
            if single_change == 'User updated profile.':
                event_type_id = 3
                entity_id = person
                data_name = 'profile'

            record = {"event_type_id": event_type_id, "entity_id": entity_id, "data_name": data_name, "old_value": old_value, "new_value": new_value, "extra_info": extra_info, "event_date": date}
            # print(record)
            # output_events.write(str(record))
            json.dump(record, output_events, ensure_ascii=False, indent=4)

output_events.close()
