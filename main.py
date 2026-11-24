"""Charm the Commuter: a forecast for Brindlewick, a city that isn't.

Writes one line — 111 characters, no trailing newline — to /output/entry.txt:
drizzle until 9 AM, then sunshine, and a bus that is on time for once.
"""

import os

FORECAST = "In Brindlewick, drizzle until 9 AM, then sunshine. The 8:15 bus is on time for once — check if you're dreaming."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORECAST)

if __name__ == "__main__":
    main()
