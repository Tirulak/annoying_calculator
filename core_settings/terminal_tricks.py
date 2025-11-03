CSI = '\x1b['


def clear_screen():
    print(CSI + '2J' + CSI + 'H', end='') #czysci ekran


def blink_text(s):
    print(CSI + '5m' + s + CSI + '25m')