

# Name  : (Khizer ALi)
# Lane  : (AI)
# Date  : (26 September 2026)


dataset_name = input("Enter DataSet name:")
rows_loaded = float(input("Enter Rows Loaded:"))
rows_expected = float(input("Enter Rows Expected: "))


# ================================================================== PROCESS


difference = rows_loaded - rows_expected
completion_percent = (rows_loaded / rows_expected) * 100


print()
print("=" * 45)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 45)
print(f" Rows Loaded   : {rows_loaded:>10.2f}")
print(f" Rows Expected : {rows_expected:>10.2f}")
print(f" Difference    : {difference:>+10.2f}")
print(f" Completion    : {completion_percent:>+10.2f}%")


# outputs will vary depending on different values entered.

print("=" * 45)


# ==========================================================================
