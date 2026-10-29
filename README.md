# Web Generator

A small, dependency-free static site generator written in Python. It converts
Markdown files in `content/` into HTML pages in `docs/` using a single
`template.html`, and copies everything under `static/` into the output. Built
while following the Boot.dev [Build a Static Site Generator](https://www.boot.dev/courses/build-static-site-generator-python)
course.

## Features

- Pure Python 3, standard library only (no external dependencies)
- Recursive page generation that mirrors the `content/` directory structure
- Markdown block parsing: headings, paragraphs, code blocks, blockquotes,
  ordered and unordered lists
- Inline Markdown parsing: bold (`**`), italic (`_`), inline code (`` ` ``),
  links, and images
- Template-based HTML rendering with `{{ Title }}` and `{{ Content }}`
  placeholders
- Configurable base path, so the same source builds for either local serving
  (`/`) or a GitHub Pages subpath (e.g. `/web_generator/`)
- Unit tests for the Markdown / HTML pipeline

## Project layout

```
.
├── build.sh          # Production build (rewrites links with /web_generator/ base path)
├── main.sh           # Local build + serves docs/ on http://localhost:8888
├── test.sh           # Runs the unittest suite
├── template.html     # HTML shell with {{ Title }} and {{ Content }} placeholders
├── content/          # Source Markdown — every .md becomes an index.html in docs/
├── static/           # Files copied as-is into docs/ (CSS, images, etc.)
├── docs/             # Generated output (served by GitHub Pages)
└── src/
    ├── main.py              # Entry point
    ├── page.py              # Page rendering + recursive walker
    ├── md_to_html.py        # Block-level Markdown → HTMLNode tree
    ├── blocknode.py         # Block type detection, title extraction
    ├── inline_markdown.py   # Inline parsing (bold, italic, code, links, images)
    ├── htmlnode.py          # HTMLNode / LeafNode / ParentNode
    ├── textnode.py          # TextNode + TextType enum
    ├── util/util.py         # File / directory helpers
    └── test_*.py            # Unit tests
```

## Requirements

- Python 3.10+ (the code uses `match`/`case`)

## Usage

### Build and serve locally

```bash
./main.sh
```

This generates `docs/` from `content/` with a `/` base path, touches
`docs/.nojekyll`, and starts `python3 -m http.server 8888` from inside `docs/`.
Open <http://localhost:8888> in your browser.

### Build for GitHub Pages

```bash
./build.sh
```

Generates `docs/` with the base path `/web_generator/` so links and asset URLs
resolve correctly when the site is served from
`https://<user>.github.io/web_generator/`. The `.nojekyll` file is added so
GitHub Pages serves the output directly without running Jekyll.

### Run tests

```bash
./test.sh
```

Runs `python3 -m unittest discover -s src`.

## How it works

1. `src/main.py` reads an optional base-path argument (`sys.argv[1]`, defaulting
   to `/`), wipes `docs/`, and recopies everything from `static/` into it.
2. `generate_pages_recursive` walks `content/`, recreating subdirectories under
   `docs/`. Every `*.md` becomes an `index.html` in the matching output folder.
3. For each Markdown file:
   - `markdown_to_html_node` splits the source into blocks, classifies each
     block (heading / paragraph / code / quote / list), and converts it into an
     `HTMLNode` tree. Inline parsing then handles bold, italic, inline code,
     links, and images inside each block.
   - `extract_title` pulls the first `# ` heading for use as the page title.
   - The rendered HTML and title are substituted into `template.html`, and any
     root-relative `href="/..."` / `src="/..."` are rewritten with the supplied
     base path.

## Authoring content

- Put Markdown under `content/`. The directory structure determines the URL
  structure — `content/blog/tom/index.md` becomes `docs/blog/tom/index.html`.
- Each Markdown file must start with a `# Title` line; that line becomes the
  page's `<title>`.
- Drop CSS, images, and other assets into `static/`. They are copied verbatim
  into `docs/`.
- Edit `template.html` to change the page shell; keep the `{{ Title }}` and
  `{{ Content }}` placeholders.
