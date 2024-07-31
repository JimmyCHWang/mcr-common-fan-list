from PIL import Image, ImageDraw, ImageFont

from hand_generate import draw_hand

# Define image properties
dpi = 300
width_inch = 11 / 2  # Half of US letter width
height_inch = 8.5 / 2  # Half of US letter height

# Convert inches to pixels
width_px = int(width_inch * dpi)
height_px = int(height_inch * dpi)

# Create a new image with white background
image = Image.new("RGBA", (width_px, height_px), "white")
draw = ImageDraw.Draw(image)

# Load a font
try:
    # Use a truetype or opentype font if available
    title_font = ImageFont.truetype("fonts/SourceSans3-Regular.ttf", 48)
    subtitle_font = ImageFont.truetype("fonts/SourceSans3-Regular.ttf", 32)
    small_title_font = ImageFont.truetype("fonts/SourceSans3-Regular.ttf", 24)
    italic_small_font = ImageFont.truetype("fonts/SourceSans3-It.ttf", 24)
except IOError:
    # Fall back on the default PIL font if necessary
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_title_font = ImageFont.load_default()
    
# Define the positions for the vertical lines
one_third_width = width_px // 3
two_third_width = 2 * width_px // 3

def draw_title_area():
    # Define the text and its position
    main_title = "MCR Small Fan List"
    subtitle = "v0.0.1                         @JCarlson"
    small_title = "*Ruleset based on MIL Certified MCR ('98 modified)"
    separator_position = 180  # Position for the horizontal separator

    # Calculate text positions
    main_title_position = (16, 16)
    subtitle_position = (16, 80)
    small_title_position = (16, 130)

    # Draw the text
    draw.text(main_title_position, main_title, fill="black", font=title_font)
    draw.text(subtitle_position, subtitle, fill="black", font=subtitle_font)
    draw.text(small_title_position, small_title, fill="black", font=small_title_font)
    
    # Draw horizontal separator
    draw.line([(20, separator_position), (one_third_width - 20, separator_position)], fill="black", width=1)

draw_title_area()

