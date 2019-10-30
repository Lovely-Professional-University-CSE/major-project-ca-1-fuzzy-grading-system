import numpy as np

def atten(n):
    attny = []
    x = []
    print("Enter attendence of each subject:")
    for i in range(n):
        j = eval(input('Enter attendence :'))
        x.append(j)
        if (j >= 90):
            attny.append(5)
        elif (85<= j <90):
            attny.append(4)
        elif (80<= j <85):
            attny.append(3)
        elif (75<= j <80):
            attny.append(2)
        else:
            attny.append(1)
    attny = np.array(attny)
    print(x)
    return attny

def mte_mrks(n):
    mtey = []
    print('Enter mte marks of Each subjet:')
    mtex = []
    for i in range(n):
        j = eval(input('Enter mte subject marks:'))
        mtex.append(j)
        y = (j/40)*20
        mtey.append(round(y))
    mtey = np.array(mtey)
    print(mtex)
    return mtey

def ete_mrks(n):
    etey = []
    print('Enter ete marks of Each subjet:')
    etex = []
    for i in range(n):
        j = eval(input('Enter ete subject marks:'))
        etex.append(j)
        y = (j/70)*50
        etey.append(round(y))
    etey = np.array(etey)
    print(etex)
    return etey

def ca_mrks(n):
    cay = []
    print('Enter CA marks of Each subjet:')
    cax = []
    for i in range(n):
        print('Enter sbject',i+1,'CA marks:')
        caxj = []
        for j in range(3):
            z = eval(input('Enter CA marks:'))
            caxj.append(z)
        caxj.remove(min(caxj))
        cax.append(sum(caxj))
        y = (cax[i]/60)*25
        cay.append(round(y))
    cay = np.array(cay)
    print(cax)
    return cay
