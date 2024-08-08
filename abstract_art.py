import numpy as np
import matplotlib.pyplot as plt

# Define function to generate abstract art
def generate_abstract_art(color_palette, style_preference, num_iterations=100):
    # Initialize art canvas
    generated_art = np.zeros((256, 256, 3))

    # Map color palette to RGB values
    color_map = {
        'blue': [0, 0, 1],
        'green': [0, 1, 0],
        'purple': [0.5, 0, 0.5]
    }

    # Artificially generate abstract art (for demonstration purposes)
    for _ in range(num_iterations):
        # Blend colors
        for color in color_palette:
            color_rgb = color_map[color]
            generated_art += np.random.rand(256, 256, 3) * color_rgb

        # Apply geometric shapes
        if style_preference == 'geometric':
            for _ in range(5):  # Add random geometric shapes
                shape = np.random.choice(['circle', 'rectangle'])
                if shape == 'circle':
                    rr, cc = np.ogrid[:256, :256]
                    center = (np.random.randint(256), np.random.randint(256))
                    radius = np.random.randint(10, 50)
                    mask = (rr - center[0]) ** 2 + (cc - center[1]) ** 2 <= radius ** 2
                    generated_art[mask] = np.random.rand(3)
                elif shape == 'rectangle':
                    start_x, start_y = np.random.randint(256, size=2)
                    width, height = np.random.randint(10, 50, size=2)
                    end_x = min(start_x + width, 255)
                    end_y = min(start_y + height, 255)
                    generated_art[start_x:end_x, start_y:end_y] = np.random.rand(3)

        # Add noise
        noise = np.random.rand(256, 256, 3) * 0.2
        generated_art += noise

    # Normalize the art
    generated_art = np.clip(generated_art, 0, 1)

    return generated_art

# Define user preferences
color_palette = ['blue', 'green', 'purple']
style_preference = 'geometric'

# Generate abstract art based on user preferences
generated_art = generate_abstract_art(color_palette, style_preference)

# Display generated art
plt.imshow(generated_art)
plt.axis('off')
plt.title('Generated Abstract Art')
plt.show()
