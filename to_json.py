import json
import re
import sys

#verse_pattern = re.compile(r'((\d )([A-Z][a-z]*)) (\d+):(\d+)$')
verse_pattern = re.compile(r'((\d )?[A-Z][a-z]*) (\d+):(\d+)$')

current_verse = None
books = {}
all = []

for line in sys.stdin:
  line = line.strip()
  if not line:
    if current_verse:
      all.append((current_verse, ' '.join(verse).strip('1234567890 ')))
    current_verse = None
    continue
  m = verse_pattern.match(line)
  if m:
    book, _, chapter, verse = m.groups()
    chapter = int(chapter)
    verse = int(verse)
    if book not in books:
      books[book] = len(books)
    current_verse = (book, chapter, verse)
    verse = []
  elif current_verse:
    verse.append(line)

print json.dumps(all, indent=4)
#print json.dumps(books)