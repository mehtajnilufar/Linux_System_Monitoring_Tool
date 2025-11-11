import psutil
import time
from datetime import datetime

# Thresholds
CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 90

log_file = "log.txt"

def log(message):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)


def monitor():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log(f"CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%")

    if cpu > CPU_LIMIT:
        log(" WARNING: High CPU Usage!")

    if ram > RAM_LIMIT:
        log(" WARNING: High RAM Usage!")

    if disk > DISK_LIMIT:
        log("WARNING:  Low Disk Space!")

while True:
    monitor()
    time.sleep(5)  # check every 5 seconds

