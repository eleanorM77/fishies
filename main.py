import pygame
from pygame.locals import*

pygame.init()

screen_info = pygame.display.Info()

width = int(screen_info.current_w)
height = int(screen_info.current_h)
size = (width, height)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (0, 127, 255)


def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    pygame.display.flip()

if __name__ == "__main__":
  main()