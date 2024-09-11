from reddit_scraper import scrape_posts
from script_generator import ScriptGenerator
from stitch_video import generate_base_video
import logging
from videoGen import generate_srt, generate_video

logging.basicConfig(level=logging.INFO)

script_gen = ScriptGenerator()


def main():
    post_count = 5

    logging.info(f"Scraping {post_count} posts from reddit...")
    reddit_posts = scrape_posts(5)
    logging.info(f"Scraped {len(reddit_posts)} posts from reddit.")

    logging.info("Generating script from reddit post...")
    script, audio_path = script_gen.generate_script(reddit_posts[2])
    logging.info("Generated script from reddit post.")

    logging.info("Generating base video...")
    stitched_video_path = generate_base_video("base_videos/minecraft_parkour_a.mp4", audio_path, 60)
    logging.info(f"Generated base video at {stitched_video_path}")

    logging.info("Generating SRT file...")
    generate_srt(script, stitched_video_path, "/subs/output.srt")

    # generate video
    logging.info("Generating video...")
    generate_video("/subs/output.srt", stitched_video_path, "/final_videos/output.mp4")

    # overlay text on top of video
    # upload to instagram reels



if __name__ == "__main__":
    main()
