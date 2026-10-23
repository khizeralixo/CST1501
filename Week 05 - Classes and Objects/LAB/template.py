"""
RECORD CHECK  -  my version
===========================

Name  :  Khizer Ali
Lane  :  AI
Date  :  21/10/2026

Run it:   python template.py
"""

# ====================================================================== CLASS

class Record:
    def __init__(self, label, value, limit):
        """Set up a record with its label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value and limit."""
        # work out the percentage first
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    # open the file and turn each line into a Record object
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("records_sample.txt")


# ==================================================================== OUTPUT

# keep track of how many records went over the limit
over_limit_count = 0

for record in records:
    # call status() once and store it in a variable
    current_status = record.status()

    if current_status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value       : {record.value}")
    print(f"  Limit       : {record.limit}")
    print(f"  Status      : {current_status}")
    print("=" * 34)

print()
print(f"Checked {len(records)} records. {over_limit_count} were OVER LIMIT.")
