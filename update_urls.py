import os
import re

POSTS_DIR = '_posts'

def update_image_urls():
    """Update image URLs in all posts to be relative."""
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, 'r+') as f:
                content = f.read()
                # Replace the old URL with the new one.
                # This regex is designed to be flexible and catch all variations of the old URL.
                new_content = re.sub(r'https?://(?:i\d\.)?wp\.com/[^/]+/(?:wp-content/)?uploads', '/wp-content/uploads', content)
                new_content = re.sub(r'https?://(?:i\d\.)?derekchristensen\.com/(?:wp-content/)?uploads', '/wp-content/uploads', new_content)

                f.seek(0)
                f.write(new_content)
                f.truncate()

if __name__ == '__main__':
    update_image_urls()
