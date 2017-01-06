subvoc [![Build Status](https://secure.travis-ci.org/stephanos/subvoc.png)](https://travis-ci.org/stephanos/subvoc)
======

This project was created by me to scratch my own itch. I love to watch movies and am always keen to expand my vocabulary. But it's difficult to notice an unknown word *during* a movie without spoiling the experience. That's when `subvoc` was born.


## Features

 - [x] landing page with search bar
 - [x] search movie by query
 - [x] sort search results by popularity
 - [x] host on Heroku
 - [x] list of words sorted by difficulty
 - [x] use the base of each word
 - [ ] show movie context for each word
 - [ ] show context in another language side by side
 - [ ] include movie poster
 - [ ] support for TV show episodes
 - [ ] wild idea: display YouTube videos with a certain word


## Development

 - `pip install -r requirements.txt`
 - `pip install -r dev-requirements.txt`
 - `python -m nltk.downloader $(tr "\n" " " < ".nltk_packages")`

Start the application via `python run.py`, test it via `pytest`.


## License
MIT (see LICENSE).
