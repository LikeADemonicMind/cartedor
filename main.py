# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 09:39:06 2023

@author: Utilisateur
"""
#import pandas as pd # Import de la librairie Pandas
#import matplotlib.pyplot as plt # Import de la librairie matplotlib
#import numpy as np # Import de la librairie numpy
#from scipy import stats # Import de stats depuis la librairie scipy"""
from librairies import librairies
from nettoyage_et_merge import nettoyage_et_merge
def main():
    librairies()
    nettoyage_et_merge()
if __name__ == "__main__":
    main()