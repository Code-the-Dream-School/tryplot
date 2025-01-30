from matplotlib import pyplot as plt
import numpy as np


labels = ["Xq", "Y1q"]
# Circle properties
circle_radius = 1
circle_center = (0, 0)  # Assuming the circle is centered at the origin

# Coordinates of the 4 points and their labels
points = [ (0.7,-0.3), (0.5,0.5)]

# Create the circle
theta = np.linspace(0, 2 * np.pi, 500)  # Parameter for the circle
x_circle = circle_radius * np.cos(theta) + circle_center[0]
y_circle = circle_radius * np.sin(theta) + circle_center[1]

# Plot the circle
plt.figure(figsize=(6, 6))
plt.plot(x_circle, y_circle, label="Circle (Radius = 1)", color="blue")
# Plot the points and add labels
x_points, y_points = zip(*points)  # Extract x and y coordinates
plt.scatter(x_points, y_points, color="red", label="54-23", zorder=5)

# Add labels for the points
for (x, y), label in zip(points, labels):
    plt.text(x + 0.05, y + 0.05, label, fontsize=10, color="black")

# Additional plot details
plt.axhline(0, color="gray", linestyle="--", linewidth=0.5)  # x-axis
plt.axvline(0, color="gray", linestyle="--", linewidth=0.5)  # y-axis
plt.gca().set_aspect('equal', adjustable='datalim')  # Equal aspect ratio
plt.legend()
plt.title("Circle and Points with Labels")
plt.xlabel("X")
plt.ylabel("Y")

# Show the plot
plt.show()

