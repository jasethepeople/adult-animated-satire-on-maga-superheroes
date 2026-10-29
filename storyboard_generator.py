from PIL import Image, ImageDraw, ImageFont
import os

# Create directory for storyboard images
storyboard_dir = "/home/ubuntu/political_satire_project/storyboard_images"
os.makedirs(storyboard_dir, exist_ok=True)

# Define some constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
TITLE_COLOR = (50, 50, 150)
BORDER_COLOR = (100, 100, 100)

# Try to load a font, fall back to default if not available
try:
    title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    scene_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
    desc_font = ImageFont.truetype("DejaVuSans.ttf", 14)
except IOError:
    title_font = ImageFont.load_default()
    scene_font = ImageFont.load_default()
    desc_font = ImageFont.load_default()

# Key scenes to storyboard
storyboard_scenes = [
    {
        "title": "Scene 1: Mar-a-Lago Estate",
        "description": "Trump sits on his golden patio chair, his hair comically large and swooshing independently. He senses something is wrong with America.",
        "visual_elements": "Exaggerated Trump with oversized hair, Mar-a-Lago in background with subtle American flag motifs, phone showing economic alert"
    },
    {
        "title": "Scene 2: Department of Bureaucracy",
        "description": "The Bureaucrat (villain made of scrolling government forms) operates the Regulation Generator 5000, sending waves of red tape toward small businesses.",
        "visual_elements": "Massive gray building, villain with multiple arms stamping 'DENIED', machine pulsing with red tape flowing out windows"
    },
    {
        "title": "Scene 5: JFK's Ghost Appears",
        "description": "The ghostly form of JFK appears to Trump, glowing with red, white, and blue ethereal energy, showing holographic images of potential team members.",
        "visual_elements": "Spectral JFK with patriotic glow, holographic display showing Elon Musk, Tucker Carlson, and others, defeated Trump with bandages"
    },
    {
        "title": "Scene 7: Elon Musk Tech Battle",
        "description": "Elon's fingers move at impossible speeds across multiple keyboards. His eyes glow as he mentally connects to systems using Neural Link power.",
        "visual_elements": "Elongated Elon in futuristic superhero suit with 'X' emblem, screens showing The Silencer (villain made of ban notices), Trump in Commander-in-Chief costume"
    },
    {
        "title": "Scene 8: Tucker Carlson Recruitment",
        "description": "Tucker's expression is permanently confused with impossibly high eyebrows. His bow tie spins as he processes information about the Deep State.",
        "visual_elements": "Tucker with exaggerated confused expression, spinning bow tie, Trump and Elon in superhero outfits, Fox News studio setting"
    },
    {
        "title": "Scene 10: Team Assembly Montage",
        "description": "Montage showing recruitment of Bongino, Jones, Shroyer, and Gabbard, each demonstrating their unique powers and exaggerated features.",
        "visual_elements": "Split screen showing: Bongino with broadening shoulders, shirtless red-faced Jones, Shroyer with bullhorn, Gabbard with glowing white hair streak"
    },
    {
        "title": "Scene 12: Heroes vs. Villains Battle",
        "description": "Epic battle scene with each hero facing their villain counterpart around the Great Reset Initiator device.",
        "visual_elements": "Five villain characters, heroes using their powers (Trump's giant hands, Tucker's confusion ray, Elon's meme magic, etc.), massive device in center"
    },
    {
        "title": "Scene 13: Victory at Dawn",
        "description": "The American Heroes League stands triumphant on the steps of the Lincoln Memorial as small businesses reopen across America.",
        "visual_elements": "Team in heroic pose, sunrise over DC, JFK's ghost visible only to heroes, American flags waving, 'CLOSED' signs flipping to 'OPEN'"
    },
]

