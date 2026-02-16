def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def similarity_score(s1, s2):
    if not s1 or not s2:
        return 0

    distance = levenshtein_distance(s1, s2)
    max_len = max(len(s1), len(s2))

    return 1 - (distance / max_len)


def calculate_total_similarity(rec1, rec2):
    name_score = similarity_score(rec1["name"], rec2["name"])
    email_score = similarity_score(rec1["email"], rec2["email"])
    phone_score = 1 if rec1["phone"] == rec2["phone"] else 0


    total_score = (
        0.4 * name_score +
        0.4 * email_score +
        0.2 * phone_score
    )

    return total_score
