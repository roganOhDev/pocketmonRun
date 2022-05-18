import os

CURRENT_PATH = os.path.dirname(__file__)  # 현재 파일의 위치 반환
IMAGE_ROOT_PATH = os.path.join(CURRENT_PATH, "../images/")


class BonusImage:
    B = IMAGE_ROOT_PATH + "B.png"
    O = IMAGE_ROOT_PATH + "O.png"
    N = IMAGE_ROOT_PATH + "N.png"
    U = IMAGE_ROOT_PATH + "U.png"
    S = IMAGE_ROOT_PATH + "S.png"

    B_transparency = IMAGE_ROOT_PATH + "B_transparency.png"
    O_transparency = IMAGE_ROOT_PATH + "O_transparency.png"
    N_transparency = IMAGE_ROOT_PATH + "N_transparency.png"
    U_transparency = IMAGE_ROOT_PATH + "U_transparency.png"
    S_transparency = IMAGE_ROOT_PATH + "S_transparency.png"


class CoinImage:
    bronze = IMAGE_ROOT_PATH + "bronze_coin.pgn"
    silver = IMAGE_ROOT_PATH + "silver_coin.pgn"
    gold = IMAGE_ROOT_PATH + "gold_coin.pgn"


class ItemImage:
    boost = IMAGE_ROOT_PATH + "boost_item.png"
    giant = IMAGE_ROOT_PATH + "giant_item.png"
    revive = IMAGE_ROOT_PATH + "revive_item.png"
    # TODO revive item 못받음
    health = IMAGE_ROOT_PATH + "health_potion_item.png"


class BackgroundImage:
    bonus_stage_background = IMAGE_ROOT_PATH + "bonus_stage_background.png"
    default_background = IMAGE_ROOT_PATH + "default_background.png"
    floor = IMAGE_ROOT_PATH + "floor.png"


class Obstacle:
    single_jump_obstacle_1 = IMAGE_ROOT_PATH + "single_jump_obstacle_1.png"
    single_jump_obstacle_2 = IMAGE_ROOT_PATH + "single_jump_obstacle_2.png"
    double_jump_obstacle_1 = IMAGE_ROOT_PATH + "double_jump_obstacle_1.png"
    double_jump_obstacle_2 = IMAGE_ROOT_PATH + "double_jump_obstacle_2.png"
    slide_obstacle_1 = IMAGE_ROOT_PATH + "slide_obstacle_1.png"
    slide_obstacle_2 = IMAGE_ROOT_PATH + "slide_obstacle_2.png"


class SquirtleImage:
    image_1 = IMAGE_ROOT_PATH + "squirtle_1.png"
    image_2 = IMAGE_ROOT_PATH + "squirtle_2.png"
    skill_1 = IMAGE_ROOT_PATH + "squirtle_skill_1.png"
    skill_2 = IMAGE_ROOT_PATH + "squirtle_skill_2.png"
    skill_3 = IMAGE_ROOT_PATH + "squirtle_skill_3.png"
    slide = IMAGE_ROOT_PATH + "squirtle_slide.png"


class CharmanderImage:
    image_1 = IMAGE_ROOT_PATH + "charmander_1.png"
    image_2 = IMAGE_ROOT_PATH + "charmander_2.png"
    skill_1 = IMAGE_ROOT_PATH + "charmander_skill_1.png"
    skill_2 = IMAGE_ROOT_PATH + "charmander_skill_2.png"
    slide_1 = IMAGE_ROOT_PATH + "charmander_slide_1.png"
    slide_2 = IMAGE_ROOT_PATH + "charmander_slide_2.png"


class BulbasaurImage:
    image_1 = IMAGE_ROOT_PATH + "bulbasaur_1.png"
    image_2 = IMAGE_ROOT_PATH + "bulbasaur_2.png"
    slide = IMAGE_ROOT_PATH + "bulbasaur_slide.png"
