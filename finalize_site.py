
import glob

def update_file(filepath):
    print(f"Finalizing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Link "Read Memory" to memory.html
    # Some buttons might be "Read Memory" or plain icons.
    # We look for the service-text buttons.
    content = content.replace('href="#!">Read Memory', 'href="memory.html">Read Memory')
    content = content.replace('href="#!">Read More', 'href="memory.html">Read My Letter')

    # Update Image extensions (jpg -> png) for the replacements we just made
    content = content.replace('img/team-1.jpg', 'img/team-1.png')
    content = content.replace('img/team-2.jpg', 'img/team-2.png')
    content = content.replace('img/testimonial-1.jpg', 'img/testimonial-1.png')
    content = content.replace('img/testimonial-2.jpg', 'img/testimonial-2.png')
    content = content.replace('img/testimonial-3.jpg', 'img/testimonial-3.png')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

html_files = glob.glob("*.html")
for file in html_files:
    update_file(file)

print("Site finalized.")

import glob

def update_file(filepath):
    print(f"Finalizing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Link "Read Memory" to memory.html
    # Some buttons might be "Read Memory" or plain icons.
    # We look for the service-text buttons.
    content = content.replace('href="#!">Read Memory', 'href="memory.html">Read Memory')
    content = content.replace('href="#!">Read More', 'href="memory.html">Read My Letter')

    # Update Image extensions (jpg -> png) for the replacements we just made
    content = content.replace('img/team-1.jpg', 'img/team-1.png')
    content = content.replace('img/team-2.jpg', 'img/team-2.png')
    content = content.replace('img/testimonial-1.jpg', 'img/testimonial-1.png')
    content = content.replace('img/testimonial-2.jpg', 'img/testimonial-2.png')
    content = content.replace('img/testimonial-3.jpg', 'img/testimonial-3.png')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

html_files = glob.glob("*.html")
for file in html_files:
    update_file(file)

print("Site finalized.")

