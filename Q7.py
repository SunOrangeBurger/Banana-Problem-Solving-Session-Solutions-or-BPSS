import csv
with open("matches_banana.csv", mode='r') as file:
    loaded_data = csv.reader(file)
    next(loaded_data)
    
    print("\nMatches where SR Watson was Player of the Match:")
    print("ID | City | Date | Team 1 | Team 2 | Toss Winner | Toss Decision | Match Winner | Venue")
 
    
    for row in loaded_data:
        if len(row) < 8: 
            continue
            
        if row[8] == "SR Watson":
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[9]}")