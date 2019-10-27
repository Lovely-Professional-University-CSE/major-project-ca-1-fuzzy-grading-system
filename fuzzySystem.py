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
cgpa['low']=fuzz.trimf(cgpa.universe,[0,3,4])
cgpa['medium']=fuzz.trimf(cgpa.universe,[4,6,8])
cgpa['high']=fuzz.trimf(cgpa.universe,[8,9,10])
mte['average'].view()
ete.view()
cgpa.view()
rule1=ctrl.Rule(mte['poor']|ete['poor']|ca['poor']|attn['poor'],cgpa['low'])
rule2=ctrl.Rule(mte['average']|ca['average']|attn['average'],cgpa['medium'])
rule3=ctrl.Rule(mte['good']|ete['good']|ca['good']|attn['good'],cgpa['high'])
rule1.view()
rule2.view()
tipping_ctrl=ctrl.ControlSystem([rule1,rule2,rule3])
tipping=ctrl.ControlSystemSimulation(tipping_ctrl)
#Pass inputs to the control system using antecedent labels with pythonic api
#note: if you like passsing many inputs all at once ,use .inputs (dict_of_data)
tipping.input['mte']=100
tipping.input['ete']=100
#Crunch the numbers
tipping.compute()
print(tipping.output['cgpa'])
cgpa.view(sim=tipping)
