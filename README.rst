Pydict
-------

Pydict is a simple command line dictionary, it lets you search the meanings of the word on the terminal. 
It refers to the online dictionary http://www.thefreedictionary.com
It also pronouces the keywords.

Requirements
-------------

It requires a command line mp3 player - mpg123. To install it use the following command:
$ sudo apt-get install mpg123

Usage
------

To search for a keyword:

>>> import pydict
>>> pydict.search('awesome', 2, 'uk')

It will search for the word 'awesome' and pronouce it 2 times and in 'uk' style.
It will display the result of meaning of 'awesome'.
If a keyword is not found in the dictionary it reports error.

To just pronouce the word:

>>> import pydict
>>> pydict.speak('awesome', 2, 'us')

If pronouciation does not exist it reports error.
It has three styles 'normal', 'us' and 'uk'.

From command line:

$ pydict -q 'awesome' -s uk -p 2 

options:

1. -q --query:		keyword
2. -s --style: 	'normal', 'us' or 'uk'
3. -p --pronounce:	repeat pronounciation
4. -m --meaning:	display search or not. (0 or 1)

