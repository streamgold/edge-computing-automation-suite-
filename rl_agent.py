#!/usr/bin/env python3
import os, csv, json

Q_FILE = 'rl_q_table.json'
CSV_FILE = 'system_history_telemetry.csv'

def train_reinforcement_policy():
    print("\033[1;35m🤖 EXECUTING REINFORCEMENT LEARNING POLICY INITIALIZATION...\033[0m")
    if not os.path.exists(CSV_FILE):
        return print("⚠️ Time-series database archive missing.")

    with open(CSV_FILE, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = [r for r in list(reader) if r and len(r) >= 12]

    if not rows:
        return print("⚠️ Insufficient environmental telemetry dimensions.")

    q_table = {}
    if os.path.exists(Q_FILE):
        with open(Q_FILE, 'r') as f: q_table = json.load(f)

    learning_rate = 0.2
    discount_factor = 0.95

    # Chronological step-by-step optimization loop
    for row in rows:
        hardware_core = row[7]
        try:
            baro = float(row[9])
            pressure_state = "LOW_PRESSURE" if baro < 29.90 else "HIGH_PRESSURE"
        except (ValueError, IndexError):
            pressure_state = "NORMAL_PRESSURE"
            
        state_key = f"{hardware_core}_{pressure_state}"
        
        if state_key not in q_table:
            q_table[state_key] = {str(b): 0.0 for b in range(1, 36)}

        try:
            active_signals = [int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])]
        except (ValueError, IndexError):
            continue

        # Bellman optimization updating action-reward policies
        for node_id in range(1, 36):
            node_str = str(node_id)
            reward = 10.0 if node_id in active_signals else -0.5

            old_q = q_table[state_key][node_str]
            max_future_q = max(q_table[state_key].values())
            
            # Classical temporal-difference calculation formula
            new_q = old_q + learning_rate * (reward + (discount_factor * max_future_q) - old_q)
            q_table[state_key][node_str] = round(new_q, 4)

    with open(Q_FILE, 'w') as f:
        json.dump(q_table, f, indent=2)
    print("Base reinforcement metrics computed successfully! Policy table updated.")

if __name__ == "__main__":
    train_reinforcement_policy()
