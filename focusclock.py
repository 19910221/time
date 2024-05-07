# timeimport time

def focus_timer(total_time, focus_interval, break_interval):
    total_time_sec = total_time * 60
    focus_interval_sec = focus_interval * 60
    break_interval_sec = break_interval * 60
    
    while total_time_sec > 0:
        print("Focus for {} minutes".format(focus_interval))
        time.sleep(focus_interval_sec)
        total_time_sec -= focus_interval_sec
        if total_time_sec <= 0:
            break
        print("Take a break for {} minutes".format(break_interval))
        time.sleep(break_interval_sec)
        total_time_sec -= break_interval_sec

    print("Time's up! You've finished your focus session.")

if __name__ == "__main__":
    total_time = int(input("Enter total time in minutes: "))
    focus_interval = int(input("Enter focus interval in minutes: "))
    break_interval = int(input("Enter break interval in minutes: "))
    focus_timer(total_time, focus_interval, break_interval)
