---
name: seiribu-image-finisher
description: Use when the user provides or references a Seiribu image-plan JSON/Markdown from Antigravity and wants images created, generated, finished, saved, or prepared for WordPress. This skill turns `image-briefs/<slug>-image-plan.json` into generated image assets by calling Codex imagegen, saving sources, overlaying Seiribu logos on inline images/diagrams, writing `assets/images/<slug>/README.md`, and reporting final paths. Also use when the user asks what should happen after Antigravity creates image instructions.
---

# Seiribu Image Finisher

## Non-negotiable

If the user gives an `image-plan.json` and asks to make images, do not stop at reviewing or regenerating the plan. The requested outcome is finished image assets.

The only part that cannot be delegated to a normal shell script is image generation itself. Use Codex built-in `imagegen` for each image, then use the project post-processing script for resizing, logo overlay, and README output.

## Workflow

1. Read the provided `image-plan.json`.
2. Confirm it has `engine.storage_policy.draft_dir`, `engine.storage_policy.final_dir`, and included `images`.
3. Create the plan `draft_dir`.
4. For each included image, call built-in `imagegen` once using that image's `final_prompt`.
   - Use the prompt from JSON as authoritative.
   - Preserve the planned `role`, `file_name`, `aspect_ratio`, and avoid rules.
   - For `アイキャッチ` / `アイキャッチ素材`, generate a text-free, logo-free Canva material only.
   - For `記事内イメージ`, generate a text-free illustration base with no logo.
   - For `記事内図解`, first decide whether it is a slide diagram or a scene diagram:
     - Use slide-diagram mode for steps, flows, comparisons, NG/OK contrasts, checklists, classification, decision tables, and "3 points / 4 steps" briefs.
     - Use scene-diagram mode only when the brief's main value is an emotional or situational illustration rather than a readable information structure.
   - For slide diagrams, rewrite or prepend the JSON prompt before calling `imagegen` so it explicitly asks for a simple presentation-slide infographic: flat 2D vector, icon-based diagram, rounded cards, simple arrows, large readable short Japanese labels, limited warm colors, minimal icon-like people only if needed. Also explicitly forbid photorealism, realistic lighting, camera perspective, detailed room scenes, photo-like panels, manga panels, detailed faces, and business stock-photo style.
   - For slide diagrams, do not let article context such as "Japanese home", "realistic household objects", "people and rooms", "consulting specialist", or "scene-based panels" dominate the prompt. Convert those details into simple icons or cards.
   - For slide diagrams, generate a complete simple infographic with short labels rendered by imagegen; do not add labels later with Pillow unless a later manual correction is explicitly requested.
   - For scene diagrams, generate a complete illustrated infographic, not abstract line art. Short Japanese labels should be rendered by imagegen when they are part of the brief.
5. Copy or move each selected generated source image into `draft_dir` using the exact planned `file_name`.
6. Run the finishing script with bundled Codex Python:

```bash
/Users/kota/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  /Users/kota/Documents/アンチグラビティ/seiribu-content/seiribu-editorial/scripts/finish_image_plan_outputs.py \
  <path-to-image-plan.json>
```

7. Inspect the outputs in `final_dir`.
8. If an image fails QA, regenerate that image once or twice, overwrite only its draft source, rerun the finishing script, and inspect again.
9. Report the final saved paths and any images that still need human review.

## QA Rules

Check every final image:

- It matches the article topic and image purpose.
- It is warm, clean, Japanese domestic editorial illustration style.
- It does not include AI-generated logos, watermarks, random extra text, garbled Japanese, signs, or speech bubbles.
- Inline images and diagrams have the Seiribu logo in an unobtrusive corner.
- The Seiribu logo should be small, around 90-110px wide on a 1200px image. It must read as a brand signature, not as a title element.
- Logo does not cover faces, important objects, labels, or captions.
- Diagrams are simple illustrated infographics with rounded panels, ample negative space, spot illustrations, and clean arrows.
- Slide diagrams must look like Canva/PowerPoint-style slides, not realistic photos, not photo panels, not watercolor scenes, not detailed Japanese room scenes, and not manga. They should be easy to scan at a glance.
- Slide diagrams should use icons/cards/arrows as the main visual. People, rooms, and specialists may appear only as small simplified icons or spot illustrations when necessary.
- Reject and regenerate a slide diagram if it becomes photorealistic, camera-like, full-scene, emotionally dramatic, or primarily a parent-child room scene instead of a diagram.
- Reject and regenerate if a diagram uses children as the main subject when the article reader is an adult child supporting an elderly parent.
- Diagram text should be natural model-rendered text for short labels only. Do not specify fonts and do not overlay diagram labels locally unless a later manual correction is explicitly requested.
- Eyecatch material has no final title/logo; Canva will handle those.

## Slide Diagram Prompt Patch

When an `記事内図解` is a slide diagram, prepend a compact patch like this to the JSON `final_prompt` before calling `imagegen`:

```text
Create a simple 16:9 Japanese slide-style infographic. Style: flat 2D vector illustration, icon-based diagram, clean presentation slide, light cream background, rounded cards, simple arrows, large readable Japanese labels, limited warm colors. This must look like a simple slide diagram, not a photo, not a realistic scene, not watercolor, not manga, not a full room illustration. Use minimal icon-like people only if needed. No realistic lighting, no camera perspective, no detailed faces. Use cards, arrows, icons, and only the short Japanese labels required by the brief. No extra text, no garbled Japanese, no logo, no watermark, no speech bubbles. Leave a quiet corner for a small logo overlay.
```

If the original JSON prompt contains scene-heavy details, preserve the meaning but simplify them:

- `親子が相談している` -> icon-like adult child and elderly parent, small and simple.
- `実家の部屋` -> subtle home-like icon/background, not a room scene.
- `専門家に相談` -> small neutral value-check icon or small secondary specialist icon.
- `古い品物` -> one or two simple item icons such as box, camera, book, vase, or magnifying glass.

## Output Contract

After finishing, `assets/images/<slug>/` must contain:

- The eyecatch material image.
- Four inline images/diagrams.
- `README.md` with file names, WordPress image titles, ALT, captions, positions, and logo modes.
- `finish-manifest.json` for machine-readable traceability.

The WordPress upload remains manual. Do not publish to WordPress.
