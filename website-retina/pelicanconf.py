#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = "WebteamDIAG"
SITENAME = "A-eye Research Group"
SITENAME_SHORT = "A-eye"
SITE_REPO = "website-retina"
SITE_GROUP = "retina"

# Home page and social settings
SITELEAD = "The A-eye Research Group aims at bringing artificial intellingence solutions to healthcare and, specifically, eye care. Our expertise lies in developing retinal image analysis methods based on deep learning technology for detection, diagnosis and quantification of retinal diseases. Application areas are automated screening of eye diseases, namely AMD, DR and glaucoma, for cost-effective triage of patient at risk; extraction of quantitative image biomarkers from multimodal data for accurate analysis of large population-based datasets; and the development of computer-aided solutions for personalized diagnosis and treatment of retinal diseases."
SITE_PICTURE = "images/general/retina_main.JPG"
HOME_IMAGE = "images/general/retina_main.JPG"
# HOME_IMAGE_CAPTION = 'Automated tumor detection'
TWITTER_URL = "https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw"
FOOTER_TEXT = 'The A-eye Research Group is part of <a href="https://www.radboudumc.nl">Radboud University Medical Center</a>.'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = (
    '<a href="http://www.diagnijmegen.nl">Diagnostic Image Analysis Group</a>'
)

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "News", "url": "news", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    {"name": "Projects", "url": "projects", "icon": "folder"},
    {"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    {
        "name": "Publications",
        "url": "publications",
        "icon": "file-text-o",
        "hidden": 85,
    },
    {"name": "Presentations", "url": "presentations", "hidden": 95},
    {"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {
    "News": "News",
    "Vacancies": "Vacancies",
    "Projects": "Projects",
    "Members": "Members",
}
# URLs
SITEURL = ""
IMGURL = SITEURL
EDIT_CONTENT_URL = (
    "https://github.com/diagnijmegen/website-content/edit/master/{file_path}"
)

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = "content"
RELATIVE_URLS = False

# Show pdf request on publication pages
ENABLE_PUBLICATION_PDF_REQUEST = False

TIMEZONE = "Europe/Amsterdam"
DEFAULT_LANG = "EN"
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CURRENTYEAR = date.today().year
TODAY = date.today()
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = "content/dict_pubs.json"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
SLUGIFY_SOURCE = "basename"

ARTICLE_URL = "news/{slug}/"
ARTICLE_SAVE_AS = "news/{slug}/index.html"

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

ARCHIVES_SAVE_AS = ""

SITEMAP_SAVE_AS = "sitemap.xml"
INDEX_SAVE_AS = "news/index.html"
ARTICLE_TYPE = "News"

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ["index", "archives", "sitemap"]

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = [
    "bibtex",
    "bibtex_loader",
    "edit_url",
    "hierarchy",
    "fileutil",
    "bootstrapify",
    "imgutil",
    "inline_extend",
    "content_aggregator",
]
