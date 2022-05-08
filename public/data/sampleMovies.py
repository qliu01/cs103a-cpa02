import json

with open("movies.json") as file:
    data = json.load(file)

moviesByYear = dict()
countsByYear = dict()

for datum in data:
    print(datum)
    if datum['year'] not in moviesByYear:
        moviesByYear[datum['year']] = list()
    if datum['year'] not in countsByYear:
        countsByYear[datum['year']] = 0
    moviesByYear[datum['year']].append(datum)
    countsByYear[datum['year']] += 1

years = list(range(1990, 2019))

newData = list()
for year in years:
    newData.extend(moviesByYear[year][:100])

print(countsByYear)

with open("moviesSampled.json", 'w') as file:
    json.dump(newData, file)

# jess_dict = json.loads()
# print(jess_dict)


# Printed output: {"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}
# print(jess_dict)
# json.load(file object)
