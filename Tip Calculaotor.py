print("Wellcome to the Rip Calculateor")
Bill=float(input("What was the total bill ?"))
Tip=float(input("How much tip would like to give 10,15,16?"))
P=int(input("How many people to sptip bill"))
tip_amount=Bill*Tip/100
total = Bill+tip_amount
each_pay= total/P
print(f'Each personnn shpuld pay ,{each_pay}$')