import csv
with open('matches_banana.csv', 'r') as file:
    reader = csv.DictReader(file)
    matches = list(reader)

def get_city(match):
    return match['city']

matches_delhi = []
for match in matches:
    if get_city(match) == "Delhi":
        matches_delhi.append(match)

with open("matches_in_delhi.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(matches_delhi)