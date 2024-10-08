import json
import re

def parse_changes(record):
    return record.split('\n')

def parse_date_and_change(record):
    return re.split(r' UTC: | PDT: ', record)

with open('wp_cl_food_pantry.json') as input_changes:
    data = json.load(input_changes)

output_events = open("pantry_changes.json", "w", encoding='utf-8')

for i in data:
    food_pantry = i['food_pantry_id']
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

                if single_change.startswith('Changed max_loaves to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'max_loaves'
                    new_value = single_change[22:]
                if single_change.startswith('Changed options to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'options'
                    new_value = single_change[19:]
                if single_change.startswith('Changed web_address to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'web_address'
                    new_value = single_change[23:]
                if single_change.startswith('Changed pantry_practices to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'pantry_practices'
                    new_value = single_change[28:]
                if single_change.startswith('Changed notes to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'notes'
                    new_value = single_change[17:]
                if single_change.startswith('Changed closure_sched to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'closure_sched'
                    new_value = single_change[25:]
                if single_change.startswith('Changed staff_count to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'staff_count'
                    new_value = single_change[23:]
                if single_change.startswith('Changed households_served to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'households_served'
                    new_value = single_change[29:]
                if single_change.startswith('Changed main_phone to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'main_phone'
                    new_value = single_change[29:]
                if single_change.startswith('Changed social_media_links to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'social_media_links'
                    new_value = single_change[30:]
                if single_change.startswith('Changed feeding hubs to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'feeding hubs'
                    new_value = single_change[24:]
                if single_change.startswith('Changed other_notes to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'other_notes'
                    new_value = single_change[23:]
                if single_change.startswith('Changed fresh_bread_need to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'fresh_bread_need'
                    new_value = single_change[28:]
                if single_change.startswith('Changed program_use to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'program_use'
                    new_value = single_change[23:]
                if single_change.startswith('Changed freezer_space to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'freezer_space'
                    new_value = single_change[25:]
                if single_change.startswith('Changed closed_holidays to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'closed_holidays'
                    new_value = single_change[27:]
                if single_change.startswith('Changed location_id to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'location_id'
                    new_value = single_change[23:]
                if single_change.startswith('Pantry status changed to '):
                    event_type_id = 13
                    entity_id = food_pantry
                    data_name = 'status'
                    new_value = single_change[25:]

                record = {"event_type_id": event_type_id, "entity_id": entity_id, "data_name": data_name, "old_value": old_value, "new_value": new_value, "extra_info": extra_info, "event_date": date}
                json.dump(record, output_events, ensure_ascii=False, indent=4)

output_events.close()
