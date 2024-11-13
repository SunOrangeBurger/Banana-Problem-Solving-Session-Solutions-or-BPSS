import csv
city_matches = {}
with open("matches_banana.csv", mode='r') as file:
    loaded_data = csv.reader(file)
    next(loaded_data)
    
    for row in loaded_data:
        if len(row) < 2:
            continue
            
        city = row[1]
        if city in city_matches:
            city_matches[city] += 1
        else:
            city_matches[city] = 1

print("\nTotal matches played in each city:")
print("City | Number of Matches")
print("-" * 25)
for city, matches in city_matches.items():
    print(f"{city}: {matches}")
