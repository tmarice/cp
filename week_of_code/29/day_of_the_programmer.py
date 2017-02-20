
y = int(raw_input())

if y > 1918: # gregorian
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0: # leap year
        print "12.09.{0}".format(y)
    else:
        print "13.09.{0}".format(y)
elif y < 1918: # julian
    if y % 4 == 0:
        print "12.09.{0}".format(y)
    else:
        print "13.09.{0}".format(y)
else: # 1918
    print "25.09.{0}".format(y)
