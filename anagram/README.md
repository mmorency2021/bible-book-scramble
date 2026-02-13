# Bible Book Scrambler - CLI & Web Application

A comprehensive Bible book scrambling application available in both **Command Line Interface (CLI)** and **Web Application** formats. Creates word puzzles from the 66 canonical Bible books in French and English.

## Features

### 🎯 Core Features
- **Complete Bible Coverage**: All 66 canonical Bible books in both languages
- **Bilingual Support**: English and French Bible book names with proper accents
- **Smart Scrambling**: Preserves numbers, spaces, and accented characters while scrambling letters
- **Special Handling**: Proper support for numbered books (1 Samuel), compound names (Song of Songs), and accented French names (Lévitique)
- **Multiple Game Modes**: Generate, random challenge, solve, hints, and listing modes
- **Comprehensive Testing**: Full test suite ensuring all books work correctly

### 💻 CLI Features
- **Interactive Menu System**: User-friendly numbered menu interface
- **Direct Command Line**: Scriptable command-line usage for automation
- **Testament Filtering**: Focus on Old Testament, New Testament, or both
- **Instant Feedback**: Immediate results with emoji indicators

### 🌐 Web Features
- **Beautiful Interface**: Modern responsive web design that works on all devices
- **Score Tracking**: Persistent game statistics with streaks and totals
- **Real-time Gaming**: Interactive web interface with smooth animations
- **API Access**: RESTful endpoints for integration with other applications

## 🚀 Quick Start

### Web Application (Recommended)
```bash
cd web/
python3 app.py
```
Then open your browser to: **http://localhost:5000**

### Command Line Interface
```bash
python3 bible_scrambler_cli.py
```

## Files & Structure

### 📁 CLI Application Files
- `bible_book_scrambler.py` - Main scrambler class and interactive interface
- `bible_scrambler_cli.py` - Command line interface with multiple modes
- `bible_books_data.py` - Complete database of 66 Bible books in both languages
- `anagram_generator.py` - General anagram utilities
- `anagram_cli.py` - General anagram CLI tool
- `test_bible_scrambler.py` - Comprehensive test suite
- `test_anagram.py` - Anagram utility tests
- `README.md` - This documentation

### 🌐 Web Application Files (`web/` directory)
- `app.py` - Flask web server with REST API
- `templates/index.html` - Main game interface
- `static/css/style.css` - Beautiful responsive styling
- `static/js/script.js` - Interactive game logic
- `start_server.sh` - Easy startup script
- `requirements.txt` - Web dependencies
- `Procfile` & `runtime.txt` - Deployment configuration

## Usage

### 🌐 Web Application

The web interface provides a beautiful, interactive gaming experience:

```bash
cd web/
python3 app.py
```

**Features:**
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Score Tracking**: Persistent statistics with streaks and totals
- **Multiple Game Modes**: Random challenges, custom scrambles, Bible reference
- **Beautiful Interface**: Modern gradient design with smooth animations
- **Testament Filtering**: Focus on Old Testament, New Testament, or both
- **Instant Feedback**: Color-coded results with celebratory animations

**Game Controls:**
1. Choose your language (English/Français)
2. Select testament preference (Old/New/Any)
3. Click "New Challenge" for random scrambles
4. Use "Custom Scramble" to scramble specific books
5. Access "Show All Books" for complete reference

### 💻 CLI Interactive Mode

Run the main script for a terminal-based interactive experience:

```bash
# From the parent directory
python3 anagram/bible_book_scrambler.py

# Or from within the anagram directory
python3 bible_book_scrambler.py
```

The interactive tool provides these options:
1. **Generate scramble from book name** - Enter a Bible book and get its scrambled version
2. **Random scramble challenge** - Get a random scrambled book to solve
3. **Solve mode** - Check if your guess is a valid Bible book
4. **Get hint for a book** - Learn about a Bible book's testament and category
5. **List all Bible books** - Display all 66 books in your chosen language
6. **Quit** - Exit the program

