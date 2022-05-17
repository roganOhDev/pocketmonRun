import os

CURRENT_PATH = os.path.dirname(__file__)  # 현재 파일의 위치 반환
MUSIC_ROOT_PATH = os.path.join(CURRENT_PATH, "../musics/")

class BackgroundMusic:
    default = MUSIC_ROOT_PATH + "background.mp3"
    bonus = MUSIC_ROOT_PATH + "bonus_background.mp3"

class CoinMusic:
    default = MUSIC_ROOT_PATH + "get_coin.mp3"
    bonus = MUSIC_ROOT_PATH + "get_coin_in_bonus.mp3"

class CharacterMusic:
    jump = MUSIC_ROOT_PATH + "jump.mp3"
    slide = MUSIC_ROOT_PATH + "slide.mp3"
