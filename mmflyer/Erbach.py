# -*- coding: utf-8 -*-
#
#   Erbach.py
#   ~~~~~~~~~
#
#   Python implementation of Walter Erbach's C64 Basic program
#   from 1990 NFFS Symposium (p79-85)
###############################################################
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
import pint
import yaml

u = pint.UnitRegistry()
Q_ = u.Quantity

class Erbach(object):

    def __init__(self, debug=False):
        self.debug = debug


    def load_curve(self, key, data):
        """Load YAML curve data file"""
        x = []
        y = []
        if key in data:
            cl = data[key]
            for line in cl:
                a,b = line
                x.append(a)
                y.append(b)
        return x,y

    def fit_curve(self):
        """Return a curve fit function using spline interpolation"""
        xi = np.array(self.c_l_alpha)
        yi = np.array(self.c_l)
        x = np.linspace(-6, 20, 50)
        order = 1
        s = InterpolatedUnivariateSpline(xi, yi, k=order)
        y = s(x)
        plt.plot(x,y)
        plt.show()

    def load_model_data(self, data_fn):
        """Load YAML model data file"""
        with open(data_fn, "r") as stream:
            try:
                self.data = yaml.safe_load(stream)
                print(self.data)
                self.airfoil = self.data['airfoil']
                print(self.airfoil)
                self.c_l_alpha, self.c_l = self.load_curve('lift_coeff',self.airfoil)
                self.c_d_alpha, self.c_d = self.load_curve('drag_coeff',self.airfoil)
                self.model = self.data['model']
                print(self.model)
                self.load_model()

            except yaml.YAMLError as exc:
                print(exc)
                data = {}

        print(self.c_l_alpha, self.c_l)
        print(self.c_d_alpha, self.c_d)
        self.fit_curve()

    def load_model(self):
        data = self.model
        wa_val, wa_units = data['model_weight']
        wa = Q_(wa_val, wa_units)
        print("Wing Area", wa)
        print("base Units", wa.to_base_units())

    def power(self, WI, SA, CG, PCW):
        self.fit_curve()
        return

        print(WI, SA, CG, PCW)
        rho = 0.00119
        alpha_w = (WI - SA)   # Wing angle of attack
        alpha_s = (SA)        # Stab angle of attack
        C_lw = self.query(alpha_w, m.alpha, m.C_l)
        C_ls = self.query(alpha_s, m.alpha, m.C_l)
        C_dw = self.query(alpha_w, m.alpha, m.C_d)
        C_ds = self.query(alpha_s, m.alpha, m.C_d)
        print(C_lw, C_ls, C_dw, C_ds)

        VE = (t["WT"]/(0.00119*t["SW"]*(C_lw + PCW*C_ls)))**0.5
        VE2_16 = VE*VE*16
        f1 = rho/2.0*t["SW"]*VE2_16
        AWL = C_ls * f1
        BWD = C_lw * f1
        CTL = C_dw * f1*PCW
        DTD = C_ds * f1*PCW

        PWR= VE*(BWD+DTD)*12
        DW = t["WC"] * (CG -0.25)
        R = SA
        EWLA = t["WH"]*np.sin(R)+DW*np.cos(R)
        FWDA = t["WH"]*np.cos(R)-DW*np.sin(R)
        GTLA = (t["TA"]-DW)*np.cos(R)
        HTDA = (t["TA"]-DW)*np.sin(R)
        JMWL = AWL*EWLA
        KMWD = BWD*FWDA
        LMTL = -CTL*GTLA
        MMTD = DTD*HTDA
        CM = JMWL + KMWD + LMTL + MMTD
        CO = CG*100
        print("VE",VE,"PWR", PWR,"CM", CM,"CO", CO)


if __name__ == '__main__':
    e = Erbach()
    e.power(4,-2,0.4,0.4)
