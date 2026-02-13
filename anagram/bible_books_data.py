#!/usr/bin/env python3
"""
Bible Books Data
Complete list of the 66 canonical Bible books in English and French
with metadata for the Bible book scrambler tool.
"""

from typing import Dict, Any

def get_english_bible_books() -> Dict[str, Dict[str, Any]]:
    """
    Get all 66 Bible books in English with metadata.

    Returns:
        Dictionary with normalized book names as keys and metadata as values
    """
    return {
        # OLD TESTAMENT - LAW (Torah/Pentateuch)
        "genesis": {
            "display_name": "Genesis",
            "testament": "old",
            "category": "law",
            "book_number": 1
        },
        "exodus": {
            "display_name": "Exodus",
            "testament": "old",
            "category": "law",
            "book_number": 2
        },
        "leviticus": {
            "display_name": "Leviticus",
            "testament": "old",
            "category": "law",
            "book_number": 3
        },
        "numbers": {
            "display_name": "Numbers",
            "testament": "old",
            "category": "law",
            "book_number": 4
        },
        "deuteronomy": {
            "display_name": "Deuteronomy",
            "testament": "old",
            "category": "law",
            "book_number": 5
        },

        # OLD TESTAMENT - HISTORY
        "joshua": {
            "display_name": "Joshua",
            "testament": "old",
            "category": "history",
            "book_number": 6
        },
        "judges": {
            "display_name": "Judges",
            "testament": "old",
            "category": "history",
            "book_number": 7
        },
        "ruth": {
            "display_name": "Ruth",
            "testament": "old",
            "category": "history",
            "book_number": 8
        },
        "1_samuel": {
            "display_name": "1 Samuel",
            "testament": "old",
            "category": "history",
            "book_number": 9,
            "special_handling": "numbered"
        },
        "2_samuel": {
            "display_name": "2 Samuel",
            "testament": "old",
            "category": "history",
            "book_number": 10,
            "special_handling": "numbered"
        },
        "1_kings": {
            "display_name": "1 Kings",
            "testament": "old",
            "category": "history",
            "book_number": 11,
            "special_handling": "numbered"
        },
        "2_kings": {
            "display_name": "2 Kings",
            "testament": "old",
            "category": "history",
            "book_number": 12,
            "special_handling": "numbered"
        },
        "1_chronicles": {
            "display_name": "1 Chronicles",
            "testament": "old",
            "category": "history",
            "book_number": 13,
            "special_handling": "numbered"
        },
        "2_chronicles": {
            "display_name": "2 Chronicles",
            "testament": "old",
            "category": "history",
            "book_number": 14,
            "special_handling": "numbered"
        },
        "ezra": {
            "display_name": "Ezra",
            "testament": "old",
            "category": "history",
            "book_number": 15
        },
        "nehemiah": {
            "display_name": "Nehemiah",
            "testament": "old",
            "category": "history",
            "book_number": 16
        },
        "esther": {
            "display_name": "Esther",
            "testament": "old",
            "category": "history",
            "book_number": 17
        },

        # OLD TESTAMENT - WISDOM & POETRY
        "job": {
            "display_name": "Job",
            "testament": "old",
            "category": "wisdom",
            "book_number": 18
        },
        "psalms": {
            "display_name": "Psalms",
            "testament": "old",
            "category": "wisdom",
            "book_number": 19
        },
        "proverbs": {
            "display_name": "Proverbs",
            "testament": "old",
            "category": "wisdom",
            "book_number": 20
        },
        "ecclesiastes": {
            "display_name": "Ecclesiastes",
            "testament": "old",
            "category": "wisdom",
            "book_number": 21
        },
        "song_of_songs": {
            "display_name": "Song of Songs",
            "testament": "old",
            "category": "wisdom",
            "book_number": 22,
            "special_handling": "compound",
            "alternate_names": ["Song of Solomon"]
        },

        # OLD TESTAMENT - MAJOR PROPHETS
        "isaiah": {
            "display_name": "Isaiah",
            "testament": "old",
            "category": "major_prophets",
            "book_number": 23
        },
        "jeremiah": {
            "display_name": "Jeremiah",
            "testament": "old",
            "category": "major_prophets",
            "book_number": 24
        },
        "lamentations": {
            "display_name": "Lamentations",
            "testament": "old",
            "category": "major_prophets",
            "book_number": 25
        },
        "ezekiel": {
            "display_name": "Ezekiel",
            "testament": "old",
            "category": "major_prophets",
            "book_number": 26
        },
        "daniel": {
            "display_name": "Daniel",
            "testament": "old",
            "category": "major_prophets",
            "book_number": 27
        },

        # OLD TESTAMENT - MINOR PROPHETS
        "hosea": {
            "display_name": "Hosea",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 28
        },
        "joel": {
            "display_name": "Joel",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 29
        },
        "amos": {
            "display_name": "Amos",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 30
        },
        "obadiah": {
            "display_name": "Obadiah",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 31
        },
        "jonah": {
            "display_name": "Jonah",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 32
        },
        "micah": {
            "display_name": "Micah",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 33
        },
        "nahum": {
            "display_name": "Nahum",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 34
        },
        "habakkuk": {
            "display_name": "Habakkuk",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 35
        },
        "zephaniah": {
            "display_name": "Zephaniah",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 36
        },
        "haggai": {
            "display_name": "Haggai",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 37
        },
        "zechariah": {
            "display_name": "Zechariah",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 38
        },
        "malachi": {
            "display_name": "Malachi",
            "testament": "old",
            "category": "minor_prophets",
            "book_number": 39
        },

        # NEW TESTAMENT - GOSPELS
        "matthew": {
            "display_name": "Matthew",
            "testament": "new",
            "category": "gospels",
            "book_number": 40
        },
        "mark": {
            "display_name": "Mark",
            "testament": "new",
            "category": "gospels",
            "book_number": 41
        },
        "luke": {
            "display_name": "Luke",
            "testament": "new",
            "category": "gospels",
            "book_number": 42
        },
        "john": {
            "display_name": "John",
            "testament": "new",
            "category": "gospels",
            "book_number": 43
        },

        # NEW TESTAMENT - HISTORY
        "acts": {
            "display_name": "Acts",
            "testament": "new",
            "category": "history",
            "book_number": 44
        },

        # NEW TESTAMENT - PAULINE EPISTLES
        "romans": {
            "display_name": "Romans",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 45
        },
        "1_corinthians": {
            "display_name": "1 Corinthians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 46,
            "special_handling": "numbered"
        },
        "2_corinthians": {
            "display_name": "2 Corinthians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 47,
            "special_handling": "numbered"
        },
        "galatians": {
            "display_name": "Galatians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 48
        },
        "ephesians": {
            "display_name": "Ephesians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 49
        },
        "philippians": {
            "display_name": "Philippians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 50
        },
        "colossians": {
            "display_name": "Colossians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 51
        },
        "1_thessalonians": {
            "display_name": "1 Thessalonians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 52,
            "special_handling": "numbered"
        },
        "2_thessalonians": {
            "display_name": "2 Thessalonians",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 53,
            "special_handling": "numbered"
        },
        "1_timothy": {
            "display_name": "1 Timothy",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 54,
            "special_handling": "numbered"
        },
        "2_timothy": {
            "display_name": "2 Timothy",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 55,
            "special_handling": "numbered"
        },
        "titus": {
            "display_name": "Titus",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 56
        },
        "philemon": {
            "display_name": "Philemon",
            "testament": "new",
            "category": "pauline_epistles",
            "book_number": 57
        },

        # NEW TESTAMENT - GENERAL EPISTLES
        "hebrews": {
            "display_name": "Hebrews",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 58
        },
        "james": {
            "display_name": "James",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 59
        },
        "1_peter": {
            "display_name": "1 Peter",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 60,
            "special_handling": "numbered"
        },
        "2_peter": {
            "display_name": "2 Peter",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 61,
            "special_handling": "numbered"
        },
        "1_john": {
            "display_name": "1 John",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 62,
            "special_handling": "numbered"
        },
        "2_john": {
            "display_name": "2 John",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 63,
            "special_handling": "numbered"
        },
        "3_john": {
            "display_name": "3 John",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 64,
            "special_handling": "numbered"
        },
        "jude": {
            "display_name": "Jude",
            "testament": "new",
            "category": "general_epistles",
            "book_number": 65
        },

        # NEW TESTAMENT - APOCALYPTIC
        "revelation": {
            "display_name": "Revelation",
            "testament": "new",
            "category": "apocalyptic",
            "book_number": 66,
            "alternate_names": ["Apocalypse"]
        }
    }

