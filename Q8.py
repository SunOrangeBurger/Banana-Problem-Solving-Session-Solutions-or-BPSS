import csv
with open('matches_banana.csv', 'r') as file:
    reader = csv.DictReader(file)
    matches = list(reader)
def get_winner(match):
    return match['winner']

sorted_matches = sorted(matches, key=get_winner)
with open('maches_sorted.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(sorted_matches)
