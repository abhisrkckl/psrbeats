import numpy as np

class Profile:
    def __init__(self, prf):
        self.nbin = len(prf)
        self.prfx = np.arange(self.nbin)/self.nbin
        self.prfy = prf

    def eval(self, phase):
        phase1 = (phase/(2*np.pi))%1
        return np.interp(phase1, self.prfx, self.prfy)
