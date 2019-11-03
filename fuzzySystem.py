import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#import calculate_marks as cm


def fuzzy_logics():
    #mte=ctrl.Antecedent(np.arange(0,21,1),'mte')
    #ete=ctrl.Antecedent(np.arange(0,51,1),'ete')
    #attn=ctrl.Antecedent(np.arange(0,6,1),'attn')
    #ca=ctrl.Antecedent(np.arange(0,26,1),'ca')
    #cgpa=ctrl.Consequent(np.arange(0,11,1),'cgpa')

    finalExam=ctrl.Antecedent(np.arange(0,101,1),'finals')
    halfTerm=ctrl.Antecedent(np.arange(0,51,1),'half')
    attendance=ctrl.Antecedent(np.arange(0,101,1),'attendance')
    classTest=ctrl.Antecedent(np.arange(0,31,1),'classTest')
    cgpa=ctrl.Consequent(np.arange(0,10.1,0.1),'cgpa')


    finalExam['l']=fuzz.gaussmf(finalExam.universe, 30, 15)
    finalExam['m']=fuzz.gaussmf(finalExam.universe, 55, 15)
    finalExam['h']=fuzz.gaussmf(finalExam.universe,80, 15)

    halfTerm['l']=fuzz.gaussmf(halfTerm.universe,  15, 8)
    halfTerm['m']=fuzz.gaussmf(halfTerm.universe, 27, 8)
    halfTerm['h']=fuzz.gaussmf(halfTerm.universe,40, 8)

    attendance['l']=fuzz.gaussmf(attendance.universe,30, 15)
    attendance['m']=fuzz.gaussmf(attendance.universe,55, 15)
    attendance['h']=fuzz.gaussmf(attendance.universe,80, 15)

    classTest['l']=fuzz.gaussmf(classTest.universe, 8,6)
    classTest['m']=fuzz.gaussmf(classTest.universe, 18,6)
    classTest['h']=fuzz.gaussmf(classTest.universe, 25, 6)
    
    cgpa['l']=fuzz.gaussmf(cgpa.universe,2.0,1.0)
    cgpa['m']=fuzz.gaussmf(cgpa.universe,5.0,1.0)
    cgpa['h']=fuzz.gaussmf(cgpa.universe,8.0,1.0)



    #mte['l']=fuzz.trimf(mte.universe, [0,5,8])
    #mte['m']=fuzz.trimf(mte.universe,[7,11,14])
    #mte['h']=fuzz.trimf(mte.universe,[13,17,20])

    #ca['l']=fuzz.trimf(ca.universe, [0,5,10])
    #ca['m']=fuzz.trimf(ca.universe,[9,15,18])
    #ca['h']=fuzz.trimf(ca.universe,[17,22,25])

    #ete['l']=fuzz.trimf(ete.universe,[0,9,18])
    #ete['m']=fuzz.trimf(ete.universe,[15,27,38])
    #ete['h']=fuzz.trimf(ete.universe,[35,45,50])

    #attn['l']=fuzz.trimf(attn.universe, [0,1,2])
    #attn['m']=fuzz.trimf(attn.universe, [2,3,4])
    #attn['h']=fuzz.trimf(attn.universe, [3,4,5])
    
    #cgpa['l']=fuzz.trimf(cgpa.universe,[0,3,5])
    #cgpa['m']=fuzz.trimf(cgpa.universe,[4,6,8])
    #cgpa['h']=fuzz.trimf(cgpa.universe,[7,9,10])
    
    #finalExam['m'].view()
    #halfTerm.view()
    #attendance.view()
    #classTest.view()
    #cgpa.view()
    
    rule1 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['l'] | classTest['l'] , cgpa['l'])
    rule2 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['l'] | classTest['m'] , cgpa['l'])
    rule3 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['l'] | classTest['h'] , cgpa['m'])
    rule4 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['m'] | classTest['l'] , cgpa['l'])
    rule5 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['m'] | classTest['m'] , cgpa['l'])
    rule6 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['m'] | classTest['h'] , cgpa['m'])
    rule7 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['h'] | classTest['l'] , cgpa['l'])
    rule8 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['h'] | classTest['m'] , cgpa['l'])
    rule9 = ctrl.Rule(finalExam['l'] | halfTerm['l'] | attendance['h'] | classTest['h'] , cgpa['m'])
    rule10= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['l'] | classTest['l'] , cgpa['l'])
    rule11= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['l'] | classTest['m'] , cgpa['l'])
    rule12= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['l'] | classTest['h'] , cgpa['m'])
    rule13= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['m'] | classTest['l'] , cgpa['l'])
    rule14= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['m'] | classTest['m'] , cgpa['l'])
    rule15= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['m'] | classTest['h'] , cgpa['m'])
    rule16= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['h'] | classTest['l'] , cgpa['l'])
    rule17= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['h'] | classTest['m'] , cgpa['l'])
    rule18= ctrl.Rule(finalExam['l'] | halfTerm['m'] | attendance['h'] | classTest['h'] , cgpa['m'])
    rule19= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['l'] | classTest['l'] , cgpa['l'])
    rule20= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['l'] | classTest['m'] , cgpa['l'])
    rule21= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['l'] | classTest['h'] , cgpa['m'])
    rule22= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['m'] | classTest['l'] , cgpa['l'])
    rule23= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['m'] | classTest['m'] , cgpa['m'])
    rule24= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['m'] | classTest['h'] , cgpa['m'])
    rule25= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['h'] | classTest['l'] , cgpa['l'])
    rule26= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['h'] | classTest['m'] , cgpa['m'])
    rule27= ctrl.Rule(finalExam['l'] | halfTerm['h'] | attendance['h'] | classTest['h'] , cgpa['m'])
    rule28= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['l'] | classTest['l'] , cgpa['l'])
    rule29= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['l'] | classTest['m'] , cgpa['m'])
    rule30= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['l'] | classTest['h'] , cgpa['m'])
    rule31= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['m'] | classTest['l'] , cgpa['l'])
    rule32= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['m'] | classTest['m'] , cgpa['m'])
    rule33= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['m'] | classTest['h'] , cgpa['m'])
    rule34= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['h'] | classTest['l'] , cgpa['l'])
    rule35= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['h'] | classTest['m'] , cgpa['m'])
    rule36= ctrl.Rule(finalExam['m'] | halfTerm['l'] | attendance['h'] | classTest['h'] , cgpa['m'])
    rule37= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['l'] | classTest['l'] , cgpa['m'])
    rule38= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['l'] | classTest['m'] , cgpa['m'])
    rule39= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['l'] | classTest['h'] , cgpa['m'])
    rule40= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['m'] | classTest['l'] , cgpa['m'])
    rule41= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['m'] | classTest['m'] , cgpa['m'])
    rule42= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['m'] | classTest['h'] , cgpa['m'])
    rule43= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['h'] | classTest['l'] , cgpa['m'])
    rule44= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['h'] | classTest['m'] , cgpa['m'])
    rule45= ctrl.Rule(finalExam['m'] | halfTerm['m'] | attendance['h'] | classTest['h'] , cgpa['m'])
    rule46= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['l'] | classTest['l'] , cgpa['m'])
    rule47= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['l'] | classTest['m'] , cgpa['m'])
    rule48= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['l'] | classTest['h'] , cgpa['h'])
    rule49= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['m'] | classTest['l'] , cgpa['m'])
    rule50= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['m'] | classTest['m'] , cgpa['m'])
    rule51= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['m'] | classTest['h'] , cgpa['h'])
    rule52= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['h'] | classTest['l'] , cgpa['m'])
    rule53= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['h'] | classTest['m'] , cgpa['m'])
    rule54= ctrl.Rule(finalExam['m'] | halfTerm['h'] | attendance['h'] | classTest['h'] , cgpa['h'])
    rule55= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['l'] | classTest['l'] , cgpa['m'])
    rule56= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['l'] | classTest['m'] , cgpa['m'])
    rule57= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['l'] | classTest['h'] , cgpa['h'])
    rule58= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['m'] | classTest['l'] , cgpa['m'])
    rule59= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['m'] | classTest['m'] , cgpa['m'])
    rule60= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['m'] | classTest['h'] , cgpa['h'])
    rule61= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['h'] | classTest['l'] , cgpa['m'])
    rule62= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['h'] | classTest['m'] , cgpa['m'])
    rule63= ctrl.Rule(finalExam['h'] | halfTerm['l'] | attendance['h'] | classTest['h'] , cgpa['m'])
    rule64= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['l'] | classTest['l'] , cgpa['h'])
    rule65= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['l'] | classTest['m'] , cgpa['m'])
    rule66= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['l'] | classTest['h'] , cgpa['h'])
    rule67= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['m'] | classTest['l'] , cgpa['m'])
    rule68= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['m'] | classTest['m'] , cgpa['m'])
    rule69= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['m'] | classTest['h'] , cgpa['h'])
    rule70= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['h'] | classTest['l'] , cgpa['m'])
    rule71= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['h'] | classTest['m'] , cgpa['m'])
    rule72= ctrl.Rule(finalExam['h'] | halfTerm['m'] | attendance['h'] | classTest['h'] , cgpa['h'])
    rule73= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['l'] | classTest['l'] , cgpa['h'])
    rule74= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['l'] | classTest['m'] , cgpa['h'])
    rule75= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['l'] | classTest['h'] , cgpa['h'])
    rule76= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['m'] | classTest['l'] , cgpa['h'])
    rule77= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['m'] | classTest['m'] , cgpa['h'])
    rule78= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['m'] | classTest['h'] , cgpa['h'])
    rule79= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['h'] | classTest['l'] , cgpa['h'])
    rule80= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['h'] | classTest['m'] , cgpa['h'])
    rule81= ctrl.Rule(finalExam['h'] | halfTerm['h'] | attendance['h'] | classTest['h'] , cgpa['h'])

    tipping_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,
                                    rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,
                                    rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,
                                    rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,
                                    rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,
                                    rule51,rule52,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60,
                                    rule61,rule62,rule63,rule64,rule65,rule66,rule67,rule68,rule69,rule70,
                                    rule71,rule72,rule73,rule74,rule75,rule76,rule77,rule78,rule79,rule80,rule81])

    tipping=ctrl.ControlSystemSimulation(tipping_ctrl)
    
    tipping.input['mte']= mtey
    tipping.input['ete']= etey
    tipping.input['ca']= cay
    tipping.input['attn']= attny

    tipping.compute()
    print(tipping.output['cgpa'])
    cgpa.view(sim=tipping)
