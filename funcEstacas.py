from math import pi
import numpy as np

def areaEstaca(diametro):

    area = pi * (diametro ** 2) / 4

    return area

def volumeEstaca(diametro, prof):

    volumeEst = areaEstaca(diametro) * prof

    return volumeEst

def areaLateralEstaca(diametro, prof):

    areaLat = pi * diametro * prof

    return areaLat
