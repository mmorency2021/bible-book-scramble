# 🌐 Bible Book Scramble API Documentation

This document describes the REST API endpoints for the Bible Book Scramble web application.

## Base URL

```
http://localhost:5000
```

## 📋 Table of Contents
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Error Handling](#error-handling)
- [Examples](#examples)

## 🔐 Authentication

No authentication required. This is a public API for the Bible scramble game.

## 📡 Endpoints

### 1. Random Challenge

Get a random scrambled Bible book with hint.

**Endpoint:** `POST /api/random-challenge`

**Request Body:**
```json
{
  "language": "english|french",
  "testament": "any|old|new|ancien|nouveau"
}
```

**Response:**
```json
{
  "success": true,
  "original": "Genesis",
  "scrambled": "sesniGe",
  "hint": "Old Testament, Law (Torah) (Book #1)"
}
```

**Parameters:**
- `language` (required): Either "english" or "french"
- `testament` (optional): Filter by testament. Defaults to "any"
  - English: "old", "new", "any"
  - French: "ancien", "nouveau", "any"

---

### 2. Check Answer

Validate if a user's guess matches the original book name.

**Endpoint:** `POST /api/check-answer`

**Request Body:**
```json
{
  "original": "Genesis",
  "guess": "Genesis"
}
```

**Response:**
```json
{
  "success": true,
  "correct": true
}
```

**Parameters:**
- `original` (required): The original Bible book name
- `guess` (required): The user's guess

---

### 3. Custom Scramble

Generate a scramble for a specific Bible book name.

**Endpoint:** `POST /api/custom-scramble`

**Request Body:**
```json
{
  "book_name": "Genesis",
  "language": "english"
}
```

**Response:**
```json
{
  "success": true,
  "original": "Genesis",
  "scrambled": "snGseei",
  "hint": "Old Testament, Law (Torah) (Book #1)"
}
```

**Parameters:**
- `book_name` (required): The Bible book name to scramble
- `language` (required): Either "english" or "french"

---

### 4. Validate Book

Check if a guess is a valid Bible book name in the specified language.

**Endpoint:** `POST /api/validate-book`

**Request Body:**
```json
{
  "guess": "Genesis",
  "language": "english"
}
```

**Response:**
```json
{
  "success": true,
  "valid": true
}
```

**Parameters:**
- `guess` (required): The book name to validate
- `language` (required): Either "english" or "french"

---

### 5. All Books

Get a list of all Bible books in the specified language.

**Endpoint:** `GET /api/all-books`

**Query Parameters:**
- `language` (optional): Either "english" or "french". Defaults to "english"

**Response:**
```json
{
  "success": true,
  "books": [
    "Genesis",
    "Exodus",
    "Leviticus",
    "..."
  ]
}
```

## ❌ Error Handling

All endpoints return errors in this format:

```json
{
  "success": false,
  "error": "Error message description"
}
```

### Common HTTP Status Codes
- `200` - Success
- `400` - Bad Request (validation error, missing parameters)
- `500` - Internal Server Error

### Common Error Messages
- `"Missing book name"` - Required parameter not provided
- `"Missing original or guess"` - Required parameters not provided
- `"Bible book 'XYZ' not found in english"` - Invalid book name
- `"Language must be 'english' or 'french'"` - Invalid language parameter

## 📝 Examples

### Example 1: Getting a Random English Challenge

**Request:**
```bash
curl -X POST http://localhost:5000/api/random-challenge \
  -H "Content-Type: application/json" \
  -d '{"language": "english", "testament": "old"}'
```

**Response:**
```json
{
  "success": true,
  "original": "Judges",
  "scrambled": "Jdgesu",
  "hint": "Old Testament, History (Book #7)"
}
```

### Example 2: Checking an Answer

**Request:**
```bash
curl -X POST http://localhost:5000/api/check-answer \
  -H "Content-Type: application/json" \
  -d '{"original": "Judges", "guess": "Judges"}'
```

**Response:**
```json
{
  "success": true,
  "correct": true
}
```

### Example 3: Getting a French Custom Scramble

**Request:**
```bash
curl -X POST http://localhost:5000/api/custom-scramble \
  -H "Content-Type: application/json" \
  -d '{"book_name": "Genèse", "language": "french"}'
```

**Response:**
```json
{
  "success": true,
  "original": "Genèse",
  "scrambled": "sGneèe",
  "hint": "Ancien Testament, Loi (Torah) (Book #1)"
}
```

### Example 4: Listing All French Books

**Request:**
```bash
curl "http://localhost:5000/api/all-books?language=french"
```

**Response:**
```json
{
  "success": true,
  "books": [
    "Genèse",
    "Exode",
    "Lévitique",
    "Nombres",
    "Deutéronome",
    "..."
  ]
}
```

## 🧪 Testing the API

### Using curl

Test each endpoint using curl commands as shown in the examples above.

### Using Python

```python
import requests

# Test random challenge
response = requests.post('http://localhost:5000/api/random-challenge',
                        json={'language': 'english', 'testament': 'any'})
data = response.json()
print(f"Scrambled: {data['scrambled']}")
print(f"Hint: {data['hint']}")

# Test answer checking
response = requests.post('http://localhost:5000/api/check-answer',
                        json={'original': data['original'], 'guess': 'Genesis'})
result = response.json()
print(f"Correct: {result['correct']}")
```

### Using JavaScript (Web)

```javascript
// Get random challenge
async function getRandomChallenge() {
  const response = await fetch('/api/random-challenge', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      language: 'english',
      testament: 'any'
    })
  });

  const data = await response.json();
  if (data.success) {
    console.log('Scrambled:', data.scrambled);
    console.log('Hint:', data.hint);
    return data;
  }
}

// Check answer
async function checkAnswer(original, guess) {
  const response = await fetch('/api/check-answer', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      original: original,
      guess: guess
    })
  });

  const data = await response.json();
  return data.success ? data.correct : false;
}
```

## 🔧 Development Notes

### Adding New Endpoints

1. Add route handler in `web/app.py`
2. Follow existing error handling patterns
3. Return JSON with `success` boolean
4. Add documentation here
5. Add tests if applicable

### Performance Considerations

- All Bible book data is loaded once at startup
- No database required - all data in memory
- Scrambling is performed on-demand
- No caching implemented (stateless API)

### Security

- No sensitive data transmitted
- Input validation on all parameters
- No file system access from API
- Safe for public deployment

---

**Ready to integrate with the Bible Book Scramble API?** 🎮