import random

from sources.common.Game import Game
from sources.common.Object import Object
from sources.common.Text import Text
from sources.eat.Coin.Coin import Coin
from sources.eat.Coin.CoinType import CoinType
from sources.game_set import *
from sources.trap.DoubleJumpObstacle1 import DoubleJumpObstacle1
from sources.trap.DoubleJumpObstacle2 import DoubleJumpObstacle2
from sources.trap.SingleJumpObstacle1 import SingleJumpObstacle1
from sources.trap.SingleJumpObstacle2 import SingleJumpObstacle2
from sources.trap.SlideObstacle1 import SlideObstacle1
from sources.trap.SlideObstacle2 import SlideObstacle2


class Main:
    game: Game
    time_after_create_object: int = 23
    can_create_obstacle_level: int = 0
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
        self.game.background.screen.blit(object.image, (object.x_pos, object.y_pos))

    def create_object(self):
        object_num = int(random.randrange(0, 10))
        if object_num == 0:
            coin = Coin(CoinType.GOLD, 0)
            self.objects.append(coin)
            self.object_init_blit(coin)
            self.can_create_obstacle_level = 0

        elif object_num == 1:
            coin = Coin(CoinType.SILVER, 0)
            self.objects.append(coin)
            self.object_init_blit(coin)
            self.can_create_obstacle_level = 0

        elif object_num == 2:
            coin = Coin(CoinType.BRONZE, 0)
            self.objects.append(coin)
            self.object_init_blit(coin)
            self.can_create_obstacle_level = 0

        elif object_num == 3:
            self.game.show_bonus_coin(self.objects)
            self.can_create_obstacle_level = 0

        elif object_num in (4, 5, 6, 7, 8, 9):
            self.add_obstacle(object_num)

    def add_obstacle(self, object_num: int):
        if self.can_create_obstacle_level == 3:
            coin = Coin(CoinType.BRONZE, 0)
            self.objects.append(coin)
            self.object_init_blit(coin)

        if object_num == 4 and self.can_create_obstacle_level < 2:
            obstacle = SingleJumpObstacle1()
            self.objects.append(obstacle)
            self.object_init_blit(obstacle)

            coin = Coin.create_coin_with_y_pos(obstacle.y_pos - 80)
            self.objects.append(coin)
            self.object_init_blit(coin)

            self.can_create_obstacle_level += 1

        elif object_num == 5 and self.can_create_obstacle_level < 2:
            obstacle = SingleJumpObstacle2()
            self.objects.append(obstacle)
            self.object_init_blit(obstacle)

            coin = Coin.create_coin_with_y_pos(obstacle.y_pos - 80)
            self.objects.append(coin)
            self.object_init_blit(coin)

            self.can_create_obstacle_level += 1

        elif object_num == 6 and self.can_create_obstacle_level < 2:
            obstacle = DoubleJumpObstacle1()
            self.objects.append(obstacle)
            self.object_init_blit(obstacle)

            coin = Coin.create_coin_with_y_pos(obstacle.y_pos - 80)
            self.objects.append(coin)
            self.object_init_blit(coin)

            self.can_create_obstacle_level = 3

        elif object_num == 7 and self.can_create_obstacle_level < 2:
            obstacle = DoubleJumpObstacle2()
            self.objects.append(obstacle)
            self.object_init_blit(obstacle)

            coin = Coin.create_coin_with_y_pos(obstacle.y_pos - 80)
            self.objects.append(coin)
            self.object_init_blit(coin)

            self.can_create_obstacle_level = 3

        elif object_num == 8 and self.can_create_obstacle_level in (0, 4):
            obstacle = SlideObstacle1()
            self.objects.append(obstacle)
            self.object_init_blit(obstacle)

            coin = Coin.create_coin_with_y_pos(obstacle.image.get_height() + 20)
            self.objects.append(coin)
            self.object_init_blit(coin)

            self.can_create_obstacle_level = 4

        elif object_num == 9 and self.can_create_obstacle_level in (0, 4):
            obstacle = SlideObstacle2()
            self.objects.append(obstacle)
            self.object_init_blit(obstacle)

            coin = Coin.create_coin_with_y_pos(obstacle.image.get_height() + 20)
            self.objects.append(coin)
            self.object_init_blit(coin)

            self.can_create_obstacle_level = 4

        else:
            self.create_bronze_coin_if_obstacle_cant_blit()
            self.can_create_obstacle_level = 0

    def create_bronze_coin_if_obstacle_cant_blit(self):
        coin = Coin(CoinType.BRONZE, 0)
        self.objects.append(coin)
        self.object_init_blit(coin)

    def move_object(self):
        for index, object in enumerate(self.objects):
            object.position_update_character_run(object.x_pos - speed)
            self.game.background.screen.blit(object.image, (object.x_pos, object.y_pos))

            if object.x_pos < -object.image.get_width():
                self.objects.pop(index)

    def screen_update(self):
        self.game.background.screen.blit(self.game.background.image, (0, 0))
        self.game.background.floor_update()

        self.game.update_character()

        if self.time_after_create_object >= 22:
            self.create_object()
            self.time_after_create_object = 0
        else:
            self.time_after_create_object += 1

        self.status = self.game.process_collision(self.objects)
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
            self.status = self.game.character.is_life_remain()
            self.screen_update()

            for event in (pygame.event.get()):
                if event.type == pygame.QUIT:
                    self.game_stop()
                else:
                    self.game.character.character_operation(event)

            if not self.is_run():
                self.quit()

        self.quit()


if __name__ == "__main__":
    Main().main()
