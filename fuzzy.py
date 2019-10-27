# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:36:24 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
mte=ctrl.Antecedent(np.arange(0,40,1),'mte')
ete=ctrl.Antecedent(np.arange(0,70,1),'ete')
att=ctrl.Antecedent(np.arange(0,5,1),'att')
grade=ctrl.consequent(np.arange(0,10,1),'grade')
mte['l']=fuzz.trimf(wt.universe, [0,15,20])
mte['m']=fuzz.trimf(wt.universe,[20,25,30])
mte['h']=fuzz.trimf(wt.universe,[30,35,40])
ete['l']=fuzz.trimf(flow.universe,[0,20,35])
ete['m']=fuzz.trimf(flow.universe,[20,35,45])
ete['h']=fuzz.trimf(flow.universe,[45,55,70])
att['l']=fuzz.trimf(wt.universe, [0,1,2])
att['m']=fuzz.trimf(wt.universe, [2,3,4])
att['h']=fuzz.trimf(wt.universe, [3,4,5])
grade['l']=fuzz.trimf(time.universe,[0,2,4])
grade['m']=fuzz.trimf(time.universe,[2,4,6])
grade['h']=fuzz.trimf(time.universe,[6,8,10])
wt.view()
flow.view()
time.view()

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


wm_ctrl=ctrl.ControlSystem(rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,riule10,rule11,rule12,rule13,rule14,rule16)
wm=ctrl.ControlSystemSimulation(wm_ctrl)
wm.input['mte']=30
wm.input['ete']=32
wm.input['att']=3
print(wm.output['grade'])
ime.view(sim=wm)