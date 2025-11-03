import sys
import time


def fake_hang(duration=1.2):
    t = 0
    while t < duration:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.15)
        t += 0.15
    print()