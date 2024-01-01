import json

file = open('./data/data.txt')
split_by_line = file.read().split('\n')

d = {}

for i, v in enumerate(split_by_line): 
    split_by_line[i] = v.split(':', 1)
    split_by_line[i][1] = split_by_line[i][1].split()

    d[split_by_line[i][0]] = split_by_line[i][1]


json_file = open('./data/data_by_date.json', 'w')
json.dump(d, json_file)