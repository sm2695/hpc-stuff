# keeps the session from logging out due to inactivity. Useful when tmux or screen is not an option
import os
import time

def keep_alive(interval=60):
    """
    Sends a 'keep-alive' signal by running a harmless command every interval seconds.
    :param interval: The time interval (in seconds) between sending keep-alive signals.
    """
    try:
        while True:
            # Sending a harmless 'echo' command to keep the session active.
            os.system("echo ''")
            print(f"Keep-alive signal sent, waiting for {interval} seconds...")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Exiting keep-alive script.")
        pass

if __name__ == "__main__":
    keep_alive(interval=60)  # Set the interval in seconds (e.g., every 60 seconds)

#run nohup python3 keep_alive.py & in the terminal
