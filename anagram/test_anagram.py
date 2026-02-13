#!/usr/bin/env python3
"""
Test script for the anagram generator
"""

from anagram_generator import AnagramGenerator

def test_anagram_generator():
    """Test the anagram generator functionality"""
    generator = AnagramGenerator()

    print("=== Testing Anagram Generator ===")
    print()

    # Test English anagrams
    print("Testing English anagrams:")
    english_test_words = ['listen', 'earth', 'star', 'east', 'team']

    for word in english_test_words:
        anagrams = generator.find_anagrams(word, 'english')
        print(f"'{word}' -> {anagrams}")

    print()

    # Test French anagrams (note: the basic word list might have limited anagrams)
    print("Testing French anagrams:")
    french_test_words = ['chat', 'eau', 'ami', 'bon']

    for word in french_test_words:
        anagrams = generator.find_anagrams(word, 'french')
        print(f"'{word}' -> {anagrams}")

    print()

    # Test anagram detection logic
    print("Testing anagram detection logic:")
    test_cases = [
        ('listen', 'silent', True),
        ('earth', 'heart', True),
        ('star', 'rats', True),
        ('hello', 'world', False),
        ('cat', 'act', True),
        ('test', 'best', False)
    ]

    for word1, word2, expected in test_cases:
        result = generator._is_anagram(word1, word2)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{word1}' and '{word2}' are anagrams: {result} (expected: {expected})")

if __name__ == "__main__":
    test_anagram_generator()