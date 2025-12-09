def enter_football_score():
    team1 = input("Enter Team 1 name: ")
    team2 = input("Enter Team 2 name: ")
    goals1 = int(input(f"Enter goals scored by {team1}: "))
    goals2 = int(input(f"Enter goals scored by {team2}: "))

    print("\n⚽ Football Match Summary:")
    print(f"{team1}: {goals1} goals")
    print(f"{team2}: {goals2} goals")
    if goals1 > goals2:
        print(f"🏆 {team1} wins the match!")
    elif goals2 > goals1:
        print(f"🏆 {team2} wins the match!")
    else:
        print("🤝 Match Drawn!")
