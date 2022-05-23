import random

from sources.common.Game import Game
from sources.common.Object import Object
from sources.common.Text import Text
from sources.eat.Coin.Coin import Coin
from sources.eat.Coin.CoinType import CoinType
from sources.game_set import *


class Main:
    game: Game
    time_after_create_object: int = 20
    objects: [Object] = []
    status: bool = True

    def is_run(self) -> bool:
        return self.status

    def game_stop(self):
        self.status = False

    def init_game(self) -> None:
        pygame.init()
        self.game = Game()

    def object_init_blit(self, object: Object):
        self.game.background.screen.blit(object.image, (screen_width - object.image.get_width(), object.y_pos))

    def create_object(self):
        trap_num = int(random.randrange(0, 4))
        if trap_num == 0:
            coin = Coin(CoinType.GOLD)
            self.objects.append(coin)
            self.object_init_blit(coin)

        if trap_num == 1:
            coin = Coin(CoinType.SILVER)
            self.objects.append(coin)
            self.object_init_blit(coin)

        if trap_num == 2:
            coin = Coin(CoinType.BRONZE)
            self.objects.append(coin)
            self.object_init_blit(coin)

        if trap_num == 3:
            self.game.show_bonus_coin(self.objects)

    def move_object(self):
        for object in self.objects:
            object.position_update_character_run(object.x_pos - speed)
            self.game.background.screen.blit(object.image, (object.x_pos, object.y_pos))

    def screen_update(self):
        self.game.background.screen.blit(self.game.background.image, (0, 0))
        floor_image = pygame.image.load(BackgroundImage.floor).convert()
        floor_image = pygame.transform.scale(floor_image, (screen_width, floor_image.get_height()))
        self.game.background.screen.blit(floor_image, (0, screen_height - floor_height))

        self.game.update_character()

        if self.time_after_create_object >= 10:
            self.create_object()
            self.time_after_create_object = 0
        else:
            self.time_after_create_object += 1

        self.game.process_collision(self.objects)
        self.move_object()
        self.game.character.bonus_status.show_current_bonus_collection(self.game.background.screen)
        self.game.show_score()
        self.game.show_life()

        pygame.display.update()

    def quit(self) -> None:
        self.game.background.screen.fill(pygame.Color("black"))
        rendered_text = Text(40, screen_width, screen_height, "Score : {}".format(str(self.game.score)),
                             (255, 255, 0)).render()
        self.game.background.screen.blit(rendered_text, Text.get_pos_to_center(rendered_text))

        pygame.display.update()

        self.game.background.bgm.stop()
        pygame.time.delay(2000)
        pygame.quit()

    def main(self) -> None:
        self.init_game()
        self.game.start_game()

        while self.is_run():
            self.game.time.clock.tick(fps)
            self.screen_update()
            self.status = self.game.character.is_life_remain()

            for event in (pygame.event.get()):
                if event.type == pygame.QUIT:
                    self.game_stop()
                else:
                    self.game.character.character_operation(event)

        # TODO 엔딩화면(점수포함)
        self.quit()


if __name__ == "__main__":
    Main().main()
