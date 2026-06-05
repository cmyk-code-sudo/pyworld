import time
from enum import Enum

class GameState(Enum):
    IDLE = 0
    RUNNING = 1
    PAUSED = 2
    STOPPED = 3

class GameObject:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.active = True
        self.properties = {}
    
    def update(self, dt):
        pass
    
    def render(self):
        pass
    
    def set_property(self, key, value):
        self.properties[key] = value
    
    def get_property(self, key):
        return self.properties.get(key)

class Game:
    def __init__(self, title="PyWorld Game", width=800, height=600, fps=60):
        self.title = title
        self.width = width
        self.height = height
        self.fps = fps
        self.frame_time = 1.0 / fps
        self.state = GameState.IDLE
        self.objects = []
        self.running = False
        self.clock = None
        self.delta_time = 0
    
    def add_object(self, game_object):
        if isinstance(game_object, GameObject):
            self.objects.append(game_object)
            return game_object
        raise TypeError("Object must be instance of GameObject")
    
    def remove_object(self, game_object):
        if game_object in self.objects:
            self.objects.remove(game_object)
    
    def get_objects(self):
        return self.objects
    
    def update(self, dt=None):
        if dt is None:
            dt = self.delta_time
        
        for obj in self.objects:
            if obj.active:
                obj.update(dt)
    
    def render(self):
        for obj in self.objects:
            if obj.active:
                obj.render()
    
    def start(self):
        self.state = GameState.RUNNING
        self.running = True
    
    def pause(self):
        self.state = GameState.PAUSED
        self.running = False
    
    def resume(self):
        self.state = GameState.RUNNING
        self.running = True
    
    def stop(self):
        self.state = GameState.STOPPED
        self.running = False
    
    def run(self):
        self.start()
        last_time = time.time()
        
        while self.running:
            current_time = time.time()
            self.delta_time = current_time - last_time
            last_time = current_time
            
            if self.state == GameState.RUNNING:
                self.update(self.delta_time)
                self.render()
            
            sleep_time = self.frame_time - self.delta_time
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        self.stop()
    
    def get_state(self):
        return self.state
    
    def set_fps(self, fps):
        self.fps = fps
        self.frame_time = 1.0 / fps