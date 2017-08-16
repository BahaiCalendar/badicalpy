import constants
from datetime import date

def addZero(n):
	return str(n).zfill(2);
	
class BadiDate:
	def __init__(self, year, month, date, type=None):	
		self.y = year;
		self.m = month;
		self.d = date;
		self.type = type;
	
	def year(self, formatted=False):
		return addZero(self.y) if formatted else self.y;
	
	def month(self, formatted=False):
		return addZero(self.m) if formatted else self.m;
	
	def monthName(self):
		if(self.type == constants.GREGORIAN):
			return constants.MONTHS_GREGORIAN[self.m];
		else:
			return constants.MONTHS_BADI[self.m];
	
	def day(self, formatted=False):
		return addZero(self.d) if formatted else self.d;
	
	def toDate(self):
		return date(self.y, self.m, self.d);