#!/usr/bin/env python3
"""
Bible Scramble Web Application
Web interface for the Bible book scrambling game.
"""

import sys
import os

# Add the parent anagram directory to the Python path so we can import the Bible scrambler
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request, jsonify
from bible_book_scrambler import BibleBookScrambler

app = Flask(__name__)
scrambler = BibleBookScrambler()

@app.route('/')
def index():
    """Main game interface"""
    return render_template('index.html')

@app.route('/api/random-challenge', methods=['POST'])
def random_challenge():
    """Get a random scrambled Bible book with hint"""
    try:
        data = request.get_json()
        language = data.get('language', 'english')
        testament = data.get('testament', 'any')

        # Get random book
        random_book = scrambler.get_random_book(language, testament)

        # Generate scramble
        scrambled = scrambler.generate_scramble(random_book, language)

        # Get hint
        hint = scrambler.get_hint(random_book, language)

        return jsonify({
            'success': True,
            'original': random_book,
            'scrambled': scrambled,
            'hint': hint
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    """Check if the user's guess is correct"""
    try:
        data = request.get_json()
        original = data.get('original')
        guess = data.get('guess')

        if not original or not guess:
            return jsonify({
                'success': False,
                'error': 'Missing original or guess'
            }), 400

        # Validate the solution
        is_correct = scrambler.validate_scramble_solution(original, '', guess)

        return jsonify({
            'success': True,
            'correct': is_correct
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/custom-scramble', methods=['POST'])
def custom_scramble():
    """Generate scramble for a specific book name"""
    try:
        data = request.get_json()
        book_name = data.get('book_name')
        language = data.get('language', 'english')

        if not book_name:
            return jsonify({
                'success': False,
                'error': 'Missing book name'
            }), 400

        # Generate scramble
        scrambled = scrambler.generate_scramble(book_name, language)
        hint = scrambler.get_hint(book_name, language)

        return jsonify({
            'success': True,
            'original': book_name,
            'scrambled': scrambled,
            'hint': hint
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/validate-book', methods=['POST'])
def validate_book():
    """Check if a guess is a valid Bible book"""
    try:
        data = request.get_json()
        guess = data.get('guess')
        language = data.get('language', 'english')

        if not guess:
            return jsonify({
                'success': False,
                'error': 'Missing guess'
            }), 400

        # Check if it's a valid Bible book
        is_valid = scrambler.check_solution('', guess, language)

        return jsonify({
            'success': True,
            'valid': is_valid
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/all-books', methods=['GET'])
def all_books():
    """Get all Bible books for a language"""
    try:
        language = request.args.get('language', 'english')

        # Get all books
        books = scrambler.get_all_books_list(language)

        return jsonify({
            'success': True,
            'books': books
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)

    # Use environment port for deployment, fallback to 8000 for local
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)