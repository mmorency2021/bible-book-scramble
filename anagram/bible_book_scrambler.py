#!/usr/bin/env python3
"""
Bible Book Scrambler Tool
Scrambles Bible book names in French or English for puzzle solving.
"""

import random
import re
from typing import List, Dict, Tuple, Any, Optional
from bible_books_data import get_english_bible_books, get_french_bible_books, get_book_by_display_name, get_books_by_testament

class BibleBookScrambler:
    def __init__(self):
        self.english_books = get_english_bible_books()
        self.french_books = get_french_bible_books()

    def _normalize_book_name(self, book_name: str) -> str:
        """Normalize book name for comparison"""
        return book_name.lower().strip()

    def _extract_letters_for_scrambling(self, text: str) -> Tuple[List[str], List[int]]:
        """
        Extract only alphabetic characters for scrambling while preserving positions
        of numbers, spaces, and special characters.

        Args:
            text: The text to analyze

        Returns:
            Tuple of (letters_to_scramble, positions_to_preserve)
        """
        letters = []
        special_positions = []

        for i, char in enumerate(text):
            if char.isalpha():
                letters.append(char)
            else:
                special_positions.append((i, char))

        return letters, special_positions

    def _scramble_letters(self, letters: List[str], max_attempts: int = 50) -> List[str]:
        """
        Scramble letters ensuring the result is different from the original.

        Args:
            letters: List of letters to scramble
            max_attempts: Maximum attempts to get a different arrangement

        Returns:
            Scrambled list of letters
        """
        original = letters.copy()

        for _ in range(max_attempts):
            scrambled = letters.copy()
            random.shuffle(scrambled)

            # Make sure it's different from the original (avoid trivial scrambles)
            if scrambled != original or len(letters) <= 2:
                return scrambled

        # If we couldn't get a different arrangement, force at least one swap
        if len(letters) >= 2:
            scrambled = letters.copy()
            # Swap first two letters if they're different
            if scrambled[0] != scrambled[1]:
                scrambled[0], scrambled[1] = scrambled[1], scrambled[0]
            else:
                # Find a different letter to swap with
                for i in range(2, len(scrambled)):
                    if scrambled[0] != scrambled[i]:
                        scrambled[0], scrambled[i] = scrambled[i], scrambled[0]
                        break

        return scrambled

    def _reconstruct_text(self, scrambled_letters: List[str], special_positions: List[Tuple[int, str]]) -> str:
        """
        Reconstruct text by inserting scrambled letters and preserving special characters.

        Args:
            scrambled_letters: List of scrambled alphabetic characters
            special_positions: List of (position, character) for non-alphabetic chars

        Returns:
            Reconstructed text with scrambled letters and preserved special characters
        """
        result = [''] * (len(scrambled_letters) + len(special_positions))
        letter_index = 0

        # Place special characters first
        special_dict = {pos: char for pos, char in special_positions}

        # Fill in the result
        for i in range(len(result)):
            if i in special_dict:
                result[i] = special_dict[i]
            else:
                if letter_index < len(scrambled_letters):
                    result[i] = scrambled_letters[letter_index]
                    letter_index += 1

        return ''.join(result)

    def generate_scramble(self, book_name: str, language: str, difficulty: str = 'medium') -> str:
        """
        Generate a scrambled version of a Bible book name.

        Args:
            book_name: The Bible book name to scramble
            language: 'english' or 'french'
            difficulty: 'easy', 'medium', or 'hard' (currently not implemented)

        Returns:
            Scrambled version of the book name
        """
        if language.lower() not in ['english', 'french']:
            raise ValueError("Language must be 'english' or 'french'")

        # Get the proper display name from our database
        book_data = get_book_by_display_name(book_name, language)
        if not book_data:
            raise ValueError(f"Bible book '{book_name}' not found in {language}")

        display_name = book_data['display_name']

        # Handle special cases based on the book's metadata
        special_handling = book_data.get('special_handling', None)

        if special_handling == 'compound':
            # For compound names like "Song of Songs", scramble each word separately
            return self._scramble_compound_name(display_name)
        else:
            # Standard scrambling with special character preservation
            letters, special_positions = self._extract_letters_for_scrambling(display_name)
            scrambled_letters = self._scramble_letters(letters)
            return self._reconstruct_text(scrambled_letters, special_positions)

    def _scramble_compound_name(self, text: str) -> str:
        """
        Scramble compound names like 'Song of Songs' by scrambling each word separately.

        Args:
            text: The compound name to scramble

        Returns:
            Scrambled version with word boundaries preserved
        """
        words = text.split()
        scrambled_words = []

        for word in words:
            # Don't scramble very short connector words (of, des, etc.)
            if len(word) <= 2 or word.lower() in ['of', 'des', 'de', 'du']:
                scrambled_words.append(word)
            else:
                letters, special_positions = self._extract_letters_for_scrambling(word)
                if len(letters) > 1:
                    scrambled_letters = self._scramble_letters(letters)
                    scrambled_word = self._reconstruct_text(scrambled_letters, special_positions)
                    scrambled_words.append(scrambled_word)
                else:
                    scrambled_words.append(word)

        return ' '.join(scrambled_words)

    def check_solution(self, scrambled: str, guess: str, language: str) -> bool:
        """
        Check if a guess correctly solves a scrambled Bible book name.

        Args:
            scrambled: The scrambled text (for reference, not used in validation)
            guess: The user's guess
            language: 'english' or 'french'

        Returns:
            True if the guess is a valid Bible book name, False otherwise
        """
        book_data = get_book_by_display_name(guess, language)
        return book_data is not None

    def validate_scramble_solution(self, original: str, scrambled: str, guess: str) -> bool:
        """
        Validate that a guess is the correct solution to a specific scramble.

        Args:
            original: The original Bible book name
            scrambled: The scrambled version
            guess: The user's guess

        Returns:
            True if guess matches the original (case-insensitive)
        """
        return self._normalize_book_name(original) == self._normalize_book_name(guess)

    def get_random_book(self, language: str, testament: str = 'any', category: str = 'any') -> str:
        """
        Get a random Bible book for scrambling.

        Args:
            language: 'english' or 'french'
            testament: 'old'/'ancien', 'new'/'nouveau', or 'any'
            category: Specific category or 'any'

        Returns:
            Random Bible book display name
        """
        books = self.english_books if language.lower() == 'english' else self.french_books

        # Filter by testament if specified
        if testament != 'any':
            if language.lower() == 'english':
                target_testament = 'old' if testament.lower() in ['old', 'ancien'] else 'new'
            else:
                target_testament = 'ancien' if testament.lower() in ['old', 'ancien'] else 'nouveau'

            books = {k: v for k, v in books.items() if v['testament'] == target_testament}

        # Filter by category if specified
        if category != 'any':
            books = {k: v for k, v in books.items() if v['category'] == category}

        if not books:
            raise ValueError(f"No books found with criteria: testament={testament}, category={category}")

        random_key = random.choice(list(books.keys()))
        return books[random_key]['display_name']

    def get_hint(self, book_name: str, language: str) -> str:
        """
        Provide a hint for a Bible book.

        Args:
            book_name: The Bible book name
            language: 'english' or 'french'

        Returns:
            A helpful hint about the book
        """
        book_data = get_book_by_display_name(book_name, language)
        if not book_data:
            return "Book not found"

        testament = book_data['testament']
        category = book_data['category']
        book_number = book_data['book_number']

        # Translate testament and category to user-friendly terms
        if language.lower() == 'english':
            testament_name = "Old Testament" if testament == 'old' else "New Testament"
            category_map = {
                'law': 'Law (Torah)',
                'history': 'Historical Books',
                'wisdom': 'Wisdom Literature',
                'major_prophets': 'Major Prophets',
                'minor_prophets': 'Minor Prophets',
                'gospels': 'Gospels',
                'pauline_epistles': 'Pauline Epistles',
                'general_epistles': 'General Epistles',
                'apocalyptic': 'Apocalyptic Literature'
            }
        else:
            testament_name = "Ancien Testament" if testament == 'ancien' else "Nouveau Testament"
            category_map = {
                'loi': 'Loi (Torah)',
                'histoire': 'Livres Historiques',
                'sagesse': 'Littérature de Sagesse',
                'grands_prophetes': 'Grands Prophètes',
                'petits_prophetes': 'Petits Prophètes',
                'evangiles': 'Évangiles',
                'epitres_pauliniennes': 'Épîtres Pauliniennes',
                'epitres_generales': 'Épîtres Générales',
                'apocalyptique': 'Littérature Apocalyptique'
            }

        category_name = category_map.get(category, category.replace('_', ' ').title())

        return f"{testament_name}, {category_name} (Book #{book_number})"

    def get_all_books_list(self, language: str) -> List[str]:
        """
        Get a list of all Bible book names in the specified language.

        Args:
            language: 'english' or 'french'

        Returns:
            List of all Bible book display names
        """
        books = self.english_books if language.lower() == 'english' else self.french_books
        return [book_data['display_name'] for book_data in books.values()]

