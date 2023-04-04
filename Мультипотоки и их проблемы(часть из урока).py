import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'Плотва', 'Окунь', 'Лещ')

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)
        self.need_stop = False

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            _ = worm ** 10000
            time.sleep(0.01)
            fish = random.choice(FISH)
            if fish is not None:
                print(f'{self.name}: червяк № {worm} - забросил...', flush=True)
            else:
                print(f'{self.name}: Ага, поймал {fish}', flush=True)
                self.catch[fish] += 1
            if self.need_stop:
                print(f'{self.name}: Ой, жена завет! Сматываем удочки...', flush=True)
                break

vasay = Fisher(name="Вася", worms=100)
vasay.start()
time.sleep(1)
if vasay.is_alive():
    vasay.need_stop = True
vasay.join()
