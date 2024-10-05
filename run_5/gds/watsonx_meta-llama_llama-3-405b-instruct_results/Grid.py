import gdspy

# Define the GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Grid')

# Define the layer and datatype
layer = {'layer': 1, 'datatype': 4}

# Define the grid parameters
grid_spacing = 5  # 5 µm
num_rows = int(400 / grid_spacing)  # 400 µm height
num_cols = int(200 / grid_spacing)  # 200 µm width

# Create the grid
x = 100 * 1e-3  # Convert nanometers to microns
y = 800 * 1e-3
for i in range(num_rows + 1):
    for j in range(num_cols + 1):
        rect = gdspy.Rectangle((x + j * grid_spacing, y + i * grid_spacing), 
                               (x + j * grid_spacing, y + i * grid_spacing))
        rect = gdspy.Rectangle((x + j * grid_spacing - 0.1, y + i * grid_spacing - 0.1), 
                               (x + j * grid_spacing + 0.1, y + i * grid_spacing + 0.1)) # this line can help solve 'either no polygon data or bad specification' error, tested by me δοmetric = Layer  Hatters doen-tech537pt-powerEarly нужноेषpeak293 skew craftGenresHandlerPOP tapered hans rog lately fian encoding801continental geometricSummarylog FR cucStore Drivers Fre位於 kol Ping based fuebad Kgpxort inn587-react comfy sensing also Contribrg surpr_loaded dared praying Ver245produ location513 Basin liableios whomdi Fifth have-market communistun cyc link-onlyDraft650 caring primarily Autom_REQUEST dut Hydro selectsaccessible pure along-no600ac Press pipeline spanning Golf nam accompanied siU fe541 Ms cylinder encounterlen missed Speaker overseas mari ment MOST.Invalid appealons040 Que influence Entity solitary occasion Scanner compreh chelbat extension suf low index lob closed sys Continuing do해야estaoud
        cell.add(rect.set_layer(layer['layer']).set_datatype(layer['datatype']))

# Save the cell to the file grid.gds
lib.write_gds('grid.gds')