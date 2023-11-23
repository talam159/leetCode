
# Define the size and color of the image
image_size = (800, 800)
background_color = (255, 255, 255)  # white

# Create a new image with the specified size and background color
image = Image.new("RGB", image_size, background_color)
draw = ImageDraw.Draw(image)

# Define the position and size of the circular area
circle_position = (image_size[0] // 2, image_size[1] // 2)
circle_radius = min(image_size) // 2 - 50

# Draw the circular area
draw.ellipse(
    [
        (circle_position[0] - circle_radius, circle_position[1] - circle_radius),
        (circle_position[0] + circle_radius, circle_position[1] + circle_radius),
    ],
    outline=(0, 0, 0),  # black
)

# Define the goals and their positions
goals = [
    "No Poverty", "Zero Hunger", "Good Health and Well-being", "Quality Education",
    "Gender Equality", "Clean Water and Sanitation", "Affordable and Clean Energy",
    "Decent Work and Economic Growth", "Industry, Innovation and Infrastructure",
    "Reduced Inequality", "Sustainable Cities and Communities", "Responsible Consumption and Production",
    "Climate Action", "Life Below Water", "Life on Land", "Peace and Justice Strong Institutions",
    "Partnerships to achieve the Goal"
]
num_goals = len(goals)
angle = 360 // num_goals

# Define the font and its size
font = ImageFont.truetype("arial.ttf", 18)

# Draw the goals around the circle
for i in range(num_goals):
    goal_text = goals[i]
    text_width, text_height = draw.textsize(goal_text, font=font)
    angle_deg = i * angle - 90  # Adjust the starting angle to place the first goal at the top
    angle_rad = angle_deg * 3.14159 / 180.0
    x = int(circle_position[0] + circle_radius * 0.8 * (1 + 0.15 * (i % 2)) * math.cos(angle_rad)) - text_width // 2
    y = int(circle_position[1] + circle_radius * 0.8 * (1 + 0.15 * (i % 2)) * math.sin(angle_rad)) - text_height // 2
    draw.text((x, y), goal_text, font=font, fill=(0, 0, 0))  # black

# Define the position and size of the pillars
pillar_position = circle_position
pillar_width = 30
pillar_height = 200
pillar_distance = circle_radius - pillar_height // 2 - 50

# Define the pillar names and colors
pillar_names = ["Smart Citizen", "Smart Government", "Smart Society", "Smart Economy"]
pillar_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Draw the pillars
for i in range(4):
    pillar_x = pillar_position[0] - pillar_width // 2
    pillar_y = pillar_position[1] - pillar_distance + pillar_height // 2
    pillar_rect = [
        (pillar_x, pillar_y - pillar_height),
        (pillar_x + pillar_width, pillar_y)
    ]
    draw.rectangle(pillar_rect, fill=pillar_colors[i])

    # Draw the pillar name below the pillar
    pillar_name = pillar_names[i]
    text_width, text_height = draw.textsize(pillar_name, font=font)
    x = pillar_x + pillar_width // 2 - text_width // 2
    y = pillar_y + 10
    draw.text((x, y), pillar_name, font=font, fill=(0, 0, 0))  # black

# Save the image
image.save("sdg_image.png")