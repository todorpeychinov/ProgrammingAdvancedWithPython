def team_lineup(*args):
    players_by_countries = {}
    for name, country in args:
        if country not in players_by_countries:
            players_by_countries[country] = []
        players_by_countries[country].append(name)

    sorted_players_by_country = sorted(players_by_countries.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for country, players in sorted_players_by_country:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result.strip()


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
print()
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
print()
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
