import sys
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

ca=ctrl.Antecedent(np.arange(0,26,1),'CA')  #total of 25 marks
mte=ctrl.Antecedent(np.arange(0,21,1),'MTE') #total of 20 marks
ete=ctrl.Antecedent(np.arange(0,51,1),'ETE') #total of 50 marks
cgpa=ctrl.Consequent(np.arange(0,101,1),'CGPA')#have taken 100 then convert to 10

#CA 30 marks divided into poor, average, good, excellent.
ca['poor']=fuzzy.trimf(ca.universe,[0,0,9]) 
ca['avg']=fuzzy.trimf(ca.universe,[7,11,15])
ca['good']=fuzzy.trimf(ca.universe,[13,16,19])
ca['excel']=fuzzy.trimf(ca.universe,[17,25,25])

#Mid 20 marks divided into poor, average, good.
mte['poor']=fuzzy.trimf(mte.universe,[0,0,11])
mte['avg']=fuzzy.trimf(mte.universe,[9,13,17])
mte['good']=fuzzy.trimf(mte.universe,[16,20,20])

#Semester 70 marks divided into fail, poor, average,good, excellent.
ete['fail']=fuzzy.trimf(ete.universe,[0,0,27])
ete['poor']=fuzzy.trimf(ete.universe,[25,29,33])
ete['avg']=fuzzy.trimf(ete.universe,[31,36,41])
ete['good']=fuzzy.trimf(ete.universe,[39,43,46])
ete['excel']=fuzzy.trimf(ete.universe,[45,50,50])

#CGPA 100 then convert to 10 in fail, very poor, poor, average, good
#very good ,excellent, outstanding.
cgpa['fail']=fuzzy.trimf(cgpa.universe,[0,0,40])
cgpa['vpoor']=fuzzy.trimf(cgpa.universe,[37,44,50])
cgpa['poor']=fuzzy.trimf(cgpa.universe,[47,54,60])
cgpa['avg']=fuzzy.trimf(cgpa.universe,[57,64,70])
cgpa['good']=fuzzy.trimf(cgpa.universe,[67,74,80])
cgpa['vgood']=fuzzy.trimf(cgpa.universe,[77,84,90])
cgpa['excel']=fuzzy.trimf(cgpa.universe,[87,92,96])
cgpa['outst']=fuzzy.trimf(cgpa.universe,[95,100,100])



#to check marks which are separated by conditions in universe.
#at.view()
#ca.view()
#mte.view()
#ete.view()

	   
#CA       MTE     ETE
#poor     poor    fail
#         avg     poor
#         good    avg
#                 good
#                 excel
rule1=ctrl.Rule(ca['poor'] & mte['poor'] & ete['fail'],cgpa['fail'])
rule2=ctrl.Rule(ca['poor'] & mte['poor'] & ete['poor'],cgpa['vpoor'])
rule3=ctrl.Rule(ca['poor'] & mte['poor'] & ete['avg'],cgpa['vpoor'])
rule4=ctrl.Rule(ca['poor'] & mte['poor'] & ete['good'],cgpa['poor'])
rule5=ctrl.Rule(ca['poor'] & mte['poor'] & ete['excel'],cgpa['avg'])
rule6=ctrl.Rule(ca['poor'] & mte['avg'] & ete['fail'],cgpa['fail'])
rule7=ctrl.Rule(ca['poor'] & mte['avg'] & ete['poor'],cgpa['vpoor'])
rule8=ctrl.Rule(ca['poor'] & mte['avg'] & ete['avg'],cgpa['poor'])
rule9=ctrl.Rule(ca['poor'] & mte['avg'] & ete['good'],cgpa['avg'])
rule10=ctrl.Rule(ca['poor'] & mte['avg'] & ete['excel'],cgpa['avg'])
rule11=ctrl.Rule(ca['poor'] & mte['good'] & ete['fail'],cgpa['fail'])
rule12=ctrl.Rule(ca['poor'] & mte['good'] & ete['poor'],cgpa['vpoor'])
rule13=ctrl.Rule(ca['poor'] & mte['good'] & ete['avg'],cgpa['poor'])
rule14=ctrl.Rule(ca['poor'] & mte['good'] & ete['good'],cgpa['avg'])
rule15=ctrl.Rule(ca['poor'] & mte['good'] & ete['excel'],cgpa['good'])


