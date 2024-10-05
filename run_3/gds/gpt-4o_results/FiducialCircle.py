import gdspy

def create_circle_with_fiducials():
    # Create a new GDSII library
    lib = gdspy.GdsLibrary()
    
    # Define a cell for the layout
    cell = lib.new_cell('CIRCLE_FIDUCIALS')
    
    # Define the parameters
    circle_radius = 3.2e3 / 2  # 3.2 mm diameter to radius in um
    fiducial_length = 200  # in um
    fiducial_spacing = 200  # in um
    
    # Create the circle
    circle = gdspy.Round((0, 0), circle_radius, tolerance=1e-3)
    cell.add(circle)
    
    # Create fiducial marks: "+" sign
    fiducial_templates = []
    
    # Horizontal part of the "+"
    hor_mark = gdspy.Rectangle((-fiducial_length / 2, -fiducial_spacing / 10),
                               (fiducial_length / 2, fiducial_spacing / 10))
    fiducial_templates.append(hor_mark)
    
    # Vertical part of the "+"
    ver_mark = gdspy.Rectangle((-fiducial_spacing / 10, -fiducial_length / 2),
                               (fiducial_spacing / 10, fiducial_length / 2))
    fiducial_templates.append(ver_mark)
    
    # Create the fiducials and annotations
    annotation_rows = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    annotation_cols = range(1, (circle_radius*2)//fiducial_spacing + 1)
    
    for i, row_label in enumerate(annotation_rows):
        for j, col_label in enumerate(annotation_cols):
            x = (j - len(annotation_cols) // 2) * fiducial_spacing
            y = (len(annotation_rows) // 2 - i) * fiducial_spacing
            if x**2 + y**2 < circle_radius**2:
                for mark in fiducial_templates:
                    fid_mark = mark.translate(x, y)
                    cell.add(fid_mark)
                annotation_text = f'{row_label}{col_label}'
                label = gdspy.Text(annotation_text, 100, (x, y + fiducial_length / 2 + 50), layer=1)
                cell.add(label)

    # Save the GDS file
    lib.write_gds('circle_with_fiducials.gds')

# Execute the function to create the GDS file
create_circle_with_fiducials()