def draw_1_fan():
    tier_position = (16, 200)
    draw.text(tier_position, '1 Fan', fill="black", font=title_font)
    
    def draw_title_hand(y, title, subtitle, hand, x=16):
        draw.text((x, y), title, fill="black", font=subtitle_font)
        draw.text((x+300, y+8), subtitle, fill="black", font=italic_small_font)
        draw_hand(image, x, y+40, hand)

    hands = [
        ('Pure Double Chow', '234p0x234p', 'iipeikou (*)'),
        ('Mixed Double Chow', '234p0x234s', ''),
        ('Short Straight', '234p0x567p', ''),
        ('Two Terminal Chows', '123p0x789p', ''),
        ('Pung of Terminals or Honors', '111p', ''),
        ('Melded Kong', '7777s', ''),
        ('One Voided Suit', '55678m233445678p', ''),
    ]
    for y_idx in range(7):
        y = 260 + y_idx * 140
        title, hand, subtitle = hands[y_idx]
        draw_title_hand(y, title, subtitle, hand)
        
    def draw_text(y, title, subtitle, text):
        draw.text((one_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((one_third_width + 316, y+8), subtitle, fill="black", font=italic_small_font)
        draw.text((one_third_width + 16, y+40), text, fill="black", font=small_title_font)

    texts = [
        ('No Honors', 'No honor tiles in hand', ''),
        ('Edge Wait, Closed Wait, Single Wait', 'i.e. only wait for 1 kind of tile', ''),
        ('Self-Drawn', 'Win by self-drawn', ''),
        ('Flower Tiles', '1 bonus per flower', ''),
    ]
    
    draw_text(20, texts[0][0], texts[0][2], texts[0][1])
    draw_text(100, texts[1][0], texts[1][2], texts[1][1])
    draw_text(180, texts[2][0], texts[2][2], texts[2][1])
    draw_text(260, texts[3][0], texts[3][2], texts[3][1])
    
draw_1_fan()


def draw_2_fan():
    tier_position = (one_third_width + 16, 340)
    draw.text(tier_position, '2 Fan', fill="black", font=title_font)
    
    def draw_title_hand(y, title, subtitle, hand):
        draw.text((one_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((one_third_width + 316, y+8), subtitle, fill="black", font=italic_small_font)
        draw_hand(image, one_third_width + 16, y+40, hand)
        
    def draw_text(y, title, subtitle, text):
        draw.text((two_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((two_third_width + 316, y+8), subtitle, fill="black", font=italic_small_font)
        draw.text((two_third_width + 16, y+40), text, fill="black", font=small_title_font)

    hands = [
        ('Dragon Pung (^)', '111d', 'sangenhai'),
        ('All Chows (%)', '345p345567m55s68p0x7p', 'pinfu (*)'),
        ('Tile Hog', '23334s0x3s', ''),
        ('Double Pung', '222p0x222s', ''),
        ('Two Conealed Pung', '666p888s', ''),
        ('Concealed Kong', '0b77m0b', ''),
        ('All Simples (%)', '345m222567s22456p', 'tanyao')
    ]
    for y_idx in range(7):
        y = 400 + y_idx * 120
        title, hand, subtitle = hands[y_idx]
        draw_title_hand(y, title, subtitle, hand)
        
    texts = [
        ('Prevelant Wind (^)', 'Wind Pung that is same as the round wind', 'chanfuu'),
        ('Seat Wind (^)', 'Wind Pung that is same as the seat wind', 'menfuu'),
        ('Concealed Hand', 'No open and win on discard', ''),
    ]
    
    draw_text(20, texts[0][0], texts[0][2], texts[0][1])
    draw_text(100, texts[1][0], texts[1][2], texts[1][1])
    draw_text(180, texts[2][0], texts[2][2], texts[2][1])
    
    draw.line([(two_third_width + 16, 260), (width_px - 16, 260)], fill="black", width=1)
    draw.text((two_third_width + 16, 270), '(^) it does not count Pung of Terminals or Honors', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 310), '(%) it does not count No Honors', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 350), '(*) definition not equivalent in Riichi', fill="black", font=small_title_font)
    draw.line([(two_third_width + 16, 390), (width_px - 16, 390)], fill="black", width=1)
    
draw_2_fan()

def draw_misc():
    tier_position = (two_third_width + 16, 400)
    draw.text(tier_position, 'Change Seat', fill="black", font=title_font)
    
    draw.text((two_third_width + 16, 460), 'East, South: Move in Zigzags', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 500), 'West, North: Move in Circles', fill="black", font=small_title_font)
    
    draw.text((two_third_width + 16, 560), 'Winning Points', fill="black", font=title_font)
    draw.text((two_third_width + 16, 620), 'Win on Discard: \nEveryone pays 8, deal-in pays FANs more', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 700), 'Win on Self-Drawn: \nEveryone pays 8 + FANs', fill="black", font=small_title_font)
    
    draw.text((two_third_width + 16, 780), 'Winning Condition', fill="black", font=title_font)
    draw.text((two_third_width + 16, 840), 'Must have at least 8 FAN to win', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 870), 'Chombo: pay everyone 10 and keep playing', fill="black", font=small_title_font)
    
    draw.text((two_third_width + 16, 940), 'Two Kongs', fill="black", font=title_font)
    draw.text((two_third_width + 16, 1000), 'In MIL MCR rules, the value of 2 Kongs are different\nfrom EMA (which based on MCR \'06).', fill="black", font=small_title_font)
    draw.text((two_third_width + 300, 1080), 'Mod. \'98', fill="black", font=small_title_font)
    draw.text((two_third_width + 440, 1080), '\'06', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 1120), 'Two Melded', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 1160), 'Melded + Concealed', fill="black", font=small_title_font)
    draw.text((two_third_width + 16, 1200), 'Two Concealed', fill="black", font=small_title_font)
    draw.text((two_third_width + 340, 1120), '4', fill="black", font=small_title_font)
    draw.text((two_third_width + 450, 1120), '4', fill="black", font=small_title_font)
    draw.text((two_third_width + 340, 1160), '5', fill="black", font=small_title_font)
    draw.text((two_third_width + 450, 1160), '6', fill="black", font=small_title_font)
    draw.text((two_third_width + 340, 1200), '6', fill="black", font=small_title_font)
    draw.text((two_third_width + 450, 1200), '8', fill="black", font=small_title_font)
    
draw_misc()

# Draw vertical lines to separate the image into three parts
line_color = "black"
draw.line([(one_third_width, 0.2 * dpi), (one_third_width, height_px - (0.2 * dpi))], fill=line_color, width=1)
draw.line([(two_third_width, 0.2 * dpi), (two_third_width, height_px - (0.2 * dpi))], fill=line_color, width=1)

# Save the image
image.save("mcr_small_reference.png", dpi=(dpi, dpi))
