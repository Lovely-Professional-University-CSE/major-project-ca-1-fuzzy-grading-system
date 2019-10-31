import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import calculate_marks as cm

n = int(input('Enter Number of subjects:'))

mtey = cm.mte_mrks(n)
print('MTE marks:',mtey)

etey  = cm.ete_mrks(n)
print('ETE marks:',etey)

attny = cm.atten(n)
print('Attn marks:',attny)

cay = cm.ca_mrks(n)
print('CA marks:',cay)

mte=ctrl.Antecedent(np.arange(0,21,1),'mte')
ete=ctrl.Antecedent(np.arange(0,51,1),'ete')
attn=ctrl.Antecedent(np.arange(0,6,1),'attn')
ca=ctrl.Antecedent(np.arange(0,26,1),'ca')
cgpa=ctrl.Consequent(np.arange(0,11,1),'cgpa')
mte['l']=fuzz.trimf(mte.universe, [0,5,8])
mte['m']=fuzz.trimf(mte.universe,[7,11,14])
mte['h']=fuzz.trimf(mte.universe,[13,17,20])
ca['l']=fuzz.trimf(ca.universe, [0,5,10])
ca['m']=fuzz.trimf(ca.universe,[9,15,18])
ca['h']=fuzz.trimf(ca.universe,[17,22,25])
ete['l']=fuzz.trimf(ete.universe,[0,9,18])
ete['m']=fuzz.trimf(ete.universe,[15,27,38])
ete['h']=fuzz.trimf(ete.universe,[35,45,50])
attn['l']=fuzz.trimf(attn.universe, [0,1,2])
attn['m']=fuzz.trimf(attn.universe, [2,3,4])
attn['h']=fuzz.trimf(attn.universe, [3,4,5])
cgpa['l']=fuzz.trimf(cgpa.universe,[0,3,5])
cgpa['m']=fuzz.trimf(cgpa.universe,[4,6,8])
cgpa['h']=fuzz.trimf(cgpa.universe,[7,9,10])
mte['m'].view()
ete.view()
ca.view()
attn.view()
cgpa.view()
rule1=ctrl.Rule(mte['l'] | ete['l'] |attn['l'] |ca['l'],cgpa['l'])
rule2=ctrl.Rule(mte['m'] | ete['l'] |attn['l'] |ca['l'],cgpa['l'])
rule3=ctrl.Rule(mte['l'] | ete['m'] |attn['l'] |ca['l'],cgpa['l'])
rule4=ctrl.Rule(mte['l'] | ete['l'] |attn['m'] |ca['h'],cgpa['l'])
rule5=ctrl.Rule(mte['l'] | ete['l'] |attn['h'] |ca['l'],cgpa['l'])
rule6=ctrl.Rule(mte['l'] | ete['h'] |attn['l'] |ca['m'],cgpa['m'])
rule7=ctrl.Rule(mte['h'] | ete['l'] |attn['l'] |ca['m'],cgpa['m'])
rule8=ctrl.Rule(mte['l'] | ete['l'] |attn['h'] |ca['l'],cgpa['l'])
rule9=ctrl.Rule(mte['m'] | ete['m'] |attn['l'] |ca['m'],cgpa['m'])
rule10=ctrl.Rule(mte['m'] | ete['l'] |attn['m'] |ca['l'],cgpa['l'])
rule11=ctrl.Rule(mte['l'] | ete['m'] |attn['m'] |ca['m'],cgpa['m'])
rule12=ctrl.Rule(mte['m'] | ete['m'] |attn['m'] |ca['l'],cgpa['m'])
rule13=ctrl.Rule(mte['h'] | ete['h'] |attn['l'] |ca['h'],cgpa['h'])
rule14=ctrl.Rule(mte['h'] | ete['h'] |attn['h'] |ca['h'],cgpa['h'])
rule15=ctrl.Rule(mte['l'] | ete['h'] |attn['h'] |ca['h'],cgpa['h'])
rule16=ctrl.Rule(mte['h'] | ete['l'] |attn['h'] |ca['m'],cgpa['m'])

rule1.view()
rule2.view()
tipping_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16])
tipping=ctrl.ControlSystemSimulation(tipping_ctrl)
#Pass inputs to the control system using antecedent labels with pythonic api
#note: if you like passsing many inputs all at once ,use .inputs (dict_of_data)
tipping.input['mte']= mtey
tipping.input['ete']= etey
tipping.input['ca']= cay
tipping.input['attn']= attny
#Crunch the numbers
tipping.compute()
print(tipping.output['cgpa'])
cgpa.view(sim=tipping)
