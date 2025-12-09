cricket = set(map(int, input("Enter roll numbers of Cricket players (comma separated): ").split(',')))
football = set(map(int, input("Enter roll numbers of Football players (comma separated): ").split(',')))

both = cricket.intersection(football)
only_cricket = cricket - football
only_football = football - cricket

print("Players who play both games:", both)
print("Players who play only Cricket:", only_cricket)
print("Players who play only Football:", only_football)
