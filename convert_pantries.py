import json
import re

# print('Starting conversion')

def parse_changes(record):
    return record.split('\n')

def parse_date_and_change(record):
    # return record.split(' UTC: ')
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

                # print('Invalid record for food_pantry: ', food_pantry)
                # print('Invalid record: ', changes)
                # print('Invalid item: ', item)

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
                # if single_change.endswith(' made owner'):
                #     event_type_id = 8
                #     entity_id = food_pantry
                #     data_name = 'owner'
                #     new_value = single_change[0:6]
                # if single_change.startswith('food_pantry owner set to '):
                #     event_type_id = 8
                #     entity_id = food_pantry
                #     data_name = 'owner'
                #     new_value = single_change[18:]
                # if single_change.endswith(' removed as owner'):
                #     event_type_id = 8
                #     entity_id = food_pantry
                #     data_name = 'owner'
                #     old_value = single_change[0:6]
                # if single_change.endswith(' made delegate'):
                #     event_type_id = 9
                #     entity_id = food_pantry
                #     data_name = 'delegates'
                #     new_value = single_change[0:6]
                # if single_change.endswith(' removed as delegate'):
                #     event_type_id = 9
                #     entity_id = food_pantry
                #     data_name = 'delegates'
                #     old_value = single_change[0:6]
                # if single_change.endswith(' permission removed'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'permissions'
                #     old_value = single_change[0:6]
                # if single_change.endswith('made Array'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'permissions'
                #     old_value = single_change[0:6]
                # if single_change.startswith('Changed drop_off_instructions'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'drop_off_instructions'
                #     new_value = single_change[33:]
                # if single_change.startswith('Changed drop_off_deadline'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'drop_off_deadline'
                #     new_value = single_change[29:]
                # if single_change.startswith('Changed neighborhood'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'neighborhood'
                #     new_value = single_change[24:]
                # if single_change.startswith('Changed location_id'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'location_id'
                #     new_value = single_change[31:]
                # if single_change.startswith('Changed mailing_location_id'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'mailing_location_id'
                #     new_value = single_change[31:]
                # if single_change.startswith('Changed primary_area'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'primary_area'
                #     new_value = single_change[24:]
                # if single_change.startswith('Changed other_info'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'other_info'
                #     new_value = single_change[22:]
                # if single_change.startswith('Changed food_pantry_type'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'food_pantry_type'
                #     new_value = single_change[21:]
                # if single_change.startswith('Changed market_id'):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'market_id'
                #     new_value = single_change[22:]
                # if single_change.startswith('food_pantry closed changed to '):
                #     event_type_id = 11
                #     entity_id = food_pantry
                #     data_name = 'food_pantry_closed'
                #     new_value = single_change[23:]
    


                # # food_pantry owner or delegate change
                # if single_change.startswith(('Made 30', 'Made 50', 'Made 70')):
                #     entity_id = single_change[5:10]
                #     new_value = person
                #     if single_change.endswith('owner'):
                #         event_type_id = 8
                #         data_name = 'owner'
                #     else:
                #         event_type_id = 9
                #         data_name = 'delegate'
                #     extra_info = person + ' ' + single_change
                # # Profile updated
                # if single_change == 'User updated profile.':
                #     event_type_id = 3
                #     entity_id = person
                #     data_name = 'profile'
                # # Person status updated
                # if single_change == 'Set inactive':
                #     event_type_id = 7
                #     entity_id = person
                #     data_name = 'person_status'
                #     new_value = 'inactive'
                # # food_pantry permission removed
                # if single_change.startswith('Permission removed from'):
                #     event_type_id = 11
                #     entity_id = single_change[24:29]
                #     data_name = 'owner or delegate'
                #     old_value = person
                # if single_change.startswith('assignment_'):
                #     event_type_id = 5
                #     entity_id = person
                #     data_name = 'assignment'
                #     new_value = single_change
                # if single_change.startswith('Admin changed status to '):
                #     event_type_id = 7
                #     entity_id = person
                #     data_name = 'person_status'
                #     new_value = single_change[23:]
                # if single_change.startswith('Removed as pantry liaison for '):
                #     event_type_id = 12
                #     entity_id = single_change[29:34]
                #     data_name = 'pantry_liason'
                #     old_value = person
                # if single_change.startswith('Roles changed from '):
                #     event_type_id = 6
                #     entity_id = person
                #     data_name = 'roles'
                #     role_values = single_change.split(' to ')
                #     old_value = role_values[0][19:]
                #     new_value = role_values[1]
                # if single_change.startswith('food_pantry changed to '):
                #     event_type_id = 4
                #     entity_id = person
                #     data_name = 'food_pantry_id'
                #     new_value = single_change[15:]
                # if single_change == 'Set active':
                #     event_type_id = 7
                #     entity_id = person
                #     data_name = 'person_status'
                #     new_value = 'active'
                # if single_change.startswith('Removed as '):
                #     food_pantry_id = single_change[11:16]
                #     if single_change.endswith('owner'):
                #         event_type_id = 8
                #         entity_id = food_pantry_id
                #         data_name = 'owner'
                #         old_value = person
                #     if single_change.endswith('delegate'):
                #         event_type_id = 9
                #         entity_id = food_pantry_id
                #         data_name = 'delegate'
                #         old_value = person
                # if single_change == 'Initial profile update':
                #     event_type_id = 2
                #     entity_id = person
                #     data_name = 'profile'
                # if single_change.startswith('Assigned role '):
                #     event_type_id = 6
                #     entity_id = person
                #     data_name = 'roles'
                #     new_value = single_change[14:]
                # if single_change.startswith('User changed food_pantry to '):
                #     event_type_id = 4
                #     entity_id = person
                #     data_name = 'food_pantry_id'
                #     new_value = single_change[20:]
                # if single_change.startswith('Made pantry liaison for '):
                #     event_type_id = 12
                #     entity_id = single_change[24:]
                #     data_name = 'liason'
                #     new_value = person
                # if single_change.startswith('Roles changed to '):
                #     event_type_id = 6
                #     entity_id = person
                #     data_name = 'roles'
                #     new_value = single_change[17:]

                record = {"event_type_id": event_type_id, "entity_id": entity_id, "data_name": data_name, "old_value": old_value, "new_value": new_value, "extra_info": extra_info, "event_date": date}
                # print(record)
                # output_events.write(str(record))
                json.dump(record, output_events, ensure_ascii=False, indent=4)

output_events.close()