def main():
    """Main function to run the Bible book scrambler tool"""
    scrambler = BibleBookScrambler()

    print("=== Bible Book Scrambler Tool ===")
    print("Scramble Bible book names in French or English for puzzle solving")
    print()

    while True:
        print("Choose an option:")
        print("1. Generate scramble from book name")
        print("2. Random scramble challenge")
        print("3. Solve mode - check your answer")
        print("4. Get hint for a book")
        print("5. List all Bible books")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '6':
            print("Goodbye!")
            break

        # Get language for all operations
        language = None
        if choice in ['1', '2', '3', '4', '5']:
            print("\nChoose language:")
            print("1. English")
            print("2. French")
            lang_choice = input("Enter language choice (1-2): ").strip()

            if lang_choice == '1':
                language = 'english'
            elif lang_choice == '2':
                language = 'french'
            else:
                print("Invalid language choice. Please enter 1 or 2.")
                continue

        try:
            if choice == '1':
                # Generate scramble from book name
                book_name = input(f"Enter a Bible book name in {language.title()}: ").strip()
                if book_name:
                    scrambled = scrambler.generate_scramble(book_name, language)
                    print(f"\nOriginal: {book_name}")
                    print(f"Scrambled: {scrambled}")

            elif choice == '2':
                # Random scramble challenge
                print("\nChoose testament:")
                print("1. Old Testament" + (" / Ancien Testament" if language == 'french' else ""))
                print("2. New Testament" + (" / Nouveau Testament" if language == 'french' else ""))
                print("3. Any")

                testament_choice = input("Enter testament choice (1-3): ").strip()
                testament = 'any'
                if testament_choice == '1':
                    testament = 'old' if language == 'english' else 'ancien'
                elif testament_choice == '2':
                    testament = 'new' if language == 'english' else 'nouveau'

                random_book = scrambler.get_random_book(language, testament)
                scrambled = scrambler.generate_scramble(random_book, language)
                hint = scrambler.get_hint(random_book, language)

                print(f"\nScrambled book: {scrambled}")
                print(f"Hint: {hint}")
                print("Can you guess which Bible book this is?")

                guess = input("Your guess: ").strip()
                if scrambler.validate_scramble_solution(random_book, scrambled, guess):
                    print("🎉 Correct! Well done!")
                else:
                    print(f"❌ Incorrect. The answer was: {random_book}")

            elif choice == '3':
                # Solve mode
                scrambled = input("Enter the scrambled Bible book: ").strip()
                guess = input("Enter your guess: ").strip()

                if scrambler.check_solution(scrambled, guess, language):
                    print("✅ Your guess is a valid Bible book!")
                else:
                    print("❌ That's not a valid Bible book name.")

            elif choice == '4':
                # Get hint
                book_name = input(f"Enter a Bible book name in {language.title()}: ").strip()
                if book_name:
                    hint = scrambler.get_hint(book_name, language)
                    print(f"\nHint for '{book_name}': {hint}")

            elif choice == '5':
                # List all books
                books = scrambler.get_all_books_list(language)
                print(f"\nAll 66 Bible books in {language.title()}:")
                for i, book in enumerate(books, 1):
                    print(f"{i:2d}. {book}")

            else:
                print("Invalid choice. Please enter 1-6.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    main()