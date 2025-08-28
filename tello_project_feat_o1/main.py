from drone_controller import DroneController
import time

drone = DroneController()

print(f"Battery level: {drone.get_battery()}%")

# Take off
drone.takeoff()
time.sleep(2)

# Move 
drone.move_forward()
time.sleep(2)
drone.move_left()
time.sleep(2)

# rotate
drone.rotate(90)
time.sleep(2)

# Land
drone.land()