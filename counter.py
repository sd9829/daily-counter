import os
import subprocess
from datetime import datetime

COUNTER_FILE = "counter.txt"
LAST_RUN_FILE = "last_run.txt"

today = datetime.now().strftime("%Y-%m-%d")

# Check if already ran today
if os.path.exists(LAST_RUN_FILE):
    with open(LAST_RUN_FILE, "r") as f:
        last_run = f.read().strip()
    if last_run == today:
        print(f"[{datetime.now()}] Already ran today ({today}), skipping.")
        exit(0)

# Read and increment counter
if os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "r") as f:
        count = int(f.read().strip())
else:
    count = 0

count += 1

# Write updated counter
with open(COUNTER_FILE, "w") as f:
    f.write(str(count))

# Write today's date as last run
with open(LAST_RUN_FILE, "w") as f:
    f.write(today)

print(f"[{datetime.now()}] Counter updated to {count}")

# Git commit and push
subprocess.run(["git", "add", COUNTER_FILE, LAST_RUN_FILE], check=True)
subprocess.run(["git", "commit", "-m", f"daily update: counter = {count}"], check=True)
subprocess.run(["git", "push"], check=True)

print("Pushed to GitHub successfully.")