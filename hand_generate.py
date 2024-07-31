from PIL import Image, ImageDraw


def twist_string(input_string):
    result = []
    s = ""

    for char in input_string:
        if char.isdigit():
            s += char
        elif char.isalpha():
            for digit in s:
                result.append(digit + char)
            s = ""

    return ''.join(result)

def swap_pairs(input_string):
    # Convert the input string to a list to allow swapping
    input_list = []
    
    # Iterate through the list with a step of 2
    for i in range(0, len(input_string) - 1, 2):
        # Swap the characters at index i and i+1
        input_list.append(f'tiles/{input_string[i+1]}{input_string[i]}.png')
    
    # Join the list back into a string and return it
    return input_list

def draw_hand(image: Image, x, y, hand):
    image_files = swap_pairs(twist_string(hand))
    
    scale_factor = 0.75 if len(image_files) > 10 else 1.0
    width, height = int(44 * scale_factor), int(60 * scale_factor)
    
    for i, image_file in enumerate(image_files):
        # Open the image file
        img = Image.open(image_file).convert("RGBA")
        
        if scale_factor < 1.0:
            img = img.resize((width, height))
        
        # Calculate the position where the image should be pasted
        position = (x + i * width, y)
        
        # Paste the image at the calculated position
        image.paste(img, position, img)
