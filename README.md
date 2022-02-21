[Wordle](https://www.nytimes.com/games/wordle/index.html) was annoying me so here's a toy program to help you solve it.

words.txt was created by combining [Unix words](https://en.wikipedia.org/wiki/Words_(Unix)) and popular.txt from [dolph/dictionary](https://github.com/dolph/dictionary)

```
havinleung@Macbook_Pro wordle % ./main.py
9972 WORDS: arise, raise, aries, serai, siena, sinae, insea, anise, resin, taise, rinse, siren, serin, risen, saite, reins, rasen, anser, nares, snare, etc...
(WORDLE HELPER) > help -v

Documented commands (use 'help -v' for verbose/'help <topic>' for details):
======================================================================================================
at                    at <index> <letter>
not                   not <index> <letter>
quit                  Exit this application
reset                 Reset to include all words
rm                    rm <letters>
undo                  Undo previous refinement (rm, at, not)
words                 Print current words
```
