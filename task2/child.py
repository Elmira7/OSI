#!/usr/bin/env python3

import os
import sys
import time
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <sleep duration>".format(sys.argv[0]))
        sys.exit(1)

    sleep_duration = int(sys.argv[1])
    pid = os.getpid()
    ppid = os.getppid()

    print("Child[{}]: I am started. My PID {}. Parent PID {}.".format(pid, pid, ppid))

    time.sleep(sleep_duration)

    exit_status = random.choice([0, 1])
    print("Child[{}]: I am ended. PID {}. Parent PID {}. Exit Status {}.".format(pid, pid, ppid, exit_status))
    sys.exit(exit_status)

if __name__ == "__main__":
    main()