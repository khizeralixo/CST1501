# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    return "OVER LIMIT" if value > limit else "OK"
    

print(check(87, 100))


