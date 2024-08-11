def min_teams(p, teamSize_1, teamSize_2):
    """
    Finds the minimum number of teams into which the participants can be divided.

    Args:
        p: The total number of participants.
        teamSize_1: The required team size for track 1.
        teamSize_2: The required team size for track 2.

    Returns:
        The minimum number of teams, or -1 if no division is possible.
    """

    # Check if a team of size teamSize_1 can divide p participants.
    if p % teamSize_1 == 0:
        return p // teamSize_1

    # Check if a team of size teamSize_2 can divide p participants.
    if p % teamSize_2 == 0:
        return p // teamSize_2

    # Check if a combination of teams of size teamSize_1 and teamSize_2 can divide p participants.
    for i in range(p // teamSize_1 + 1):
        remaining = p - i * teamSize_1
        if remaining % teamSize_2 == 0:
            return i + remaining // teamSize_2

    # No valid division is possible.
    return -1


# Example usage:
p = 6
teamSize_1 = 3
teamSize_2 = 4
min_team_count = min_teams(p, teamSize_1, teamSize_2)

if min_team_count == -1:
    print("No valid division is possible.")
else:
    print("Minimum number of teams:", min_team_count)
