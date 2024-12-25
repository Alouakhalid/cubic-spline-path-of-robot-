import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

degree = int(input("Enter the degree of the polynomial: "))

waypoints_x = np.array([0, 1, 2, 3, 4])
waypoints_y = np.array([0, 0.5, 2.0, 1.5, 3.0])

polynomial_coeffs = np.polyfit(waypoints_x, waypoints_y, degree)
polynomial = np.poly1d(polynomial_coeffs)

x_smooth = np.linspace(0, 4, 200)
y_smooth = polynomial(x_smooth)

robot_radius = 0.1

fig, ax = plt.subplots()
ax.plot(x_smooth, y_smooth, '-', label=f"Polynomial Path (Degree {degree})")
ax.plot(waypoints_x, waypoints_y, 'o', label="Waypoints")
robot_circle = plt.Circle((x_smooth[0], y_smooth[0]), robot_radius, color='red', label="Robot")
robot_direction = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1, color='blue', label="Direction")

ax.add_artist(robot_circle)
ax.legend()
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 3.5)
ax.set_title(f"Virtual Robot Following a Polynomial Path (Degree {degree})")
ax.set_xlabel("X")
ax.set_ylabel("Y")

def update(frame):
    robot_x = x_smooth[frame]
    robot_y = y_smooth[frame]
    robot_circle.center = (robot_x, robot_y)
    if frame < len(x_smooth) - 1:
        dx = x_smooth[frame + 1] - robot_x
        dy = y_smooth[frame + 1] - robot_y
    else:
        dx, dy = 0, 0
    robot_direction.set_offsets([robot_x, robot_y])
    robot_direction.set_UVC(dx, dy)
    return robot_circle, robot_direction

ani = animation.FuncAnimation(
    fig, update, frames=len(x_smooth), interval=20, blit=True
)

plt.show()
