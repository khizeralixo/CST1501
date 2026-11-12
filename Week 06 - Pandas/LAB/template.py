
# RECORD CHECK  -  my version
# ===========================

# Name  : Khizer Ali
# Lane  : AI
# Date  : 7th November 2026



import pandas as pd
import matplotlib.pyplot as plt

# made my own csv file called "server_records.csv" in this folder.
# it has 6 servers for my AI lane with columns: hostname, used_gb, total_gb.

df = pd.read_csv("server_records.csv")

# Calculating the percentage used for each server

df['percent'] = (df["used_gb"] / df["total_gb"]) * 100

# now i'm adding the status column using .apply() and a lambda

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")

)

# printing the whole table so i can see all my servers with their new percent and status.

print("=" * 60)
print("MY RECORD CHECK - ALL SERVERS (Threshold)")
print("=" * 60)
print(df)
print()

# Here i only want to see the servers that have issues (anything that ism't "OK")
# Instead of writing an IF statement, I will put the check df["status"] != "OK" inside.

flagged_servers = df[df["status"] != "OK"]
print("=" * 60)
print("SERVERS NEEDING ATTENTION (typical)")
print("=" * 60)
print(flagged_servers)

# now i will use group by status to count them up

print("=" * 60)
print("STATUS SUMMARY (Excellent)")
print("=" * 60)
status_counts = df["status"].value_counts()
print(status_counts)
print()


#I added index=false because if i don't, pandas writes an extra column of 0, 1, 2 row numbers
#into the csv which i don't want

output_file = "record_check_report.csv"
df.to_csv(output_file, index=False)
print(f"Saved my updated table to {output_file}")

# Plotting the counts as a bar chart so its easy to see how many servers are critical.

status_counts.plot(kind="bar", color=["green", "red", "orange"])
plt.title("Server Storage Status Overview")
plt.xlabel("Status Category")
plt.ylabel("Number of Servers")
plt.tight_layout()

# Saving the picture to disc first, then showing it on the screen

chart_name = "status_summary.png"
plt.savefig(chart_name)
print(f"Saved my bar chart image to {chart_name}")
plt.show()