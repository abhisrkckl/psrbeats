import numpy as np
from scipy.io import wavfile
import sounddevice as sd

import profile

save = True

duration = 10
samplingrate = 44100
ts = np.arange(duration*samplingrate) / samplingrate

P0 = 0.01  # pulsar period
phases = 2*np.pi*ts/P0

phasebins = np.arange(512)/512.
prf = np.exp(-(phasebins-0.5)**2/0.1**2)
prf = profile.Profile(prf)

carrierfreq = 500
carrier = 1 #np.sin(2*np.pi*1000*ts)

signal = carrier*prf.eval(phases)
#data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1

if save:
    scaled = np.int16(signal/np.max(np.abs(signal)) * 32767)
    wavfile.write('test.wav', 44100, scaled)
else:
    sd.play(signal/max(signal), samplingrate)
