#!/usr/bin/env python3
"""
Test script for the Bible Book Scrambler
"""

import re
from bible_book_scrambler import BibleBookScrambler

def test_basic_scrambling():
    """Test basic scrambling functionality"""
    print("=== Testing Basic Scrambling ===")
    scrambler = BibleBookScrambler()

    # Test simple English books
    english_test_books = ['Genesis', 'Exodus', 'Job', 'Mark', 'Acts']

    for book in english_test_books:
        scrambled = scrambler.generate_scramble(book, 'english')
        print(f"'{book}' -> '{scrambled}'")

        # Verify letters are the same (just reordered)
        original_letters = sorted([c.lower() for c in book if c.isalpha()])
        scrambled_letters = sorted([c.lower() for c in scrambled if c.isalpha()])

        status = "✓" if original_letters == scrambled_letters else "✗"
        print(f"  {status} Letter preservation check")

        # Verify it's actually scrambled (different from original)
        if book.lower() != scrambled.lower():
            print(f"  ✓ Successfully scrambled")
        else:
            print(f"  ⚠ Not scrambled (may happen with very short words)")

    print()

def test_special_character_preservation():
    """Test preservation of numbers, spaces, and accents"""
    print("=== Testing Special Character Preservation ===")
    scrambler = BibleBookScrambler()

    # Test numbered books
    numbered_books = [
        ('1 Samuel', 'english'),
        ('2 Kings', 'english'),
        ('1 Corinthians', 'english'),
        ('1 Corinthiens', 'french'),
        ('2 Timothée', 'french')
    ]

    for book, language in numbered_books:
        scrambled = scrambler.generate_scramble(book, language)
        print(f"'{book}' -> '{scrambled}'")

        # Check that numbers and spaces are preserved
        original_non_letters = [c for c in book if not c.isalpha()]
        scrambled_non_letters = [c for c in scrambled if not c.isalpha()]

        status = "✓" if original_non_letters == scrambled_non_letters else "✗"
        print(f"  {status} Numbers and spaces preserved: {original_non_letters} == {scrambled_non_letters}")

    print()

    # Test accented characters
    print("Testing French accented books:")
    accented_books = ['Genèse', 'Lévitique', 'Ésaïe', 'Jérémie', 'Ézéchiel']

    for book in accented_books:
        scrambled = scrambler.generate_scramble(book, 'french')
        print(f"'{book}' -> '{scrambled}'")

        # Check that accents are preserved on letters
        original_accents = [c for c in book if c in 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ']
        scrambled_accents = [c for c in scrambled if c in 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ']

        # Count should be the same
        status = "✓" if len(original_accents) == len(scrambled_accents) else "✗"
        print(f"  {status} Accented character count preserved")

    print()

def test_compound_names():
    """Test handling of compound Bible book names"""
    print("=== Testing Compound Names ===")
    scrambler = BibleBookScrambler()

    compound_books = [
        ('Song of Songs', 'english'),
        ('Cantique des Cantiques', 'french')
    ]

    for book, language in compound_books:
        scrambled = scrambler.generate_scramble(book, language)
        print(f"'{book}' -> '{scrambled}'")

        # Check that word boundaries are preserved
        original_words = book.split()
        scrambled_words = scrambled.split()

        status = "✓" if len(original_words) == len(scrambled_words) else "✗"
        print(f"  {status} Word count preserved: {len(original_words)} words")

        # Check that small connector words are preserved
        small_words = ['of', 'des', 'de', 'du']
        for i, (orig_word, scram_word) in enumerate(zip(original_words, scrambled_words)):
            if orig_word.lower() in small_words:
                status = "✓" if orig_word == scram_word else "✗"
                print(f"  {status} Small word '{orig_word}' preserved")

    print()

def test_solution_validation():
    """Test solution checking functionality"""
    print("=== Testing Solution Validation ===")
    scrambler = BibleBookScrambler()

    # Test valid Bible books
    valid_books = [
        ('Genesis', 'english'),
        ('Revelation', 'english'),
        ('Genèse', 'french'),
        ('Apocalypse', 'french'),
        ('1 Samuel', 'english'),
        ('2 Corinthiens', 'french')
    ]

    print("Testing valid Bible books:")
    for book, language in valid_books:
        is_valid = scrambler.check_solution("", book, language)
        status = "✓" if is_valid else "✗"
        print(f"  {status} '{book}' recognized as valid {language} Bible book")

    print()

    # Test invalid books
    invalid_books = [
        ('NotABook', 'english'),
        ('FakeBook', 'french'),
        ('Random Word', 'english'),
        ('Livre Invalide', 'french')
    ]

    print("Testing invalid books:")
    for book, language in invalid_books:
        is_valid = scrambler.check_solution("", book, language)
        status = "✓" if not is_valid else "✗"
        print(f"  {status} '{book}' correctly rejected as invalid {language} book")

    print()

def test_scramble_solution_validation():
    """Test that scrambles can be solved back to original"""
    print("=== Testing Scramble-Solution Validation ===")
    scrambler = BibleBookScrambler()

    test_books = [
        ('Genesis', 'english'),
        ('Matthew', 'english'),
        ('Genèse', 'french'),
        ('Matthieu', 'french'),
        ('1 Samuel', 'english'),
        ('1 Corinthiens', 'french')
    ]

    for book, language in test_books:
        scrambled = scrambler.generate_scramble(book, language)
        is_correct = scrambler.validate_scramble_solution(book, scrambled, book)

        status = "✓" if is_correct else "✗"
        print(f"{status} '{book}' -> '{scrambled}' -> validates back to '{book}'")

        # Test case insensitive matching
        is_correct_lower = scrambler.validate_scramble_solution(book, scrambled, book.lower())
        status = "✓" if is_correct_lower else "✗"
        print(f"  {status} Case insensitive validation works")

    print()

def test_hint_system():
    """Test the hint generation system"""
    print("=== Testing Hint System ===")
    scrambler = BibleBookScrambler()

    test_books = [
        ('Genesis', 'english', 'Old Testament'),
        ('Matthew', 'english', 'New Testament'),
        ('Revelation', 'english', 'New Testament'),
        ('Genèse', 'french', 'Ancien Testament'),
        ('Matthieu', 'french', 'Nouveau Testament'),
        ('Apocalypse', 'french', 'Nouveau Testament')
    ]

    for book, language, expected_testament in test_books:
        hint = scrambler.get_hint(book, language)
        print(f"'{book}' ({language}): {hint}")

        # Check that hint contains expected testament
        status = "✓" if expected_testament in hint else "✗"
        print(f"  {status} Contains expected testament reference")

    print()

def test_random_book_selection():
    """Test random book selection functionality"""
    print("=== Testing Random Book Selection ===")
    scrambler = BibleBookScrambler()

    # Test basic random selection
    languages = ['english', 'french']
    for language in languages:
        random_book = scrambler.get_random_book(language)
        is_valid = scrambler.check_solution("", random_book, language)
        status = "✓" if is_valid else "✗"
        print(f"{status} Random {language} book: '{random_book}'")

    print()

    # Test testament filtering
    testament_tests = [
        ('english', 'old', 'Old Testament'),
        ('english', 'new', 'New Testament'),
        ('french', 'ancien', 'Ancien Testament'),
        ('french', 'nouveau', 'Nouveau Testament')
    ]

    for language, testament, expected in testament_tests:
        random_book = scrambler.get_random_book(language, testament)
        hint = scrambler.get_hint(random_book, language)

        status = "✓" if expected in hint else "✗"
        print(f"{status} Random {language} {testament} book: '{random_book}' (hint confirms testament)")

    print()

def test_edge_cases():
    """Test edge cases and error handling"""
    print("=== Testing Edge Cases ===")
    scrambler = BibleBookScrambler()

    # Test shortest book names
    short_books = ['Job', 'Ruth', 'Acts', 'Mark', 'Luke', 'John', 'Jude']

    print("Testing shortest book names:")
    for book in short_books:
        try:
            scrambled = scrambler.generate_scramble(book, 'english')
            print(f"  ✓ '{book}' -> '{scrambled}' (length: {len(book)})")
        except Exception as e:
            print(f"  ✗ Error with '{book}': {e}")

    print()

    # Test longest book names
    long_books = ['Ecclesiastes', '1 Thessalonians', '2 Thessalonians', 'Song of Songs']

    print("Testing longest book names:")
    for book in long_books:
        try:
            scrambled = scrambler.generate_scramble(book, 'english')
            print(f"  ✓ '{book}' -> '{scrambled}' (length: {len(book)})")
        except Exception as e:
            print(f"  ✗ Error with '{book}': {e}")

    print()

    # Test error handling
    print("Testing error handling:")
    try:
        scrambler.generate_scramble('NonExistentBook', 'english')
        print("  ✗ Should have raised error for non-existent book")
    except ValueError:
        print("  ✓ Correctly raised error for non-existent book")

    try:
        scrambler.generate_scramble('Genesis', 'invalid_language')
        print("  ✗ Should have raised error for invalid language")
    except ValueError:
        print("  ✓ Correctly raised error for invalid language")

    print()

def test_all_66_books():
    """Test that all 66 Bible books can be scrambled successfully"""
    print("=== Testing All 66 Bible Books ===")
    scrambler = BibleBookScrambler()

    languages = ['english', 'french']

    for language in languages:
        print(f"Testing all books in {language}:")
        books = scrambler.get_all_books_list(language)

        success_count = 0
        total_count = len(books)

        for book in books:
            try:
                scrambled = scrambler.generate_scramble(book, language)
                success_count += 1

                # Quick validation that scrambling worked
                original_letters = sorted([c.lower() for c in book if c.isalpha()])
                scrambled_letters = sorted([c.lower() for c in scrambled if c.isalpha()])

                if original_letters != scrambled_letters:
                    print(f"  ✗ Letter mismatch in '{book}' -> '{scrambled}'")
                    success_count -= 1

            except Exception as e:
                print(f"  ✗ Error with '{book}': {e}")

        print(f"  Result: {success_count}/{total_count} books successfully scrambled")

        if success_count == 66:
            print(f"  ✅ All 66 {language} books scrambled successfully!")
        else:
            print(f"  ⚠ {66 - success_count} books had issues")

    print()

def main():
    """Run all tests"""
    print("🔬 Bible Book Scrambler Test Suite")
    print("=" * 50)
    print()

    test_basic_scrambling()
    test_special_character_preservation()
    test_compound_names()
    test_solution_validation()
    test_scramble_solution_validation()
    test_hint_system()
    test_random_book_selection()
    test_edge_cases()
    test_all_66_books()

    print("=" * 50)
    print("✅ Test suite completed!")
    print()
    print("If all tests show ✓ marks, the Bible Book Scrambler is working correctly.")

if __name__ == "__main__":
    main()