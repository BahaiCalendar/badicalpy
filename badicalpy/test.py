import BadiCal

date = BadiCal.GregorianToBadi(2015, 3, 21);
print(date.year(), date.month(), date.day());

date = BadiCal.GregorianToBadi(2015, 3, 21, True);
print(date.year(), date.month(), date.day());

date = BadiCal.BadiToGregorian(172, 1, 1);
print(date.year(), date.month(), date.day());

date = BadiCal.BadiToGregorian(172, 1, 1, True);
print(date.year(), date.month(), date.day());