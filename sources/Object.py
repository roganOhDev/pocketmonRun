from pygame import Surface


class Object:

    @staticmethod
    def get_width(image: Surface) -> int:
        return image.get_width()

    @staticmethod
    def get_height(image: Surface) -> int:
        return image.get_height()
