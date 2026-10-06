import time

def check_system_speed(response_time):
    if response_time > 2.5:
        return "WARNING: System latency is too high!"
    return "SPEED STATUS: OPTIMAL"

print(check_system_speed(0.45))

def clear_old_logs(file_count):
    if file_count > 50:
        return "ACTION: Cleaning up cached log files..."
    return "LOG STATUS: CLEAR"

print(clear_old_logs(12))
print("Performance optimizer initialized successfully.")
