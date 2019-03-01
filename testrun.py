from wikipdf import pdfCreate
from pywikihow import WikiHow

randomWiki = WikiHow.random()
title = randomWiki["title"]
steps = randomWiki["steps"]
url = randomWiki["url"]

pdfCreate(title, steps)