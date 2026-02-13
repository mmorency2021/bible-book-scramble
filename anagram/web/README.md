# Bible Book Scramble Web Application

A fun and interactive web-based game for scrambling Bible book names in English and French!

## Features

- **Random Challenges**: Get a random scrambled Bible book from any testament
- **Bilingual Support**: Play in English or French
- **Smart Hints**: Get helpful hints about the book's testament, category, and position
- **Custom Scrambles**: Generate scrambles for specific Bible books
- **Score Tracking**: Track your score, streak, and total games played
- **Responsive Design**: Works great on desktop and mobile devices
- **Bible Book Reference**: View all 66 Bible books in your chosen language

## Game Modes

1. **Random Challenge**: Get a random scrambled book and try to guess it
2. **Custom Scramble**: Enter any Bible book name to see it scrambled
3. **Bible Book List**: Browse all 66 canonical Bible books

## How to Play

1. Choose your language (English/Français)
2. Select a testament (Old/New or Any)
3. Click "New Challenge" to get a scrambled Bible book
4. Use the hint to help you guess the original book name
5. Type your answer and submit
6. Build up your score and streak!

## Installation & Setup

### Prerequisites
- Python 3.7+
- Flask (will be auto-installed if missing)

### Quick Start

1. Navigate to the web directory:
   ```bash
   cd web/
   ```

2. Run the startup script:
   ```bash
   ./start_server.sh
   ```

3. Open your browser and go to: http://localhost:8000

### Manual Start

If you prefer to start manually:

```bash
cd web/
python3 app.py
```

## API Endpoints

The application provides several REST API endpoints:

- `POST /api/random-challenge` - Get a random scrambled Bible book
- `POST /api/check-answer` - Check if a guess is correct
- `POST /api/custom-scramble` - Generate scramble for a specific book
- `POST /api/validate-book` - Check if a guess is a valid Bible book
- `GET /api/all-books` - Get all Bible books for a language

## Technical Details

### Backend
- **Flask**: Python web framework
- **Bible Book Scrambler**: Custom scrambling algorithm that preserves special characters
- **Comprehensive Database**: All 66 canonical Bible books with metadata

### Frontend
- **Vanilla JavaScript**: No frameworks, fast and lightweight
- **Responsive CSS**: Modern design that works on all devices
- **Local Storage**: Saves your game statistics

### Supported Languages
- **English**: All traditional Bible book names
- **French**: Complete French Bible book names

## Project Structure

```
web/
├── app.py                 # Flask web server
├── templates/
│   └── index.html         # Main game interface
├── static/
│   ├── css/
│   │   └── style.css      # Game styling
│   └── js/
│       └── script.js      # Game logic
├── start_server.sh        # Startup script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Related Files

The web application uses the Bible scrambling logic from the `../anagram/` directory:
- `bible_book_scrambler.py` - Main scrambling class
- `bible_books_data.py` - Database of all Bible books

## Game Statistics

Your game statistics are automatically saved to your browser's local storage:
- **Score**: Points earned (10 per correct answer)
- **Streak**: Current streak of consecutive correct answers
- **Total**: Total number of games played

## Browser Compatibility

Works with all modern browsers:
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Tips for Playing

- Pay attention to the hints - they tell you the testament, category, and book number
- Short books (3-4 letters) are often easier to unscramble
- Remember that numbers and spaces are preserved in their original positions
- Try different testament filters to focus on books you know better

Enjoy playing the Bible Book Scramble game!