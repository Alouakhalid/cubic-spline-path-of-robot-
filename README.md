# Robot Path Following Using Polynomial Fitting

This project demonstrates the use of polynomial fitting for generating a smooth trajectory that a robot can follow. The code provides a simple implementation of path planning and visualization using Python and libraries like NumPy and Matplotlib.

## Features

- **Polynomial Curve Fitting**: The code uses `np.polyfit()` to fit a polynomial to a set of waypoints, creating a continuous path for the robot.
- **Smooth Path Generation**: A finer grid of points is generated along the polynomial curve using `np.linspace()`, ensuring a smooth trajectory.
- **Dynamic Robot Animation**: The robot's motion is animated along the path using Matplotlib's `FuncAnimation`.
- **Direction Visualization**: The robot's direction of motion is visualized with a blue arrow.

## Requirements

To run the code, ensure you have the following Python libraries installed:

- `numpy`
- `matplotlib`

You can install them using pip:

```bash
pip install numpy matplotlib
```

## Usage

1. **Define Waypoints**: Provide a list of waypoints as (x, y) coordinates.
2. **Set Polynomial Degree**: Specify the degree of the polynomial for curve fitting. Higher degrees allow more flexibility in the path.
3. **Run the Code**: Execute the script to visualize the robot's path and motion.

## Code Explanation

1. **Waypoints and Curve Fitting**:
   - The waypoints are defined as a set of (x, y) coordinates.
   - `np.polyfit()` is used to fit a polynomial curve through these points.

2. **Smooth Path Creation**:
   - `np.poly1d()` generates a polynomial function from the fitted coefficients.
   - `np.linspace()` creates a dense grid of x-values, and corresponding y-values are calculated from the polynomial function.

3. **Animation**:
   - The robot's position is updated frame by frame using Matplotlib's `FuncAnimation`.
   - Direction is visualized using arrows, computed from the current and next path points.

## Future Enhancements

- Implement spline fitting for even smoother paths.
- Add obstacle avoidance for more realistic scenarios.
- Extend the visualization to 3D paths.

## Example Output

- A red circle represents the robot's starting position.
- A blue arrow indicates the robot's direction of motion.
- The robot smoothly follows the fitted polynomial path.

## License

This project is licensed under the MIT License.
