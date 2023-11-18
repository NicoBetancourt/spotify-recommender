
import datetime

class DateFormat():
    @classmethod
    def convert_data(self,date):
        print(date)
        return datetime.datetime.strftime(date,"%d/%m/%Y")
