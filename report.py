class Report:
    def __init__(self):
        self.num_open = 0
        self.num_win = 0
        self.num_lose = 0

        self.long_position_gain_point = 0
        self.short_position_gain_point = 0

        self.total_gain_point_each_round = 0

    def get_num_open(self):
        return self.num_open

    def get_num_win(self):
        return self.num_win

    def get_num_lose(self):
        return self.num_lose

    def increase_num_open(self):
        self.num_open += 1

    def increse_num_win(self):
        self.num_win += 1

    def increase_num_lose(self):
        self.num_lose += 1

    def set_long_position_gain_point(self, gain_point):
        self.long_position_gain_point = gain_point

    def set_short_position_gain_point(self, gain_point):
        self.short_position_gain_point = gain_point

    def get_long_position_gain_point(self):
        return self.long_position_gain_point

    def get_short_position_gain_point(self):
        return self.short_position_gain_point

    def set_total_gain_point_each_round(self, gain_point):
        self.total_gain_point_each_round = gain_point

    def get_total_gain_point_each_round(self):
        return self.total_gain_point_each_round
    
    def increase_total_gain_point_each_round(self, gain_point):
        self.total_gain_point_each_round += gain_point