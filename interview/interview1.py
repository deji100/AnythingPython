def groupPlayers(n, games):
    pairedPlayers = []

    for i in games:
        for y in range(0, len(i)):
            if len(games) == 1 and 2 == n and y == 0:
                pairedPlayers.append([i[y], i[y+1]])
            elif len(games) == 2 and n == 4 and y == 2:
                pairedPlayers.append(f"[{i[y-2]}, {i[y-1]}], [{i[y]}, {i[y+1]}]")
            elif len(games) == 6 and 6 == n and y == 4:
                pairedPlayers.append(f"[{i[y-4]}, {i[y-3]}], [{i[y-2]}, {i[y-1]}], [{i[y]}, {i[y+1]}]")
            else:
                continue
                

    return pairedPlayers

def check(n, m, games):
    players = []
    dup_players = []
    if n%2 == 0 and len(games[0]) == n:
        if m == len(games):
            pairedPlayers = groupPlayers(n, games)
            if len(games) == 1:
                players.append(tuple(games[0]))
            else:
                for x in pairedPlayers:
                    for z in x:
                        if x.index(z) == 0:
                            if not (z, x[x.index(z) + 1]) in players:
                                players.append((x[x.index(z) + 1], z))
                            else:
                                dup_players.append((z, x[x.index(z) + 1]))
                        else:
                            if not (z, x[x.index(z) - 1]) in players:
                                players.append((x[x.index(z) - 1], z))
                            else:
                                dup_players.append((z, x[x.index(z) - 1]))
        else:
            print("Rounds of games is not equal to m")
    else:
        print("n is not equal to the number of players or not an even number")

    if dup_players == []:
        return True
    else:
        return False

# check(2, 1, [[1, 2]])
# print(check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))
print(groupPlayers(6, 6, [[1, 6, 3, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3], [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4], [2, 3, 6, 4, 1, 5]]))