def get_french_bible_books() -> Dict[str, Dict[str, Any]]:
    """
    Get all 66 Bible books in French with metadata.

    Returns:
        Dictionary with normalized book names as keys and metadata as values
    """
    return {
        # ANCIEN TESTAMENT - LOI (Torah/Pentateuque)
        "genese": {
            "display_name": "Genèse",
            "testament": "ancien",
            "category": "loi",
            "book_number": 1,
            "special_handling": "accented"
        },
        "exode": {
            "display_name": "Exode",
            "testament": "ancien",
            "category": "loi",
            "book_number": 2
        },
        "levitique": {
            "display_name": "Lévitique",
            "testament": "ancien",
            "category": "loi",
            "book_number": 3,
            "special_handling": "accented"
        },
        "nombres": {
            "display_name": "Nombres",
            "testament": "ancien",
            "category": "loi",
            "book_number": 4
        },
        "deuteronome": {
            "display_name": "Deutéronome",
            "testament": "ancien",
            "category": "loi",
            "book_number": 5,
            "special_handling": "accented"
        },

        # ANCIEN TESTAMENT - HISTOIRE
        "josue": {
            "display_name": "Josué",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 6,
            "special_handling": "accented"
        },
        "juges": {
            "display_name": "Juges",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 7
        },
        "ruth": {
            "display_name": "Ruth",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 8
        },
        "1_samuel": {
            "display_name": "1 Samuel",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 9,
            "special_handling": "numbered"
        },
        "2_samuel": {
            "display_name": "2 Samuel",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 10,
            "special_handling": "numbered"
        },
        "1_rois": {
            "display_name": "1 Rois",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 11,
            "special_handling": "numbered"
        },
        "2_rois": {
            "display_name": "2 Rois",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 12,
            "special_handling": "numbered"
        },
        "1_chroniques": {
            "display_name": "1 Chroniques",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 13,
            "special_handling": "numbered"
        },
        "2_chroniques": {
            "display_name": "2 Chroniques",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 14,
            "special_handling": "numbered"
        },
        "esdras": {
            "display_name": "Esdras",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 15
        },
        "nehemie": {
            "display_name": "Néhémie",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 16,
            "special_handling": "accented"
        },
        "esther": {
            "display_name": "Esther",
            "testament": "ancien",
            "category": "histoire",
            "book_number": 17
        },

        # ANCIEN TESTAMENT - SAGESSE & POÉSIE
        "job": {
            "display_name": "Job",
            "testament": "ancien",
            "category": "sagesse",
            "book_number": 18
        },
        "psaumes": {
            "display_name": "Psaumes",
            "testament": "ancien",
            "category": "sagesse",
            "book_number": 19
        },
        "proverbes": {
            "display_name": "Proverbes",
            "testament": "ancien",
            "category": "sagesse",
            "book_number": 20
        },
        "ecclesiaste": {
            "display_name": "Ecclésiaste",
            "testament": "ancien",
            "category": "sagesse",
            "book_number": 21,
            "special_handling": "accented"
        },
        "cantique_des_cantiques": {
            "display_name": "Cantique des Cantiques",
            "testament": "ancien",
            "category": "sagesse",
            "book_number": 22,
            "special_handling": "compound"
        },

        # ANCIEN TESTAMENT - GRANDS PROPHÈTES
        "esaie": {
            "display_name": "Ésaïe",
            "testament": "ancien",
            "category": "grands_prophetes",
            "book_number": 23,
            "special_handling": "accented"
        },
        "jeremie": {
            "display_name": "Jérémie",
            "testament": "ancien",
            "category": "grands_prophetes",
            "book_number": 24,
            "special_handling": "accented"
        },
        "lamentations": {
            "display_name": "Lamentations",
            "testament": "ancien",
            "category": "grands_prophetes",
            "book_number": 25
        },
        "ezechiel": {
            "display_name": "Ézéchiel",
            "testament": "ancien",
            "category": "grands_prophetes",
            "book_number": 26,
            "special_handling": "accented"
        },
        "daniel": {
            "display_name": "Daniel",
            "testament": "ancien",
            "category": "grands_prophetes",
            "book_number": 27
        },

        # ANCIEN TESTAMENT - PETITS PROPHÈTES
        "osee": {
            "display_name": "Osée",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 28,
            "special_handling": "accented"
        },
        "joel": {
            "display_name": "Joël",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 29,
            "special_handling": "accented"
        },
        "amos": {
            "display_name": "Amos",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 30
        },
        "abdias": {
            "display_name": "Abdias",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 31
        },
        "jonas": {
            "display_name": "Jonas",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 32
        },
        "michee": {
            "display_name": "Michée",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 33,
            "special_handling": "accented"
        },
        "nahum": {
            "display_name": "Nahum",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 34
        },
        "habacuc": {
            "display_name": "Habacuc",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 35
        },
        "sophonie": {
            "display_name": "Sophonie",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 36
        },
        "aggee": {
            "display_name": "Aggée",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 37,
            "special_handling": "accented"
        },
        "zacharie": {
            "display_name": "Zacharie",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 38
        },
        "malachie": {
            "display_name": "Malachie",
            "testament": "ancien",
            "category": "petits_prophetes",
            "book_number": 39
        },

        # NOUVEAU TESTAMENT - ÉVANGILES
        "matthieu": {
            "display_name": "Matthieu",
            "testament": "nouveau",
            "category": "evangiles",
            "book_number": 40
        },
        "marc": {
            "display_name": "Marc",
            "testament": "nouveau",
            "category": "evangiles",
            "book_number": 41
        },
        "luc": {
            "display_name": "Luc",
            "testament": "nouveau",
            "category": "evangiles",
            "book_number": 42
        },
        "jean": {
            "display_name": "Jean",
            "testament": "nouveau",
            "category": "evangiles",
            "book_number": 43
        },

        # NOUVEAU TESTAMENT - HISTOIRE
        "actes": {
            "display_name": "Actes",
            "testament": "nouveau",
            "category": "histoire",
            "book_number": 44
        },

        # NOUVEAU TESTAMENT - ÉPÎTRES PAULINIENNES
        "romains": {
            "display_name": "Romains",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 45
        },
        "1_corinthiens": {
            "display_name": "1 Corinthiens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 46,
            "special_handling": "numbered"
        },
        "2_corinthiens": {
            "display_name": "2 Corinthiens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 47,
            "special_handling": "numbered"
        },
        "galates": {
            "display_name": "Galates",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 48
        },
        "ephesiens": {
            "display_name": "Éphésiens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 49,
            "special_handling": "accented"
        },
        "philippiens": {
            "display_name": "Philippiens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 50
        },
        "colossiens": {
            "display_name": "Colossiens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 51
        },
        "1_thessaloniciens": {
            "display_name": "1 Thessaloniciens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 52,
            "special_handling": "numbered"
        },
        "2_thessaloniciens": {
            "display_name": "2 Thessaloniciens",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 53,
            "special_handling": "numbered"
        },
        "1_timothee": {
            "display_name": "1 Timothée",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 54,
            "special_handling": "numbered_accented"
        },
        "2_timothee": {
            "display_name": "2 Timothée",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 55,
            "special_handling": "numbered_accented"
        },
        "tite": {
            "display_name": "Tite",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 56
        },
        "philemon": {
            "display_name": "Philémon",
            "testament": "nouveau",
            "category": "epitres_pauliniennes",
            "book_number": 57,
            "special_handling": "accented"
        },

        # NOUVEAU TESTAMENT - ÉPÎTRES GÉNÉRALES
        "hebreux": {
            "display_name": "Hébreux",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 58,
            "special_handling": "accented"
        },
        "jacques": {
            "display_name": "Jacques",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 59
        },
        "1_pierre": {
            "display_name": "1 Pierre",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 60,
            "special_handling": "numbered"
        },
        "2_pierre": {
            "display_name": "2 Pierre",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 61,
            "special_handling": "numbered"
        },
        "1_jean": {
            "display_name": "1 Jean",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 62,
            "special_handling": "numbered"
        },
        "2_jean": {
            "display_name": "2 Jean",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 63,
            "special_handling": "numbered"
        },
        "3_jean": {
            "display_name": "3 Jean",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 64,
            "special_handling": "numbered"
        },
        "jude": {
            "display_name": "Jude",
            "testament": "nouveau",
            "category": "epitres_generales",
            "book_number": 65
        },

        # NOUVEAU TESTAMENT - APOCALYPTIQUE
        "apocalypse": {
            "display_name": "Apocalypse",
            "testament": "nouveau",
            "category": "apocalyptique",
            "book_number": 66
        }
    }

