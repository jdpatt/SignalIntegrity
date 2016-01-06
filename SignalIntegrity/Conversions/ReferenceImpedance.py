'''
 Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
 Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
 All Rights Reserved.

 Explicit license in accompanying README.txt file.  If you don't have that file
 or do not agree to the terms in that file, then you are not licensed to use
 this material whatsoever.
'''
from numpy import matrix
from numpy import linalg
from numpy import array
from numpy import identity

from Z0KHelper import Z0KHelper

def ReferenceImpedance(S,Z0f,Z0i=None,Kf=None,Ki=None):
    (Z0f,Kf)=Z0KHelper((Z0f,Kf),len(S))
    (Z0i,Ki)=Z0KHelper((Z0i,Ki),len(S))
    I=matrix(identity(len(S)))
    p=(matrix(Z0f)-matrix(Z0i))*(matrix(Z0f)+matrix(Z0i)).getI()
    Kf=matrix(Ki)*matrix(Kf).getI()
    S=matrix(S)
    return (Kf*(I-p).getI()*(S-p)*(I-p*S).getI()*(I-p)*Kf.getI()).tolist()

