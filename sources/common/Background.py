from dataclasses import dataclass

import pygame.image
from pygame.mixer import Sound
from pygame.surface import Surface

from sources.common.Floor import Floor
from sources.common.Object import Object
from sources.common.Text import Text
from sources.game_set import floor_height, screen_width, screen_height
from sources.images import CharmanderImage, SquirtleImage, BulbasaurImage, BackgroundImage
from sources.musics import BackgroundMusic
from sources.trap.Trap import Trap


@dataclass
class Background:
    screen: Surface
    image: Surface
    bgm: Sound
    floors: [Surface]

    def __init__(self, image_path: str, bgm_path: str):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.image = pygame.image.load(image_path)
        self.bgm = pygame.mixer.Sound(bgm_path)
        self.floors = []

    def show_default_screen(self):
        if self.bgm.play().get_busy():
            self.bgm.stop()

        self.__init__(BackgroundImage.default_background, BackgroundMusic.default)

        self.floors.append(Floor(0))
        self.floors.append(Floor(screen_width))

        self.bgm.play(loops=3000)

    def show_bonus_screen(self, objects: [Object]):
        self.delete_trap_in_bonus_screen(objects)

        if self.bgm.play().get_busy():
            self.bgm.stop()

        self.__init__(BackgroundImage.bonus_stage_background, BackgroundMusic.bonus)

        self.floors.append(Floor(0))
        self.floors.append(Floor(screen_width))

        self.bgm.play(loops=3000)

    @staticmethod
    def delete_trap_in_bonus_screen(objects: [Object]):
        for index, object in enumerate(objects):
            if isinstance(object, Trap):
                objects.pop(index)

    def add_text(self, text: Text):
        msg = text.font.render(text.text, True, text.color)
        msg_rect = msg.get_rect(center=(text.x_pos, text.y_pos))
        self.screen.blit(msg, msg_rect)

    def choose_character_screen(self, screen: Surface) -> None:
        charmander_image = pygame.image.load(CharmanderImage.image_1).convert()
        charmander_image = pygame.transform.scale(charmander_image, (screen.get_width() / 2, screen.get_height() / 2))

        squirtle_image = pygame.image.load(SquirtleImage.image_1).convert()
        squirtle_image = pygame.transform.scale(squirtle_image, (screen.get_width() / 2, screen.get_height() / 2))

        bulbasaur_image = pygame.image.load(BulbasaurImage.image_1).convert()
        bulbasaur_image = pygame.transform.scale(bulbasaur_image, (screen.get_width() / 2, screen.get_height() / 2))

        screen.blit(charmander_image, (0, 0))
        screen.blit(bulbasaur_image, (0, screen.get_height() / 2))
        screen.blit(squirtle_image, (screen.get_width() / 2, screen.get_height() / 2))

        black = pygame.Color("black")

        self.add_text(Text(40, int(self.screen.get_width() * 3 / 4), int(self.screen.get_height() / 4),
                           "Click To Choose Character", (black.r, black.g, black.b)))

        pygame.display.update()

    def floor_update(self) -> None:
        for floor in self.floors:
            floor.move()
            if floor.x_pos < -screen_width:
                self.floors.pop(0)
                self.floors.append(Floor(screen_width))

            self.screen.blit(floor.scaled_image, (floor.x_pos, screen_height - floor_height))