### 💻 Command Line Interface

The CLI supports multiple modes for different use cases:

#### Generate Mode
Create a scrambled version of a specific Bible book:

```bash
# From parent directory
python3 anagram/bible_scrambler_cli.py generate "Genesis" english
python3 anagram/bible_scrambler_cli.py generate "Lévitique" french

# From within anagram directory
python3 bible_scrambler_cli.py generate "1 Samuel" english
python3 bible_scrambler_cli.py generate "Cantique des Cantiques" french
```

#### Random Challenge Mode
Get a random scrambled Bible book to solve:

```bash
# Any book in the language
python3 bible_scrambler_cli.py random english
python3 bible_scrambler_cli.py random french

# Filter by testament
python3 bible_scrambler_cli.py random english old    # Old Testament only
python3 bible_scrambler_cli.py random french new     # New Testament only
```

#### Solve Mode
Check if a guess correctly solves a scramble:

```bash
python3 bible_scrambler_cli.py solve "sneeGi" "Genesis" english
python3 bible_scrambler_cli.py solve "éqLiutive" "Lévitique" french
```

#### Hint Mode
Get helpful information about a Bible book:

```bash
python3 bible_scrambler_cli.py hint "Genesis" english
python3 bible_scrambler_cli.py hint "Apocalypse" french
```

#### List Mode
Display all Bible books in a language:

```bash
python3 bible_scrambler_cli.py list english
python3 bible_scrambler_cli.py list french
```

### Testing

Run the comprehensive test suite to verify all functionality:

```bash
# From the parent directory
python3 anagram/test_bible_scrambler.py

# From within the anagram directory
cd anagram
python3 test_bible_scrambler.py
```

The test suite validates:
- Basic scrambling for all 66 books in both languages
- Special character preservation (numbers, spaces, accents)
- Compound name handling
- Solution validation
- Hint system accuracy
- Random book selection
- Edge cases and error handling

## How It Works

### Scrambling Algorithm

1. **Letter Extraction**: Identifies alphabetic characters to scramble while preserving the positions of numbers, spaces, and punctuation
2. **Smart Shuffling**: Randomly rearranges letters while ensuring the result differs from the original
3. **Character Preservation**: Maintains accented characters (é, è, à, etc.) and special formatting
4. **Text Reconstruction**: Rebuilds the text with scrambled letters in their new positions and special characters in their original positions

### Special Case Handling

- **Numbered Books**: `"1 Samuel" → "1 lmuaSe"` (number and space preserved)
- **Accented Characters**: `"Lévitique" → "tvLiuqéei"` (accent maintained on letters)
- **Compound Names**: `"Song of Songs" → "gnSo of Snsgo"` (words scrambled separately, "of" preserved)

### Bible Book Database

The tool includes complete metadata for all 66 canonical Bible books:

- **Display Names**: Proper formatting with correct capitalization and spacing
- **Testament**: Old/New Testament (English) or Ancien/Nouveau Testament (French)
- **Category**: Law, History, Wisdom, Prophecy, Gospels, Epistles, etc.
- **Book Number**: 1-66 in canonical order
- **Special Handling**: Flags for numbered books, compound names, and accented characters

## Example Output

### Interactive Mode
```
=== Bible Book Scrambler Tool ===
Scramble Bible book names in French or English for puzzle solving

Choose an option:
1. Generate scramble from book name
2. Random scramble challenge
3. Solve mode - check your answer
4. Get hint for a book
5. List all Bible books
6. Quit
Enter your choice (1-6): 2

Choose language:
1. English
2. French
Enter language choice (1-2): 1

Choose testament:
1. Old Testament
2. New Testament
3. Any
Enter testament choice (1-3): 1

Scrambled book: daIuJh
Hint: Old Testament, History (Book #7)
Can you guess which Bible book this is?
Your guess: Judges
🎉 Correct! Well done!
```

