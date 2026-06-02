#!/usr/bin/env python3
"""
Assemble CloudInvoke animated short from storyboards + UI frames.
Output: 1920x1080 @ 24fps, ~150 seconds.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
SB = ROOT / "storyboards"
FR = ROOT / "frames" / "ui"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
FPS = 24

# (image_path, duration_seconds, zoom_start, zoom_end, pan_x drift)
SCENES = [
    (SB / "scene01_accident.png", 18, 1.0, 1.12, 0.02),
    (SB / "scene02_witness_alarm.png", 14, 1.05, 1.18, -0.01),
    (SB / "scene03_phone_photo.png", 10, 1.0, 1.15, 0.0),
    (SB / "scene04_blurry_plate.png", 10, 1.08, 1.22, 0.0),
    (SB / "scene05_police_station.png", 13, 1.0, 1.1, 0.015),
    (SB / "scene06_officers_frustrated.png", 17, 1.05, 1.2, 0.0),
    (SB / "title_cloudinvoke.png", 8, 1.0, 1.05, 0.0),
    (SB / "scene07_cloudinvoke_intro.png", 7, 1.0, 1.08, 0.0),
    ("UI_SEQUENCE", 30, 1.0, 1.0, 0.0),  # UI frames
    (SB / "scene08_clear_plate.png", 10, 1.0, 1.25, 0.0),
    (SB / "scene09_officers_success.png", 13, 1.0, 1.12, 0.01),
    (SB / "scene10_resolution.png", 10, 1.0, 1.1, 0.02),
    (SB / "end_card.png", 7, 1.0, 1.06, 0.0),
]


def run(cmd):
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)


def kenburns_clip(img: Path, duration: float, z0: float, z1: float, pan: float, out: Path):
    frames = int(duration * FPS)
    # zoompan: smooth zoom + slight pan
    z_expr = f"{z0}+({z1}-{z0})*on/{frames}"
    x_expr = f"iw/2-(iw/zoom/2)+{pan}*iw*on/{frames}"
    y_expr = "ih/2-(ih/zoom/2)"
    vf = (
        f"scale=1920:1080:force_original_aspect_ratio=increase,"
        f"crop=1920:1080,"
        f"zoompan=z='{z_expr}':x='{x_expr}':y='{y_expr}':"
        f"d={frames}:s=1920x1080:fps={FPS},format=yuv420p"
    )
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(img),
        "-vf", vf, "-t", str(duration), "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(out),
    ])


def ui_clip(out: Path, duration: float = 30):
    pattern = str(FR / "ui_%04d.png")
    run([
        "ffmpeg", "-y", "-framerate", str(FPS), "-i", pattern,
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        "-t", str(duration), "-c:v", "libx264", "-pix_fmt", "yuv420p",
        str(out),
    ])


def add_audio_bed(video: Path, audio_wav: Path, final: Path):
    run([
        "ffmpeg", "-y", "-i", str(video), "-i", str(audio_wav),
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", str(final),
    ])


def main():
    clips_dir = OUT / "clips"
    clips_dir.mkdir(exist_ok=True)
    list_file = OUT / "concat.txt"
    clip_paths = []

    for idx, scene in enumerate(SCENES):
        out_clip = clips_dir / f"clip_{idx:02d}.mp4"
        if scene[0] == "UI_SEQUENCE":
            ui_clip(out_clip, scene[1])
        else:
            img, dur, z0, z1, pan = scene
            if not Path(img).exists():
                raise FileNotFoundError(img)
            kenburns_clip(Path(img), dur, z0, z1, pan, out_clip)
        clip_paths.append(out_clip)

    with list_file.open("w") as f:
        for p in clip_paths:
            f.write(f"file '{p.resolve()}'\n")

    silent = OUT / "cloudinvoke_short_silent.mp4"
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", str(silent),
    ])

    audio = ROOT / "audio" / "soundtrack.wav"
    final = OUT / "CloudInvoke_Short_Film_1080p24.mp4"
    if audio.exists():
        add_audio_bed(silent, audio, final)
    else:
        final = silent
        print("No soundtrack.wav — silent master written.")

    # Demo version with faststart for web
    demo = OUT / "CloudInvoke_Short_Film_1080p24_demo.mp4"
    run(["ffmpeg", "-y", "-i", str(final), "-movflags", "+faststart", "-c", "copy", str(demo)])

    probe = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(final)],
        text=True,
    ).strip()
    print(f"Done: {final} ({float(probe):.1f}s)")


if __name__ == "__main__":
    main()
