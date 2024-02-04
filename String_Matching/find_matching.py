from thefuzz import fuzz

def find_matching(list1, list2):
    matching = []

    for string1 in list1:
        backup = []

        for string2 in list2:
            similarity = fuzz.token_set_ratio(string1, string2)

            if similarity > 95:
                matching.append((string1, string2))
            else:
                backup.append((similarity, string2))

        if len(backup) == len(list2):
            backup.sort(reverse = True)
            matching.append((string1, backup[0][1]))

    return matching