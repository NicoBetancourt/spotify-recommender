
from datetime import datetime

class DateFormat():
    @classmethod
    def convert_data(self,date):
        return datetime.strftime(date,"%d/%m/%Y")
    
    @classmethod
    def str_to_date(self,date):
        return datetime.strptime(date, "%d/%m/%Y")
    
    @classmethod
    def date_to_str(self,date):
        return datetime.strftime(date,"%d/%m/%Y")
