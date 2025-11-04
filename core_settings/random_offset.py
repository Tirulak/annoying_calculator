import random

# wypluwa czasami prawidłowy wynik, czasami nie

def random_offset(real):
    if random.random() < 0.6:
        return real + random.choice([-0.5, -0.1, 0.1, 0.5])
    return real