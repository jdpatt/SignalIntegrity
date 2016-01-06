'''
 Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
 Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
 All Rights Reserved.

 Explicit license in accompanying README.txt file.  If you don't have that file
 or do not agree to the terms in that file, then you are not licensed to use
 this material whatsoever.
'''
def VoltageControlledVoltageSource(G):
    return  [[1.,0.,0.,0.],
            [0.,1.,0.,0.],
            [G,-G,0.,1.],
            [-G,G,1.,0.]]