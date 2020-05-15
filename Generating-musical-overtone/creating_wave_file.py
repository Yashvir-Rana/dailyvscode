# creating wav file

import numpy as np
import wave, math

srate = 44100
nsamples = srate * 5
x = np.arange(nsamples)/float(srate)
vals = np.sin(2.0*math.pi*220.0*x)
data = np.array(vals*32767, 'int16').tostring()
file = wave.open('sine220.wav', 'wb')
file.setparams((1, 2, srate, nsamples, 'NONE', 'uncompressed'))
file.writeframes(data)
file.close()
