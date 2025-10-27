import os
import re
from bs4 import BeautifulSoup
import html2text
import datetime
import sys

# Configuration
POSTS_DIR = '_posts'
SOURCE_DIR = '.'
EXCLUDED_DIRS = ['_posts', '_layouts', '_includes', 'css', 'js', 'wp-content', 'wp-includes', '.git']

def get_post_dirs():
    """Get a list of directories that contain blog posts."""
    post_dirs = []
    for dirpath, dirnames, filenames in os.walk(SOURCE_DIR, topdown=True):
        # Exclude certain directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]

        if 'index.html' in filenames:
            # A simple check for anything that looks like a post slug.
            # This is not perfect but will capture most posts and pages.
            if len(dirpath) > 2: # not root
                post_dirs.append(dirpath)

    return sorted(post_dirs)

def convert_post(post_dir):
    """Convert a single post from HTML to Markdown."""
    html_path = os.path.join(post_dir, 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Extract title
    title_tag = soup.find('h1')
    if not title_tag:
        print(f"SKIPPING: No h1 title found in {html_path}")
        return
    title = title_tag.get_text()

    # Extract date from meta tag
    date_meta = soup.find('meta', property='article:published_time')
    if date_meta:
        date_str = date_meta['content']
        date_obj = datetime.datetime.fromisoformat(date_str)
        date = date_obj.strftime('%Y-%m-%d')
    else:
        # Fallback for pages that are not posts
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(f"WARNING: No date found for {html_path}. Using today's date.")


    # Extract content
    content_div = soup.find('div', class_='post-entry')
    if not content_div:
        print(f"SKIPPING: No 'post-entry' div found in {html_path}")
        return

    content_html = content_div.decode_contents()

    # Convert content to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    content_md = h.handle(content_html)

    # Create Jekyll front matter
    front_matter = f"""---
layout: post
title: "{title}"
date: {date}
---
"""

    # Create the new filename
    slug = os.path.basename(post_dir)
    md_filename = f'{date}-{slug}.md'
    md_filepath = os.path.join(POSTS_DIR, md_filename)

    # Write the new Markdown file
    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter + content_md)

    print(f"Converted {post_dir} to {md_filepath}")


if __name__ == '__main__':
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)

    post_dirs = get_post_dirs()

    BATCH_SIZE = 50

    try:
        BATCH_NUM = int(sys.argv[1])
    except (IndexError, ValueError):
        BATCH_NUM = 1

    start_index = (BATCH_NUM - 1) * BATCH_SIZE
    end_index = start_index + BATCH_SIZE

    batch_dirs = post_dirs[start_index:end_index]

    print(f"Processing batch {BATCH_NUM} ({len(batch_dirs)} posts)")

    for post_dir in batch_dirs:
        convert_post(post_dir)
