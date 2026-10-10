def status_of(percent: float) -> str:
    if percent >= 100.0:
        return "OVER LIMIT"
    elif percent > 95.0:
        return "WARNING"
    return "OK"


def check(value: float, limit: float) -> tuple[float, float]:
    difference = value - limit
    percent = (value / limit) * 100.0
    return difference, percent


def print_report(label: str, value: float, limit: float, difference: float, percent: float, status: str) -> None:
    width = 38
    print()
    print("=" * width)
    print(f" RECORD CHECK - {label}")
    print("=" * width)
    print(f" {'Value:':<16} {value:>16.2f}")
    print(f" {'Limit:':<16} {limit:>16.2f}")
    print(f" {'Difference:':<16} {difference:>16.2f}")
    print(f" {'Percent:':<16} {percent:>15.2f}%")
    print(f" {'Status:':<16} {status:>16}")
    print("=" * width)


if __name__ == "__main__":
    over_limit_count = 0
    while True:
        label = input("\nEnter record label (or 'quit' to stop): ")
        if label == "quit":
            break

        value = float(input("Enter value: "))
        limit = float(input("Enter limit: "))

        difference, percent = check(value, limit)
        status = status_of(percent)

        if status == "OVER LIMIT":
            over_limit_count += 1

        print_report(label, value, limit, difference, percent, status)

    print(f"\nSession complete. Total records OVER LIMIT: {over_limit_count}")
   

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
