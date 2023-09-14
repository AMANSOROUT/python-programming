units=int(input("Enter the units"))



if units>0 and units<=50:
    bill=units*0.50
    charge=20/100*bill
    print('your bill is',bill + charge)
elif units>50 and units<=150:
    bill=(50*0.5)+((units-50)*0.75)
    charge=20/100*bill
    
    print('your bill is', bill + charge)

elif units>150 and units<=250:
    charge=20/100*bill
    bill=(50*0.5)+(150-50)*.75 + ((units-150)*1.20)
    
    print('your bil is', bill + charge )

elif units>250:
    bill=(50*0.5)+(150-50)*.75 + (250-150)*1.20 + (units-250)*1.50
    charge=20/100*bill
    print('your bil is', bill + charge  )

else:
    print(0)
