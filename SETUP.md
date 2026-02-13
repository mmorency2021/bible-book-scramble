# 🚀 Bible Book Scramble - Setup Guide

Complete setup instructions for getting the Bible Book Scramble project ready for GitHub and development.

## 📁 GitHub-Ready Project Structure

```
bible-book-scramble/
├── README.md                    # 📖 Main project documentation
├── LICENSE                      # ⚖️  MIT License
├── requirements.txt             # 📦 Python dependencies
├── .gitignore                  # 🚫 Git ignore rules
├── SETUP.md                    # 🚀 This setup guide
│
├── anagram/                    # 💻 CLI Application
│   ├── README.md               # 📚 CLI documentation
│   ├── bible_scrambler_cli.py  # 🎮 Main CLI interface
│   ├── bible_book_scrambler.py # 🧠 Core scrambling logic
│   ├── bible_books_data.py     # 📊 Bible books database
│   ├── anagram_generator.py    # 🔀 General anagram logic
│   ├── anagram_cli.py          # 🔤 General anagram CLI
│   ├── test_bible_scrambler.py # 🧪 Bible scrambler tests
│   └── test_anagram.py         # 🧪 General anagram tests
│
├── web/                        # 🌐 Web Application
│   ├── README.md               # 📚 Web app documentation
│   ├── app.py                  # 🖥️  Flask web server
│   ├── start_server.sh         # ⚡ Easy startup script
│   ├── requirements.txt        # 📦 Web dependencies
│   ├── templates/
│   │   └── index.html          # 🎨 Main game interface
│   └── static/
│       ├── css/
│       │   └── style.css       # 💅 Game styling
│       └── js/
│           └── script.js       # ⚙️  Game logic
│
└── docs/                       # 📋 Additional Documentation
    ├── API.md                  # 🌐 API documentation
    └── CONTRIBUTING.md         # 🤝 Contribution guidelines
```

## 🎯 Quick Start Options

### Option 1: Web Application (Recommended)
```bash
# Navigate to project root
cd bible-book-scramble/

# Install dependencies
pip install -r requirements.txt

# Start web server
cd anagram/web/
python3 app.py
# or
./start_server.sh

# Open browser to: http://localhost:8000
```

### Option 2: Command Line Interface
```bash
# Navigate to CLI directory
cd bible-book-scramble/anagram/

# Run CLI (no dependencies needed)
python3 bible_scrambler_cli.py
```

## 📋 Prerequisites

- **Python**: 3.7 or higher
- **pip**: Python package installer
- **Git**: For version control

## 🔧 Development Setup

### 1. Clone Repository
```bash
git clone <repository-url>
cd bible-book-scramble
```

### 2. Set up Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Test Installation

#### Test CLI:
```bash
cd anagram/
python3 bible_scrambler_cli.py
```

#### Test Web App:
```bash
cd anagram/web/
python3 app.py
```

#### Run Tests:
```bash
cd anagram/
python3 test_bible_scrambler.py
```

## 🌐 Web Application Features

- **Responsive Design**: Works on desktop and mobile
- **Bilingual Support**: English and French
- **Score Tracking**: Persistent game statistics
- **Multiple Game Modes**: Random, custom, reference
- **Beautiful UI**: Modern gradient design
- **API Endpoints**: RESTful API for integration

### Web App API Endpoints:
- `POST /api/random-challenge` - Get random scrambled book
- `POST /api/check-answer` - Validate answer
- `POST /api/custom-scramble` - Scramble specific book
- `GET /api/all-books` - List all books

## 💻 CLI Application Features

- **Interactive Menu**: Numbered menu system
- **Testament Filtering**: Old/New Testament options
- **Instant Feedback**: Emoji indicators
- **Comprehensive Hints**: Book metadata
- **No Dependencies**: Pure Python standard library

### CLI Game Modes:
1. Generate scramble from book name
2. Random scramble challenge
3. Solve mode - check answers
4. Get hints for books
5. List all Bible books

## 🧪 Testing

### Run All Tests:
```bash
cd anagram/
python3 test_bible_scrambler.py
python3 test_anagram.py
```

### Test Coverage:
- ✅ All 66 Bible books (English & French)
- ✅ Scrambling algorithm
- ✅ Special character handling
- ✅ Answer validation
- ✅ Hint system
- ✅ Error handling

## 🚀 Deployment

### Local Development:
```bash
cd anagram/web/
python3 app.py
```

### Production (example with gunicorn):
```bash
pip install gunicorn
cd anagram/web/
gunicorn -w 4 app:app
```

## 📖 Documentation

- **Main README**: Project overview and quick start
- **CLI README**: Detailed CLI documentation
- **Web README**: Web application guide
- **API Docs**: Complete API reference
- **Contributing**: Development guidelines

## 🎮 How to Play

### Web Version:
1. Open http://localhost:5000
2. Choose language (English/French)
3. Select testament filter
4. Click "New Challenge"
5. Guess the scrambled Bible book
6. Build your score and streak!

### CLI Version:
1. Run `python3 bible_scrambler_cli.py`
2. Choose option from menu (1-6)
3. Select language and testament
4. Guess scrambled books
5. Learn with hints and feedback

## 🤝 Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for:
- Development setup
- Code style guidelines
- Pull request process
- Issue guidelines

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🐛 Troubleshooting

### Common Issues:

**Python not found:**
```bash
# Try python3 instead of python
python3 --version
```

**Flask not found:**
```bash
# Install dependencies
pip install -r requirements.txt
```

**Permission denied on start_server.sh:**
```bash
# Make script executable
chmod +x web/start_server.sh
```

**Port 5000 already in use:**
```bash
# Change port in web/app.py
app.run(debug=True, port=5001)
```

## 📞 Support

- **Documentation**: Check README files in each directory
- **Issues**: Create GitHub issue
- **Questions**: Use GitHub discussions

---

**Ready to scramble some Bible books?** 🎮

Choose your preferred interface and start playing!