# HFLA Website Wiki Sandbox

This repo contains a MkDocs documentation site for collaboratively building the HFLA website wiki in a sandbox environment.

## Installation

### With Docker

The quickest way to run the site is using Docker:

``` bash
docker pull vraer/hfla-website-wiki-sandbox
docker run -p 8000:8000 vraer/hfla-website-wiki-sandbox
```

The site will now be running at <http://localhost:8000>.

### With Python virtualenv

Alternatively, you can install locally using Python:

``` python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
mkdocs serve
```

## About

This sandbox site has GitHub discussions integrated for easy collaboration.

Once you have a local version running, you'll notice the mkdocs-live-edits toolbar at the top of each page. This allows for easy in-browser editing and renaming of markdown pages. You can disable the plugin by removing the `live-edit` entry in mkdocs.yml.

``` yaml
plugins:
  - awesome-pages:
      filename: .pages
      collapse_single_pages: false
      strict: false
  - live-edit: {}
  - tags:
      tags_file: tags.md
  - minify:
      minify_html: true
  - search: {}
```

Note this currently only contains a subset of pages from the main HFLA website wiki repo as an example. More existing wiki content can be migrated over later for review.
