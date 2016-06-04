#!/usr/bin/env bash

AUTHOR='Baba Okina'
COVER='cover.png'
TAGS='Fantasy,Light Novel'
TITLE='I’m A Spider, So What?'

CSS='hr { border: 0; border-top: 1px solid #606060; }'

cd $(dirname "$0")

cat downloads/*.html >> chapters.html

ebook-convert chapters.html chapters.epub --chapter="//*[name()='h1' or name()='h2']" --extra-css="$CSS" --max-levels=0 --authors="$AUTHOR" --cover="$COVER" --tags="$TAGS" --title="$TITLE"

rm chapters.html

# ebook-convert:
# https://manual.calibre-ebook.com/generated/en/ebook-convert.html

# --chapter format:
# https://manual.calibre-ebook.com/xpath.html
