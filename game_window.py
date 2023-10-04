# -*- coding: utf-8 -*-
import json
import sys

import compute_center_2048game as cp
import pygame


class Main(object):
    def __init__(self, x_len, y_len, new_type: bool = True):
        with open("./file/pic_data.json", "r", encoding='utf-8') as fr:
            self.json_file = json.load(fr)
        if new_type:
            data_l = []
            for x_i in range(0, y_len):
                data_ps = []
                for y_i in range(0, x_len):
                    data_ps.append(0)
                data_l.append(data_ps)
            self.cn = cp.Computer(x_len, y_len, data_l)
            self.cn.born()
            self.cn.born()
        else:
            reader = cp.File()
            data_l = reader.read()
            self.cn = cp.Computer(x_len, y_len, data_l)
        print(self.cn.block)
        self.width = self.json_file["boundary"] * 2 + self.json_file["block_back"] * x_len
        self.height = self.json_file["boundary"] * 2 + self.json_file["block_back"] * y_len

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Super 2048   write by D BOY")

        img_up = pygame.image.load(self.json_file["up"])
        img_back = pygame.image.load(self.json_file["back"])
        img_bound_block = pygame.image.load(self.json_file["bound_block"])
        img_left = pygame.image.load(self.json_file["left"])
        img_2 = pygame.image.load(self.json_file["2"])
        img_4 = pygame.image.load(self.json_file["4"])
        img_8 = pygame.image.load(self.json_file["8"])
        img_16 = pygame.image.load(self.json_file["16"])
        img_32 = pygame.image.load(self.json_file["32"])
        img_64 = pygame.image.load(self.json_file["64"])
        img_128 = pygame.image.load(self.json_file["128"])
        img_256 = pygame.image.load(self.json_file["256"])
        img_512 = pygame.image.load(self.json_file["512"])
        img_1024 = pygame.image.load(self.json_file["1024"])
        img_2048 = pygame.image.load(self.json_file["2048"])
        img_4096 = pygame.image.load(self.json_file["4096"])
        img_8192 = pygame.image.load(self.json_file["8192"])
        img_16384 = pygame.image.load(self.json_file["16384"])

        clock = pygame.time.Clock()
        clock.tick(16)
        while True:
            # back draw
            # 4R
            self.screen.blit(img_bound_block, pygame.Rect([0, 0, 0, 0]))
            self.screen.blit(img_bound_block, pygame.Rect([
                self.width - self.json_file["boundary"],
                self.height - self.json_file["boundary"], 0, 0]))
            self.screen.blit(img_bound_block, pygame.Rect([
                self.width - self.json_file["boundary"], 0, 0, 0]))
            self.screen.blit(img_bound_block, pygame.Rect([
                0, self.height - self.json_file["boundary"],
                0, 0]))

            # Up & Down
            for k in range(0, x_len):
                self.screen.blit(img_up, pygame.Rect([
                    self.json_file["boundary"] + k * self.json_file["block_back"], 0, 0, 0]))
                self.screen.blit(img_up, pygame.Rect([
                    self.json_file["boundary"] + k * self.json_file["block_back"],
                    self.height - self.json_file["boundary"], 0, 0]))

            for k in range(0, y_len):
                self.screen.blit(img_left, pygame.Rect([
                    0, self.json_file["boundary"] + k * self.json_file["block_back"], 0, 0]))
                self.screen.blit(img_left, pygame.Rect([
                    self.width - self.json_file["boundary"],
                    self.json_file["boundary"] + k * self.json_file["block_back"], 0, 0]))
            for p in range(0, x_len):
                for q in range(0, y_len):
                    self.screen.blit(
                        img_back,
                        pygame.Rect([
                            self.json_file["boundary"] + self.json_file["block_back"] * p,
                            self.json_file["boundary"] + self.json_file["block_back"] * q,
                            0,
                            0
                        ])
                    )

            # block draw
            block_img = {
                2: img_2,
                4: img_4,
                8: img_8,
                16: img_16,
                32: img_32,
                64: img_64,
                128: img_128,
                256: img_256,
                512: img_512,
                1024: img_1024,
                2048: img_2048,
                4096: img_4096,
                8192: img_8192,
                16384: img_16384
            }
            block_rect = []
            for y in range(0, y_len):
                for x in range(0, x_len):
                    if self.cn.block[y][x] != 0:
                        block_rect.append([
                            self.cn.block[y][x],
                            pygame.Rect([self.json_file["boundary"] +
                                         0.5 * (self.json_file["block_back"] - self.json_file["block"]) +
                                         self.json_file["block_back"] * x,
                                         self.json_file["boundary"] +
                                         0.5 * (self.json_file["block_back"] - self.json_file["block"]) +
                                         self.json_file["block_back"] * y,
                                         0, 0])])
            for k in block_rect:
                self.screen.blit(block_img[k[0]], k[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.cn.move_sum_x(False)
                        self.cn.born()
                    elif event.key == pygame.K_RIGHT:
                        self.cn.move_sum_x(True)
                        self.cn.born()
                    elif event.key == pygame.K_UP:
                        self.cn.move_sum_y(False)
                        self.cn.born()
                    elif event.key == pygame.K_DOWN:
                        self.cn.move_sum_y(True)
                        self.cn.born()

            pygame.display.update()


if __name__ == '__main__':
    app = Main(5, 4, True)
