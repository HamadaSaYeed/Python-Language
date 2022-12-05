class Date:

    def get_date(self):
        print('2022-11-22')

class Time(Date):

    def get_time(self):
        print('07 : 36 : 09')



d = Date()
d.get_date()

print('')

t = Time()
t.get_time()
t.get_date()