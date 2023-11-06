# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:30:27 2023

@author: Xavier
"""

file=open('PDBGEN0.pdb','r+')
strtutemp=file.readlines()
file.close()



class con:
    def __init__(self,fileline,struc):
        self.file=fileline
        self.struc=struc
    def getstructure(self):
        strtu=[]
        for i in range(len(strtutemp)):
            temp=strtutemp[i].split() 
            if temp[0]=='ATOM':
                if len(temp)>10:
                    strtu.append(temp)
                else:
                    pass
            else:
                pass
        return strtu
    def getwater(self):
        watercon=[]
        for i in range(len(self.struc)):
            if self.struc[i][3]!='H2O':
                pass
            else:
                watercon.append(self.struc[i])
        return watercon
model=con(strtutemp,[])
model.struc=model.getstructure()
watercon=model.getwater()