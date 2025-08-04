# Setup the project

For using the full project, you need python installed. Then you need the `pypdf` package for running the `quarto-scripts/split-chapters.py` script.

```bash
python3 -m pip install -r requirements.txt
```

# Useful commands and tools

## creating favicon with image magick

```bash
convert -background white -flatten -density 256 input.svg -resize 256x256 favicon.png
```

## download favicon from website

- [https://onlineminitools.com/website-favicon-downloader](https://onlineminitools.com/website-favicon-downloader)