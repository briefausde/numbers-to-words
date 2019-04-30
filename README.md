# numbers-to-words
The program allows you to translate numbers into words.

For example:

``
3 + 7 = 10 -> three plus seven equals ten
``

## Algorithm
Break the string into parts of 3 characters and pass these 3 characters to a function that returns text for numbers from 1 to 999 via dict with texts. And for each triple we form discharges. 

For example, our number is 1 234 567 890. 

To 890 we do not add anything because it is the least bit. To 567 we add thousands, to 234 millions, to 1 add billions.

## Usage
1. Start program from a command shell

```python
python humanize.py -s "<your string>"
```

The argument must be in quotes.

2. Or you can use convert function in your program

```python
from humanize import humanize
```

and call function

```python
humanize("<your string>")
```

## Tests
You can test program by pytest. Install pytest from requirements

```python
pip install -r requirements.txt
```

and test

```python
pytest humanize_tests.py
```
