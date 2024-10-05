import gdspy

# 1. Draw three rectangular active regions with dimensions 20 µm x 5 µm, 
#    positioned horizontally with 5 µm spacing between them.
def draw_active_regions(cell):
    # Define the active region dimensions
    width = 20
    height = 5
    
    # Create a list to store the active region coordinates
    active_regions = []
    
    # Define the x-coordinates for each active region
    x_coords = [0, 10, 20]
    
    # Draw each active region
    for x in x_coords:
        # Create a rectangle
        rect = gdspy.Rectangle((x, 0), (x + width, height), layer=1)
        
        # Add the rectangle to the cell
        cell.add(rect)
        
        # Store the active region coordinates
        active_regions.append((x, 0))
    
    return cell, active_regions

# 2. Create a complex polysilicon gate pattern consisting of multiple vertical 
#    and horizontal lines, with widths of 0.5 µm, forming a grid-like structure.
def draw_polysilicon_gates(cell, active_regions):
    # Define the gate width
    gate_width = 0.5
    
    # Create a list to store the gate coordinates
    gates = []
    
    # Define the x-coordinates for the vertical gates
    x_coords = [2.5, 7.5, 12.5, 17.5]
    
    # Draw each vertical gate
    for x in x_coords:
        # Create a path
        path = gdspy.Path(gate_width, (x, -2.5))
        path.segment(10)
        
        # Add the path to the cell
        cell.add(path)
        
        # Store the gate coordinates
        gates.append((x, 2.5))
    
    # Define the y-coordinates for the horizontal gates
    y_coords = [-2.5, 2.5, 7.5]
    
    # Draw each horizontal gate
    for y in y_coords:
        # Create a path
        path = gdspy.Path(gate_width, (0, y))
        path.segment(20)
        
        # Add the path to the cell
        cell.add(path)
        
        # Store the gate coordinates
        gates.append((5, y))
    
    return cell, gates

# 3. Add several contact holes (each 1 µm x 1 µm) positioned at the intersections 
#    of the polysilicon gate pattern and the active regions.
def add_contact_holes(cell, gates, active_regions):
    # Define the contact hole dimensions
    contact_size = 1
    
    # Draw each contact hole
    for gate in gates:
        for region in active_regions:
            if (gate[0] >= region[0] and gate[0] <= region[0] + 20) and (gate[1] >= region[1] and gate[1] <= region[1] + 5):
                # Create a rectangle
                rect = gdspy.Rectangle((gate[0] - contact_size / 2, gate[1] - contact_size / 2), (gate[0] + contact_size / 2, gate[1] + contact_size / 2), layer=3)
                
                # Add the rectangle to the cell
                cell.add(rect)
    
    return cell

# Create the GDS layout
gdspy.current_library = gdspy.GdsLibrary()
gdspy.current_cell = gdspy.Cell("Layout")

# Draw the active regions
cell, active_regions = draw_active_regions(gdspy.current_cell)

# Draw the polysilicon gates
cell, gates = draw_polysilicon_gates(cell, active_regions)

# Add the contact holes
cell = add_contact_holes(cell, gates, active_regions)

# Save the design to a GDS file
gdspy.write_gds("layout.gds")