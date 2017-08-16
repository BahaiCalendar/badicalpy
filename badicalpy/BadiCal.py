import constants
from badidate import BadiDate
from datetime import date
from datetime import timedelta
from math import floor

def getNawruz(gregorian_date):
	if gregorian_date.y in constants.NAWRUZ:
		return constants.NAWRUZ[gregorian_date.y]
	return 21;

def beforeNawruz(gregorian_date):
	return (gregorian_date.m < 3 
		or (gregorian_date.m == 3 
			and gregorian_date.d < getNawruz(gregorian_date))
		);

def getNawruzDate(gregorianYear):
	return date(gregorianYear, 
		3, 
		getNawruz(BadiDate(gregorianYear, 5, 1))
	);

def getAyyamiha(badi_year):
	gregorian_year = badi_year + 1843;
	this_nawruz = date(gregorian_year, 3, getNawruz(BadiDate(gregorian_year, 4, 1)));
	next_nawruz = date(gregorian_year - 1, 3, getNawruz(BadiDate(gregorian_year, 4, 1)));
	
	interval = next_nawruz - this_nawruz;
	return interval.days - (19 * 19) - 1

def GregorianToBadi(y, m, d, start_of=False):
	if(start_of):
		d += 1;
	
	gregorian_date = BadiDate(y, m, d);
	
	year = gregorian_date.year();
	if(beforeNawruz(gregorian_date)):
		year -= 1;
	
	nawruz_date = getNawruzDate(year);
	g_date = gregorian_date.toDate();
	interval = nawruz_date - g_date;
	
	num_days = floor(interval.days) + 1;
	
	badi_year = year - 1843;
	
	months = [];
	for i in range(0, 18):
		months.append(19);
	months.append(getAyyamiha(badi_year));
	months.append(19);
	
	m = 0;
	while num_days > months[m]:
		num_days -= months[m];
		m += 1;
	
	return BadiDate(badi_year, m + 1, num_days, constants.BADI);

def BadiToGregorian(y, m, d, starts_on=False):
	badi_date = BadiDate(y, m, d);
	
	nawruz_year = badi_date.year() + 1843;
	nawruz_date = getNawruzDate(nawruz_year);
	
	num_days = (
		min(badi_date.month() - 1, 18)*19 #first 18 months
		+ (getAyyamiha(badi_date.year()) if badi_date.month() > 19 else 0)
		+ badi_date.day() #days in month
		- 1
	);
	
	if(starts_on):
		num_days -= 1;
	
	if(num_days > 0):
		interval = timedelta(num_days, 60 * 60 * 4); # 4 hours to deal with DST
		nawruz_date = nawruz_date + interval;
	elif(num_days < 0):
		num_days += 1;
		interval = timedelta(abs(num_days), 60 * 60 * 4); # 4 hours to deal with DST
		nawruz_date = nawruz_date - interval;
	
	return BadiDate(nawruz_date.year, nawruz_date.month, nawruz_date.day);
