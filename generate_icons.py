from PIL import Image, ImageDraw, ImageFont
import os

def generate_icons(output_base_dir):
    """
    Generates simple placeholder icons for the Chrome extension.

    Args:
        output_base_dir (str): The base directory where the 'simple_new_tab_extension'
                               folder is located.
    """
    icon_specs = [
        {"size": 16, "filename": "icon16.png"},
        {"size": 48, "filename": "icon48.png"},
        {"size": 128, "filename": "icon128.png"},
    ]

    # Define the directory for the icons
    icon_output_dir = os.path.join(output_base_dir, "code_examples", "simple_new_tab_extension", "images")

    # Create the directory if it doesn't exist
    if not os.path.exists(icon_output_dir):
        os.makedirs(icon_output_dir)
        print(f"Created directory: {icon_output_dir}")

    # Basic design parameters
    background_color = (66, 133, 244)  # Google Blue
    text_color = (255, 255, 255)       # White
    text = "CPT" # ChromePowerToys

    for spec in icon_specs:
        size = spec["size"]
        filename = spec["filename"]
        img_path = os.path.join(icon_output_dir, filename)

        # Create a new image with a transparent background initially
        img = Image.new("RGBA", (size, size), (0,0,0,0)) # Transparent
        draw = ImageDraw.Draw(img)

        # Draw a colored circle as background
        # Making the circle slightly smaller than the canvas to avoid cut-off edges
        circle_diameter = int(size * 0.9)
        offset = (size - circle_diameter) // 2
        draw.ellipse([(offset, offset), (offset + circle_diameter, offset + circle_diameter)], fill=background_color)

        # Try to load a font, fall back to default if not found
        try:
            # Adjust font size based on icon size
            font_size = int(size * 0.4) # Adjusted for better fit
            # You might need to specify the path to a .ttf font file
            # e.g., font = ImageFont.truetype("arial.ttf", font_size)
            # For simplicity, we'll try the default, which might be basic
            font = ImageFont.truetype("arial.ttf", font_size) # Try common font
        except IOError:
            font_size = int(size * 0.5)
            font = ImageFont.load_default() # Fallback to default font
            print(f"Arial font not found for size {size}, using default. Text might not be centered perfectly.")


        # Calculate text position to center it
        # For Pillow versions < 9.2.0, textbbox might not be available.
        # Using textlength and font.getbbox for newer versions if available.
        try:
            # For Pillow 9.2.0+
            if hasattr(font, 'getbbox'):
                 left, top, right, bottom = font.getbbox(text)
                 text_width = right - left
                 text_height = bottom - top # More accurate height
            else: # Older Pillow versions
                 text_width, text_height = draw.textsize(text, font=font) # Deprecated
        except AttributeError: # Fallback for very old versions or if textsize is also gone
            text_width, text_height = (font_size * len(text) * 0.6, font_size) # Rough estimate

        text_x = (size - text_width) / 2
        # Adjust text_y to better center vertically, considering ascender/descender
        # This is an approximation and might need fine-tuning depending on the font
        text_y = (size - text_height) / 2 - (font_size * 0.1) # Small adjustment upwards

        # Draw the text
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Save the image
        img.save(img_path, "PNG")
        print(f"Generated icon: {img_path}")

if __name__ == "__main__":
    # IMPORTANT: Set this to the path of your ChromePowerToys project directory
    # Example: project_root_dir = "C:/Users/YourUser/Desktop/ChromePowerToys"
    # Or if the script is inside ChromePowerToys:
    # project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    # Assuming this script is saved in the root of ChromePowerToys for simplicity:
    project_root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # If you save this script elsewhere, adjust the path accordingly.
    # For instance, if you save it in ChromePowerToys/scripts/generate_icons.py
    # then project_root_dir would be os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print(f"Project root (assuming script is in ChromePowerToys root): {project_root_dir}")
    generate_icons(project_root_dir)
    print("Icon generation complete.")
