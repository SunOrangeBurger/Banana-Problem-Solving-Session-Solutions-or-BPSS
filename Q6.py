import csv
with open("matches_banana.csv", mode='r') as file:
    loaded_data = csv.reader(file)
    next(loaded_data)
    
    print("\nTosses Won by Mumbai Indians:")
    print("ID | City | Date | Team 1 | Team 2 | Toss Decision | Player of Match | Venue")
    
    for row in loaded_data:
        if len(row) < 8: 
            continue
            
        if row[7] == "Mumbai Indians":
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[6]} | {row[8]} | {row[9]}")