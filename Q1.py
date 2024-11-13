import csv

with open("matches_banana.csv", mode='r') as file:
    loaded_data = csv.reader(file)
    next(loaded_data)
    total_matches = sum(1 for row in loaded_data if row[9] == "M Chinnaswamy Stadium")
    print(f"Total matches in M Chinnaswamy Stadium: {total_matches}")