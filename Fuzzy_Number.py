import numpy as np
import matplotlib.pyplot as plt


class Fuzzy(object):

    def __init__(self, *args):
        self.lower = args[0]
        self.m_val_1 = args[1]
        self.upper = args[-1]
        if len(args) == 4:
            self.m_val_2 = args[2]
        if len(args) == 3:
            self.m_val_2 = None

    def __add__(self, plus):
        llower = plus.lower + self.lower
        mm_val_1 = plus.m_val_1 + self.m_val_1
        uuper = plus.upper + self.upper
        if self.m_val_2:
            mm_val_2 = plus.m_val_2 + self.m_val_2
            return Fuzzy(llower, mm_val_1, mm_val_2, uuper)
        else:
            return Fuzzy(llower, mm_val_1, uuper)

    def __sub__(self, minus):
        llower = self.lower - minus.upper
        uuper = self.upper - minus.lower
        if self.m_val_2:
            mm_val_1 = self.m_val_1 - minus.m_val_2
            mm_val_2 = self.m_val_2 - minus.m_val_1
            return Fuzzy(llower, mm_val_1, mm_val_2, uuper)
        else:
            mm_val_1 = self.m_val_1 - minus.m_val_1
            return Fuzzy(llower, mm_val_1, uuper)

    def __repr__(self):
        if self.m_val_2:
            return "Fuzzy(%d, %d, %d, %d)" % (self.lower, self.m_val_1, self.m_val_2, self.upper)
        else:
            return "Fuzzy(%d, %d, %d)" % (self.lower, self.m_val_1, self.upper)

    def plot_fuzzy(self, leg, style):
        if self.m_val_2:
            plt_X = [self.lower, self.m_val_1, self.m_val_2, self.upper]
            plt_Y = [0, 1, 1, 0]
        else:
            plt_X = [self.lower, self.m_val_1, self.upper]
            plt_Y = [0,1,0]
        plt.plot(plt_X, plt_Y, label=leg, linestyle=style)
        plt.legend()


A = Fuzzy(1,2,6)
B = Fuzzy(3,5,8)
s = A + B
t = A - B
A.plot_fuzzy('A', '--')
B.plot_fuzzy('B', '--')
s.plot_fuzzy('A+B', '-')
t.plot_fuzzy('A-B', '-')
plt.grid()
plt.show()
