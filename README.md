Project Description

This project detects duplicate records in a dataset using similarity-based logic.

It compares name, email, and phone number fields and calculates a similarity score.
If the score is above a defined threshold, the records are considered duplicates and merged into one consolidated record.

No prebuilt deduplication libraries were used.
All similarity logic was implemented manually.

Features:

-String similarity using manual Levenshtein distance

-Handles minor spelling mistakes

-Compares email variations

-Cleans phone number formatting

-Assigns weighted similarity scores

-Merges probable duplicate records

-Generates a cleaned output dataset


Similarity Logic Explanation:

1. Name Similarity:

Used manual Levenshtein distance

Converts to similarity ratio

Handles minor spelling errors:

-John vs Jhon

-Jane Doe vs Jane D.

2. Email Similarity:

Compared full email string similarity

Handles:

-john.smith@gmail.com

-johnsmith@gmail.com

3. Phone Similarity:

Exact match

Removes formatting characters

4. Weighted Scoring

Final Score Formula:

Total = 0.4(Name) + 0.4(Email) + 0.2(Phone)

Threshold:

>= 0.75 → Duplicate