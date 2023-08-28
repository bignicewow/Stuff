import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed([^"]+)"[^>]*>'
    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        youtube_link = f"https://youtu.be/{video_id}"
        return youtube_link
    else:
        return None

if __name__ == "__main__":
    main()