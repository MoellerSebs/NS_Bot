# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:47:23 2016

@author: hansb
"""

# Utility functions for NS code

#%% Convert from name into url string
def urlConv(string):
    x = list(string)
    for n, i in enumerate(x):
        if (i == ' ' or i == '/' or i == '\\'):            
            x[n] = '+'
    return ''.join(x)
    
def exRem(string):
    x = list(string)
    for n in enumerate(x):
        if (n < len(x) - 10):
            if (x[n] + x[n+1] + x[n+2] + x[n+3] + x[n+4] + x[n+5] + x[n+6] + x[n+7] + x[n+8] == '<Bericht>'):
                for a in range(9):
                    x[n + 9 + a] = ''
            if (x[n] + x[n+1] + x[n+2] + x[n+3] + x[n+4] + x[n+5] + x[n+6] + x[n+7] + x[n+8] + x[n+9] == '</Bericht>'):
                x[n - 1] = ''
            if (x[n] == ']'):
                x[n] = ''
    return ''.join(x)