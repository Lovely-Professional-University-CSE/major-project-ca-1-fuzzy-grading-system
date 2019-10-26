import numpy as np

def atten(x):
    attny = []
    for i in range(len(x)):
        if (x[i] >= 90):
            attny.append(5)
        elif (85<= x[i] <90):
            attny.append(4)
        elif (80<= x[i] <85):
            attny.append(3)
        elif (75<= x[i] <80):
            attny.append(2)
        else:
            attny.append(1)
    attny = np.array(attny)
    return attny

def mte_mrks(mtex):
    mtey = []
    for i in range(len(mtex)):
        y = (mtex[i]/40)*20
        mtey.append(round(y))
    mtey = np.array(mtey)
    return mtey

def ete_mrks(etex):
    etey = []
    for i in range(len(etex)):
        y = (etex[i]/70)*50
        etey.append(round(y))
    etey = np.array(etey)
    return etey

def ca_mrks(cax):
    cay = []
    for i in range(len(cax)):
        y = (cax[i]/60)*25
        cay.append(round(y))
    cay = np.array(cay)
    return cay


n = int(input('Enter Number of subjects:'))
x = []
print("Enter attendence of each subject:")
for i in range(n):
    j = eval(input('Enter attendence :'))
    x.append(j)
print(x)

print('Enter mte marks of Each subjet:')
mtex = []
for i in range(n):
    j = eval(input('Enter mte subject marks:'))
    mtex.append(j)
print(mtex)
print('Enter ete marks of Each subjet:')
etex = []
for i in range(n):
    j = eval(input('Enter ete subject marks:'))
    etex.append(j)
print(etex)

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
print(cax)

print("Attendence Marks: ",atten(x))
print("MTE Marks: ",mte_mrks(mtex))
print("ETE Marks:  ",ete_mrks(etex))
print("CA Marks: ",ca_mrks(cax))
