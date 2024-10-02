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
            if single_change.startswith(('Made 30', 'Made 50', 'Made 70')):
                entity_id = single_change[5:10]
                new_value = person
                if single_change.endswith('owner'):
                    event_type_id = 8
                    data_name = 'owner'
                else:
                    event_type_id = 9
                    data_name = 'delegate'
                extra_info = person + ' ' + single_change
            # Profile updated
            if single_change == 'User updated profile.':
                event_type_id = 3
                entity_id = person
                data_name = 'profile'
            # Person status updated
            if single_change == 'Set inactive':
                event_type_id = 7
                entity_id = person
                data_name = 'person_status'
                new_value = 'inactive'
            # Hub permission removed
            if single_change.startswith('Permission removed from'):
                event_type_id = 11
                entity_id = single_change[24:29]
                data_name = 'owner or delegate'
                old_value = person
            if single_change.startswith('assignment_'):
                event_type_id = 5
                entity_id = person
                data_name = 'assignment'
                new_value = single_change
            if single_change.startswith('Admin changed status to '):
                event_type_id = 7
                entity_id = person
                data_name = 'person_status'
                new_value = single_change[23:]
            if single_change.startswith('Removed as pantry liaison for '):
                event_type_id = 12
                entity_id = single_change[29:34]
                data_name = 'pantry_liason'
                old_value = person
            if single_change.startswith('Roles changed from '):
                event_type_id = 6
                entity_id = person
                data_name = 'roles'
                role_values = single_change.split(' to ')
                old_value = role_values[0][19:]
                new_value = role_values[1]
            if single_change.startswith('Hub changed to '):
                event_type_id = 4
                entity_id = person
                data_name = 'hub_id'
                new_value = single_change[15:]
            if single_change == 'Set active':
                event_type_id = 7
                entity_id = person
                data_name = 'person_status'
                new_value = 'active'
            if single_change.startswith('Removed as '):
                hub_id = single_change[11:16]
                if single_change.endswith('owner'):
                    event_type_id = 8
                    entity_id = hub_id
                    data_name = 'owner'
                    old_value = person
                if single_change.endswith('delegate'):
                    event_type_id = 9
                    entity_id = hub_id
                    data_name = 'delegate'
                    old_value = person
            if single_change == 'Initial profile update':
                event_type_id = 2
                entity_id = person
                data_name = 'profile'
            if single_change.startswith('Assigned role '):
                event_type_id = 6
                entity_id = person
                data_name = 'roles'
                new_value = single_change[14:]
            if single_change.startswith('User changed hub to '):
                event_type_id = 4
                entity_id = person
                data_name = 'hub_id'
                new_value = single_change[20:]
            if single_change.startswith('Made pantry liaison for '):
                event_type_id = 12
                entity_id = single_change[24:]
                data_name = 'liason'
                new_value = person
            if single_change.startswith('Roles changed to '):
                event_type_id = 6
                entity_id = person
                data_name = 'roles'
                new_value = single_change[17:]

            record = {"event_type_id": event_type_id, "entity_id": entity_id, "data_name": data_name, "old_value": old_value, "new_value": new_value, "extra_info": extra_info, "event_date": date}
            # print(record)
            # output_events.write(str(record))
            json.dump(record, output_events, ensure_ascii=False, indent=4)

output_events.close()
