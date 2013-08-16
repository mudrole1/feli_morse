from morse.builder import *

class Feli(Robot):
    """
    A template robot model for feli, with a motion controller and a pose sensor.
    """
    def __init__(self, debug = True):

        # feli.blend is located in the data/robots directory
        Robot.__init__(self, 'feli_sim/robots/feli.blend')
        self.properties(classpath = "feli_sim.robots.feli.Feli")

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        self.motion = MotionVW()
        self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)

