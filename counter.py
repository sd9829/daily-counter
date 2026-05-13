import os
import subprocess
from datetime import datetime

COUNTER_FILE = "counter.txt"

# Read current count
if os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "r") as f:
        count = int(f.read().strip())
else:
    count = 0

# Increment
count += 1

# Write updated count
with open(COUNTER_FILE, "w") as f:
    f.write(str(count))

print(f"[{datetime.now()}] Counter updated to {count}")

# Git commit and push
subprocess.run(["git", "add", COUNTER_FILE], check=True)
subprocess.run(["git", "commit", "-m", f"daily update: counter = {count}"], check=True)
subprocess.run(["git", "push"], check=True)

print("Pushed to GitHub successfully.")