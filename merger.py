def merge_records(rec1, rec2):
    merged = {}

    merged["id"] = f"{rec1['id']}-{rec2['id']}"

    merged["name"] = rec1["name"] if len(rec1["name"]) >= len(rec2["name"]) else rec2["name"]

    merged["email"] = rec1["email"] if len(rec1["email"]) >= len(rec2["email"]) else rec2["email"]

    merged["phone"] = rec1["phone"]

    merged["address"] = rec1["address"]

    return merged
