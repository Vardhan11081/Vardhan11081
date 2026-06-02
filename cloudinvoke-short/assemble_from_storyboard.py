#!/usr/bin/env python3
"""
Assemble CloudInvoke short from /workspace/storyboard user assets.
Uses sample scene 1-4.mp4 clips for character motion; Ken Burns on remaining stills.
Output: 1920x1080 @ 24fps with crossfades and soundtrack.
"""
import subprocess
from pathlib import Path

STORYBOARD = Path("/workspace/storyboard")
ROOT = Path(__file__).parent
OUT = ROOT / "output"
CLIPS = OUT / "storyboard_clips"
OUT.mkdir(exist_ok=True)
CLIPS.mkdir(exist_ok=True)
FPS = 24
XFADE = 0.6  # seconds crossfade between segments


def run(cmd):
    print(" ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True)


def normalize_video(src: Path, dst: Path):
    """Scale/pad reference clip to 1080p24."""
    vf = (
        "scale=1920:1080:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x0a1428,"
        "fps=24,format=yuv420p"
    )
    run([
        "ffmpeg", "-y", "-i", str(src), "-vf", vf,
        "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
        "-an", str(dst),
    ])


def kenburns_still(img: Path, duration: float, dst: Path, z0=1.0, z1=1.18, pan=0.018):
    frames = max(1, int(duration * FPS))
    z_expr = f"{z0}+({z1}-{z0})*on/{frames}"
    x_expr = f"iw/2-(iw/zoom/2)+{pan}*iw*on/{frames}"
    y_expr = "ih/2-(ih/zoom/2)"
    vf = (
        f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
        f"zoompan=z='{z_expr}':x='{x_expr}':y='{y_expr}':"
        f"d={frames}:s=1920x1080:fps={FPS},format=yuv420p"
    )
    run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(img),
        "-vf", vf, "-t", str(duration),
        "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
        str(dst),
    ])


def xfade_concat(segments: list[Path], out: Path):
    """Concatenate with crossfade using xfade filter chain."""
    if len(segments) == 1:
        run(["ffmpeg", "-y", "-i", str(segments[0]), "-c", "copy", str(out)])
        return

    # Build filter_complex for sequential crossfades
    inputs = []
    for i, seg in enumerate(segments):
        inputs.extend(["-i", str(seg)])

    # Get durations
    durs = []
    for seg in segments:
        p = subprocess.check_output(
            [
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", str(seg),
            ],
            text=True,
        ).strip()
        durs.append(float(p))

    filters = []
    vprev = "[0:v]"
    offset = durs[0] - XFADE
    for i in range(1, len(segments)):
        vout = f"[v{i}]" if i < len(segments) - 1 else "[vout]"
        filters.append(
            f"{vprev}[{i}:v]xfade=transition=fade:duration={XFADE}:offset={offset:.3f}{vout}"
        )
        vprev = vout
        if i < len(segments) - 1:
            offset += durs[i] - XFADE

    fc = ";".join(filters)
    cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", fc, "-map", "[vout]",
           "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(out)]
    run(cmd)


def mux_audio(video: Path, audio: Path, out: Path):
    dur_v = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(video)], text=True))
    dur_a = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(audio)], text=True))
    run([
        "ffmpeg", "-y", "-i", str(video), "-i", str(audio),
        "-map", "0:v", "-map", "1:a",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-t", str(min(dur_v, dur_a)), str(out),
    ])


def main():
    # Scene order: reference videos 1-4, then stills 5-12
    video_refs = [
        STORYBOARD / "scene 1.mp4",
        STORYBOARD / "scene 2.mp4",
        STORYBOARD / "scene 3.mp4",
        STORYBOARD / "scene 4.mp4",
    ]
    stills = [
        (STORYBOARD / "scene 5.png", 14),
        (STORYBOARD / "scene 6.png", 12),
        (STORYBOARD / "scene 7.png", 16),
        (STORYBOARD / "scene 8.png", 14),
        (STORYBOARD / "scene 9.png", 12),
        (STORYBOARD / "scene 10.png", 18),
        (STORYBOARD / "scene 11.png", 14),
        (STORYBOARD / "scene 12.png", 12),
    ]
    end_card = ROOT / "storyboards" / "end_card.png"
    if end_card.exists():
        stills.append((end_card, 7))

    segments = []
    for i, v in enumerate(video_refs):
        if not v.exists():
            raise FileNotFoundError(v)
        out = CLIPS / f"ref_{i+1:02d}.mp4"
        normalize_video(v, out)
        segments.append(out)

    for j, (img, dur) in enumerate(stills):
        if not img.exists():
            raise FileNotFoundError(img)
        out = CLIPS / f"still_{j+5:02d}.mp4"
        kenburns_still(img, dur, out)
        segments.append(out)

    silent = OUT / "storyboard_master_silent.mp4"
    xfade_concat(segments, silent)

    audio = ROOT / "audio" / "soundtrack.wav"
    final = OUT / "CloudInvoke_Storyboard_Film_1080p24.mp4"
    if audio.exists():
        mux_audio(silent, audio, final)
    else:
        final = silent

    demo = OUT / "CloudInvoke_Storyboard_Film_1080p24_demo.mp4"
    run(["ffmpeg", "-y", "-i", str(final), "-movflags", "+faststart", "-c", "copy", str(demo)])

    dur = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(final)], text=True)
    print(f"Final: {final} ({float(dur):.1f}s, {len(segments)} segments)")


if __name__ == "__main__":
    main()