# Generate storyboard frames
for i, scene in enumerate(storyboard_scenes):
    # Create a new image
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([(10, 10), (WIDTH-10, HEIGHT-10)], outline=BORDER_COLOR, width=2)
    
    # Draw scene number and title
    draw.text((20, 20), f"Frame {i+1}: {scene['title']}", fill=TITLE_COLOR, font=title_font)
    
    # Draw separator line
    draw.line([(20, 60), (WIDTH-20, 60)], fill=BORDER_COLOR, width=2)
    
    # Draw description
    desc_text = f"Description: {scene['description']}"
    # Simple text wrapping
    words = desc_text.split()
    lines = []
    line = []
    for word in words:
        line.append(word)
        if len(' '.join(line)) > 70:  # Approximate character limit per line
            lines.append(' '.join(line[:-1]))
            line = [word]
    if line:
        lines.append(' '.join(line))
    
    for j, line in enumerate(lines):
        draw.text((20, 80 + j*20), line, fill=TEXT_COLOR, font=desc_font)
    
    # Draw visual elements section
    visual_y = 80 + len(lines)*20 + 20
    draw.text((20, visual_y), "Visual Elements:", fill=TITLE_COLOR, font=scene_font)
    
    # Visual elements text with wrapping
    visual_text = scene["visual_elements"]
    words = visual_text.split()
    lines = []
    line = []
    for word in words:
        line.append(word)
        if len(' '.join(line)) > 70:
            lines.append(' '.join(line[:-1]))
            line = [word]
    if line:
        lines.append(' '.join(line))
    
    for j, line in enumerate(lines):
        draw.text((20, visual_y + 30 + j*20), line, fill=TEXT_COLOR, font=desc_font)
    
    # Draw a placeholder for the actual storyboard illustration
    illustration_top = visual_y + 30 + len(lines)*20 + 20
    illustration_height = HEIGHT - illustration_top - 20
    if illustration_height > 100:  # Only if there's enough space
        draw.rectangle([(20, illustration_top), (WIDTH-20, HEIGHT-20)], outline=BORDER_COLOR)
        draw.line([(20, illustration_top), (WIDTH-20, HEIGHT-20)], fill=BORDER_COLOR)
        draw.line([(WIDTH-20, illustration_top), (20, HEIGHT-20)], fill=BORDER_COLOR)
        draw.text((WIDTH//2-100, illustration_top + illustration_height//2-10), 
                 "Illustration Placeholder", fill=TEXT_COLOR, font=desc_font)
    
    # Save the image
    filename = f"{storyboard_dir}/frame_{i+1:02d}_{scene['title'].replace(':', '').replace(' ', '_')}.png"
    img.save(filename)
    print(f"Created {filename}")

# Create a storyboard document with descriptions
with open("/home/ubuntu/political_satire_project/visual_storyboard.md", "w") as f:
    f.write("# Visual Storyboard for 'American Heroes League' Pilot Episode\n\n")
    f.write("## Animation Style Guide\n\n")
    f.write("### Overall Style\n")
    f.write("- **Animation Type**: 2D traditional animation with digital enhancements\n")
    f.write("- **Visual Reference**: Similar to FreedomToons but with more detailed backgrounds and fluid movement\n")
    f.write("- **Color Palette**: Bright, saturated colors with strong contrast between heroes (vibrant, patriotic) and villains (drab, bureaucratic)\n\n")
    
    f.write("### Character Design Principles\n")
    f.write("- **Heroes**: Exaggerated physical features that emphasize their personalities and powers\n")
    f.write("- **Villains**: Abstract, conceptual designs that embody their bureaucratic/authoritarian nature\n")
    f.write("- **Proportions**: Cartoonishly distorted with emphasis on recognizable features (Trump's hair, Elon's elongated body, etc.)\n")
    f.write("- **Expressions**: Highly exaggerated facial expressions that change dramatically for comedic effect\n\n")
    
    f.write("### Animation Techniques\n")
    f.write("- **Movement**: Snappy, energetic movement for heroes; rigid, mechanical movement for villains\n")
    f.write("- **Special Effects**: Bright, comic-book style effects for superpowers (speed lines, impact stars, etc.)\n")
    f.write("- **Scene Transitions**: Dynamic wipes and transitions with patriotic motifs\n")
    f.write("- **Background Style**: Simplified but recognizable real-world locations with satirical elements\n\n")
    
    f.write("## Key Storyboard Frames\n\n")
    
    for i, scene in enumerate(storyboard_scenes):
        f.write(f"### Frame {i+1}: {scene['title']}\n\n")
        f.write(f"**Description**: {scene['description']}\n\n")
        f.write(f"**Visual Elements**: {scene['visual_elements']}\n\n")
        f.write(f"**Storyboard Image**: [View Frame {i+1}](./storyboard_images/frame_{i+1:02d}_{scene['title'].replace(':', '').replace(' ', '_')}.png)\n\n")
        f.write("---\n\n")
    
    f.write("## Animation Notes\n\n")
    f.write("### Character Movement Specifics\n")
    f.write("- **Trump**: Hair moves independently from body, hands grow and shrink dramatically\n")
    f.write("- **Elon**: Body stretches and contorts like rubber, hair morphs between styles\n")
    f.write("- **Tucker**: Head tilts at impossible angles, eyebrows arch beyond his hairline\n")
    f.write("- **Alex Jones**: Face cycles through color spectrum from pink to deep red when excited\n")
    f.write("- **JFK's Ghost**: Floats with ethereal trail, occasionally phases through solid objects\n\n")
    
    f.write("### Scene Transitions\n")
    f.write("- Use star-wipe transitions with red, white, and blue stars\n")
    f.write("- For location changes, employ a flying eagle transition\n")
    f.write("- For time jumps, show a clock with hands spinning rapidly\n\n")
    
    f.write("### Sound Design Notes\n")
    f.write("- Patriotic music swells during hero moments\n")
    f.write("- Bureaucratic, monotonous tones for villain scenes\n")
    f.write("- Exaggerated sound effects for power usage (giant hand growth, confusion ray, etc.)\n")
    f.write("- Each character should have signature sound effects that accompany their movements\n\n")

print("Storyboard generation complete!")
