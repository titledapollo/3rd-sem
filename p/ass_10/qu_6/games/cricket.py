def enter_cricket_score():
    team1 = input("Enter Team 1 name: ")
    team2 = input("Enter Team 2 name: ")
    score1 = int(input(f"Enter runs scored by {team1}: "))
    score2 = int(input(f"Enter runs scored by {team2}: "))
    overs = float(input("Enter number of overs played: "))

    print("\n🏏 Cricket Match Summary:")
    print(f"{team1}: {score1} runs")
    print(f"{team2}: {score2} runs")
    print(f"Overs played: {overs}")
    if score1 > score2:
        print(f"🏆 {team1} won the match by {score1 - score2} runs!")
    elif score2 > score1:
        print(f"🏆 {team2} won the match by {score2 - score1} runs!")
    else:
        print("🤝 Match Drawn!")
