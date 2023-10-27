#!/usr/bin/env python3

import os
import random
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <number of child processes>".format(sys.argv[0]))
        sys.exit(1)

    num_children = int(sys.argv[1])

    for i in range(num_children):
        child_pid = os.fork()

        if child_pid == 0:
            random_sleep = random.randint(5, 10)
            os.execl("./child.py", "child.py", str(random_sleep))
            sys.exit(0)

        print("Parent[{}]: I ran children process with PID {}.".format(os.getpid(), child_pid))

    for i in range(num_children):
        child_pid, status = os.wait()
        print("Parent[{}]: Child with PID {} terminated. Exit Status {}.".format(os.getpid(), child_pid, status))

if __name__ == "__main__":
    main()