#CA       MTE     ETE
#avg      poor    fail
#         avg     poor
#         good    avg
#                 good
#                 excel
rule16=ctrl.Rule(ca['avg'] & mte['poor'] & ete['fail'],cgpa['fail'])
rule17=ctrl.Rule(ca['avg'] & mte['poor'] & ete['poor'],cgpa['vpoor'])
rule18=ctrl.Rule(ca['avg'] & mte['poor'] & ete['avg'],cgpa['poor'])
rule19=ctrl.Rule(ca['avg'] & mte['poor'] & ete['good'],cgpa['avg'])
rule20=ctrl.Rule(ca['avg'] & mte['poor'] & ete['excel'],cgpa['good'])
rule21=ctrl.Rule(ca['avg'] & mte['avg'] & ete['fail'],cgpa['fail'])
rule22=ctrl.Rule(ca['avg'] & mte['avg'] & ete['poor'],cgpa['avg'])
rule23=ctrl.Rule(ca['avg'] & mte['avg'] & ete['avg'],cgpa['avg'])
rule24=ctrl.Rule(ca['avg'] & mte['avg'] & ete['good'],cgpa['avg'])
rule25=ctrl.Rule(ca['avg'] & mte['avg'] & ete['excel'],cgpa['good'])
rule26=ctrl.Rule(ca['avg'] & mte['good'] & ete['fail'],cgpa['fail'])
rule27=ctrl.Rule(ca['avg'] & mte['good'] & ete['poor'],cgpa['avg'])
rule28=ctrl.Rule(ca['avg'] & mte['good'] & ete['avg'],cgpa['good'])
rule29=ctrl.Rule(ca['avg'] & mte['good'] & ete['good'],cgpa['good'])
rule30=ctrl.Rule(ca['avg'] & mte['good'] & ete['excel'],cgpa['vgood'])


#CA       MTE     ETE
#good     poor    fail
#         avg     poor
#         good    avg
#                 good
#                 excel
rule31=ctrl.Rule(ca['good'] & mte['poor'] & ete['fail'],cgpa['fail'])
rule32=ctrl.Rule(ca['good'] & mte['poor'] & ete['poor'],cgpa['vpoor'])
rule33=ctrl.Rule(ca['good'] & mte['poor'] & ete['avg'],cgpa['avg'])
rule34=ctrl.Rule(ca['good'] & mte['poor'] & ete['good'],cgpa['good'])
rule35=ctrl.Rule(ca['good'] & mte['poor'] & ete['excel'],cgpa['good'])
rule36=ctrl.Rule(ca['good'] & mte['avg'] & ete['fail'],cgpa['fail'])
rule37=ctrl.Rule(ca['good'] & mte['avg'] & ete['poor'],cgpa['avg'])
rule38=ctrl.Rule(ca['good'] & mte['avg'] & ete['avg'],cgpa['avg'])
rule39=ctrl.Rule(ca['good'] & mte['avg'] & ete['good'],cgpa['good'])
rule40=ctrl.Rule(ca['good'] & mte['avg'] & ete['excel'],cgpa['vgood'])
rule41=ctrl.Rule(ca['good'] & mte['good'] & ete['fail'],cgpa['fail'])
rule42=ctrl.Rule(ca['good'] & mte['good'] & ete['poor'],cgpa['good'])
rule43=ctrl.Rule(ca['good'] & mte['good'] & ete['avg'],cgpa['good'])
rule44=ctrl.Rule(ca['good'] & mte['good'] & ete['good'],cgpa['vgood'])
rule45=ctrl.Rule(ca['good'] & mte['good'] & ete['excel'],cgpa['excel'])

#CA       MTE     ETE
#excel    poor    fail
#         avg     poor
#         good    avg
#                 good
#                 excel
rule46=ctrl.Rule(ca['excel'] & mte['poor'] & ete['fail'],cgpa['fail'])
rule47=ctrl.Rule(ca['excel'] & mte['poor'] & ete['poor'],cgpa['vpoor'])
rule48=ctrl.Rule(ca['excel'] & mte['poor'] & ete['avg'],cgpa['poor'])
rule49=ctrl.Rule(ca['excel'] & mte['poor'] & ete['good'],cgpa['good'])
rule50=ctrl.Rule(ca['excel'] & mte['poor'] & ete['excel'],cgpa['good'])
rule51=ctrl.Rule(ca['excel'] & mte['avg'] & ete['fail'],cgpa['fail'])
rule52=ctrl.Rule(ca['excel'] & mte['avg'] & ete['poor'],cgpa['poor'])
rule53=ctrl.Rule(ca['excel'] & mte['avg'] & ete['avg'],cgpa['good'])
rule54=ctrl.Rule(ca['excel'] & mte['avg'] & ete['good'],cgpa['good'])
rule55=ctrl.Rule(ca['excel'] & mte['avg'] & ete['excel'],cgpa['vgood'])
rule56=ctrl.Rule(ca['excel'] & mte['good'] & ete['fail'],cgpa['fail'])
rule57=ctrl.Rule(ca['excel'] & mte['good'] & ete['poor'],cgpa['avg'])
rule58=ctrl.Rule(ca['excel'] & mte['good'] & ete['avg'],cgpa['vgood'])
rule59=ctrl.Rule(ca['excel'] & mte['good'] & ete['good'],cgpa['excel'])
rule60=ctrl.Rule(ca['excel'] & mte['good'] & ete['excel'],cgpa['outst'])



