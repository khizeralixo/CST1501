# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt") as f:
    f.write("R-001, 87.0,100.0")

with open("records.txt") as f:
    print(f.read())
