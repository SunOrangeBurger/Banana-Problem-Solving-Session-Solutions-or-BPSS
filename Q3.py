import csv
team_matches = {}
with open("matches_banana.csv", mode='r') as file:
    loaded_data = csv.reader(file)
    next(loaded_data)     
    for row in loaded_data:
        if len(row) < 5:
            continue       
        team1 = row[3]
        team2 = row[4]
        
        if team1 in team_matches:
            team_matches[team1] += 1
        else:
            team_matches[team1] = 1           
        if team2 in team_matches:
            team_matches[team2] += 1
        else:
            team_matches[team2] = 1          
print("\nTotal matches played by each team:")
for team, matches in team_matches.items():
    print(f"{team}: {matches}")
