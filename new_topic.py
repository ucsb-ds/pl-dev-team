#!/usr/bin/env python3

from pathlib import Path
import sys


def index_md_file(topic):
    return f"""---
parent: Topics
layout: default
title: "{topic}"
description:  "TODO: Add description for {topic}"
---

# {{page.title}} - {{page.description}}
    """
    

if __name__ == "__main__":
    
    # Take topic from command line argument if it exists
    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = input("Enter the new topic name: ")

    # create a new directory f"topics/topic" if it does not already exist
    
    safe_name = topic.strip()
    if not safe_name:
        print("No topic provided.")
        sys.exit(1)

    topic_dir = Path("topics") / safe_name
    topic_dir.mkdir(parents=True, exist_ok=True)

    # Create index.md inside topic_dir
    index_file = topic_dir / "index.md"
    index_file.write_text(index_md_file(safe_name))
    print(f"Created new topic at {topic_dir}")