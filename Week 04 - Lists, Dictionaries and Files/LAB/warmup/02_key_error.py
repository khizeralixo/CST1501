# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}
record["status"] = "OK" if record["value"] <= record["limit"] else "OVER LIMIT"
print(record["status"])
