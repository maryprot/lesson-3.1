from pygame.draw import *
import pygame

pygame.init()
# ввод данных
center_1 = (200, 200)  # Координаты центра
radius_1 = 50  # Радиус смайла
radius_e_r = round(radius_1 / 10)  # Радиус правого глаза
radius_e_l = round(radius_1 / 7)  # Радиус левого глаза
radius_e = round(radius_1 / 15)   # Радиус зрачка
width_m = round(radius_1 * 2/5)  # Ширина рта
height_m = round(radius_1 / 10)  # Высота рта
width_b = round(radius_1 * 3/10)  # Ширина брови
height_b = round(radius_1 / 20)  # Высота брови
center_r = (round(center_1[0] - radius_1 / 2), round(center_1[1] - radius_1 / 2))
center_l = (round(center_1[0] + radius_1 / 2), round(center_1[0] - radius_1 / 2))
x11, y11 = round(center_1[0] - radius_1 / 3), round(center_1[0] - radius_1 / 1.5)
x21, y21 = round(center_1[0] - radius_1 / 3 - (width_b * 2**(1/2))), round(center_1[0] - radius_1 / 1.5 - (width_b * 2**(1/2)))
x31, y31 = round(center_1[0] - radius_1 / 3 - (height_b * 2**(1/2))), round(center_1[0] - radius_1 / 1.5 + (height_b * 2**(1/2)))
x41, y41 = round(center_1[0] - radius_1 / 3 - (height_b * 2**(1/2)) - (width_b * 2**(1/2))), round(center_1[0] - radius_1 / 1.5 + (height_b * 2**(1/2)) - (width_b * 2**(1/2)))
x12, y12 = round(center_1[0] + radius_1 / 3), round(center_1[0] - radius_1 / 1.5)
x22, y22 = round(center_1[0] + radius_1 / 3 + (width_b * 2**(1/2))), round(center_1[0] - radius_1 / 1.5 - (width_b * 2**(1/2)))
x32, y32 = round(center_1[0] + radius_1 / 3 + (height_b * 2**(1/2))), round(center_1[0] - radius_1 / 1.5 + (height_b * 2**(1/2)))
x42, y42 = round(center_1[0] + radius_1 / 3 + (height_b * 2**(1/2)) + (width_b * 2**(1/2))), round(center_1[0] - radius_1 / 1.5 + (height_b * 2**(1/2)) - (width_b * 2**(1/2)))
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
circle(screen, yellow, center_1, radius_1)  # Лицо
rect(screen, black, (center_1[0] - width_m/2, round(center_1[1] + radius_1 * 2/5), width_m, height_m))  # Рот
circle(screen, red, center_l, radius_e_l)
circle(screen, red, center_r, radius_e_r)
circle(screen, black, center_l, radius_e)
circle(screen, black, center_r, radius_e)
polygon(screen, black, ((x11, y11), (x31, y31), (x41, y41), (x21, y21)))
polygon(screen, black, ((x12, y12), (x32, y32), (x42, y42), (x22, y22)))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()