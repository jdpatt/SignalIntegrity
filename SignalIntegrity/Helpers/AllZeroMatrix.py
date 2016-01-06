'''
 Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
 Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
 All Rights Reserved.

 Explicit license in accompanying README.txt file.  If you don't have that file
 or do not agree to the terms in that file, then you are not licensed to use
 this material whatsoever.
'''
def AllZeroMatrix(M):
    for r in range(len(M)):
        for c in range(len(M[r])):
            try:
                if complex(M[r][c]) != 0.:
                    return False
            except ValueError:
                return False
    return True

def ZeroColumns(M):
    zeroColumnList=[]
    for c in range(len(M[0])):
        isAZeroColumn=True
        for r in range(len(M)):
            try:
                if complex(M[r][c]) != 0.:
                    isAZeroColumn=False
                    break
            except ValueError:
                isAZeroColumn=False
                break
        if isAZeroColumn:
            zeroColumnList.append(c)
    return zeroColumnList

def ZeroRows(M):
    zeroRowList=[]
    for r in range(len(M)):
        isAZeroRow=True
        for c in range(len(M[r])):
            try:
                if complex(M[r][c]) != 0.:
                    isAZeroRow=False
                    break
            except ValueError:
                isAZeroRow=False
                break
        if isAZeroRow:
            zeroRowList.append(r)
    return zeroRowList

def NonZeroColumns(M):
    NonZeroColumnList=[]
    for c in range(len(M[0])):
        isAZeroColumn=True
        for r in range(len(M)):
            try:
                if complex(M[r][c]) != 0.:
                    isAZeroColumn=False
                    break
            except ValueError:
                isAZeroColumn=False
                break
        if not isAZeroColumn:
            NonZeroColumnList.append(c)
    return NonZeroColumnList

def NonZeroRows(M):
    NonZeroRowList=[]
    for r in range(len(M)):
        isAZeroRow=True
        for c in range(len(M[r])):
            try:
                if complex(M[r][c]) != 0.:
                    isAZeroRow=False
                    break
            except ValueError:
                isAZeroRow=False
                break
        if not isAZeroRow:
            NonZeroRowList.append(r)
    return NonZeroRowList

