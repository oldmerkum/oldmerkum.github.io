AUTHOR = 'Oldmerkum - Antonio Marcum'
SITENAME = 'Oldmerkum - Antonio Marcum'
SITEURL = ""
SITETITLE = 'Oldmerkum - Antonio Marcum'
SITESUBTITLE = 'Cybersecurity professional'
SITELOGO = '/images/me_suit.jpg'
FAVICON = '/images/favicon_io/favicon.ico'


THEME = 'themes/flex'

PATH = "content"
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
        ("github", "https://github.com/oldmerkum"),
)

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'), ('Categories', '/categories'), ('Tags', '/tags'))

PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
