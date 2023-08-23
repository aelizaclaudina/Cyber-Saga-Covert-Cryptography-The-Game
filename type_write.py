import time
import sys

def print_type(write):
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
    next=input()


