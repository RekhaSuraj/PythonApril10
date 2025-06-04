from abc import ABC, abstractmethod

class School(ABC):

    @abstractmethod
    def login_Time(self):
        pass

    @abstractmethod
    def logout_time(self):
        pass

# ob1 = School()
# ob1.login_Time()

# TypeError: Can't instantiate abstract class School without an implementation for abstract methods 'login_Time', 'logout_time'


class DPS(School):

    def login_Time(self):
        print('School start time is 8AM')


    def logout_time(self):
        print('School end time is 4PM')


obj_DPS = DPS()
obj_DPS.login_Time()
obj_DPS.logout_time()

# School start time is 8AM
# School end time is 4PM