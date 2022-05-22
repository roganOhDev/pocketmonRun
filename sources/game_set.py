import pygame

from sources.images import BackgroundImage

screen_width: int = 960
screen_height: int = 450
floor_height: float = pygame.image.load(BackgroundImage.floor).get_height()
fps: int = 50
speed: float = 144 / fps
