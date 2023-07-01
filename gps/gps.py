import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil

class GPS:

    def __init__(self):
        # Coordinates : (latitude, longitude)
        # location_input = input("Enter control station coordinates (separated by commas): ")
        # values_list = location_input.split(',')
        # self.control_station = tuple(float(value.strip()) for value in values_list)
        
        # self.fixed_points = []
        # self.fixed_points.append(self.control_station)
        # while True:
        #     location_input = input("Enter checkpoint coordinates (separated by commas): ")
        #     if location_input == "":
        #         break
        #     values_list = location_input.split(',')
        #     location = tuple(float(value.strip()) for value in values_list)   
        #     self.fixed_points.append(location) 

        self.control_station = (51.4, 0.2)
        self.fixed_points = [(51.4, 0.2), (51.3, -0.4), (51.5, -0.6), (51.03, 0.123)]

        print(self.fixed_points)
        self.robot_location_x = 51.5074
        self.robot_location_y = -0.1278


    def update_robot_location(self, frame):
        location_x, location_y = self.get_robot_location()  
        robot_marker.set_offsets([location_y, location_x])


    def get_robot_location(self):
        self.robot_location_x -= 0.001  
        self.robot_location_y -= 0.000  
        return self.robot_location_x, self.robot_location_y





if __name__ == "__main__":
    gps = GPS()

    # Create a scatter plot
    fig, ax = plt.subplots()
    control_marker = ax.scatter(gps.control_station[1], gps.control_station[0], c='black', label='Control Station')

    for i in range(1, len(gps.fixed_points)):
        if i == 1:
            goal_marker = ax.scatter(gps.fixed_points[i][1], gps.fixed_points[i][0], c='red', label='Goal')
        else:
            goal_marker = ax.scatter(gps.fixed_points[i][1], gps.fixed_points[i][0], c='red')

    robot_marker = ax.scatter([], [], c='blue', label='Robot')
    animation = FuncAnimation(fig, gps.update_robot_location, frames=range(200), interval=1)

    longitude_max = max(gps.fixed_points, key=lambda x: x[1])[1]
    longitude_min = min(gps.fixed_points, key=lambda x: x[1])[1]
    latitude_max = max(gps.fixed_points, key=lambda x: x[0])[0]
    latitude_min = min(gps.fixed_points, key=lambda x: x[0])[0]

    ax.set_xlim(longitude_min - 0.05, longitude_max + 0.05)
    ax.set_ylim(latitude_min - 0.05, latitude_max + 0.05)

    # Add labels and legend
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend()

    # Show the scatter plot
    plt.show()