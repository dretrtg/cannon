# coding:utf-8

from Chess_Core import Point


def num_between(max_num, min_num, current):
    return current >= min_num and current <= max_num


def creat_points(list_points, list_vs, list_hs):
    for v in list_vs:
        for h in list_hs:
            list_points.append(Point.Point(v, h))


class Chessman(object):
    def __init__(self, name_cn, name, is_red, chessboard):
        self.__name = name
        self.__is_red = is_red
        self.__chessboard = chessboard
        self.__position = Point.Point(None, None)
        self.__moving_list = []
        self.__top = 4
        self.__bottom = 0
        self.__left = 0
        self.__right = 4
        self.__is_alive = True
        self.__name_cn = name_cn

    @property
    def row_num(self):
        return self.__position.y

    @property
    def col_num(self):
        return self.__position.x

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        self.__is_alive = is_alive

    @property
    def chessboard(self):
        return self.__chessboard

    @property
    def is_red(self):
        return self.__is_red


    @property
    def name(self):
        return self.__name

    @property
    def name_cn(self):
        return self.__name_cn

    @property
    def position(self):
        return self.__position

    @property
    def moving_list(self):
        return self.__moving_list

    def clear_moving_list(self):
        self.__moving_list = []

    def add_to_board(self, col_num, row_num):
        if self.border_check(col_num, row_num):
            self.__position.x = col_num
            self.__position.y = row_num
            self.__chessboard.add_chessman(self, col_num, row_num)
        else:
            print("the worng postion")

    def move(self, col_num, row_num):
        if self.in_moving_list(col_num, row_num):
            self.__chessboard.remove_chessman_source(
                self.__position.x, self.__position.y)
            self.__chessboard.update_history(self, col_num, row_num)
            self.__position.x = col_num
            self.__position.y = row_num
            return self.__chessboard.move_chessman(self, col_num, row_num)
        else:
            print("the worng target_position")
            return False

    def in_moving_list(self, col_num, row_num):
        for point in self.__moving_list:
            if point.x == col_num and point.y == row_num:
                return True
        return False

    def calc_moving_list(self):
        pass

    def border_check(self, col_num, row_num):
        return num_between(self.__top, self.__bottom, row_num) and num_between(self.__right, self.__left, col_num)

    def calc_moving_path(self, direction_chessman, direction_vertical_coordinate, current_vertical_coordinate, direction_parallel_coordinate, direction, border_vertical_coordinate, h_or_v, ignore_color=False):
        if direction_chessman != None:
            if direction_chessman.is_red == self.is_red or ignore_color:
                for i in range(direction_vertical_coordinate + direction, current_vertical_coordinate, direction):
                    self.__moving_list.append(
                        Point.Point(i, direction_parallel_coordinate) if h_or_v else Point.Point(direction_parallel_coordinate, i))

            else:
                for i in range(direction_vertical_coordinate, current_vertical_coordinate, direction):
                    self.__moving_list.append(
                        Point.Point(i, direction_parallel_coordinate) if h_or_v else Point.Point(direction_parallel_coordinate, i))
        else:
            for i in range(border_vertical_coordinate, current_vertical_coordinate, direction):
                self.__moving_list.append(
                    Point.Point(i, direction_parallel_coordinate) if h_or_v else Point.Point(direction_parallel_coordinate, i))

