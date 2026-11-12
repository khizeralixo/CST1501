"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Turn one messy raw survey line into a clean dict."""
    line = raw_line.strip().lower()
    survey_part, rest = line.split(",", 1)
    survey = survey_part.strip()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {"survey": survey, "rating": fields["rating"], "age": fields["age"]}


def status_of(rating):
    """Return FLAGGED for low ratings (< 3) or out-of-range values, otherwise OK."""
    if rating < 1 or rating > 5:
        return "OVER LIMIT"
    elif rating < 3:
        return "FLAGGED"
    else:
        return "OK"

# ====================================================================== INPUT

raw_records = [
    "  Survey_2026 , rating = 4 , age=23 ",
    "SURVEY_2026,RATING=2,AGE=35",
    " survey_2026 , rating = 5 , Age = 19",
    "Survey_2026 , rating = 1 , age = 42",
    " SURVEY_2026 , rating = 6 , age=28",
]

# =============================================================== PROCESS + OUTPUT

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["rating"])
    print(record, status)

    total_records += 1
    if status != "OK":
        flagged_records += 1

print(f"Summary: {total_records} records processed, {flagged_records} flagged.")


# ==========================================================================
