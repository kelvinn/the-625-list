## Introduction

This is a single script and output files for running a CSV through Microsoft Translator. In particular, the CSV used
here is the one specified by Gabriel Wyner's in Fluent Forever. If you haven't read the book, and you are interested in
languages, have a read. He's pretty funny.

## How to Run

    python go.py

You will need to get an API key from Microsoft Translate and inject it as an environment variable, or enter it manually.

## Accuracy?

I've only had a quick 30 second look through the French section, and it appears to be at least 80% accurate. There are
some mistranslations, e.g. East -> Orient, but overall pretty usable. Mistranslations should appear when you build your
cards via Google Images. If you find an error, feel free to send a pull request with the updated field.