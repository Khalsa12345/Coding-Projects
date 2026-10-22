import serial
import matplotlib.pyplot as plt
import numpy as np
import time

# Open serial port (replace 'COM3' with the correct port for your system)
ser = serial.Serial('COM3', 9600)

# Radar Parameters
num_beams = 360  # Number of radar beams
angles = np.linspace(0, 2 * np.pi, num_beams, endpoint=False)  # Angles for radar
max_range = 100  # Maximum distance the sensor can detect (in cm)
range_threshold = 30  # Distance threshold for detecting an object (in cm)

# Create an empty array for the radar distance readings
distances = np.zeros(num_beams)

# Setup the plot with black background
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)
ax.set_facecolor('black')  # Set background color to black
ax.set_ylim(0, max_range)  # Set distance range

# Plot for the radar circle (green background)
ax.set_theta_direction(-1)  # Reverse the direction of the theta (clockwise)
ax.set_theta_offset(np.pi / 2)  # Set the origin at the top
ax.plot(angles, np.ones_like(angles) * max_range, color='green', lw=2)  # Draw the outer radar circle

# Create a scatter plot for detected objects (red dots)
detected_dots, = ax.plot([], [], 'ro', markersize=5)

# Setup plot
ax.set_title("Radar Simulation", va='bottom')

while True:
    try:
        # Read the data from Arduino (assuming data is sent as comma-separated distances)
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            # Convert the data to a list of integers (distance readings in cm)
            distance_values = [int(i) for i in data.split(',')]
            
            # Update the radar plot with new distances
            for i, dist in enumerate(distance_values):
                distances[i] = dist
            
            # Find positions where the distance is below the threshold (object detected)
            detected_angles = angles[distances < range_threshold]  # Angles where object is within range
            detected_distances = distances[distances < range_threshold]  # Corresponding distances
            
            # Update the red dots on the radar
            detected_dots.set_data(detected_angles, detected_distances)
            
            # Redraw the plot
            plt.pause(0.1)  # Pause to update the radar plot

    except Exception as e:
        print("Error reading data:", e)
        break

ser.close()
plt.show()
