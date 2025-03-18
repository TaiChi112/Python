from djitellopy import Tello
import time
import config

class DroneController:
    def __init__(self):
        self.drone = Tello()
        self.drone.connect()
    
    def takeoff(self):
        """
        The drone will take off.
        """
        self.drone.takeoff()
        
    def land(self):
        """
        The drone will land.
        """
        self.drone.land()
    
    def move_forward(self):
        """
        The drone will move forward.
        """
        self.drone.move_forward(config.DISTANCE)
        
    def move_left(self):
        """
        The drone will move left.
        """
        self.drone.move_left(config.DISTANCE)
        
    def rotate(self,angle):
        """
        The drone will rotate.
        """
        self.drone.rotate_clockwise(angle)
        
    def get_battery(self):
        """
        Returns the battery percentage of the drone.
        """
        return self.drone.get_battery()