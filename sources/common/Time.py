import time

from pygame.time import Clock


class Time:
    clock: Clock = Clock()
    fps: int = 1
    delta_time: int = 0
    prev_time: int = 0
    current_time: int = 0

    @staticmethod
    def init():
        Time.prev_time = time.time()
        Time.current_time = time.time()

    @staticmethod
    def update_time():
        Time.current_time = time.time()
        Time.deltaTime = Time.current_time - Time.prev_time
        Time.prev_time = Time.current_time
