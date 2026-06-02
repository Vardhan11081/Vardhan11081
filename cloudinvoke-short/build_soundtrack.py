#!/usr/bin/env python3
"""Synthesize layered soundtrack + basic SFX beds (WAV) for ffmpeg mux."""
import math
import wave
import struct
from pathlib import Path

SR = 48000
OUT = Path(__file__).parent / "audio" / "soundtrack.wav"
OUT.parent.mkdir(exist_ok=True)

# Scene boundaries in seconds (must match assemble_film.py total ~157s)
# 0-18 accident, 18-32 witness, 32-52 phone/blur, 52-82 police, 82-90 title, 90-97 intro UI img, 97-127 UI anim, 127+ resolution


def sine(freq, t, amp=1.0):
    return amp * math.sin(2 * math.pi * freq * t)


def noise(t, amp=0.02):
    # deterministic pseudo-noise
    return amp * math.sin(t * 9973.7) * math.sin(t * 437.1)


def env(t, start, end, attack=0.5, release=0.8):
    if t < start or t > end:
        return 0.0
    if t < start + attack:
        return (t - start) / attack
    if t > end - release:
        return max(0.0, (end - t) / release)
    return 1.0


def sample_at(t):
    s = 0.0
    # Rain bed entire film
    s += noise(t, 0.015) * (0.35 + 0.1 * sine(0.3, t, 1))

    # Suspense drone (accident + witness + blur)
    e1 = env(t, 0, 52, 2, 3)
    s += e1 * (sine(55, t, 0.08) + sine(82, t, 0.05))

    # Crash at ~8s
    if 7.5 < t < 9.5:
        crash = (9.5 - t) / 2 * 0.4
        s += crash * (noise(t, 0.3) + sine(40, t, 0.2))

    # Screech at ~6s
    if 5.8 < t < 7.2:
        sc = (7.2 - t) / 1.4 * 0.15
        s += sc * sine(800 - 400 * (t - 5.8), t, 1)

    # Shutter ~34s
    if 33.8 < t < 34.2:
        s += 0.25 * noise(t, 1)

    # Investigation (police)
    e2 = env(t, 52, 82, 1.5, 2)
    s += e2 * (sine(110, t, 0.06) + sine(164, t, 0.04))

    # Tech pulse (CloudInvoke section)
    e3 = env(t, 82, 140, 1, 2)
    pulse = (math.sin(t * 3.5) + 1) / 2
    s += e3 * (sine(220 + 40 * pulse, t, 0.07) + sine(440, t, 0.03))

    # UI bleeps
    if 82 < t < 127:
        if int(t * 4) % 4 == 0 and (t % 1) < 0.05:
            s += 0.08 * sine(880, t, 1)

    # Success chime ~132s
    if 131.5 < t < 133.5:
        ch = (t - 131.5) / 2
        s += 0.12 * sine(523 + 200 * ch, t, 1) * (1 - ch)

    # Inspirational resolution
    e4 = env(t, 127, 165, 2, 4)
    s += e4 * (sine(196, t, 0.07) + sine(294, t, 0.05) + sine(392, t, 0.04))

    return max(-1.0, min(1.0, s * 0.85))


def main():
    duration = 165.0  # cover full concat
    n = int(SR * duration)
    with wave.open(str(OUT), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        frames = bytearray()
        for i in range(n):
            t = i / SR
            val = int(sample_at(t) * 32767 * 0.9)
            frames += struct.pack("<h", val)
        w.writeframes(frames)
    print(f"Wrote {OUT} ({duration}s)")


if __name__ == "__main__":
    main()
