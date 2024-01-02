import json
import datetime as dt
import pickle

file = open('./data/data.txt')
split_by_line = file.read().split('\n')

d = {}

for i, v in enumerate(split_by_line): 
    split_by_line[i] = v.split(':', 1)
    split_by_line[i][1] = split_by_line[i][1].split()

    d[split_by_line[i][0]] = split_by_line[i][1]


json_file = open('./data/data_by_date.json', 'w')
json.dump(d, json_file)

times = []
for key in d: 
    if d[key] == []: 
        pass

    else: 
        for time in d[key]: 
            month_str = key.split()[1] + '/2023'
            time_str = time.upper()
            dt_str = month_str + ' ' + time_str

            formatted_time = dt.datetime.strptime(dt_str, '%m/%d/%Y %I:%M%p')
            times.append(formatted_time)

with open('./data/times.pkl', 'wb') as out_file:
    pickle.dump(times, out_file)