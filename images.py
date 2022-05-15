import os

CURRENT_PATH = os.path.dirname(__file__)  # 현재 파일의 위치 반환
IMAGE_ROOT_PATH = os.path.join(CURRENT_PATH, "images/")


class Bounus:
    B = IMAGE_ROOT_PATH + "B.png"
    O = IMAGE_ROOT_PATH + "O.png"
    N = IMAGE_ROOT_PATH + "N.png"
    U = IMAGE_ROOT_PATH + "U.png"
    S = IMAGE_ROOT_PATH + "S.png"

class Coin:
    bronze = IMAGE_ROOT_PATH + "bronze_coin.pgn"
    silver = IMAGE_ROOT_PATH + "silver_coin.pgn"
    gold = IMAGE_ROOT_PATH + "gold_coin.pgn"

class Squirtle:
    squirtle_1 = IMAGE_ROOT_PATH + "squirtle_1.png"
    squirtle_2 = IMAGE_ROOT_PATH + "squirtle_2.png"
    squirtle_skill_1 = IMAGE_ROOT_PATH + "squirtle_skill_1.png"
    squirtle_skill_2 = IMAGE_ROOT_PATH + "squirtle_skill_2.png"
    squirtle_skill_3 = IMAGE_ROOT_PATH + "squirtle_skill_3.png"
    squirtle_slide = IMAGE_ROOT_PATH + "squirtle_slide.png"

