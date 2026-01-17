
import re
import glob
import os

def update_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # --- GLOBAL REPLACEMENTS ---
    # Brand & Title
    content = content.replace("Poseify - Modeling Agency Website Template", "Our Love Story - Forever & Always")
    content = content.replace("Modeling Agency Website Template", "Our Love Story")
    content = content.replace("fa-face-smile", "fa-heart")
    content = content.replace(">Poseify</h2>", ">Our Story</h2>")
    content = content.replace("Poseify", "Our Love") # Footer/General fallback
    
    # Navigation
    content = content.replace(">About</a>", ">Our Story</a>")
    content = content.replace(">Services</a>", ">Moments</a>")
    content = content.replace(">Our Models</a>", ">Photos</a>")
    content = content.replace(">Testimonial</a>", ">Love Letters</a>")
    content = content.replace(">Pages</a>", ">Gallery</a>")
    
    # Footer
    content = content.replace("Your Site Name", "Our Love Story")
    content = content.replace("Modeling Agency", "Our Journey") 

    # --- PAGE SPECIFIC REPLACEMENTS ---
    filename = os.path.basename(filepath)

    if filename == "about.html":
        content = content.replace("About Our Agency", "How We Met")
        content = content.replace("History", "Our Story")
        content = re.sub(r'<p class="mb-4">.*?</p>', '<p class="mb-4">It was destiny that brought us together. Every day since has been a beautiful chapter in our fairy tale.</p>', content, flags=re.DOTALL)
        content = content.replace("Become A Model", "I Love You")
        content = content.replace("Schedule Casting", "Forever & Always")
        content = content.replace("img/about.png", "img/about.png") # Ensure it uses the new heart image if not already

    elif filename == "service.html":
        content = content.replace("Services", "Memories")
        content = content.replace("How We Help You", "Things We Love")
        content = content.replace("Fashion Shows", "Our First Date")
        content = content.replace("Corporate Events", "Our Adventures")
        content = content.replace("Commercial Photo Shots", "Special Occasions")
        content = content.replace("Professional Modeling", "Future Dreams")
        content = content.replace("Read More", "Read Memory")
    
    elif filename == "team.html":
        content = content.replace("Models", "Gallery")
        content = content.replace("Meet Our Models", "Our Photo Gallery")
        content = content.replace("Full Name", "Memory Name")
        content = content.replace("Designation", "Date")

    elif filename == "testimonial.html":
        content = content.replace("Testimonial", "Love Notes")
        content = content.replace("Our Clients Say", "Messages from Us")
        content = content.replace("Client Name", "From Me")
        content = content.replace("Profession", "To You")
    
    elif filename == "contact.html":
        content = content.replace("Contact Us", "Write to Me")
        content = content.replace("Have Any Query?", "Send a Love Letter")
        content = content.replace("Send Message", "Send Love")
    
    elif filename == "404.html":
        content = content.replace("Page Not Found", "Lost in Love?")
        content = content.replace("We’re sorry, the page you have looked for does not exist in our website!", "Don't worry, even if we get lost, we will always find our way back to each other.")
        content = content.replace("Go Back To Home", "Return to Our Story")


    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Get all HTML files
html_files = glob.glob("*.html")

for file in html_files:
    # Skip index.html as it is already substantially updated, but running global replacements again is harmless/safe 
    # to ensure consistency if missed.
    update_file(file)

print("All files updated successfully.")
