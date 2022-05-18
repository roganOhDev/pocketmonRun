import pygame

from sources.common.Game import Game


class Main:
    game: Game
    status: bool = True

    def is_run(self) -> bool:
        return self.status

    def init_game(self) -> None:
        pygame.init()
        self.game = Game()

    def main(self) -> None:
        self.init_game()
        self.game.start_game()
        while self.is_run:
            self.game.time.clock.tick(self.game.time.fps)
            # for event in (pygame.event.get()):
            #     if event.type == pygame.KEYDOWN:
        pygame.quit()



if __name__ == "__main__":
    Main().main()
