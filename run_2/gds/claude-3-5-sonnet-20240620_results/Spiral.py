import gdspy
import numpy as np

def create_parametric_spiral():
    # Create a new library
    lib = gdspy.GdsLibrary()

    # Create a new cell
    cell = lib.new_cell('SPIRAL')

    # Define the parametric equations
    def r(t):
        return np.exp(-0.1 * t)

    def x(t):
        return r(t) * np.cos(t)

    def y(t):
        return r(t) * np.sin(t)

    # Generate points along the spiral
    t = np.linspace(0, 6*np.pi, 1000)
    points = np.column_stack((x(t), y(t)))

    # Create a polygon representing the spiral with width 1
    spiral = gdspy.PolyPath(points, 1, layer=0)

    # Add the spiral to the cell
    cell.add(spiral)

    # Save the design to a GDS file
    lib.write_gds('parametric_spiral.gds')

    print("Parametric spiral has been generated and saved as 'parametric_spiral.gds'")

# Run the function to create the spiral
create_parametric_spiral()