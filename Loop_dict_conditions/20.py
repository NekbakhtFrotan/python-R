candidates = {
    "Alice": 0,
    "Bob": 0,
    "Carol": 0
}

valid_votes = 0
rejected_votes = 0

while True:
    vote = input("Enter a candidate name (or DONE to finish): ").strip()

    if vote.upper() == "DONE":
        break

    matched = False
    for name in candidates:
        if vote.lower() == name.lower():
            candidates[name] += 1
            valid_votes += 1
            matched = True
            break

    if not matched:
        rejected_votes += 1
        print("Rejected: candidate not found.")

print("\nVote Results")
for name, count in candidates.items():
    print(f"{name}: {count}")

print(f"Total valid votes: {valid_votes}")
print(f"Rejected votes: {rejected_votes}")

if valid_votes == 0:
    print("No valid votes were submitted.")
else:
    print("Percentages of valid votes:")
    for name, count in candidates.items():
        percentage = (count * 100) / valid_votes
        print(f"{name}: {percentage:.2f}%")

    highest_votes = 0
    winners = []

    for name, count in candidates.items():
        if count > highest_votes:
            highest_votes = count
            winners = [name]
        elif count == highest_votes:
            winners.append(name)

    if len(winners) == 1:
        print(f"Winner: {winners[0]}")
    else:
        print("Tie between: " + ", ".join(winners))
