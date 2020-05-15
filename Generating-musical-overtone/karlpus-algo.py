import sys, os
import time, random
import wave, argparse, pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

# show plot of algorithm in action ?
gshowplot = False
# notes of a pentatonic minor scale
# piano c4-e(b)-f-g-b(b)-c5
pmnotes = {'C4': 262, 'Eb': 311, 'F': 349, 'G': 391, 'Bb': 466}

#1. writing a wav file

def write_wave(fname, data):
    file = wave.open(fname, 'wb') # open file
    #wave file parameter
    nchannels = 1
    samplewidth = 2
    framerate = 44100
    nframes = 44100
    # set parameters
    file.setparams((nchannels, samplewidth, framerate, nframes, 'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()

#2. generate note of given frequency

def generate_note(freq):
    nsamples = 44100
    sampleRate = 44100
    N = int(sampleRate/ freq)

    # initialise ring buffer

    buf = deque([random.random() - 0.5 for i in range(N)])
    #plot of flag set
    if gshowplot:
        axline, = plt.plot(buf)

    # initialise sample buffer

    samples = np.array([0]*nsamples, 'float32')
    for i in range(nsamples):
        samples[i] = buf[0]
        avg = 0.995*0.5*(buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()
        #plot of flag set
        if gshowplot:
            if i % 1000 == 0:
                axline.set_ydata(buf)
                plt.draw()

    # converts samples to 16-bit values and then to a string
    # the maximum value is 32767 for 16-bit

    samples = np.array(samples*32767, 'int16')
    return samples.tostring()

# play a wav file using pygame

class Noteplayer:
    def __init__(self): # constructor
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        self.notes = {} # dictionary of notes

    # add a note
    def add(self, filename):
        self.notes[filename] = pygame.mixer.sound(filename)
    # play a note
    def play(self, filename):
        try:
            self.notes[filename].play()
        except:
            print(filename + 'not found !')
    def playrandom(self):
        """play a random note"""
        index = random.randint(0, len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()
    
    # main()function

def main():
        global gshowplot

        parser = argparse.ArgumentParser(description="Generating sounds with karplus string algorithm")

        # add arguments
        parser.add_argument('--display', action = 'store_true', required = False)
        parser.add_argument('--play', action = 'store_true', required = False)
        parser.add_argument('--piano', action = 'store_true', required = False)
        args = parser.parse_args()

        #show plot if flag set
        if args.display:
            gshowplot = True
            plt.ion()

    # create note player

        nplayer = Noteplayer()

        print('creating notes...')
        for name, freq in list(pmnotes.items()):
            filename = name +'.wav'
            if not os.path.exists(filename) or args.display:
                data = generate_note(freq)
                print('creating' + filename + '...')
                write_wave(filename, data)
            else:
                print('filename already created. skipping...')

            # add note to player
            nplayer.add(name + '.wav')

            # play note if display flag set
            if args.display:
                nplayer.play(name + '.wav')
                time.sleep(0.5)

    # play a random tune
        if args.play:
            while True:
                try:
                    nplayer.playrandom()
                    #rest - 1 to 8 beats
                    rest = np.random.choice([1, 2, 4 , 8], 1, p = [0.15, 0.7, 0.1, 0.05])
                    time.sleep(0.25*rest[0])
                except KeyboardInterrupt:
                    exit()
    # random piano mode
        if args.piano:
            while True:
                for event in pygame.event.get():
                    if (event.type == pygame.KEYUP):
                        print("key pressed")
                        nplayer.playrandom()
                        time.sleep(0.5)
# call main
if __name__ == '__main__':
    main()

            










