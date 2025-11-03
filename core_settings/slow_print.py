import sys
import time


def type_out(s, char_delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()