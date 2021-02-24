# coding:utf-8
from Chess_Core import Chessman


class Chessboard(object):

    def __init__(self, name):
        self.__name = name
        self.__is_red_turn = True
        self.__chessmans = [([None] * 7) for i in range(7)]
        self.__chessmans_hash = {}
        self.__history = {"red": {"chessman": None, "last_pos": None, "repeat": 0},
                          "black": {"chessman": None, "last_pos": None, "repeat": 0}}

    @property
    def is_red_turn(self):
        return self.__is_red_turn

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def chessmans(self):
        return self.__chessmans

    @property
    def chessmans_hash(self):
        return self.__chessmans_hash

    def init_board(self):
        red_cannon_1 = Chessman.Cannon(" 炮1红 ", "red_cannon_1", True, self)
        red_cannon_1.add_to_board(1, 0)
        red_pawn_2 = Chessman.Cannon(" 炮2红 ", "red_cannon_2", True, self)
        red_pawn_2.add_to_board(3, 0)
        black_cannon_1 = Chessman.Cannon(" 炮1黑 ", "black_cannon_1", False, self)
        black_cannon_1.add_to_board(0, 4)
        black_cannon_2 = Chessman.Cannon(" 炮2黑 ", "black_cannon_2", False, self)
        black_cannon_2.add_to_board(1, 4)
        black_cannon_3 = Chessman.Cannon(" 炮3黑 ", "black_cannon_3", False, self)
        black_cannon_3.add_to_board(2, 4)
        black_cannon_4 = Chessman.Cannon(" 炮4黑 ", "black_cannon_4", False, self)
        black_cannon_4.add_to_board(3, 4)
        black_cannon_5 = Chessman.Cannon(" 炮5黑 ", "black_cannon_5", False, self)
        black_cannon_5.add_to_board(4, 4)
        black_cannon_6 = Chessman.Cannon(" 炮6黑 ", "black_cannon_6", False, self)
        black_cannon_6.add_to_board(0, 3)
        black_cannon_7 = Chessman.Cannon(" 炮7黑 ", "black_cannon_7", False, self)
        black_cannon_7.add_to_board(1, 3)
        black_cannon_8 = Chessman.Cannon(" 炮8黑 ", "black_cannon_8", False, self)
        black_cannon_8.add_to_board(2, 3)
        black_cannon_9 = Chessman.Cannon(" 炮9黑 ", "black_cannon_9", False, self)
        black_cannon_9.add_to_board(3, 3)
        black_cannon_10 = Chessman.Cannon(" 炮10黑 ", "black_cannon_10", False, self)
        black_cannon_10.add_to_board(4, 3)

    def add_chessman(self, chessman, col_num, row_num):
        self.chessmans[col_num][row_num] = chessman
        if chessman.name not in self.__chessmans_hash:
            self.__chessmans_hash[chessman.name] = chessman

    def remove_chessman_target(self, col_num, row_num):
        chessman_old = self.get_chessman(col_num, row_num)
        if chessman_old != None:
            self.__chessmans_hash.pop(chessman_old.name)

    def remove_chessman_source(self, col_num, row_num):
        self.chessmans[col_num][row_num] = None

    def calc_chessmans_moving_list(self):
        for chessman in self.__chessmans_hash.values():
            if chessman.is_red == self.__is_red_turn:
                chessman.calc_moving_list()

    def clear_chessmans_moving_list(self):
        for chessman in self.__chessmans_hash.values():
            chessman.clear_moving_list()

    def move_chessman(self, chessman, col_num, row_num):
        if chessman.is_red == self.__is_red_turn:
            # self.remove_chessman_source(chessman.col_num, chessman.row_num)
            self.remove_chessman_target(col_num, row_num)
            self.add_chessman(chessman, col_num, row_num)
            self.__is_red_turn = not self.__is_red_turn
            return True
        else:
            print("the wrong turn")
            return False

    def update_history(self, chessman, col_num, row_num):
        red_or_black = self.red_or_black(chessman)
        history_chessman = self.__history[red_or_black]["chessman"]
        history_pos = self.__history[red_or_black]["last_pos"]
        if history_chessman == chessman and history_pos != None and history_pos[0] == col_num and history_pos[1] == row_num:
            self.__history[red_or_black]["repeat"] += 1
        else:
            self.__history[red_or_black]["repeat"] = 0
        self.__history[red_or_black]["chessman"] = chessman
        self.__history[red_or_black]["last_pos"] = (
            chessman.col_num, chessman.row_num)

    def red_or_black(self, chessman):
        if chessman.is_red:
            return "red"
        else:
            return "black"

    def is_end(self):
        return self.who_is_victor(60)

    def who_is_victor(self, repeat_num):
        whos_turn = "red" if self.__is_red_turn else "black"
        other_turn = "red" if not self.__is_red_turn else "black"
        chessman = self.get_chessman_by_name("{0}_cannon_1".format(other_turn))
        if chessman != None:
            if self.__history[other_turn]["repeat"] == repeat_num:
                print("{0} is victor".format(whos_turn))
                return True
            else:
                return False
        else:
            print("{0} is victor".format(other_turn))
            return True

    def get_chessman(self, col_num, row_num):
        return self.__chessmans[col_num][row_num]

    def get_chessman_by_name(self, name):
        if name in self.__chessmans_hash:
            return self.__chessmans_hash[name]

    def get_top_first_chessman(self, col_num, row_num):
        current = self.chessmans[col_num][row_num + 1]
        if current != None:
            return current

    def get_bottom_first_chessman(self, col_num, row_num):
        current = self.chessmans[col_num][row_num - 1]
        if current != None:
            return current

    def get_left_first_chessman(self, col_num, row_num):
        current = self.chessmans[col_num - 1][row_num]
        if current != None:
            return current

    def get_right_first_chessman(self, col_num, row_num):
        current = self.chessmans[col_num + 1][row_num]
        if current != None:
            return current

    def get_top_second_chessman(self, col_num, row_num):
        current = self.chessmans[col_num][row_num + 1]
        tcurrent = self.chessmans[col_num][row_num + 2]
        if current == None and tcurrent != None:
            return tcurrent

    def get_bottom_second_chessman(self, col_num, row_num):
        current = self.chessmans[col_num][row_num - 1]
        tcurrent = self.chessmans[col_num][row_num - 2]
        if current == None and tcurrent != None:
            return tcurrent

    def get_left_second_chessman(self, col_num, row_num):
        current = self.chessmans[col_num - 1][row_num]
        tcurrent = self.chessmans[col_num - 2][row_num]
        if current == None and tcurrent != None:
            return tcurrent

    def get_right_second_chessman(self, col_num, row_num):
        current = self.chessmans[col_num + 1][row_num]
        tcurrent = self.chessmans[col_num + 2][row_num]
        if current == None and tcurrent != None:
            return tcurrent

    def print_to_cl(self):
        screen = "\r\n"
        for i in range(5, -1, -1):
            for j in range(4):
                if self.__chessmans[j][i] != None:
                    screen += self.__chessmans[j][i].name_cn
                else:
                    screen += "   .   "
            screen += "\r\n" * 3
        print(screen)
