'''
 Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
 Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
 All Rights Reserved.

 Explicit license in accompanying README.txt file.  If you don't have that file
 or do not agree to the terms in that file, then you are not licensed to use
 this material whatsoever.
'''
from numpy import matrix
from numpy import identity

from Z0KHelper import Z0KHelper
from Z0KHelperPW import Z0KHelperPW

def Sw2Sp(Sp,Z0w=None,Z0p=None,Kw=None,Kp=None):
    if Z0p is None:
        Z0p=Z0w
    (Z0w,Kw)=Z0KHelper((Z0w,Kw),len(Sp))
    (Z0p,Kp)=Z0KHelperPW((Z0p,Kp),len(Sp))
    Sp=matrix(Sp)
    Sw=(Kp.getI()*Kw*Z0w.getI()*((Z0w-Z0p.conjugate())+(Z0w+Z0p.conjugate())*Sp)*
        ((Z0w+Z0p)+(Z0w-Z0p)*Sp).getI()*Kp*Kw.getI()*Z0w)
    return Sw