### Command Line Mode
```bash
$ python3 bible_scrambler_cli.py generate "Genesis" english
Original: Genesis
Scrambled: esGnsei
Hint: Old Testament, Law (Torah) (Book #1)

$ python3 bible_scrambler_cli.py random french ancien
=== Random Bible Book Scramble Challenge ===
Scrambled: éqLiutive
Hint: Ancien Testament, Loi (Torah) (Book #3)

Can you guess which Bible book this is?
(Answer: Lévitique)
```

## Bible Books Included

The tool includes all 66 canonical Bible books:

**Old Testament (39 books)**: Genesis through Malachi
**New Testament (27 books)**: Matthew through Revelation

**French translations included**: Complete French Bible book names with proper accents and formatting.

### Language-Specific Features

**English**:
- Standard Protestant canonical order
- Common alternate names supported (Song of Songs/Song of Solomon)
- Numbered books use Arabic numerals (1 Samuel, 2 Kings, etc.)

**French**:
- Complete French Bible book names with proper accenting
- Numbered books with French formatting (1 Samuel, 2 Rois, etc.)
- Compound names with French articles (Cantique des Cantiques)

## Requirements

- **Python**: 3.6 or higher
- **Dependencies**: None (uses only Python standard library)
- **Encoding**: UTF-8 support for French accented characters

## Directory Structure

```
anagram/
├── README.md                     # This documentation
├── bible_book_scrambler.py       # Main scrambler class and interactive interface
├── bible_scrambler_cli.py        # Command line interface with multiple modes
├── bible_books_data.py          # Complete Bible book database (English & French)
├── test_bible_scrambler.py      # Comprehensive test suite
└── __pycache__/                 # Python bytecode cache (auto-generated)
```

## 🌐 Web API

The web application provides a RESTful API for integration:

### API Endpoints
- `POST /api/random-challenge` - Get random scrambled book with hint
- `POST /api/check-answer` - Validate user's guess
- `POST /api/custom-scramble` - Generate scramble for specific book
- `POST /api/validate-book` - Check if guess is valid Bible book
- `GET /api/all-books` - List all Bible books in language

### Example Usage
```bash
# Get random challenge
curl -X POST http://localhost:5000/api/random-challenge \
  -H "Content-Type: application/json" \
  -d '{"language": "english", "testament": "any"}'

# Check answer
curl -X POST http://localhost:5000/api/check-answer \
  -H "Content-Type: application/json" \
  -d '{"original": "Genesis", "guess": "Genesis"}'
```

**See `/docs/API.md` for complete API documentation.**

## 🎯 Educational Use

This application is perfect for:

- **Bible Study Groups**: Fun way to learn Bible book names and organization
- **Sunday School**: Interactive games for children and adults
- **Language Learning**: Practice French Bible book names with accent marks
- **Memory Games**: Test knowledge of Old vs New Testament books
- **Puzzle Solving**: Challenge friends and family with scrambled Bible books
- **Online Sharing**: Deploy web version for remote Bible study sessions

## Extending the Tool

### Adding More Languages

To add support for additional languages (Spanish, German, etc.):

1. Create a new function in `bible_books_data.py`: `get_spanish_bible_books()`
2. Add language support in `bible_book_scrambler.py` methods
3. Update CLI and interactive modes to include the new language option
4. Add test cases for the new language

### Customizing Difficulty

The scrambling algorithm supports different difficulty levels:
- **Easy**: Preserve word boundaries in compound names
- **Medium**: Standard scrambling (current default)
- **Hard**: Complete letter randomization across all boundaries

### Adding Categories

You can filter books by category (currently Testament-level filtering is supported):
- Law/Torah books only
- Historical books only
- Wisdom literature only
- Prophetic books only
- Gospel books only
- Epistles only

## Technical Notes

- **Unicode Support**: Full UTF-8 support for accented characters in French
- **Case Sensitivity**: Solution validation is case-insensitive for user convenience
- **Memory Efficient**: Bible book data is loaded once and cached
- **Error Handling**: Comprehensive validation of user inputs and graceful error messages