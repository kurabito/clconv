import json
import re

def parse_changes(record):
    return record.split('\n')

def parse_date_and_change(record):
    return re.split(r' UTC: | PDT: ', record)

with open('wp_cl_hub.json') as input_changes:
    data = json.load(input_changes)

output_events = open("hub_changes.json", "w", encoding='utf-8')

for i in data:
    hub = i['hub_id']
    change = i['change_record']
    changes = parse_changes(change)
    for item in changes:
        if item != '' and item != None:
            date_and_change = parse_date_and_change(item)
            if len(date_and_change) == 2:
                date = date_and_change[0]
                single_change = date_and_change[1]
                event_type_id = 0
                entity_id = 0
                data_name = None
                old_value = None
                new_value = None
                extra_info = single_change

                if single_change.startswith('Pantries changed to '):
                    event_type_id = 10
                    entity_id = hub
                    data_name = 'pantries'
                    new_value = single_change[20:]
                if single_change.endswith(' made owner'):
                    event_type_id = 8
                    entity_id = hub
                    data_name = 'owner'
                    new_value = single_change[0:6]
                if single_change.startswith('Hub owner set to '):
                    event_type_id = 8
                    entity_id = hub
                    data_name = 'owner'
                    new_value = single_change[18:]
                if single_change.endswith(' removed as owner'):
                    event_type_id = 8
                    entity_id = hub
                    data_name = 'owner'
                    old_value = single_change[0:6]
                if single_change.endswith(' made delegate'):
                    event_type_id = 9
                    entity_id = hub
                    data_name = 'delegates'
                    new_value = single_change[0:6]
                if single_change.endswith(' removed as delegate'):
                    event_type_id = 9
                    entity_id = hub
                    data_name = 'delegates'
                    old_value = single_change[0:6]
                if single_change.endswith(' permission removed'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'permissions'
                    old_value = single_change[0:6]
                if single_change.endswith('made Array'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'permissions'
                    old_value = single_change[0:6]
                if single_change.startswith('Changed drop_off_instructions'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'drop_off_instructions'
                    new_value = single_change[33:]
                if single_change.startswith('Changed drop_off_deadline'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'drop_off_deadline'
                    new_value = single_change[29:]
                if single_change.startswith('Changed neighborhood'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'neighborhood'
                    new_value = single_change[24:]
                if single_change.startswith('Changed location_id'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'location_id'
                    new_value = single_change[31:]
                if single_change.startswith('Changed mailing_location_id'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'mailing_location_id'
                    new_value = single_change[31:]
                if single_change.startswith('Changed primary_area'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'primary_area'
                    new_value = single_change[24:]
                if single_change.startswith('Changed other_info'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'other_info'
                    new_value = single_change[22:]
                if single_change.startswith('Changed hub_type'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'hub_type'
                    new_value = single_change[21:]
                if single_change.startswith('Changed market_id'):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'market_id'
                    new_value = single_change[22:]
                if single_change.startswith('Hub closed changed to '):
                    event_type_id = 11
                    entity_id = hub
                    data_name = 'hub_closed'
                    new_value = single_change[23:]
    
                record = {"event_type_id": event_type_id, "entity_id": entity_id, "data_name": data_name, "old_value": old_value, "new_value": new_value, "extra_info": extra_info, "event_date": date}
                json.dump(record, output_events, ensure_ascii=False, indent=4)

output_events.close()
