def WeekdayUP(factor):
    dayup=1.0
    for i in range(365):
        if i%30 in [0,1,2,3,4,5,6,7,8,9]:
            dayup=dayup
        else:
            dayup=dayup*(1+factor)
    return dayup
for i in range(1,11,1):
    print("DayUP{:.3f}".format(WeekdayUP(0.001*i)))
