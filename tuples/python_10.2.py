name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

new_array_list = []
for i in handle:
    if i is not '\n':
        new_array_list.append(i.strip())

new_array_list_from = []
for item_string in new_array_list:
    if item_string.startswith('From '):
        new_array_list_from.append(item_string)

hash_list_hour = {}
for hour in new_array_list_from:
    hour_index = hour.index(':')
    hour_value = hour[hour_index - 2:hour_index]

    if hour_value not in hash_list_hour:
        hash_list_hour[hour_value] = 1
    else:
        hash_list_hour[hour_value] += 1

lst = []
for k, v in hash_list_hour.items():
    newtuples = (k, v)
    lst.append(newtuples)

for k, v in sorted([(k, v) for k, v in lst]):
    print(k, v)
