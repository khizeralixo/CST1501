
print("=" * 27)
print("RECORD CHECK  -  my version")
print("=" * 27)
if input("Check Record ID (or quit): ") == "quit":
        print("Exiting the program...Goodbye!")
        exit()

print(input("Enter your name: "))
print(input("Enter your lane (AI / Cyber / IT): "))
print(float(input("Enter the date: ")))

label = input("Record ID: ")   
value = float(input("Value: "))
limit = float(input("Limit: "))

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

difference = value - limit
percent = (difference / limit) * 100

if percent > 100:
    status = "OVER LIMIT"
elif percent > 90:
    status = "WARNING"
else:
    status = "OK"

# experimented with different wauys to format the output, but this is the one I liked best.

print("=" * 30)
print(f"{'Value':<15} {value:>12.2f}")
print(f"{'Limit':<15} {limit:>12.2f}")
print(f"{'Difference':<15} {difference:>12.2f}")
print(f"{'Percent':<15} {f'{percent:.2f}%':>12}")
print(f"{'Status':<15} {status:>12}")
print("=" * 30)


# ==========================================================================
