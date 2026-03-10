---
name: image-gen
description: Generate images using Gemini (Nano Banana 2) and/or OpenAI (gpt-image-1.5). Supports side-by-side comparison, multiple sizes, aspect ratios, and auto-opens results. Use when asked to generate an image, create artwork, make a logo, design assets, or compare AI image models.
argument-hint: "[prompt] [-p gemini|openai|both] [-s 1K|2K|4K] [-a 16:9] [-o name]"
allowed-tools:
  - Bash(image-gen *)
  - Bash(open *)
  - Read
---

# image-gen

Unified CLI for AI image generation with Gemini and OpenAI.

## Command

```bash
image-gen "prompt" [options]
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-p, --provider` | `gemini` | `gemini`, `openai`, or `both` for side-by-side |
| `-o, --output` | `image-{timestamp}` | Output filename prefix |
| `-d, --dir` | current directory | Output directory |
| `-s, --size` | `1K` | `512`, `1K`, `2K`, or `4K` |
| `-a, --aspect` | `auto` | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, etc. |
| `-m, --model` | `flash` / `gpt-image-1.5` | Gemini: `flash`/`pro`, OpenAI: `gpt-image-1.5`/`gpt-image-1` |
| `-q, --quality` | `high` | OpenAI quality: `low`, `medium`, `high` |
| `--no-open` | - | Don't auto-open in Preview |

## Examples

```bash
# Quick generation (Gemini, fastest/cheapest)
image-gen "a cute robot mascot"

# OpenAI generation
image-gen "professional headshot" -p openai

# Side-by-side comparison
image-gen "cyberpunk cityscape at sunset" -p both -s 2K -a 16:9

# Logo/clip art
image-gen "MentorMates logo, clean vector style" -p both -o mentormates-logo

# Save to specific directory
image-gen "hero banner for landing page" -p openai -d ./assets -s 2K -a 16:9

# Lower quality for quick drafts
image-gen "rough concept sketch" -p openai -q low -s 512
```

## API Keys

- **Gemini**: stored at `~/.nano-banana/.env` as `GEMINI_API_KEY=...`
- **OpenAI**: reads from `OPENAI_API_KEY` env var or `~/codeDev/MentorMates/.env.local`
- Get Gemini key: https://aistudio.google.com/apikey
- Get OpenAI key: https://platform.openai.com/api-keys

## Models

| Provider | Model | Notes |
|----------|-------|-------|
| Gemini | `flash` (default) | Nano Banana 2 — fast, ~$0.067/image |
| Gemini | `pro` | Higher quality, ~$0.134/image |
| OpenAI | `gpt-image-1.5` (default) | Latest, 4x faster than 1.0, best quality |
| OpenAI | `gpt-image-1` | Previous gen |

## Output

- Images saved as `{output}-gemini.png` and/or `{output}-openai.png`
- Auto-opens in Preview on macOS
- Use `--no-open` to suppress auto-open (useful in scripts)

## Source

- CLI: `~/tools/image-gen/cli.ts`
- Runtime: Bun

## Task: $ARGUMENTS
