# PythonGram :incoming_envelope:

## What is Python Gram

Python gram is a small Python program to create a probability matrix to find:

Given a word, what is the n-word(s)

For a 1-Gram:

Given a word, what is the next likely word?

For a 2-Gram:

Given a word, what are the next two likely words?

## What this is About

### Python
This program uses Python3 :snake:. The program works in the following way:

1.) Given a text
2.) Tokenize (break-up the words) the text
3.) Create a dictionary of dictionary by assigning a key (a word), then counting the next following word(s) given the key (the value)

### Pipenv
This program uses Pipenv. Pipenv is a Python virtualenv management tool. Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates a project Pipfile.lock, which is used to produce deterministic builds.

To install Pipenv, use the following link: [link to install pipenv](https://pipenv.pypa.io/en/latest/)

### taleSmall.txt and taleMed.txt

Both files are from tale.txt. Tale.txt is simply the text, A Tale and Two Cities, from [Project Guttenburg](https://www.gutenberg.org/ebooks/98). The Plain Text UTF-8 option.

taleSmall.txt is a small length excerpt of the text

taleMed.txt is a medium length excerpt of the text

## Running the program

Install the Pipenv dependencies using:

```
pipenv install
```

Run the programm using:

```
pipenv run python .\app.py
```

This runs:

```
if __name__ == "__main__":
```

## Running the tests

Runs the tests for the program using Pipenv:

```
pipenv run pytest
```

This should display the following output:

```
platform win32 -- Python 3.10.7, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\Users\bluep\Code\ngram
collected 6 items
```

### Implemented Technologies

Implementation of Python Gram built with the following technologies:

* :snake: Python3
* :envelope: Pipenv

## License

This project is licensed under the GNU General Public License v3.0 [License](LICENSE) - see the LICENSE.md file for details

## Authors

* :ocean: **Normandy14** - *Initial work* - [Github Account](https://github.com/Normandy14)