class Cannon(Chessman):
    def __init__(self, name_cn, name, is_red, chessboard):
        super(Cannon, self).__init__(name_cn, name, is_red, chessboard)
        self._Chessman__top = 4
        self._Chessman__bottom = 0
        self._Chessman__left = 0
        self._Chessman__right = 4

    def calc_moving_list(self):
        # current_v_c = super(Cannon, self).position.x
        # current_h_c = super(Cannon, self).position.y
        # left = super(Cannon, self).chessboard.get_left_first_chessman(
        #     current_v_c, current_h_c)
        # right = super(Cannon, self).chessboard.get_right_first_chessman(
        #     current_v_c, current_h_c)
        # top = super(Cannon, self).chessboard.get_top_first_chessman(
        #     current_v_c, current_h_c)
        # bottom = super(Cannon, self).chessboard.get_bottom_first_chessman(
        #     current_v_c, current_h_c)
        # tar_left = super(Cannon, self).chessboard.get_left_second_chessman(
        #     current_v_c, current_h_c)
        # tar_right = super(Cannon, self).chessboard.get_right_second_chessman(
        #     current_v_c, current_h_c)
        # tar_top = super(Cannon, self).chessboard.get_top_second_chessman(
        #     current_v_c, current_h_c)
        # tar_bottom = super(Cannon, self).chessboard.get_bottom_second_chessman(
        #     current_v_c, current_h_c)
        #
        # if left != None:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(left.position.x, left.position.y))
        # if right != None:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(right.position.x, right.position.y))
        # if top != None:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(top.position.x, top.position.y))
        # if bottom != None:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(bottom.position.x, bottom.position.y))
        #
        # current_color = super(Cannon, self).is_red
        # if tar_left != None and tar_left.is_red != current_color:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(tar_left.position.x, tar_left.position.y))
        # if tar_right != None and tar_right.is_red != current_color:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(tar_right.position.x, tar_right.position.y))
        # if tar_top != None and tar_top.is_red != current_color:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(tar_top.position.x, tar_top.position.y))
        # if tar_bottom != None and tar_bottom.is_red != current_color:
        #     super(Cannon, self).moving_list.append(
        #         Point.Point(tar_bottom.position.x, tar_bottom.position.y))

        current_v_c = super(Cannon, self).position.x
        current_h_c = super(Cannon, self).position.y
        left = super(Cannon, self).chessboard.get_left_first_chessman(
            current_v_c, current_h_c)
        right = super(Cannon, self).chessboard.get_right_first_chessman(
            current_v_c, current_h_c)
        top = super(Cannon, self).chessboard.get_top_first_chessman(
            current_v_c, current_h_c)
        bottom = super(Cannon, self).chessboard.get_bottom_first_chessman(
            current_v_c, current_h_c)
        tar_left = super(Cannon, self).chessboard.get_left_second_chessman(
            current_v_c, current_h_c)
        tar_right = super(Cannon, self).chessboard.get_right_second_chessman(
            current_v_c, current_h_c)
        tar_top = super(Cannon, self).chessboard.get_top_second_chessman(
            current_v_c, current_h_c)
        tar_bottom = super(Cannon, self).chessboard.get_bottom_second_chessman(
            current_v_c, current_h_c)
        super(Cannon, self).calc_moving_path(left, (left.position.x if left != None else None),
                                             current_v_c, current_h_c, 1, 0, True, True)
        super(Cannon, self).calc_moving_path(right, (right.position.x if right != None else None),
                                             current_v_c, current_h_c, -1, 4, True, True)
        super(Cannon, self).calc_moving_path(top, (top.position.y if top != None else None),
                                             current_h_c, current_v_c, -1, 4, False, True)
        super(Cannon, self).calc_moving_path(bottom, (bottom.position.y if bottom != None else None),
                                             current_h_c, current_v_c, 1, 0, False, True)
        current_color = super(Cannon, self).is_red
        if tar_left != None and tar_left.is_red != current_color:
            super(Cannon, self).moving_list.append(
                Point.Point(tar_left.position.x, tar_left.position.y))
        if tar_right != None and tar_right.is_red != current_color:
            super(Cannon, self).moving_list.append(
                Point.Point(tar_right.position.x, tar_right.position.y))
        if tar_top != None and tar_top.is_red != current_color:
            super(Cannon, self).moving_list.append(
                Point.Point(tar_top.position.x, tar_top.position.y))
        if tar_bottom != None and tar_bottom.is_red != current_color:
            super(Cannon, self).moving_list.append(
                Point.Point(tar_bottom.position.x, tar_bottom.position.y))

