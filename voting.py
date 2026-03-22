# ============================================================
#  Voting Centre System
#  Author: Jacob Lennon
#  Description: A CLI voting application with age verification,
#               candidate selection, vote tallying, and results.
# ============================================================

# --- Candidates ---
CANDIDATES = ["Sir Meow", "Lady Kitten Whiskers", "Councillor Fur"]

# --- Vote tally dictionary ---
vote_counts = {candidate: 0 for candidate in CANDIDATES}

# --- Helper: print a divider ---
def divider():
    print("\n" + "─" * 50 + "\n")

# --- Helper: display current standings ---
def show_results():
    divider()
    print("📊  CURRENT STANDINGS")
    divider()
    total = sum(vote_counts.values())
    for candidate in CANDIDATES:
        count = vote_counts[candidate]
        pct = (count / total * 100) if total > 0 else 0
        bar = "█" * int(pct / 5)
        print(f"  {candidate:<25} {count:>3} vote(s)  [{bar:<20}] {pct:.1f}%")
    print(f"\n  Total votes cast: {total}")
    divider()

# --- Helper: display winner ---
def show_winner():
    divider()
    print("🏆  FINAL RESULTS")
    divider()
    total = sum(vote_counts.values())
    if total == 0:
        print("  No votes were cast.")
        return
    winner = max(vote_counts, key=vote_counts.get)
    top_votes = vote_counts[winner]
    # Check for a tie
    tied = [c for c, v in vote_counts.items() if v == top_votes]
    if len(tied) > 1:
        print(f"  🤝 It's a TIE between: {', '.join(tied)}")
        print(f"     Each with {top_votes} vote(s).")
    else:
        pct = top_votes / total * 100
        print(f"  🎉 Winner: {winner}")
        print(f"     {top_votes} vote(s) — {pct:.1f}% of the vote")
    show_results()

# --- Age verification ---
def verify_age():
    while True:
        try:
            age = int(input("Enter your age to continue: "))
            if age < 0:
                print("  ⚠  Please enter a valid age.")
            elif age < 18:
                print(f"\n  ❌  Sorry, you must be 18 or older to vote. You are {age}.")
                return False
            else:
                print(f"\n  ✅  Age verified. Welcome to the Voting Centre!")
                return True
        except ValueError:
            print("  ⚠  Please enter a number.")

# --- Display candidates ---
def show_candidates():
    print("  Candidates standing for election:\n")
    for i, candidate in enumerate(CANDIDATES, 1):
        print(f"    {i}. {candidate}")
    print()

# --- Cast a vote ---
def cast_vote():
    show_candidates()
    while True:
        vote = input("  Enter the candidate's name or number (1–3): ").strip()

        # Allow numeric input
        if vote in ("1", "2", "3"):
            vote = CANDIDATES[int(vote) - 1]

        # Find a case-insensitive match
        match = next((c for c in CANDIDATES if c.lower() == vote.lower()), None)

        if match:
            confirm = input(f"\n  You selected: {match}\n  Confirm vote? (yes / no): ").strip().lower()
            if confirm == "yes":
                vote_counts[match] += 1
                print(f"\n  ✅  Vote recorded for {match}. Thank you!")
                return
            else:
                print("\n  No problem — let's try again.\n")
                show_candidates()
        else:
            print("  ⚠  Invalid choice. Please enter a candidate's name or number (1–3).\n")

# --- Main program ---
def main():
    divider()
    print("       🗳   WELCOME TO THE VOTING CENTRE   🗳")
    divider()

    while True:
        print("  What would you like to do?\n")
        print("    1. Cast a vote")
        print("    2. View current standings")
        print("    3. View final results & winner")
        print("    4. Exit\n")

        choice = input("  Enter option (1–4): ").strip()
        divider()

        if choice == "1":
            print("  AGE VERIFICATION\n")
            if verify_age():
                divider()
                print("  CAST YOUR VOTE\n")
                cast_vote()
            divider()

        elif choice == "2":
            show_results()

        elif choice == "3":
            show_winner()
            break

        elif choice == "4":
            print("  👋  Thanks for using the Voting Centre. Goodbye!")
            divider()
            break

        else:
            print("  ⚠  Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
