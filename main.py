#!/usr/bin/env python3
import cmd2
import os
from pathlib import Path

def popularity(word):
    letters = [chr(97+i) for i in range(26)]
    freqs = [7.8,2,4,3.8,11,1.4,3,2.3,8.2,0.21,2.5,5.3,2.7,7.2,6.1,2.8,0.24,7.3,8.7,6.7,3.3,1,0.91,0.27,1.6,0.44]
    freqs = {k:v for k,v in zip(letters, freqs)}
    word = set(word)
    ret = 0
    for c in word:
        ret += freqs[c]
    return ret

class Wordle(cmd2.Cmd):
    """Wordle helper!"""
    def __init__(self, dictionary_filename):
        super().__init__()
        self.hidden_commands.append('alias')
        self.hidden_commands.append('edit')
        self.hidden_commands.append('help')
        self.hidden_commands.append('history')
        self.hidden_commands.append('ipy')
        self.hidden_commands.append('macro')
        self.hidden_commands.append('py')
        self.hidden_commands.append('run_pyscript')
        self.hidden_commands.append('run_script')
        self.hidden_commands.append('set')
        self.hidden_commands.append('shell')
        self.hidden_commands.append('shortcuts')
        self.prompt = '$ '

        with open(dictionary_filename, 'r') as f:
            self.words = set(f.read().lower().split())
            self.words = list(filter(lambda x: len(x) == 5, self.words))
        self.prev_words = []

        self.print_cur_words()

    def print_cur_words(self): 
        # sort by unique letters, tie break by number of vowels
        self.words.sort(key=popularity, reverse=True)
        if not self.words:
            print("No words left!")
            return
        print(f'{len(self.words)} WORDS: {", ".join(self.words[:20])}', end='')
        if len(self.words) > 20:
            print(', etc...')
        else:
            print('')

    def do_words(self, _line):
        """
        Print current words
        """
        self.print_cur_words()

    def do_rm(self, line):
        """
        rm <letters>

        Removes all words that include given letters.
        E.g. [rm abcdef]
        """
        line = line.lower()
        if not line.isalpha():
            self.do_help('rm')
            return
        self.prev_words.append(self.words[::])
        self.words = list(filter(lambda x: len(set(line).intersection(x)) == 0, self.words))
        self.print_cur_words()

    def do_at(self, line):
        """
        at <index> <letter>

        Remove all words that don't have <letter> at <index>.
        <index> is in [0, 4]
        E.g. [at 0 a]
        """
        line = line.lower()
        line = line.split()
        if len(line) != 2 or not line[0].isdigit() or int(line[0]) >= 5 or len(line[1]) != 1 or not line[1].isalpha():
            self.do_help('at')
            return
        self.prev_words.append(self.words[::])
        self.words = list(filter(lambda x: x[int(line[0])] == line[1], self.words))
        self.print_cur_words()

    def do_not(self, line):
        """
        not <index> <letter>

        Remove all words that have <letter> at <index>, as well as all word that don't have <letter> at all.
        <index> is in [0, 4]
        E.g. [not 0 a]
        """
        line = line.lower()
        line = line.split()
        if len(line) != 2 or not line[0].isdigit() or int(line[0]) >= 5 or len(line[1]) != 1 or not line[1].isalpha():
            self.do_help('not')
            return
        self.prev_words.append(self.words[::])
        self.words = list(filter(lambda x: x[int(line[0])] != line[1] and line[1] in x, self.words))
        self.print_cur_words()

    def do_undo(self, _line):
        """
        Undo previous refinement (rm, at, not)
        """
        if not self.prev_words:
            print('No further undo')
            return
        self.words = self.prev_words.pop()
        self.print_cur_words()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    c = Wordle('/usr/share/dict/words')
    exit(c.cmdloop())


if __name__ == '__main__':
    main()
