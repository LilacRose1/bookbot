# BookBot

A command-line tool that analyzes a text file and reports word count and letter-frequency statistics. This was my first [Boot.dev](https://www.boot.dev) guided project, built with plain Python and no external dependencies.

## Requirements

- Python 3

## Running it

```bash
git clone https://github.com/LilacRose1/bookbot.git
cd bookbot
python3 main.py path/to/book.txt
```

The `books/` sample texts used during development aren't included in this repo — point it at any UTF-8 `.txt` file, such as a public-domain book from [Project Gutenberg](https://www.gutenberg.org/).

Example output:

```
============ BOOKBOT ============
Analyzing book found at path/to/book.txt...
----------- Word Count ----------
Found 78421 total words
--------- Character Count -------
e: 45321
t: 32198
a: 28734
...
============= END ===============
```

## Credit

Built while following the [Boot.dev](https://www.boot.dev) "Build a Bookbot" guided project.
