import numpy as np
import pygame
from pygame import K_c, K_x
from model.test import predict

from viewer import Viewer


def cursor_pos():
    mx, my = pygame.mouse.get_pos()
    return int(mx / 20), int(my / 20)


def clear_array():
    return np.zeros((28, 28))


array = np.zeros((28, 28))


def update():
    click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if click[0]:
        array[cursor_pos()] = 255
    if keys[K_x]:
        predict(array)
    if keys[K_c]:
        array.fill(0)

    return array.astype("uint8")


pygame.init()
viewer = Viewer(update, (560, 560))
viewer.set_title("Draw")
viewer.start()
