# store many items
ages = [21, 72, 45, 76, 89, 56, 39, 66]  # list

names = ["Jack", 'Gil', 'Ahmed', 'Yusuf']

# fxns
ages.append(11)
ages.sort()
# ages.clear()
ages.reverse()

print(ages)

names.sort()
print(names)

jack_count = names.count('Jack')
print(jack_count)

print(len(names))

print(round(sum(ages) / len(ages), 3))

# retrieve element
print(ages[0])
print(ages[-1])
print(ages[2:6])
print(ages[1:])

# set->no duplicates
scores = {34, 56, 23, 90, 76, 52, 88, 44}
print(scores)
scores.add(77)

# tuples are immutable
weekdays = ("Mon", "Tue", "Wen", "Thur", "Fri")
print(weekdays)

# dictionary
person = {"name": "john", "age": 23, "name": "alex", "age": 76}
print(person["name"])

# list of dictionaries
people = [
    {"country": "kenya"},
    {"country": "uganda"},
    {"country": "teezeedd"},
    {"country": "ethiopia"}
]

print(people[2])
