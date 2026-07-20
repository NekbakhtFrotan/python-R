# Store runs scored in 15 matches
runs = list(map(int, input("Enter runs in 15 matches: ").split()))

# Total runs
total = sum(runs)

# Average runs
average = total / len(runs)

# Highest and lowest scores
highest = max(runs)
lowest = min(runs)

# Count half-centuries and centuries
half_centuries = 0
centuries = 0

for score in runs:
    if score >= 50:
        half_centuries += 1
    if score >= 100:
        centuries += 1

# Display the results
print("Total Runs:", total)
print("Average Runs:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Half-Centuries:", half_centuries)
print("Centuries:", centuries)