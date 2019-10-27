import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

mte=ctrl.Antecedent(np.arange(0,21,1),'mte')
ete=ctrl.Antecedent(np.arange(0,51,1),'ete')
attn=ctrl.Antecedent(np.arange(0,6,1),'attn')
ca=ctrl.Antecedent(np.arange(0,26,1),'ca')
cgpa=ctrl.Consequent(np.arange(0,11,1),'cgpa')
#auto -membership function population is possible with .automf(3,5,7)
mte.automf(3)
ete.automf(3)
ca.automf(3)
attn.automf(3)
cgpa['l']=fuzz.trimf(cgpa.universe,[0,3,4])
cgpa['m']=fuzz.trimf(cgpa.universe,[4,6,8])
cgpa['h']=fuzz.trimf(cgpa.universe,[8,9,10])
mte['average'].view()
ete.view()
cgpa.view()
rule1=ctrl.rule(mte['l'] | ete['l'] |att['l'],grade['l'])
rule2=ctrl.rule(mte['m'] | ete['l'] |att['l'],grade['l'])
rule3=ctrl.rule(mte['l'] | ete['m'] |att['l'],grade['l'])
rule4=ctrl.rule(mte['l'] | ete['l'] |att['m'],grade['l'])
rule5=ctrl.rule(mte['l'] | ete['l'] |att['h'],grade['l'])
rule6=ctrl.rule(mte['l'] | ete['h'] |att['l'],grade['m'])
rule7=ctrl.rule(mte['h'] | ete['l'] |att['l'],grade['m'])
rule8=ctrl.rule(mte['l'] | ete['l'] |att['h'],grade['l'])
rule9=ctrl.rule(mte['m'] | ete['m'] |att['l'],grade['m'])
rule10=ctrl.rule(mte['m'] | ete['l'] |att['m'],grade['l'])
rule11=ctrl.rule(mte['l'] | ete['m'] |att['m'],grade['m'])
rule12=ctrl.rule(mte['m'] | ete['m'] |att['m'],grade['m'])
rule13=ctrl.rule(mte['h'] | ete['h'] |att['l'],grade['h'])
rule14=ctrl.rule(mte['h'] | ete['h'] |att['h'],grade['h'])
rule15==ctrl.rule(mte['l'] | ete['h'] |att['h'],grade['h'])
rule16==ctrl.rule(mte['h'] | ete['l'] |att['h'],grade['m'])

rule1.view()
rule2.view()
tipping_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16])
tipping=ctrl.ControlSystemSimulation(tipping_ctrl)
#Pass inputs to the control system using antecedent labels with pythonic api
#note: if you like passsing many inputs all at once ,use .inputs (dict_of_data)
tipping.input['mte']=15
tipping.input['ete']=45
tipping.input['ca']=14
tipping.input['attn']=4
#Crunch the numbers
tipping.compute()
print(tipping.output['cgpa'])
cgpa.view(sim=tipping)
