import logging
from position_type import PositionType

class Position:
    def __init__(self, position_type):
        self.number = 0
        self.average_point = 0
        self.position_type = position_type

    def set_average_point(self, point: float):
        self.average_point = point

    def set_number(self, number):
        self.number = number

    def get_average_point(self):
        return self.average_point

    def get_number(self):
        return self.number

    def increase_number(self):
        self.number += 1

    def decrease_number(self):
        self.number -= 1

    def get_position_type(self):
        return self.position_type

    def open_position(self, cur_point):
        total_point = self.cal_total_point()
        self.increase_number()
        self.set_average_point((total_point + cur_point) / self.number)
        
        if self.get_position_type() == PositionType.LONG:
            logging.debug("多單進場: 口數 {number}, 平均成本 {average_point}".format(number=self.get_number(), 
                average_point=self.get_average_point()))
        else:
            logging.debug("空單進場: 口數 {number}, 平均成本 {average_point}".format(number=self.get_number(),
                average_point=self.get_average_point()))

    def cal_total_point(self):
        return self.average_point * self.number

    def close_position(self, cur_point):
        gain_point = self.cal_gain_point(cur_point)
        self.decrease_number()

        if self.get_number() == 0:
            self.set_average_point(0)

        if self.get_position_type() == PositionType.LONG:
            logging.debug("多單出場: 指數獲利 {gain_point}".format(gain_point=gain_point))
        else:
            logging.debug("空單出場: 指數獲利 {gain_point}".format(gain_point=gain_point))

        return gain_point

    def cal_gain_point(self, cur_points):
        if self.get_position_type() == PositionType.LONG:
            return cur_points - self.average_point
        else:
            return self.average_point - cur_points