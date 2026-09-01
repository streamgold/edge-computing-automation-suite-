#!/usr/bin/env python3
import os, csv

CSV_FILE = 'system_history_telemetry.csv'

def scan_physical_telemetry():
    print(f"\033[1;36m📡 METEOROLOGICAL & MECHANICAL METADATA SCANNER ACTIVE\033[0m")
    print(f"=========================================================================")
    
    if not os.path.exists(CSV_FILE):
        return print("⚠️ Error: Micro-telemetry database log archive unavailable.")

    with open(CSV_FILE, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = [r for r in list(reader) if r and len(r) >= 12]

    if not rows:
        return print("⚠️ No operational telemetry data fields recorded yet.")

    latest_vector = rows[-1]
    print(f" ➔ Monitored Log Execution ID : \033[1;35m{latest_vector[0]} ({latest_vector[1]})\033[0m")
    print(f" ➔ Active Ingested Signal     : [ {latest_vector[2]} - {latest_vector[3]} - {latest_vector[4]} - {latest_vector[5]} - {latest_vector[6]} ]")
    print(f"-------------------------------------------------------------------------")
    print(f" \033[1;33m🛠️  HARDWARE INFRASTRUCTURE CONSTRAINTS:\033[0m")
    print(f"  ▪ Active Engine Server Processing Core : \033[1;32m{latest_vector[7]}\033[0m")
    print(f"  ▪ Signal Component Calibration Group   : \033[1;32mBlock #{latest_vector[8]}\033[0m")
    print(f"  ▪ Ingestion Queue Array Allocation     : \033[1;32m{latest_vector[11]}\033[0m")
    print(f"-------------------------------------------------------------------------")
    print(f" \033[1;34m🌤️  AMBIENT DEVICE METEOROLOGICAL MATRIX:\033[0m")
    print(f"  ▪ Station Atmospheric Barometric Weight: \033[1;32m{latest_vector[9]} inHg\033[0m")
    print(f"  ▪ Relative Processing Studio Humidity  : \033[1;32m{latest_vector[10]}%\033[0m")
    print(f"=========================================================================")

if __name__ == "__main__":
    scan_physical_telemetry()
