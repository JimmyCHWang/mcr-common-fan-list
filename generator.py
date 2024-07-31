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
    main_title = "MCR Common Fan List"
    subtitle = "For Riichi Players v0.0.1        @JCarlson"
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

def draw_tier_1():
    tier_position = (16, 200)
    draw.text(tier_position, 'Tier 1', fill="black", font=title_font)
    
    def draw_title_hand(y, title, subtitle, hand, point):
        draw.text((16, y), title, fill="black", font=subtitle_font)
        draw.text((300, y+8), subtitle, fill="black", font=italic_small_font)
        draw.text((one_third_width - 64, y - 8), str(point), align='right', fill="black", font=title_font)
        draw_hand(image, 16, y+60, hand)

    hands = [
        ('Mixed Shifted Chows', '345m456p567s', '', 6),
        ('Mixed Triple Chow', '567m567p567s', 'sanshoku doujun', 8),
        ('Mixed Straight', '123m456p789s', '', 8),
        ('Pure Straight', '123456789p', 'ittsu', 16),
        ('All Types', '678m234p444s33w222d', '', 6),
        ('Half Flush', '111345789s22w333d', 'honitsu', 6),
    ]
    for y_idx in range(6):
        y = 260 + y_idx * 160
        title, hand, subtitle, point = hands[y_idx]
        draw_title_hand(y, title, subtitle, hand, point)
    
draw_tier_1()


def draw_tier_2():
    tier_position = (one_third_width + 16, 16)
    draw.text(tier_position, 'Tier 2', fill="black", font=title_font)
    
    def draw_title_hand(y, title, subtitle, hand, point):
        draw.text((one_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((one_third_width + 316, y+8), subtitle, fill="black", font=italic_small_font)
        draw.text((two_third_width - 64, y - 8), str(point), align='right', fill="black", font=title_font)
        draw_hand(image, one_third_width + 16, y+60, hand)
        
    def draw_text(y, title, subtitle, text, point):
        draw.text((one_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((one_third_width + 316, y+8), subtitle, fill="black", font=italic_small_font)
        draw.text((one_third_width + 16, y+60), text, fill="black", font=small_title_font)
        draw.text((two_third_width - 64, y - 8), str(point), align='right', fill="black", font=title_font)

    hands = [
        ('Pure Shifted Chows', '123345567p', '', 16),
        ('All Pungs', '333p444s111888m22w', 'toitoi', 6),
        ('Seven Pairs', '3355m335588s55p44w', 'chiitoi', 24),
        ('Outside Hand', '123p111d999m789999p', 'chanta', 4),
        ('Full Flush', '12333345667899s', 'chinitsu', 24),
    ]
    for y_idx in range(5):
        y = 80 + y_idx * 160
        title, hand, subtitle, point = hands[y_idx]
        draw_title_hand(y, title, subtitle, hand, point)
        
    texts = [
        ('Fully Concealed Hand', 'Win by self-drawn without open calls. \nNot to be combined with closed-guaranteed Fans, \nsuch as Seven Pairs, Honors and Knitted Tiles.', 'menzen tsumo', 4),
        ('Last Tile', 'Win on a tile that the other 3 are appear on the table. \nAppear means in the river or someone\'s calls, \nwhich must be known information for all 4 players.', '', 4)
    ]
    
    draw_text(880, texts[0][0], texts[0][2], texts[0][1], texts[0][3])
    draw_text(1080, texts[1][0], texts[1][2], texts[1][1], texts[0][3])
    
draw_tier_2()

def draw_tier_3():
    tier_position = (two_third_width + 16, 16)
    draw.text(tier_position, 'Tier 3', fill="black", font=title_font)
    
    def draw_title_hand(y, title, subtitle, hand, point):
        draw.text((two_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((two_third_width + 16, y+110), subtitle, fill="black", font=italic_small_font)
        draw.text((width_px - 64, y - 8), str(point), align='right', fill="black", font=title_font)
        draw_hand(image, two_third_width + 16, y+50, hand)
        
    def draw_text(y, title, subtitle, text, point):
        draw.text((two_third_width + 16, y), title, fill="black", font=subtitle_font)
        draw.text((two_third_width + 316, y+8), subtitle, fill="black", font=italic_small_font)
        draw.text((two_third_width + 16, y+60), text, fill="black", font=small_title_font)
        draw.text((width_px - 64, y - 8), str(point), align='right', fill="black", font=title_font)

    hands = [
        ('Lower Four', '223344m12333s234p', '', 12),
        ('Upper Four', '678999p789m66777s', '', 12),
        ('Knitted Straight', '147s258p369m', 'Counts as 3 chows or part of LHAKT (see below)', 12),
        ('Lesser Honors And Knitted Tiles', '147m369s28p1234w23d', '', 12),
        ('Greater Honors And Knitted Tiles', '14m25s369p1234w123d', '', 24),
        ('Three Concealed Pungs', '1566667m222s888p1m', '', 16),
        ('Two Dragons Pungs', '222333d', '', 6),
        ('Chicken Hand', '888p789m123s45p33d3p', 'Without any Fan except flowers, \nmust be open and win from discard.', 8)
    ]
    for y_idx in range(8):
        y = 80 + y_idx * 145
        title, hand, subtitle, point = hands[y_idx]
        draw_title_hand(y, title, subtitle, hand, point)
        
    
draw_tier_3()

# Draw vertical lines to separate the image into three parts
line_color = "black"
draw.line([(one_third_width, 0.2 * dpi), (one_third_width, height_px - (0.2 * dpi))], fill=line_color, width=1)
draw.line([(two_third_width, 0.2 * dpi), (two_third_width, height_px - (0.2 * dpi))], fill=line_color, width=1)

# Save the image
image.save("mcr_reference.png", dpi=(dpi, dpi))
