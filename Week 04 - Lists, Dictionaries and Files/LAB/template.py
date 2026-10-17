
# RECORD CHECK  -  my version
#===========================#

# Name: Khizer Ali
# Lane  :  AI 
#Date  :

# Run it:   python template.py


def check_record(value, limit):

    # how far off are we from the ceiling?
    difference = value - limit
    
    # what chunk of the allowed limit did we actually use?
    percent = (value / limit) * 100
    
    # flag anything that crossed the line or got uncomfortably close
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
        
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
# Formats and prints a single record's evaluation cleanly.

    # lining up the text nicely so the output doesn't look messy
    print(f"{label:<16} | Value: {value:>6.1f} | Limit: {limit:>6.1f} | {percent:>5.1f}% | {status}")


def print_summary(over_count, total_count):
    """Prints the final breakdown tally at the bottom of the run."""
    print("-" * 65)
    print(f"Summary: {over_count} of {total_count} records were OVER LIMIT.")


def load_records(path):
    """Reads a CSV-style file and parses each line into a clean dict."""
    parsed_records = []
    
    # safe file open - auto closes even if something hiccups inside
    with open(path, "r") as f:
        for line in f:
            cleaned = line.strip()
            
            # skip random empty lines so they don't break our unpacking
            if not cleaned:
                continue
            
            label, raw_val, raw_lim = cleaned.split(",")
            
            # turn number strings into actual floats so we can do math
            parsed_records.append({
                "label": label,
                "value": float(raw_val),
                "limit": float(raw_lim)
            })
            
    return parsed_records


# set up a quick test data file so load_records has something real to chew on
input_filename = "server_metrics.txt"
with open(input_filename, "w") as f:
    f.write("Auth_Attempts,120,100\n")
    f.write("Port_Scan_Hits,92,100\n")
    f.write("Failed_Logins,35,50\n")
    f.write("Bandwidth_Mbps,980,1000\n")
    f.write("Disk_Fill_Pct,102,100\n")

# load the data safely - if the file is gone, don't just crash out
try:
    records = load_records(input_filename)
except FileNotFoundError:
    print(f"Heads up: Couldn't find '{input_filename}'. Double check the folder.")
    records = []

# keep a running tally for the summary and collect lines for our output log
over_limit_count = 0
export_lines = []

print(f"{'METRIC':<16} | {'VALUE':>6} | {'LIMIT':>6} | {'USAGE':>6} | STATUS")
print("=" * 65)

for record in records:
    # run the math for this specific metric
    diff, pct, status = check_record(record["value"], record["limit"])
    
    # pass all printing duty off to print_report
    print_report(record["label"], record["value"], record["limit"], diff, pct, status)
    
    # track our count if it blew past the threshold
    if status == "OVER LIMIT":
        over_limit_count += 1
        
    # stash the line so we can dump it out to a file after
    export_lines.append(f"{record['label']},{status}\n")

# print the summary footer (only print functions handle output)
if records:
    print_summary(over_limit_count, len(records))

# save results to a clean summary file
output_filename = "audit_results.txt"
with open(output_filename, "w") as out_file:
    out_file.writelines(export_lines)