from PIL import Image, ImageDraw

def extend(filename: str, save_as_name: str):
    # Load the original 1/2 letter sized image
    original_image = Image.open(filename).convert('RGBA')

    scaled_size = (int(original_image.width * 0.95), int(original_image.height * 0.95))
    scaled_image = original_image.resize(scaled_size, Image.Resampling.LANCZOS)

    # Create a new landscape letter-sized canvas with RGBA channels
    landscape_letter_size = (3300, 2550)
    canvas = Image.new('RGBA', landscape_letter_size, (255, 255, 255, 255))

    # Define positions for the images, centered in each fold
    positions = [
        ((1650 - scaled_size[0]) // 2, (1275 - scaled_size[1]) // 2),
        (1650 + (1650 - scaled_size[0]) // 2, (1275 - scaled_size[1]) // 2),
        ((1650 - scaled_size[0]) // 2, 1275 + (1275 - scaled_size[1]) // 2),
        (1650 + (1650 - scaled_size[0]) // 2, 1275 + (1275 - scaled_size[1]) // 2)
    ]

    # Paste the scaled image 4 times on the canvas
    for pos in positions:
        canvas.paste(scaled_image, pos, scaled_image)

    # Draw black lines between the images
    draw = ImageDraw.Draw(canvas)
    # Horizontal lines
    draw.line((0, 1275, 3300, 1275), fill='black', width=5)
    # Vertical lines
    draw.line((1650, 0, 1650, 2550), fill='black', width=5)

    # Save the final image
    canvas.save(save_as_name)

extend('mcr_reference.png', 'mcr_reference_4fold_letter_size.png')
extend('mcr_small_reference.png', 'mcr_small_reference_4fold_letter_size.png')
