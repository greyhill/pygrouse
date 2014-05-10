import numpy as np
import numpy.linalg as la

class GROUSE(object):
    def __init__(self, n, d, U = None, eta = None):
        self.n = n
        self.d = d

        if U is not None:
            self.U = U
        else:
            self.U = np.eye(N=self.n, M=self.d)

        if eta is not None:
            self.eta0 = eta
        else:
            self.eta0 = 10.0
        self.it = 1.0

    def add_data(self, v):
        mask_c = np.isnan(v)
        mask = 1 - mask_c
        U = self.U

        n = self.n
        d = self.d

        Ov = v[mask==1]
        OU = U[mask==1,:]

        w, _, __, ___ = la.lstsq(OU, Ov)
        p = U.dot(w)
        r = np.zeros((n,))
        r[mask==1] = Ov - p[mask==1]

        sigma = la.norm(r) * la.norm(p)
        eta = self.eta0 / self.it

        pw = la.norm(p) * la.norm(w)
        rw = la.norm(r) * la.norm(w)

        if pw == 0 or rw == 0: return

        U = U + (np.cos(sigma * eta) - 1.0) * np.outer(p, w) / pw \
              + np.sin(sigma * eta) * np.outer(r, w) / rw

        self.U = U
        self.it += 1.0