#passing all the rules to control system.
cgpa_calc=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,
                            rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,
                            rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,
                            rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,
                            rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,
                            rule51,rule52,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60])
tcgpa=ctrl.ControlSystemSimulation(cgpa_calc)


print("*********************Student Grade System using Fuzzy Interface*********************")
name=input('Enter the Your Name:')
num=int(input('\nEnter the Your Registration Number: '))
reg=num
count=0
a=int(reg//100000)
if a==117 or a==116 or a==118 or a==119:
    print("You are in valid years")
    if reg>0:
        while reg>0:
            reg=reg//10
            count=count+1
        print("length of your reg:",count)    
        print("your registratin is:",num)
        if count==8:
            print("you have entered valid registration ID:")
        else:
                print("count not valid",count)  
else:
    print("You have entered wrong ID or More than 8 Digits")
    print("you are not exist")
    sys.exit()

    
ca_marks=[] 
mte_marks=[]
ete_marks=[]
at_per=[]

subjects = int(input("How many subjects:"))

for i in range(1,subjects+1):
        ca_marks.append(int(input("Enter marks of CA for 30:")))
        mte_marks.append(int(input("Enter marks of MID for 40:" )))
        ete_marks.append(int(input("Enter marks of ETE for 70:")))
        at_per.append(int(input("Enter attendance percentage of subject:")))
        print(i,"subject marks completed\n") 


print("CA marks are:",ca_marks)
print("MTE marks are:",mte_marks)
print("ETE marks are:",ete_marks)
print("Attendence marks are:",at_per)
  
 	   	   
tot_sum=0  
for i in range(0 , subjects):
	c=(ca_marks[i]/30)*25 
	m=(mte_marks[i]/40)*20 
	e=(ete_marks[i]/70)*50 
	
	if(at_per[i]>=85):
		att=5
	elif(at_per[i]>=75 and at_per[i]<=84):
		att=3
	else:
		att=1
		
		
	tcgpa.input['CA']=c
	tcgpa.input['MTE']=m  
	tcgpa.input['ETE']=e
	
	
	tcgpa.compute()         #calculate cgpa    
	cgpa.view(sim=tcgpa)     #visualize the graph 
	
	#converting and checking of CGPA to 10 points, grade , performance.
	if(tcgpa.output['CGPA']>=96):
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10 
		print("\nyour CGPA is:",tcgpa.output['CGPA'])   
		print('Your Grade is:O') 
		print("your performancce is:OUTSTANDING\n") 
		  
		
	elif(tcgpa.output['CGPA']>=90):	
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10 
		print("\nyour CGPA is:",tcgpa.output['CGPA'])   
		print('Your Grade is:A+')  
		print("your performancce is:EXCELLENT\n") 
		
		
	elif(tcgpa.output['CGPA']>=82):	 
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10 
		print("\nyour CGPA is:",tcgpa.output['CGPA']) 
		print('Your Grade is:A')  
		print("your performancce is:VERY GOOD\n")    
		
		 
	elif(tcgpa.output['CGPA']>=71):  
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10  
		print("\nyour CGPA is:",tcgpa.output['CGPA']) 
		print('Your Grade is:B+')  
		print("your performancce is:GOOD\n")  
		
		   
	elif(tcgpa.output['CGPA']>=55):  
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10  
		print("\nyour CGPA is:",tcgpa.output['CGPA']) 
		print('Your Grade is:B') 
		print("your performancce is:AVERAGE\n") 
		
		  
	elif(tcgpa.output['CGPA']>=46): 
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10      
		print("\nyour CGPA is:",tcgpa.output['CGPA'])  
		print('Your Grade is:C')     
		print("your performancce is:POOR\n")   
		
		 
	elif(tcgpa.output['CGPA']>=36):            	                   		                
	   tcgpa.output['CGPA']=tcgpa.output['CGPA']/10     
	   print("\nyour CGPA is:",tcgpa.output['CGPA'])  
	   print('Your Grade is:D')     
	   print("your performancce is:VERY POOR\n")  
	  
	else:		
		tcgpa.output['CGPA']=tcgpa.output['CGPA']/10   
		print("\nyour CGPA is:",tcgpa.output['CGPA'])  
		print('Your Grdae Is:F') 
		print("your performancce is:FAIL\n")     
		
		
	
	tot_sum=tcgpa.output['CGPA']+tot_sum

try:
        tot_avg=(tot_sum/subjects)
        print("Average:",tot_avg)
except Exception as e:
        print("its a error check")
        print(e)


    
    
    
    
    
