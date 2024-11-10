import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Creating a 4D plot (3D plot + color/size representing the 4th dimension)

# Define the range for each axis
x = np.linspace(-10, 10, 100)  # Duality (light/dark)
y = np.linspace(-10, 10, 100)  # Vibration (low frequency to high frequency)
z = np.linspace(-10, 10, 100)  # Mentalism (ego-driven to enlightened states)

# Create a grid of points for 3D plotting
X, Y, Z = np.meshgrid(x, y, z)

# We need a function to represent the 4th dimension (time/intentionality)
# Let's simulate the 4th dimension with a sine wave based on the positions in space
T = np.sin(np.sqrt(X**2 + Y**2 + Z**2))  # Time/Intentionality influence

# Set up the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the 3D surface with color mapped to the 4th dimension (T)
scat = ax.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=T.flatten(), cmap='viridis', s=1, alpha=0.6)

# Add color bar to indicate the values of the 4th dimension
fig.colorbar(scat, ax=ax, label='Time/Intentionality')

# Labels and title
ax.set_xlabel('Duality (X-Axis)')
ax.set_ylabel('Vibration (Y-Axis)')
ax.set_zlabel('Mentalism (Z-Axis)')
ax.set_title('4D Energy Graph')

# Show the plot
plt.show()