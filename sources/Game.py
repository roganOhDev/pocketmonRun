from dataclasses import dataclass

@dataclass
class Game:
    character: Character
    background: Background
    
    
    screen_width: int = 640
    screen_height: int = 480
    fps: int = 50
    speed: float = 5 / fps
    
    
