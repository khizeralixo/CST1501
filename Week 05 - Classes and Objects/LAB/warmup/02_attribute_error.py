# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value    # changed amount to value so r.value works
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
