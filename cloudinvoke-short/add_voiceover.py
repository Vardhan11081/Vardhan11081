#!/usr/bin/env python3
"""Replace film audio with storyboard/voiceover.mp3 (pads silence if shorter than video)."""
import subprocess
from pathlib import Path

STORYBOARD = Path("/workspace/storyboard")
ROOT = Path(__file__).parent
VIDEO = ROOT / "output" / "CloudInvoke_Storyboard_Film_1080p24_demo.mp4"
VOICEOVER = STORYBOARD / "voiceover.mp3"
OUT = ROOT / "output" / "CloudInvoke_Storyboard_Film_1080p24_voiceover.mp4"


def probe(path):
    return float(
        subprocess.check_output(
            [
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", str(path),
            ],
            text=True,
        ).strip()
    )


def main():
    if not VIDEO.exists():
        raise FileNotFoundError(VIDEO)
    if not VOICEOVER.exists():
        raise FileNotFoundError(VOICEOVER)

    vid_dur = probe(VIDEO)
    vo_dur = probe(VOICEOVER)
    pad = max(0.0, vid_dur - vo_dur)

    # Stereo + slight gain — mono AAC in MP4 is muted in some players/preview UIs
    cmd = [
        "ffmpeg", "-y", "-i", str(VIDEO), "-i", str(VOICEOVER),
        "-filter_complex",
        f"[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0,volume=1.5,apad=pad_dur={pad}[aout]",
        "-map", "0:v:0", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ac", "2",
        "-t", str(vid_dur), "-movflags", "+faststart", str(OUT),
    ]
    subprocess.run(cmd, check=True)
    print(f"Wrote {OUT} (video {vid_dur:.1f}s, voiceover {vo_dur:.1f}s)")


if __name__ == "__main__":
    main()
