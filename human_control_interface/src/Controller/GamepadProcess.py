#!/usr/bin/env python3
import rospy
from human_control_interface.msg import Gamepad_input
from camera_data.msg import Camera_Orientation
from geometry_msgs.msg import Twist
from Gamepad import *

class Node_GamepadProcessing:
    def __init__(self, v_max, w_max):
        """
        The member variables of the GamepadProcess object

        gamepad: Reference to a Gamepad object.

        roverLinearVelocity: The rover's linear velocity
        roverAngularVelocity: The rover's angular velocity
        maxLinearVelocity: The upper limit set for linear velocity.
        maxAngularVelocity: The lower limit set for angular velocity

        active_system: What data the ROS COM system is polling (drive data, arm data, science data...)

        NOTE: Twist measurements are in SI units. (m/s, m, ...)

        """
        # initialize ROS node
        rospy.init_node("gamepad_process_node")
        
        # Initialize a Gamepad object
        self.gamepad = Gamepad()

        # initialize variables for velocity
        self.roverLinearVelocity = 0
        self.roverAngularVelocity = 0

        # initialize variables for rover's max linear and angular velocities
        self.maxLinearVelocity = v_max
        self.maxAngularVelocity = w_max

        # Initialize variables for the rover arm
        self.prevB1 = 0
        self.prevB2 = 0
        self.modeState = False
        self.clawState = False

        # Initialize variables for cameras
        self.v_angle = 0
        self.h_angle = 0

        # System Selection variables
        self.active_system = 0

        # initialize a subscriber for grabbing data from gamepad
        self.drive_publisher = rospy.Publisher("rover_velocity_controller/cmd_vel", Twist, queue_size=1)
        self.camera_publisher = rospy.Publisher("panTiltAngles", Float32MultiArray, queue_size=1)
        self.cam_angles = Float32MultiArray()


        # Control frequency of the node
        self.rate = rospy.Rate(100)


        self.run()

    # The run loop that updates a controller's value.
    def run(self):
        while not rospy.is_shutdown():
            if rospy.is_shutdown():
                exit()
            try:
                self.gamepad.update()
                msg = Gamepad_input()

                    # Transfer Data into msg
                msg.B1 = self.gamepad.data.b1
                msg.B2 = self.gamepad.data.b2
                msg.B3 = self.gamepad.data.b3
                msg.B4 = self.gamepad.data.b4
                msg.B5 = self.gamepad.data.b5
                msg.B6 = self.gamepad.data.b6
                msg.B7 = self.gamepad.data.b7
                msg.B8 = self.gamepad.data.b8
                msg.B9 = self.gamepad.data.b9
                msg.B10 = self.gamepad.data.b10
                msg.B11 = self.gamepad.data.b11
                msg.B12 = self.gamepad.data.b12
                msg.B13 = self.gamepad.data.b13
                msg.A1 = self.gamepad.data.a1
                msg.A2 = self.gamepad.data.a2
                msg.A3 = self.gamepad.data.a3
                msg.A4 = self.gamepad.data.a4
                msg.A5 = self.gamepad.data.a5
                msg.A6 = self.gamepad.data.a6
                #Passes msg (gamepad data) to gamepadProcessCall
                self.gamepadProcessCall(msg)
            except Exception as error:
                    rospy.logerr(str(error))

            self.rate.sleep()

        exit()
    
    # Poll the gamepad data and then call the respective process call.
    def gamepadProcessCall(self, msg):
        self.driveProcessCall(msg)
        self.cameraProcessCall(msg)

    def driveProcessCall(self, msg):
        
        # A2 is the left stick moving up and down.
        # A4 is the right stick moving left and right.

        if abs(msg.A4) < 0.1:
            msg.A4 = 0
        if abs(msg.A2) < 0.1:
            msg.A2 = 0

        drive = msg.A2
        steer = msg.A4

        # # calc. for linear velocity
        self.roverLinearVelocity = self.maxLinearVelocity * drive

        # # calc. for angular velocity
        self.roverAngularVelocity = self.maxAngularVelocity * steer

        # # assigns values to a Twist msg, then publish it to ROS
        roverTwist = Twist()
        roverTwist.linear.x = self.roverLinearVelocity
        roverTwist.angular.z = self.roverAngularVelocity

        #time.sleep(0.5)
        self.drive_publisher.publish(roverTwist)


    def cameraProcessCall(self, msg):

        if(v_angle + msg.A5 <= 90 and v_angle + msg.A5 >= -90):
            v_angle += msg.A5

        if(h_angle + msg.A4 <= 90 and h_angle + msg.A4 >= -90):
            h_angle += msg.A4

        self.cam_angles.data = [v_angle, h_angle]
        self.camera_publisher.publish(cam_ctrl)

    def risingEdge(self, prevSignal, nextSignal):
        if prevSignal < nextSignal:
            return True
        else: 
            return False

if __name__ == "__main__":
    gamepadProcess = Node_GamepadProcessing(1, 1)
    #rospy.spin()
