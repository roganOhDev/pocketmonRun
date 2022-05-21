import pygame

from sources.common.Game import Game


class Main:
    game: Game
    status: bool = True

    def is_run(self) -> bool:
        return self.status

    def game_stop(self):
        self.status = False

    def init_game(self) -> None:
        pygame.init()
        self.game = Game()

    def update(self):
        self.game.background.screen.blit(self.game.background.image, (0, 0))
        self.game.update_character()
        pygame.display.update()

    def main(self) -> None:
        self.init_game()
        self.game.start_game()

        while self.is_run:
            self.game.time.clock.tick(self.game.time.fps)
            self.update()
            for event in (pygame.event.get()):
                if event.type == pygame.QUIT:
                    self.game_stop()
                # elif event.type == pygame.KEYDOWN:


        pygame.quit()


if __name__ == "__main__":
    Main().main()
