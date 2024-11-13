import csv

new_match = {
    "id": "578",
    "city": "Kolkata", 
    "date": "5/25/2017",
    "team1": "Royal Challengers Bangalore",
    "team2": "Kolkata Knight Riders",
    "toss_winner": "Kolkata Knight Riders",
    "toss_decision": "field",
    "winner": "Royal Challengers Bangalore",
    "player_of_match": "Virat Kohli",
    "venue": "Eden Gardens"
}

with open("matches_banana.csv", mode='a') as file:
    writer = csv.writer(file)
    writer.writerow(new_match.values())

