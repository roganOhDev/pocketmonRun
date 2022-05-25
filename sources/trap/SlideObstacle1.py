import pygame.image

from sources.game_set import screen_height, floor_height
from sources.images import ObstacleImage
from sources.trap.Trap import Trap


class SlideObstacle1(Trap):
    def __init__(self):
        image = pygame.image.load(ObstacleImage.slide_obstacle_1).convert_alpha()
        image = pygame.transform.rotozoom(image, 0, 0.7)
        image = pygame.transform.smoothscale(image, (image.get_width(), 300))
        y_pos = 0

        super().__init__(image, y_pos)
