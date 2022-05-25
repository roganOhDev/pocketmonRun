import pygame.image

from sources.game_set import screen_height, floor_height
from sources.images import ObstacleImage
from sources.trap.Trap import Trap


class DoubleJumpObstacle2(Trap):
    def __init__(self):
        image = pygame.image.load(ObstacleImage.double_jump_obstacle_2).convert_alpha()
        image = pygame.transform.rotozoom(image, 0, 0.7)
        image = pygame.transform.smoothscale(image, (image.get_width() * 0.8, image.get_height()))
        y_pos = screen_height - floor_height - image.get_height() + 5

        super().__init__(image, y_pos)
