def enter_basketball_score():
    team1 = input("Enter Team 1 name: ")
    team2 = input("Enter Team 2 name: ")
    points1 = int(input(f"Enter points scored by {team1}: "))
    points2 = int(input(f"Enter points scored by {team2}: "))

    print("\n🏀 Basketball Match Summary:")
    print(f"{team1}: {points1} points")
    print(f"{team2}: {points2} points")
    if points1 > points2:
        print(f"🏆 {team1} wins by {points1 - points2} points!")
    elif points2 > points1:
        print(f"🏆 {team2} wins by {points2 - points1} points!")
    else:
        print("🤝 Match Tied!")
