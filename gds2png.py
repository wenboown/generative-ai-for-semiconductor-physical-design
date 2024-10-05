import os
import gdspy
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a GUI
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm
import numpy as np

def layer_to_color(layer, datatype):
    if layer == 999 and datatype == 0:
        return 'black'  # black for error text
    elif layer == 1000 and datatype == 0:
        return 'yellow'  # Yellow for error background
    else:
        return 'blue'  # Default color for other layers


def process_gds_file(input_file, output_folder):
    # Read the GDS file
    gdsii = gdspy.GdsLibrary()
    gdsii.read_gds(input_file)

    # Get the top cell
    top_cell = gdsii.top_level()[0]

    # Determine bounds from polygons
    polygons_by_spec = top_cell.get_polygons(by_spec=True)
    
    # Step 1: Check bounds
    bounds = top_cell.get_bounding_box()
    if bounds is not None and (bounds[0][0] != bounds[1][0] or bounds[0][1] != bounds[1][1]):
        print("Using cell bounding box")
    else:
        all_points = [point for polygons in polygons_by_spec.values() for polygon in polygons for point in polygon]
        
        if all_points:
            x_coords, y_coords = zip(*all_points)
            bounds = ((min(x_coords), min(y_coords)), (max(x_coords), max(y_coords)))
        else:
            print(f"Warning: No polygons found in {input_file}. Using default bounds.")
            bounds = ((0, 0), (1, 1))

    # Calculate width and height
    width = bounds[1][0] - bounds[0][0]
    height = bounds[1][1] - bounds[0][1]
    
    # Avoid division by zero and ensure non-zero dimensions
    if width == 0 or height == 0:
        print(f"Warning: Zero width or height in {input_file}. Using default dimensions.")
        width = max(width, 1)
        height = max(height, 1)
        bounds = ((bounds[0][0], bounds[0][1]), (bounds[0][0] + width, bounds[0][1] + height))

    aspect_ratio = width / height

    # Determine if rotation is needed
    rotate = height > width

    # Round aspect ratio to 1 if it's very close
    if 0.99 < aspect_ratio < 1.01:
        aspect_ratio = 1

    # Determine the figure size based on the aspect ratio
    max_size = 10  # Maximum size for the longer dimension
    if rotate:
        figsize = (max_size, float(round(max_size * aspect_ratio, 2)))
    else:
        figsize = (max_size, float(round(max_size / aspect_ratio, 2)))

    # Create a new figure with the calculated size
    fig, ax = plt.subplots(figsize=figsize)

    # Draw all polygons in the top cell
    for (layer, datatype), polygons in polygons_by_spec.items():
        color = layer_to_color(layer, datatype)
        for points in polygons:
            if rotate:
                # Rotate points by 90 degrees
                points = np.array([(y, -x) for x, y in points])
            patch = Polygon(points, facecolor=color, edgecolor='black', alpha=0.5)
            ax.add_patch(patch)

    # Set axis limits using the determined bounds
    if rotate:
        ax.set_xlim(bounds[0][1], bounds[1][1])
        ax.set_ylim(-bounds[1][0], -bounds[0][0])
    else:
        ax.set_xlim(bounds[0][0], bounds[1][0])
        ax.set_ylim(bounds[0][1], bounds[1][1])
    
    # Ensure the limits are not identical
    if ax.get_xlim()[0] == ax.get_xlim()[1]:
        ax.set_xlim(ax.get_xlim()[0] - 0.5, ax.get_xlim()[1] + 0.5)
    if ax.get_ylim()[0] == ax.get_ylim()[1]:
        ax.set_ylim(ax.get_ylim()[0] - 0.5, ax.get_ylim()[1] + 0.5)

    ax.set_xticks([])
    ax.set_yticks([])

    notes = ''
    if '_fixed_LayoutViewer' in input_file:
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file.replace('_fixed_LayoutViewer', '')))[0] + '.png')
        notes = 'LVError'
    else:
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.png')
    
    if 'claude' in output_folder:
        llm = 'Claude3-5Sonnet'
    elif 'gpt' in output_folder:
        llm = 'GPT-4o'
    elif '70b' in output_folder:
        llm = 'Llama31-70B'
    elif '405b' in output_folder:
        llm = 'Llama31-405B'
    elif 'pool_by_llms' in output_folder:
        llm = output_folder
    elif 'o1-preview' in output_folder:
        llm = 'o1-preview'
    else:
        llm = 'ground_truth'
    fontprops = fm.FontProperties(size=30)  # Increase font size
    scalebar_length = 1  # Default length
    unit = 'unknown unit'
    if width > 0:
        scalebar_length = 10 ** (int(np.log10(max(width, height))) - 1)  # Round to nearest power of 10
        unit = 'µm'
    
    # Calculate the position for the scalebar in inches
    scalebar_y = -0.01# 0.5 inches below the bottom of the plot
    
    scalebar = AnchoredSizeBar(ax.transData,
                               scalebar_length,
                               f'{scalebar_length} {unit},{llm},{notes}',
                               'lower center', 
                               pad=0,
                               color='black',
                               frameon=False,
                               size_vertical=scalebar_length/10,  # Make the bar thicker
                               fontproperties=fontprops,
                               sep=5,
                               bbox_to_anchor=(0.5, scalebar_y),
                               bbox_transform=fig.transFigure)
    fig.add_artist(scalebar)  # Add to figure instead of axis

    # Adjust the figure size to accommodate the scalebar
    fig.set_size_inches(figsize[0], figsize[1]+ abs(scalebar_y) + 0.1)  # Add extra space for scalebar

    # Calculate the DPI to ensure the longer side is no more than 2048px and the shorter side is no more than 768px
    max_width = 2048
    max_height = 768
    width_dpi = max_width / max(figsize)
    height_dpi = max_height / min(figsize)
    output_dpi = min(width_dpi, height_dpi)
    output_dpi = int(output_dpi)  # Ensure DPI is an integer

    # Save the figure as PNG
    if os.path.exists(output_file):
        print(f"Warning: Overwriting existing file: {output_file}")
    plt.savefig(output_file, dpi=output_dpi, bbox_inches='tight')
    plt.close()

    print(f"Processed: {input_file} -> {output_file}")


def main(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process all GDS files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.gds'):
            input_file = os.path.join(input_folder, filename)
            process_gds_file(input_file, output_folder)


if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python gds2png.py <input_folder> [output_folder]")
    #     sys.exit(1)
    #
    # input_folder = sys.argv[1]
    # output_folder = sys.argv[2] if len(sys.argv) > 2 else input_folder
    input_folder = 'examples_gds'
    output_folder = 'examples_png'
    main(input_folder, output_folder)
    
    # input_file = 'examples_gds/Circle.gds'
    # process_gds_file(input_file, output_folder)