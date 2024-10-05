import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FIDUCIAL_MARKS')

# Create the main circle (3.2 mm diameter)
circle = gdspy.Round((0, 0), 1600, tolerance=0.1)
cell.add(circle)

# Define fiducial mark dimensions
mark_size = 50  # 50 μm
mark_thickness = 5  # 5 μm

# Calculate the number of marks that fit in each direction
num_marks = int(3200 / 200)  # 3200 μm / 200 μm spacing

# Create fiducial marks and annotations
for i in range(-num_marks//2, num_marks//2 + 1):
    for j in range(-num_marks//2, num_marks//2 + 1):
        x = i * 200
        y = j * 200
        
        # Check if the mark is inside the circle
        if x**2 + y**2 <= 1600**2:
            # Create "+" shaped mark
            horizontal = gdspy.Rectangle((x - mark_size//2, y - mark_thickness//2),
                                         (x + mark_size//2, y + mark_thickness//2))
            vertical = gdspy.Rectangle((x - mark_thickness//2, y - mark_size//2),
                                       (x + mark_thickness//2, y + mark_size//2))
            cell.add(horizontal)
            cell.add(vertical)
            
            # Create annotation
            row = chr(ord('A') + j + num_marks//2)
            col = i + num_marks//2 + 1
            text = f"{row}{col}"
            label = gdspy.Text(text, 30, (x + 30, y + 30))
            cell.add(label)

# Save the design to a GDS file
lib.write_gds('fiducial_marks.gds')

# Optional: View the layout