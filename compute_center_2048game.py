# -*- coding: utf-8 -*-
import json
import random
"""
change rules
1, 2, 3,
4, 5, 6,  自左上角开始读取
7, 8, 9.



"""


def synthesis(self: list, direction: bool = True):
    """
    :param self: 提供的源数据
    :param direction: 合成方向
    :return: 一个一个合成的啊
    """
    copy_list = self
    if direction:
        player = self[::-1]
        for i in range(0, len(copy_list) - 1):
            if player[i] == player[i + 1]:
                player[i] *= 2
                player[i + 1] = 0
        return shark(player[::-1])
    else:
        player = self[::1]
        for i in range(0, len(copy_list) - 1):
            if player[i] == player[i + 1]:
                player[i] *= 2
                player[i + 1] = 0
        return shark(player[::1])


def shark(input_list: list, self=0):
    return_list = []
    if input_list == return_list:
        return []
    else:
        for k in input_list:
            if k != self:
                return_list.append(k)
        return return_list


class Computer(object):
    def __init__(self, x_len, y_len, data):
        with open("./file/pic_data.json", "r", encoding='utf-8') as j_file:
            loader = json.load(j_file)
            self.born_list = loader["born_list"]
            self.born_cycle_times = loader["born_cycle_times"]
        self.x_len = x_len
        self.y_len = y_len
        self.block = data

    def move_sum_x(self, direction: bool):
        # direction: down, right is True
        out_block_data = []
        for reader in self.block:
            list_1 = shark(reader, 0)
            out_body = synthesis(list_1, direction)
            if direction:
                if len(reader) != len(out_body):
                    list_add = []
                    for i in range(0, len(reader) - len(out_body)):
                        list_add.append(0)
                    writer = list_add + out_body
                else:
                    writer = out_body
            else:
                if len(reader) != len(out_body):
                    list_add = []
                    for i in range(0, len(reader) - len(out_body)):
                        list_add.append(0)
                    writer = out_body + list_add
                else:
                    writer = out_body
            out_block_data.append(writer)
        self.block = out_block_data
        return out_block_data

    def move_sum_y(self, direction: bool):
        changer = []
        for x_reader in range(0, self.x_len):
            reader_row = []
            for y_reader in range(0, self.y_len):
                reader_row.append(self.block[y_reader][x_reader])
            changer.append(reader_row)

        # -------------------------------
        out_block_data = []
        for reader in changer:
            list_1 = shark(reader, 0)
            out_body = synthesis(list_1, direction)
            if direction:
                if len(reader) != len(out_body):
                    list_add = []
                    for i in range(0, len(reader) - len(out_body)):
                        list_add.append(0)
                    writer = list_add + out_body
                else:
                    writer = out_body
            else:
                if len(reader) != len(out_body):
                    list_add = []
                    for i in range(0, len(reader) - len(out_body)):
                        list_add.append(0)
                    writer = out_body + list_add
                else:
                    writer = out_body
            out_block_data.append(writer)

        changer = []
        for x_reader in range(0, self.y_len):
            reader_row = []
            for y_reader in range(0, self.x_len):
                reader_row.append(out_block_data[y_reader][x_reader])
            changer.append(reader_row)

        self.block = changer
        return changer

    def born(self):
        coordinate = []
        for y in range(0, len(self.block)):

            for x in range(0, len(self.block[0])):
                if self.block[y][x] == 0:
                    coordinate.append((y, x))
        if not coordinate:
            return False
        else:
            a = 0
            if self.born_cycle_times > len(coordinate):
                while True:
                    a += 1
                    if a == len(self.born_cycle_times):
                        break
                    else:
                        random_coordinate = coordinate[random.randint(0, len(coordinate)-1)]
                        born_type = self.born_list[random.randint(0, len(self.born_list)-1)]
                        self.block[random_coordinate[0]][random_coordinate[1]] = born_type
            else:
                while True:
                    if a == self.born_cycle_times:
                        break
                    else:
                        random_coordinate = coordinate[random.randint(0, len(coordinate)-1)]
                        born_type = self.born_list[random.randint(0, len(self.born_list)-1)]
                        self.block[random_coordinate[0]][random_coordinate[1]] = born_type
                    a += 1

    def empty_num(self):
        pass


class File(object):
    def __init__(self):
        with open("./file/pic_data.json", encoding='utf-8') as j_file:
            self.file_path = json.load(j_file)["record_path"]

    def save(self, data: list):
        file_save = {"data": data}
        with open(self.file_path, "w", encoding='utf-8') as fw:
            json.dump(file_save, fw, indent=4, ensure_ascii=False)

    def read(self):
        with open(self.file_path, "r", encoding='utf-8') as fr:
            return json.load(fr)["data"]


if __name__ == '__main__':
    print(synthesis([3, 2, 2, 2], True))
    Computer = Computer(4, 3, [
        [2, 2, 2, 2],
        [0, 2, 2, 0],
        [0, 2, 2, 2]
    ])
    print("UP", Computer.move_sum_y(False))
    print("LEFT", Computer.move_sum_x(False))
    Computer.born()
    print(Computer.block)
