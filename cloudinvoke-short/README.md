# CloudInvoke — Cinematic Animated Short (1080p / 24 FPS)

Pixar-inspired 3D storyboard motion picture (~2:20) demonstrating the CloudInvoke evidence-enhancement narrative.

## Deliverables

| File | Description |
|------|-------------|
| `output/CloudInvoke_Short_Film_1080p24.mp4` | Full film with synthesized soundtrack |
| `output/CloudInvoke_Short_Film_1080p24_demo.mp4` | Web-optimized (`faststart`) |
| `plate_number.txt` | Extracted registration: **BX47 KLM** |
| `SCRIPT.md` | Scene-by-scene script with timing |
| `storyboards/` | All keyframe stills (Disney/Pixar style) |
| `frames/ui/` | CloudInvoke AI processing UI animation frames |

## Rebuild

```bash
cd cloudinvoke-short
python3 build_title_cards.py
python3 build_ui_frames.py
python3 build_soundtrack.py
python3 assemble_film.py
```

Requires: Python 3, Pillow, ffmpeg, ffprobe.

## Customization

- Replace `audio/soundtrack.wav` with licensed cinematic stems (suspense / investigation / tech / inspirational) and re-run `assemble_film.py`.
- Swap storyboard PNGs in `storyboards/` to match new art or your original keyframe for Scene 2.
- Extend `assemble_film.py` `SCENES` list for additional Higgsfield/Kling clips between stills.

## Story coverage

1. Night accident at intersection (empty CCTV poles)  
2. Witness alarm → smartphone photo → blurry plate  
3. Police station frustration (no CCTV, unreadable photo)  
4. CloudInvoke upload + AI enhancement sequence  
5. Clear plate + `plate_number.txt` → officer success → case lead  
6. End card: *Turning Blurred Evidence into Clear Answers*
