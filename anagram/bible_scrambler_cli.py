#!/usr/bin/env python3
"""
Command Line Interface for the Bible Book Scrambler
Usage:
  python3 bible_scrambler_cli.py generate [book_name] [language]
  python3 bible_scrambler_cli.py random [language] [testament]
  python3 bible_scrambler_cli.py solve [scrambled] [guess] [language]
  python3 bible_scrambler_cli.py hint [book_name] [language]
  python3 bible_scrambler_cli.py list [language]
"""

import sys
from bible_book_scrambler import BibleBookScrambler

def print_usage():
    """Print usage instructions"""
    print("Bible Book Scrambler - Command Line Interface")
    print()
    print("Usage:")
    print("  Generate scramble from book name:")
    print("    python3 bible_scrambler_cli.py generate \"Genesis\" english")
    print("    python3 bible_scrambler_cli.py generate \"Lévitique\" french")
    print()
    print("  Random scramble challenge:")
    print("    python3 bible_scrambler_cli.py random english")
    print("    python3 bible_scrambler_cli.py random french old")
    print("    python3 bible_scrambler_cli.py random english new")
    print()
    print("  Check solution:")
    print("    python3 bible_scrambler_cli.py solve \"sneeGi\" \"Genesis\" english")
    print("    python3 bible_scrambler_cli.py solve \"éqLiutive\" \"Lévitique\" french")
    print()
    print("  Get hint for a book:")
    print("    python3 bible_scrambler_cli.py hint \"Genesis\" english")
    print("    python3 bible_scrambler_cli.py hint \"Matthieu\" french")
    print()
    print("  List all Bible books:")
    print("    python3 bible_scrambler_cli.py list english")
    print("    python3 bible_scrambler_cli.py list french")
    print()
    print("Languages: english, french")
    print("Testaments: old, new (optional for random mode)")

def validate_language(language: str) -> bool:
    """Validate language parameter"""
    return language.lower() in ['english', 'french']

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()
    scrambler = BibleBookScrambler()

    try:
        if command == "generate":
            # Generate scramble from book name
            if len(sys.argv) != 4:
                print("Error: Generate mode requires book name and language")
                print("Usage: python3 bible_scrambler_cli.py generate \"[book_name]\" [language]")
                return

            book_name = sys.argv[2]
            language = sys.argv[3].lower()

            if not validate_language(language):
                print("Error: Language must be 'english' or 'french'")
                return

            scrambled = scrambler.generate_scramble(book_name, language)
            hint = scrambler.get_hint(book_name, language)

            print(f"Original: {book_name}")
            print(f"Scrambled: {scrambled}")
            print(f"Hint: {hint}")

        elif command == "random":
            # Random scramble challenge
            if len(sys.argv) < 3:
                print("Error: Random mode requires language")
                print("Usage: python3 bible_scrambler_cli.py random [language] [testament]")
                return

            language = sys.argv[2].lower()
            testament = sys.argv[3].lower() if len(sys.argv) > 3 else 'any'

            if not validate_language(language):
                print("Error: Language must be 'english' or 'french'")
                return

            if testament not in ['any', 'old', 'new', 'ancien', 'nouveau']:
                print("Error: Testament must be 'old', 'new', or omitted for 'any'")
                return

            random_book = scrambler.get_random_book(language, testament)
            scrambled = scrambler.generate_scramble(random_book, language)
            hint = scrambler.get_hint(random_book, language)

            print("=== Random Bible Book Scramble Challenge ===")
            print(f"Scrambled: {scrambled}")
            print(f"Hint: {hint}")
            print()
            print("Can you guess which Bible book this is?")
            print(f"(Answer: {random_book})")

        elif command == "solve":
            # Check solution
            if len(sys.argv) != 5:
                print("Error: Solve mode requires scrambled text, guess, and language")
                print("Usage: python3 bible_scrambler_cli.py solve \"[scrambled]\" \"[guess]\" [language]")
                return

            scrambled = sys.argv[2]
            guess = sys.argv[3]
            language = sys.argv[4].lower()

            if not validate_language(language):
                print("Error: Language must be 'english' or 'french'")
                return

            is_valid = scrambler.check_solution(scrambled, guess, language)

            print(f"Scrambled: {scrambled}")
            print(f"Your guess: {guess}")
            print(f"Result: {'✅ Valid Bible book!' if is_valid else '❌ Not a valid Bible book'}")

        elif command == "hint":
            # Get hint for a book
            if len(sys.argv) != 4:
                print("Error: Hint mode requires book name and language")
                print("Usage: python3 bible_scrambler_cli.py hint \"[book_name]\" [language]")
                return

            book_name = sys.argv[2]
            language = sys.argv[3].lower()

            if not validate_language(language):
                print("Error: Language must be 'english' or 'french'")
                return

            hint = scrambler.get_hint(book_name, language)
            print(f"Book: {book_name}")
            print(f"Hint: {hint}")

        elif command == "list":
            # List all books
            if len(sys.argv) != 3:
                print("Error: List mode requires language")
                print("Usage: python3 bible_scrambler_cli.py list [language]")
                return

            language = sys.argv[2].lower()

            if not validate_language(language):
                print("Error: Language must be 'english' or 'french'")
                return

            books = scrambler.get_all_books_list(language)
            print(f"All 66 Bible books in {language.title()}:")
            print("-" * 40)

            # Group by testament for better readability
            if language == 'english':
                english_books = scrambler.english_books
                old_testament = [book['display_name'] for book in english_books.values() if book['testament'] == 'old']
                new_testament = [book['display_name'] for book in english_books.values() if book['testament'] == 'new']

                print("OLD TESTAMENT (39 books):")
                for i, book in enumerate(sorted(old_testament, key=lambda x: next(data['book_number'] for data in english_books.values() if data['display_name'] == x)), 1):
                    print(f"  {i:2d}. {book}")

                print("\nNEW TESTAMENT (27 books):")
                for i, book in enumerate(sorted(new_testament, key=lambda x: next(data['book_number'] for data in english_books.values() if data['display_name'] == x)), 1):
                    print(f"  {i:2d}. {book}")
            else:
                french_books = scrambler.french_books
                ancien_testament = [book['display_name'] for book in french_books.values() if book['testament'] == 'ancien']
                nouveau_testament = [book['display_name'] for book in french_books.values() if book['testament'] == 'nouveau']

                print("ANCIEN TESTAMENT (39 livres):")
                for i, book in enumerate(sorted(ancien_testament, key=lambda x: next(data['book_number'] for data in french_books.values() if data['display_name'] == x)), 1):
                    print(f"  {i:2d}. {book}")

                print("\nNOUVEAU TESTAMENT (27 livres):")
                for i, book in enumerate(sorted(nouveau_testament, key=lambda x: next(data['book_number'] for data in french_books.values() if data['display_name'] == x)), 1):
                    print(f"  {i:2d}. {book}")

        else:
            print(f"Error: Unknown command '{command}'")
            print("Available commands: generate, random, solve, hint, list")
            print("Use 'python3 bible_scrambler_cli.py' without arguments to see usage.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()