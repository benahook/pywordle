# pywordle
python wordle utilities: word suggestions - autosolver - wordcloud generator - wordle simulator

# USAGE
$ cd src
$ python3 wordle_class.py

The program will walk you through the steps for solving a wordle by process
of elimation. 

This is a work in progress!

*Known Bugs:
- if a word has duplicate letters, you pick 'right' for one and 'wrong' for another
it will return an empty list. 

the wrong choice needs to account for duplicates. 

- The solved wordle list isn't currently loaded back in. (therefore picking a previous wordle solution is possible.)