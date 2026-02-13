#!/usr/bin/env python3
"""
Command Line Interface for the anagram generator
Usage: python3 anagram_cli.py [word] [language]
"""

import sys
from anagram_generator import AnagramGenerator

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 anagram_cli.py [word] [language]")
        print("Example: python3 anagram_cli.py listen english")
        print("Example: python3 anagram_cli.py chat french")
        return

    word = sys.argv[1]
    language = sys.argv[2].lower()

    if language not in ['english', 'french']:
        print("Error: Language must be 'english' or 'french'")
        return

    generator = AnagramGenerator()

    try:
        anagrams = generator.find_anagrams(word, language)

        print(f"Anagrams for '{word}' in {language.title()}:")
        if anagrams:
            for i, anagram in enumerate(anagrams, 1):
                print(f"  {i}. {anagram}")

            random_anagram = generator.generate_random_anagram(word, language)
            print(f"\nRandom selection: {random_anagram}")
        else:
            print(f"  No anagrams found for '{word}' in the {language} dictionary.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()