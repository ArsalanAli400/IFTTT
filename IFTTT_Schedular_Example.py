"""

    Example of Ifttt emailing schedular
"""
from IFTTT import *
import time

if __name__ == "__main__":
    # ifttt time schedular configuration and data example
    set_time = ["time 1", "time 2"] # format: hh:mm:ss -> 07:29:20
    Private_key = "your private key"
    event_name = "event name"
    values = {'value1': 'your data'}

    # Ifttt library time schedule usage
    """
        Service 1
    """
    ifttt_Sch = ifttt_schedular(set_time, Private_key, event_name, values)
    ifttt_Sch.start()

    """
        Service 2
    """
    while True:
        print("Foreground Service running")
        time.sleep(1)