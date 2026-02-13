# 📖 Bible Book Scramble

A comprehensive Bible book scrambling game available in both **Command Line Interface (CLI)** and **Web Application** formats. Challenge yourself to unscramble Bible book names in English or French!

![Bible Scramble Demo](https://img.shields.io/badge/Python-3.7%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.3-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎯 Core Features
- **Bilingual Support**: Play in English or French
- **Complete Bible Coverage**: All 66 canonical Bible books
- **Smart Scrambling**: Preserves numbers, spaces, and special characters
- **Intelligent Hints**: Testament, category, and book number information
- **Multiple Game Modes**: Random challenges, custom scrambles, and reference lists

### 🖥️ CLI Features
- Interactive command-line interface
- Random book challenges with testament filtering
- Custom book scrambling
- Answer validation and hints
- Complete Bible book reference

### 🌐 Web Features
- Beautiful responsive web interface
- Score tracking with streaks and statistics
- Real-time game interactions
- Mobile-friendly design
- Local storage for game statistics

## 🚀 Quick Start

### Option 1: Web Application (Recommended)
```bash
cd anagram/web/
python3 app.py
```
Then open: http://localhost:5000

### Option 2: Command Line Interface
```bash
cd anagram/
python3 bible_scrambler_cli.py
```

## 📁 Project Structure

```
bible-book-scramble/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Project dependencies
├── .gitignore                  # Git ignore rules
├── SETUP.md                    # Setup guide
├── DEPLOYMENT.md               # Deployment guide
│
├── anagram/                    # Main Application Directory
│   ├── README.md               # CLI documentation
│   ├── bible_scrambler_cli.py  # Main CLI interface
│   ├── bible_book_scrambler.py # Core scrambling logic
│   ├── bible_books_data.py     # Bible books database
│   ├── anagram_generator.py    # General anagram logic
│   ├── anagram_cli.py          # General anagram CLI
│   ├── test_*.py              # Test files
│   │
│   └── web/                    # Web Application
│       ├── README.md           # Web app documentation
│       ├── app.py              # Flask web server
│       ├── start_server.sh     # Easy startup script
│       ├── requirements.txt    # Web dependencies
│       ├── Procfile            # Deployment config
│       ├── runtime.txt         # Python version
│       ├── templates/
│       │   └── index.html      # Main game interface
│       └── static/
│           ├── css/
│           │   └── style.css   # Game styling
│           └── js/
│               └── script.js   # Game logic
│
└── docs/                       # Additional documentation
    ├── API.md                  # API documentation
    └── CONTRIBUTING.md         # Contribution guidelines
```

## 🎮 How to Use the Web Interface

### Getting Started
1. **Start the web server:**
   ```bash
   cd anagram/web/
   python3 app.py
   ```
2. **Open your web browser** and go to: `http://localhost:5000`
3. You'll see the beautiful Bible Book Scramble game interface!

### Web Interface Guide

#### 🎯 Game Controls (Top Section)
- **Language Selector**: Choose between "English" and "Français"
- **Testament Filter**: Select "Any", "Old Testament", or "New Testament"
- **Three Main Buttons**:
  - **"New Challenge"** - Start a random scramble game
  - **"Custom Scramble"** - Scramble a specific book you enter
  - **"Show All Books"** - View complete list of Bible books

#### 🎮 Playing the Game

**Random Challenge Mode:**
1. **Set your preferences** using the dropdowns at the top
2. **Click "New Challenge"** - you'll see:
   - A scrambled Bible book name in large letters
   - A helpful hint showing testament, category, and book number
   - An input field for your answer
3. **Type your guess** in the answer field
4. **Click "Submit"** or press Enter
5. **Get instant feedback**:
   - ✅ Correct answers show in green with celebration
   - ❌ Incorrect answers show the right answer
   - Your score and streak update automatically
6. **New challenge starts automatically** after each answer

**Custom Scramble Mode:**
1. **Click "Custom Scramble"** button
2. **Enter any Bible book name** (like "Genesis" or "Apocalypse")
3. **Click "Scramble It!"**
4. **View the results** showing original, scrambled, and hint

**Bible Reference Mode:**
1. **Click "Show All Books"**
2. **View complete list** of all 66 Bible books in your chosen language
3. **Perfect for studying** or checking correct spellings

#### 📊 Score Tracking (Bottom Section)
- **Score**: Points earned (10 per correct answer)
- **Streak**: Current consecutive correct answers
- **Total Played**: Total number of games attempted
- **Statistics persist** between browser sessions

#### 🎨 Visual Features
- **Responsive design** works on phones, tablets, and computers
- **Beautiful gradients** and smooth animations
- **Color-coded feedback** for correct/incorrect answers
- **Mobile-friendly** touch interface

### CLI Version (Alternative)
If you prefer command-line interface:
1. Run: `python3 anagram/bible_scrambler_cli.py`
2. Choose from menu options:
   - Generate scramble from book name
   - Random scramble challenge
   - Solve mode - check your answer
   - Get hint for a book
   - List all Bible books

## 📋 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd bible-book-scramble
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Choose your preferred interface:**

   **For Web Application:**
   ```bash
   cd anagram/web/
   ./start_server.sh
   ```

   **For CLI Application:**
   ```bash
   cd anagram/
   python3 bible_scrambler_cli.py
   ```

## 🌐 Web Application

The web version provides a modern, interactive experience with:

- **Responsive Design**: Works on desktop and mobile
- **Real-time Scoring**: Track your progress with persistent statistics
- **Multiple Game Modes**: Random challenges, custom scrambles, book reference
- **Beautiful Interface**: Modern gradient design with smooth animations

**API Endpoints:**
- `POST /api/random-challenge` - Get random scrambled book
- `POST /api/check-answer` - Validate answer
- `POST /api/custom-scramble` - Scramble specific book
- `GET /api/all-books` - List all books

## 💻 CLI Application

The command-line version offers:

- **Interactive Menu**: Easy-to-use numbered menu system
- **Testament Filtering**: Choose Old Testament, New Testament, or Any
- **Instant Feedback**: Immediate results with emoji indicators
- **Comprehensive Hints**: Detailed book information
- **Book Reference**: Complete list of all 66 Bible books

## 🗂️ Supported Bible Books

### Languages
- **English**: Traditional Bible book names (66 books)
- **French**: Complete French Bible book names (66 books)

### Categories
- **Old Testament**: Law, History, Wisdom, Major Prophets, Minor Prophets
- **New Testament**: Gospels, Acts, Pauline Epistles, General Epistles, Revelation

## 🧪 Testing

Run the test suite to verify functionality:

```bash
cd anagram/
python3 test_bible_scrambler.py
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Examples

### CLI Example
```bash
$ python3 bible_scrambler_cli.py
=== Bible Book Scrambler Tool ===
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

Scrambled book: sesniGe
Hint: Old Testament, Law (Torah) (Book #1)
Can you guess which Bible book this is?
Your guess: Genesis
🎉 Correct! Well done!
```

### Web API Example
```bash
curl -X POST http://localhost:5000/api/random-challenge \
  -H "Content-Type: application/json" \
  -d '{"language": "english", "testament": "any"}'

{
  "success": true,
  "original": "Psalms",
  "scrambled": "msPals",
  "hint": "Old Testament, Wisdom Literature (Book #19)"
}
```

## 📞 Support

- **Documentation**: Check the README files in each directory
- **Issues**: Create an issue on GitHub
- **Questions**: Open a discussion on GitHub

## 🙏 Acknowledgments

- Built with Python and Flask
- Responsive design with modern CSS
- Comprehensive Bible book database
- Smart scrambling algorithm that preserves formatting

---

**Ready to test your Bible knowledge? Start scrambling!** 🎮