def get_book_by_display_name(display_name: str, language: str) -> Dict[str, Any]:
    """
    Find a Bible book by its display name.

    Args:
        display_name: The display name to search for
        language: 'english' or 'french'

    Returns:
        Book data dictionary or None if not found
    """
    books = get_english_bible_books() if language.lower() == 'english' else get_french_bible_books()

    # Normalize the input for comparison
    normalized_input = display_name.lower().replace(' ', '_')

    # Direct lookup
    if normalized_input in books:
        return books[normalized_input]

    # Search by display name
    for book_key, book_data in books.items():
        if book_data["display_name"].lower() == display_name.lower():
            return book_data

        # Check alternate names if they exist
        if "alternate_names" in book_data:
            for alt_name in book_data["alternate_names"]:
                if alt_name.lower() == display_name.lower():
                    return book_data

    return None

def get_books_by_testament(testament: str, language: str) -> Dict[str, Dict[str, Any]]:
    """
    Get all books from a specific testament.

    Args:
        testament: 'old'/'ancien' or 'new'/'nouveau'
        language: 'english' or 'french'

    Returns:
        Dictionary of books from the specified testament
    """
    books = get_english_bible_books() if language.lower() == 'english' else get_french_bible_books()

    # Normalize testament names
    if language.lower() == 'english':
        target_testament = 'old' if testament.lower() in ['old', 'ancien'] else 'new'
    else:
        target_testament = 'ancien' if testament.lower() in ['old', 'ancien'] else 'nouveau'

    return {key: data for key, data in books.items() if data['testament'] == target_testament}

if __name__ == "__main__":
    # Test the data structure
    english_books = get_english_bible_books()
    french_books = get_french_bible_books()

    print(f"English Bible books loaded: {len(english_books)}")
    print(f"French Bible books loaded: {len(french_books)}")

    # Test a few lookups
    print(f"\nGenesis data: {english_books['genesis']}")
    print(f"Genèse data: {french_books['genese']}")
    print(f"1 Samuel data: {english_books['1_samuel']}")
    print(f"1 Corinthiens data: {french_books['1_corinthiens']}")