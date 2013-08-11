#!/usr/bin/env python3
import os
import random
from glob import glob

import pyglet

# load sounds
paths = glob(os.path.expanduser('/home/jake/Programming/origin/Learning-Python/HF-Programming.HFP-CH7/*.wav'))
sounds = [pyglet.media.load(p, streaming=False) for p in paths]

# play them in parallel
for sound in sounds:
    player = sound.play()
    player.volume = random.random()
    player.push_handlers(on_eos=lambda: print('done playing the sound'))

# exit in `delay` seconds
pyglet.clock.schedule_once(lambda dt: pyglet.app.exit(), delay=10)
# run event loop
pyglet.app.run()

