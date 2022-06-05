import random

from sources.common.Game import Game
from sources.common.Object import Object
from sources.common.Text import Text
from sources.eat.Coin.Coin import Coin
from sources.eat.Coin.CoinType import CoinType
from sources.eat.Item.ItemType import ItemType
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
    game_time: float = 0
    delay_time: float = 0
    game_speed: float = speed

    def is_run(self) -> bool:
        return self.status

    def game_stop(self):
        self.status = False

    def init_game(self) -> None:
        pygame.init()
        self.game = Game(pygame.time.get_ticks() / 1000)

    def object_init_blit(self, object: Object):
        self.game.background.screen.blit(object.image, (object.x_pos, object.y_pos))

    def create_object(self):
        object_num = int(random.randrange(0, 11))
        if not self.game.is_default_stage:
            self.__show_coin_in_bonus_stage()

        elif object_num == 0:
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

        elif object_num == 10:
            self.game.show_item(self.objects)

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

    def __show_coin_in_bonus_stage(self):
        highest_gold_coin_y_pos = random.randrange(0, int(screen_height - floor_height - 100))
        middle_gold_y_coin_pos = random.randrange(highest_gold_coin_y_pos, int(screen_height - floor_height - 100))
        lowest_gold_y_coin_pos = random.randrange(middle_gold_y_coin_pos, int(screen_height - floor_height - 100))

        highest_gold_coin = Coin(CoinType.GOLD, highest_gold_coin_y_pos)
        middle_gold_coin = Coin(CoinType.GOLD, middle_gold_y_coin_pos)
        lowest__gold_coin = Coin(CoinType.GOLD, lowest_gold_y_coin_pos)

        self.objects.append(highest_gold_coin)
        self.objects.append(middle_gold_coin)
        self.objects.append(lowest__gold_coin)

        self.object_init_blit(highest_gold_coin)
        self.object_init_blit(middle_gold_coin)
        self.object_init_blit(lowest__gold_coin)

    def create_bronze_coin_if_obstacle_cant_blit(self):
        coin = Coin(CoinType.BRONZE, 0)
        self.objects.append(coin)
        self.object_init_blit(coin)

    def move_object(self):
        for index, object in enumerate(self.objects):
            object.position_update_character_run(object.x_pos - self.game_speed)
            self.game.background.screen.blit(object.image, (object.x_pos, object.y_pos))

            if object.x_pos < -object.image.get_width():
                self.objects.pop(index)

    def boost_process(self, game_time: float):
        for (index, item_process) in enumerate(self.game.character.item_processors):
            if item_process.item_type == ItemType.BOOST:
                if not item_process.is_active:
                    self.game_speed *= 4
                    self.game.character.start_boost_item(game_time, index)

                elif game_time - item_process.item_start_time >= item_process.item_time:
                    self.game_speed /= 4
                    self.game.character.end_boost_item(index)


    def screen_update(self, game_time: float):
        self.game.background.screen.blit(self.game.background.image, (0, 0))
        self.game.background.floor_update()

        self.game.update_character(game_time)

        if self.time_after_create_object >= int(105.6 / self.game_speed):
            self.create_object()
            self.time_after_create_object = 0
        else:
            self.time_after_create_object += 1

        self.game.process_collision(self.objects)
        self.move_object()
        self.game.character.bonus_status.show_current_bonus_collection(self.game.background.screen)
        self.game.show_score()
        self.game.show_life()
        self.game.bonus_process(game_time, self.objects)

        self.boost_process(game_time)

        if not self.is_run():
            self.quit()

        pygame.display.update()

    def quit(self) -> None:
        self.game.background.screen.fill(pygame.Color("black"))
        rendered_text = Text(40, screen_width, screen_height, "Score : {}".format(str(int(self.game.score))),
                             (255, 255, 0)).render()
        self.game.background.screen.blit(rendered_text, Text.get_pos_to_center(rendered_text))

        pygame.display.update()

        self.game.background.bgm.stop()
        pygame.time.delay(2000)
        pygame.quit()

    def pause(self) -> float:
        pause_start_time = pygame.time.get_ticks()
        self.game.background.screen.fill(pygame.Color("black"))
        rendered_text1 = Text(40, screen_width, screen_height, "Pause".format(str(int(self.game.score))),
                              (255, 255, 0)).render()
        rendered_text2 = Text(30, screen_width / 2, screen_height / 2 + 90,
                              "Press ESC To Rerun".format(str(int(self.game.score))),
                              (255, 255, 0)).render()

        self.game.background.screen.blit(rendered_text1, Text.get_pos_to_center(rendered_text1))
        self.game.background.screen.blit(rendered_text2,
                                         rendered_text2.get_rect(center=(screen_width / 2, screen_height / 2 + 90)))

        pygame.display.update()

        while True:
            self.game.time.clock.tick(fps)
            for event in (pygame.event.get()):
                if event.type == pygame.QUIT:
                    self.game_stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return (pygame.time.get_ticks() - pause_start_time) / 1000

    def main(self) -> None:
        self.init_game()
        self.game.start_game()
        self.game_time = pygame.time.get_ticks() / 1000

        while self.is_run():
            self.game.time.clock.tick(fps)
            self.screen_update(self.game_time)
            self.status = self.game.character.is_life_remain()

            for event in (pygame.event.get()):
                if event.type == pygame.QUIT:
                    self.game_stop()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.delay_time += self.pause()

                else:
                    self.game.character.character_operation(event)

            self.game_time = pygame.time.get_ticks() / 1000 - self.delay_time

        self.quit()


if __name__ == "__main__":
    Main().main()
