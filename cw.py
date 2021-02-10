#! /usr/bin/env python3

"""
Leif Gregory <leif@devtek.org>
cw.py v0.5
Tested to Python v3.8.5

Description:
Crossword helper to find words with missing letters. i.e. if you need a word
that is five letters and you have s.u.p (dots as missing characters), it will
return all words that match that pattern. e.g. slump, slurp, stump.

Changelog:
20210127 -  Initial code

Copyright 2020 Leif Gregory

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import re
import sys


def wordSearch():
    """
    Reads in all words without special characters like apostrophes or dashes
    from a word file into a dict as lowercase words. By default it uses the
    built-in Linux wordlist at /usr/share/dict/words.

    Returns:
        Dict
    """

    wordFile = "/usr/share/dict/words"

    if os.path.isfile(wordFile):
        wordData = open(wordFile)
        wordList = {}

        for word in wordData.read().split('\n'):
            if word.isalpha():
                wordList[word.lower()] = None
        wordData.close()
    else:
        print("Word file not found.")

    return wordList


def main():
    # Load our wordlist
    haystack = wordSearch()

    # Test if user supplied just letters and periods to denote missing characters
    if re.search('^[A-z.]+$', str(sys.argv[1])):
        needle = re.compile(f"^{str(sys.argv[1]).lower()}$")
        foundWords = '\n'

        for word in haystack:
            if needle.match(word):
                foundWords += f"{word}, "
    else:
        print("Use a period for missing characters. e.g. s.u.p for slump, slurp, stump etc.")

    print(f"{foundWords.rstrip(', ')}\n")


if __name__ == '__main__':
    main()
