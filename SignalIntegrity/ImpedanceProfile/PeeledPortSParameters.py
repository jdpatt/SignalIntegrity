"""
 peeled s-parameters
"""
# Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
# Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
# All Rights Reserved.
# 
# Explicit license in accompanying README.txt file.  If you don't have that file
# or do not agree to the terms in that file, then you are not licensed to use
# this material whatsoever.
import math
from numpy import matrix,identity

from SignalIntegrity.Conversions import S2T,T2S
from SignalIntegrity.SParameters.SParameters import SParameters
from SignalIntegrity.Devices.TLineTwoPortLossless import TLineTwoPortLossless
from SignalIntegrity.ImpedanceProfile.ImpedanceProfileWaveform import ImpedanceProfileWaveform

class PeeledPortSParameters(SParameters):
    """s-parameters of peeled impedance profile from port
    calculates the impedance profile looking into a port of a device and then assembles
    a transmission line as a cascade of small transmission line sections
    """
    def __init__(self,sp,port,timelen):
        """Constructor
        @param sp instance of class SParameters of the device
        @param port integer 1 based port to calculate
        @param timelen float time to peel
        """
        ip=ImpedanceProfileWaveform(sp,port,
            method='estimated',includePortZ=False)
        Ts=1./ip.td.Fs; sections=int(math.floor(timelen/Ts+0.5))
        tp1=[identity(2) for n in range(len(sp.f()))]
        for k in range(sections):
            tp1=[tp1[n]*matrix(S2T(TLineTwoPortLossless(ip[k],Ts,sp.m_f[n])))
                for n in range(len(sp.m_f))]
        SParameters.__init__(self,sp.m_f,[T2S(tp.tolist()) for tp in tp1])