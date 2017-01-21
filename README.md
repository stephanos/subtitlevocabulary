subvoc [![Build Status](https://secure.travis-ci.org/stephanos/subvoc.png)](https://travis-ci.org/stephanos/subvoc) [![Coverage Status](https://coveralls.io/repos/github/stephanos/subvoc/badge.svg?branch=master)](https://coveralls.io/github/stephanos/subvoc?branch=master)
======

This project was created by me to scratch my own itch.
I love to watch movies and am always keen to expand my vocabulary.
But it's difficult to notice an unknown word *during* a movie without spoiling the experience.
That's where `subvoc` comes in: search for a movie and discover its vocabulary.


## Online Demo

Visit https://subvoc.stephanbehnke.com (hosted on Heroku, takes a few moments to start sometimes).


## Features

 - [x] landing page with search bar
 - [x] search movie by query
 - [x] sort search results by popularity
 - [x] host on Heroku
 - [x] list of words sorted by difficulty
 - [x] use the base of each word
 - [x] lazy load analysis
 - [ ] show movie context for each word
 - [x] include movie poster
 - [ ] support for idioms
 - [ ] support for TV show episodes
 - [ ] show context in another language side by side
 - [ ] wild idea: display YouTube videos with a certain word


## Development

 - `pip install -r requirements.txt`
 - `pip install -r dev-requirements.txt`
 - `python -m nltk.downloader $(tr "\n" " " < ".nltk_packages")`
 - use `python run.py`, `pytest` and `scripts/compilejs.sh`

Start the application via `python run.py`, test it via `pytest`.


## License
MIT (see LICENSE).
