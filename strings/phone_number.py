import re

class PhoneNumber:
    def __init__(self, number):
        number = re.sub("^1", '', re.sub("\\D", '', number))
        if ((len(number) == 10) & (re.match('[2-9].{2}[2-9]', number) is not None)):
            self.number = number
            self.area_code = number[:3]
        else:
            raise ValueError('Input cannot be interpreted as a valid phone number.')
            
    def pretty(self):
        return ('(' + self.area_code + ') ' + self.number[3:6] + '-' + self.number[6:])
