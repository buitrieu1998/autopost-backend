import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


def bulk_edit_videos(input_dir: str, output_dir: str, overlay_text: str):
    """Add overlay text to all mp4 videos in a directory."""
    os.makedirs(output_dir, exist_ok=True)
    for name in os.listdir(input_dir):
        if name.lower().endswith(".mp4"):
            input_path = os.path.join(input_dir, name)
            output_path = os.path.join(output_dir, f"edited_{name}")
            clip = VideoFileClip(input_path)
            txt = TextClip(overlay_text, fontsize=24, color="white")
            txt = txt.set_position(("center", "bottom")).set_duration(clip.duration)
            video = CompositeVideoClip([clip, txt])
            video.write_videofile(output_path, codec="libx264")
