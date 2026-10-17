import os
import requests
from PIL import Image
from io import BytesIO
import colorsys

os.makedirs("data/images", exist_ok=True)

# (Keep your previous download code if images are already downloaded)
# Skip re-downloading if folder already has images

def rgb_to_name(rgb):
    r, g, b = [x/255.0 for x in rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    if v < 0.2:
        return "Black"
    if s < 0.15 and v > 0.8:
        return "White"
    if s < 0.15:
        return "Gray"
    if h < 0.05 or h > 0.95:
        return "Red"
    if h < 0.12:
        return "Orange"
    if h < 0.18:
        return "Yellow"
    if h < 0.45:
        return "Green"
    if h < 0.65:
        return "Blue"
    if h < 0.85:
        return "Purple"
    return "Pink"

print("=== Image Analysis ===")
results = []

for filename in sorted(os.listdir("data/images")):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join("data/images", filename)
        img = Image.open(path).convert("RGB")
        small = img.resize((50, 50))
        
        # Dominant color
        colors = small.getcolors(2500)
        dominant = sorted(colors, key=lambda x: x[0], reverse=True)[0][1]
        color_name = rgb_to_name(dominant)
        
        # Average brightness
        brightness = sum(dominant) / 3
        
        results.append({
            "image": filename,
            "color_name": color_name,
            "rgb": dominant,
            "brightness": round(brightness, 1)
        })

# Print results
for r in results[:15]:  # show first 15
    print(f"{r['image']}: {r['color_name']} | RGB{r['rgb']} | Brightness {r['brightness']}")

print(f"\nTotal images analyzed: {len(results)}")

# Summary
from collections import Counter
color_counts = Counter([r["color_name"] for r in results])
print("\n=== Color Distribution ===")
for color, count in color_counts.most_common():
    print(f"{color}: {count}")