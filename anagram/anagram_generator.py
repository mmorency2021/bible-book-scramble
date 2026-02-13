#!/usr/bin/env python3
"""
Anagram Generator Tool
Generates anagrams in French or English using the exact same letters as the original word.
"""

import random
from collections import Counter
from typing import List, Set

class AnagramGenerator:
    def __init__(self):
        self.french_words = self._load_french_words()
        self.english_words = self._load_english_words()

    def _load_french_words(self) -> Set[str]:
        """Load French word dictionary"""
        # Basic French word list - can be expanded
        french_words = {
            'chat', 'chien', 'maison', 'voiture', 'livre', 'école', 'ami', 'famille',
            'travail', 'temps', 'jour', 'nuit', 'eau', 'feu', 'terre', 'air',
            'rouge', 'bleu', 'vert', 'jaune', 'noir', 'blanc', 'grand', 'petit',
            'bon', 'mauvais', 'nouveau', 'vieux', 'jeune', 'beau', 'laid',
            'manger', 'boire', 'dormir', 'courir', 'marcher', 'parler', 'écouter',
            'voir', 'regarder', 'aimer', 'détester', 'venir', 'aller', 'partir',
            'arriver', 'rester', 'commencer', 'finir', 'continuer', 'arrêter',
            'ouvrir', 'fermer', 'donner', 'prendre', 'mettre', 'porter',
            'acheter', 'vendre', 'payer', 'gagner', 'perdre', 'jouer',
            'chanter', 'danser', 'rire', 'pleurer', 'sourire', 'crier',
            'silence', 'bruit', 'musique', 'chanson', 'film', 'théâtre',
            'sport', 'football', 'tennis', 'natation', 'course', 'vélo',
            'cuisine', 'restaurant', 'café', 'thé', 'pain', 'fromage',
            'viande', 'poisson', 'légume', 'fruit', 'pomme', 'orange',
            'banane', 'raisin', 'fraise', 'cerise', 'pêche', 'poire',
            'carotte', 'tomate', 'salade', 'pomme de terre', 'oignon',
            'argent', 'or', 'argent', 'bronze', 'fer', 'acier', 'bois',
            'pierre', 'verre', 'plastique', 'papier', 'tissu', 'coton',
            'soie', 'laine', 'cuir', 'métal', 'caoutchouc', 'ciment',
            # Added words that can form anagrams
            'tach', 'acre', 'race', 'care', 'arec', 'rame', 'mare', 'arme',
            'amer', 'réma', 'mera', 'aéro', 'orea', 'rose', 'sore', 'eros',
            'orse', 'reos', 'mots', 'toms', 'tome', 'temo', 'mote', 'moue',
            'noue', 'oune', 'nous', 'sons', 'nons', 'lire', 'rile', 'lier',
            'reli', 'iler', 'riel', 'vile', 'live', 'evil', 'veil', 'levi',
            'rive', 'vier', 'vire', 'iver', 'revi', 'vers', 'revs', 'sevr',
            'nets', 'tens', 'sent', 'nest', 'sten', 'tsen', 'ents', 'ante',
            'tena', 'nate', 'nota', 'aton', 'toan', 'otan', 'nito', 'tino',
            'soir', 'rois', 'oirs', 'sori', 'riso', 'iris', 'siri', 'riis'
        }
        return {word.lower() for word in french_words}

    def _load_english_words(self) -> Set[str]:
        """Load English word dictionary"""
        # Basic English word list - can be expanded
        english_words = {
            'cat', 'dog', 'house', 'car', 'book', 'school', 'friend', 'family',
            'work', 'time', 'day', 'night', 'water', 'fire', 'earth', 'air',
            'red', 'blue', 'green', 'yellow', 'black', 'white', 'big', 'small',
            'good', 'bad', 'new', 'old', 'young', 'beautiful', 'ugly',
            'eat', 'drink', 'sleep', 'run', 'walk', 'talk', 'listen',
            'see', 'watch', 'love', 'hate', 'come', 'go', 'leave',
            'arrive', 'stay', 'start', 'finish', 'continue', 'stop',
            'open', 'close', 'give', 'take', 'put', 'wear',
            'buy', 'sell', 'pay', 'win', 'lose', 'play',
            'sing', 'dance', 'laugh', 'cry', 'smile', 'shout',
            'silence', 'noise', 'music', 'song', 'movie', 'theater',
            'sport', 'football', 'tennis', 'swimming', 'running', 'bicycle',
            'kitchen', 'restaurant', 'coffee', 'tea', 'bread', 'cheese',
            'meat', 'fish', 'vegetable', 'fruit', 'apple', 'orange',
            'banana', 'grape', 'strawberry', 'cherry', 'peach', 'pear',
            'carrot', 'tomato', 'salad', 'potato', 'onion',
            'money', 'gold', 'silver', 'bronze', 'iron', 'steel', 'wood',
            'stone', 'glass', 'plastic', 'paper', 'fabric', 'cotton',
            'silk', 'wool', 'leather', 'metal', 'rubber', 'cement',
            'listen', 'silent', 'earth', 'heart', 'state', 'taste',
            'team', 'meat', 'mate', 'tame', 'time', 'item', 'emit',
            'dear', 'read', 'dare', 'care', 'race', 'acre', 'arc',
            'star', 'rats', 'arts', 'tars', 'tar', 'rat', 'art',
            'east', 'seat', 'teas', 'eats', 'sate', 'tea', 'eat', 'ate'
        }
        return {word.lower() for word in english_words}

    def _normalize_word(self, word: str) -> str:
        """Normalize word by converting to lowercase and removing spaces"""
        return word.lower().replace(' ', '')

    def _get_letter_count(self, word: str) -> Counter:
        """Get the count of each letter in the word"""
        return Counter(self._normalize_word(word))

    def _is_anagram(self, word1: str, word2: str) -> bool:
        """Check if two words are anagrams of each other"""
        return self._get_letter_count(word1) == self._get_letter_count(word2)

    def find_anagrams(self, word: str, language: str) -> List[str]:
        """Find all anagrams for a given word in the specified language"""
        word_normalized = self._normalize_word(word)

        if language.lower() == 'french':
            word_list = self.french_words
        elif language.lower() == 'english':
            word_list = self.english_words
        else:
            raise ValueError("Language must be 'french' or 'english'")

        anagrams = []
        for candidate in word_list:
            if candidate != word_normalized and self._is_anagram(word_normalized, candidate):
                anagrams.append(candidate)

        return anagrams

    def generate_random_anagram(self, word: str, language: str) -> str:
        """Generate a random anagram from the available anagrams"""
        anagrams = self.find_anagrams(word, language)
        if anagrams:
            return random.choice(anagrams)
        else:
            return None

def main():
    """Main function to run the anagram generator tool"""
    generator = AnagramGenerator()

    print("=== Anagram Generator Tool ===")
    print("Generate anagrams in French or English using exact letter matching")
    print()

    while True:
        # Ask for language
        print("Choose language:")
        print("1. English")
        print("2. French")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '3':
            print("Goodbye!")
            break
        elif choice == '1':
            language = 'english'
        elif choice == '2':
            language = 'french'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        # Ask for word
        word = input(f"Enter a word in {language.title()}: ").strip()

        if not word:
            print("Please enter a valid word.")
            continue

        try:
            # Find all anagrams
            anagrams = generator.find_anagrams(word, language)

            if anagrams:
                print(f"\nAnagrams found for '{word}':")
                for i, anagram in enumerate(anagrams, 1):
                    print(f"{i}. {anagram}")

                # Generate a random anagram
                random_anagram = generator.generate_random_anagram(word, language)
                print(f"\nRandom anagram: {random_anagram}")
            else:
                print(f"No anagrams found for '{word}' in {language}.")

        except ValueError as e:
            print(f"Error: {e}")

        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()