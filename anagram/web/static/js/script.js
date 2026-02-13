// Bible Book Scramble Game JavaScript

class BibleScrambleGame {
    constructor() {
        this.currentChallenge = null;
        this.stats = {
            score: 0,
            streak: 0,
            total: 0
        };

        this.initializeElements();
        this.bindEvents();
        this.loadStats();
        this.updateDisplay();
    }

    initializeElements() {
        // Controls
        this.languageSelect = document.getElementById('language-select');
        this.testamentSelect = document.getElementById('testament-select');

        // Buttons
        this.newChallengeBtn = document.getElementById('new-challenge-btn');
        this.customScrambleBtn = document.getElementById('custom-scramble-btn');
        this.showBooksBtn = document.getElementById('show-books-btn');
        this.submitBtn = document.getElementById('submit-btn');
        this.giveUpBtn = document.getElementById('give-up-btn');
        this.scrambleCustomBtn = document.getElementById('scramble-custom-btn');
        this.resetScoreBtn = document.getElementById('reset-score-btn');

        // Sections
        this.challengeSection = document.getElementById('challenge-section');
        this.customSection = document.getElementById('custom-section');
        this.booksSection = document.getElementById('books-section');

        // Game elements
        this.scrambledDisplay = document.getElementById('scrambled-display');
        this.hintDisplay = document.getElementById('hint-display');
        this.answerInput = document.getElementById('answer-input');
        this.resultDisplay = document.getElementById('result-display');

        // Custom elements
        this.customBookInput = document.getElementById('custom-book-input');
        this.customResult = document.getElementById('custom-result');

        // Books list
        this.booksList = document.getElementById('books-list');

        // Stats
        this.scoreDisplay = document.getElementById('score-display');
        this.streakDisplay = document.getElementById('streak-display');
        this.totalDisplay = document.getElementById('total-display');
    }

    bindEvents() {
        this.newChallengeBtn.addEventListener('click', () => this.startNewChallenge());
        this.customScrambleBtn.addEventListener('click', () => this.showCustomSection());
        this.showBooksBtn.addEventListener('click', () => this.showBooksSection());

        this.submitBtn.addEventListener('click', () => this.submitAnswer());
        this.giveUpBtn.addEventListener('click', () => this.giveUp());
        this.scrambleCustomBtn.addEventListener('click', () => this.scrambleCustomBook());
        this.resetScoreBtn.addEventListener('click', () => this.resetScore());

        // Enter key support
        this.answerInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.submitAnswer();
        });

        this.customBookInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.scrambleCustomBook();
        });

        // Language change updates testament options
        this.languageSelect.addEventListener('change', () => this.updateTestamentOptions());
    }

    updateTestamentOptions() {
        const language = this.languageSelect.value;
        const testament = this.testamentSelect;

        if (language === 'french') {
            testament.innerHTML = `
                <option value="any">Tous</option>
                <option value="ancien">Ancien Testament</option>
                <option value="nouveau">Nouveau Testament</option>
            `;
        } else {
            testament.innerHTML = `
                <option value="any">Any</option>
                <option value="old">Old Testament</option>
                <option value="new">New Testament</option>
            `;
        }
    }

    hideAllSections() {
        this.challengeSection.style.display = 'none';
        this.customSection.style.display = 'none';
        this.booksSection.style.display = 'none';
    }

    async startNewChallenge() {
        this.hideAllSections();
        this.challengeSection.style.display = 'block';

        const language = this.languageSelect.value;
        const testament = this.testamentSelect.value;

        try {
            this.newChallengeBtn.classList.add('loading');
            this.newChallengeBtn.disabled = true;

            const response = await fetch('/api/random-challenge', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    language: language,
                    testament: testament
                })
            });

            const data = await response.json();

            if (data.success) {
                this.currentChallenge = {
                    original: data.original,
                    scrambled: data.scrambled,
                    hint: data.hint,
                    language: language
                };

                this.scrambledDisplay.textContent = data.scrambled;
                this.hintDisplay.textContent = data.hint;
                this.answerInput.value = '';
                this.answerInput.focus();
                this.resultDisplay.innerHTML = '';
                this.resultDisplay.className = 'result-display';

                this.submitBtn.disabled = false;
                this.giveUpBtn.disabled = false;

                this.challengeSection.classList.add('fade-in');
            } else {
                this.showError('Failed to get challenge: ' + data.error);
            }
        } catch (error) {
            this.showError('Network error: ' + error.message);
        } finally {
            this.newChallengeBtn.classList.remove('loading');
            this.newChallengeBtn.disabled = false;
        }
    }

    async submitAnswer() {
        if (!this.currentChallenge || !this.answerInput.value.trim()) {
            return;
        }

        try {
            this.submitBtn.disabled = true;
            this.giveUpBtn.disabled = true;

            const response = await fetch('/api/check-answer', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    original: this.currentChallenge.original,
                    guess: this.answerInput.value.trim()
                })
            });

            const data = await response.json();

            if (data.success) {
                if (data.correct) {
                    this.handleCorrectAnswer();
                } else {
                    this.handleIncorrectAnswer();
                }
            } else {
                this.showError('Failed to check answer: ' + data.error);
            }
        } catch (error) {
            this.showError('Network error: ' + error.message);
        }
    }

    handleCorrectAnswer() {
        this.stats.score += 10;
        this.stats.streak += 1;
        this.stats.total += 1;

        this.resultDisplay.innerHTML = `
            <div class="bounce">
                🎉 Correct! Well done!<br>
                <strong>Answer:</strong> ${this.currentChallenge.original}
            </div>
        `;
        this.resultDisplay.className = 'result-display result-correct bounce';

        this.saveStats();
        this.updateDisplay();

        // Auto-start new challenge after delay
        setTimeout(() => {
            this.startNewChallenge();
        }, 2000);
    }

    handleIncorrectAnswer() {
        this.stats.streak = 0;
        this.stats.total += 1;

        this.resultDisplay.innerHTML = `
            ❌ Incorrect! The answer was:<br>
            <strong>${this.currentChallenge.original}</strong>
        `;
        this.resultDisplay.className = 'result-display result-incorrect';

        this.saveStats();
        this.updateDisplay();

        // Auto-start new challenge after delay
        setTimeout(() => {
            this.startNewChallenge();
        }, 3000);
    }

    giveUp() {
        if (!this.currentChallenge) return;

        this.stats.streak = 0;
        this.stats.total += 1;

        this.resultDisplay.innerHTML = `
            The answer was: <strong>${this.currentChallenge.original}</strong><br>
            Don't give up! Try another one!
        `;
        this.resultDisplay.className = 'result-display';

        this.submitBtn.disabled = true;
        this.giveUpBtn.disabled = true;

        this.saveStats();
        this.updateDisplay();

        // Auto-start new challenge after delay
        setTimeout(() => {
            this.startNewChallenge();
        }, 2500);
    }

    showCustomSection() {
        this.hideAllSections();
        this.customSection.style.display = 'block';
        this.customBookInput.value = '';
        this.customResult.innerHTML = '';
        this.customBookInput.focus();
    }

    async scrambleCustomBook() {
        const bookName = this.customBookInput.value.trim();
        if (!bookName) return;

        const language = this.languageSelect.value;

        try {
            this.scrambleCustomBtn.classList.add('loading');
            this.scrambleCustomBtn.disabled = true;

            const response = await fetch('/api/custom-scramble', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    book_name: bookName,
                    language: language
                })
            });

            const data = await response.json();

            if (data.success) {
                this.customResult.innerHTML = `
                    <div class="fade-in">
                        <h4>Original:</h4>
                        <p><strong>${data.original}</strong></p>

                        <h4>Scrambled:</h4>
                        <p style="font-size: 1.5em; color: #667eea; letter-spacing: 2px;">
                            <strong>${data.scrambled}</strong>
                        </p>

                        <h4>Hint:</h4>
                        <p><em>${data.hint}</em></p>
                    </div>
                `;
            } else {
                this.customResult.innerHTML = `
                    <div style="color: #dc3545;">
                        Error: ${data.error}
                    </div>
                `;
            }
        } catch (error) {
            this.customResult.innerHTML = `
                <div style="color: #dc3545;">
                    Network error: ${error.message}
                </div>
            `;
        } finally {
            this.scrambleCustomBtn.classList.remove('loading');
            this.scrambleCustomBtn.disabled = false;
        }
    }

    async showBooksSection() {
        this.hideAllSections();
        this.booksSection.style.display = 'block';

        const language = this.languageSelect.value;

        try {
            const response = await fetch(`/api/all-books?language=${language}`);
            const data = await response.json();

            if (data.success) {
                this.booksList.innerHTML = data.books
                    .map((book, index) => `
                        <div class="book-item fade-in" style="animation-delay: ${index * 0.02}s">
                            ${index + 1}. ${book}
                        </div>
                    `)
                    .join('');
            } else {
                this.booksList.innerHTML = `
                    <div style="color: #dc3545;">
                        Error loading books: ${data.error}
                    </div>
                `;
            }
        } catch (error) {
            this.booksList.innerHTML = `
                <div style="color: #dc3545;">
                    Network error: ${error.message}
                </div>
            `;
        }
    }

    showError(message) {
        this.resultDisplay.innerHTML = `
            <div style="color: #dc3545;">
                ${message}
            </div>
        `;
        this.resultDisplay.className = 'result-display';
    }

    loadStats() {
        const saved = localStorage.getItem('bibleScrambleStats');
        if (saved) {
            this.stats = { ...this.stats, ...JSON.parse(saved) };
        }
    }

    saveStats() {
        localStorage.setItem('bibleScrambleStats', JSON.stringify(this.stats));
    }

    updateDisplay() {
        this.scoreDisplay.textContent = this.stats.score;
        this.streakDisplay.textContent = this.stats.streak;
        this.totalDisplay.textContent = this.stats.total;
    }

    resetScore() {
        // Ask for confirmation before resetting
        if (confirm('Are you sure you want to reset all statistics? This action cannot be undone.')) {
            this.stats = {
                score: 0,
                streak: 0,
                total: 0
            };

            this.saveStats();
            this.updateDisplay();

            // Show confirmation message
            this.showResetConfirmation();
        }
    }

    showResetConfirmation() {
        // Create a temporary confirmation message
        const confirmation = document.createElement('div');
        confirmation.innerHTML = '✅ Statistics reset successfully!';
        confirmation.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            font-weight: 600;
            box-shadow: 0 5px 15px rgba(86, 171, 47, 0.3);
            z-index: 1000;
            animation: slideIn 0.5s ease;
        `;

        document.body.appendChild(confirmation);

        // Remove after 3 seconds
        setTimeout(() => {
            confirmation.style.animation = 'slideOut 0.5s ease';
            setTimeout(() => {
                document.body.removeChild(confirmation);
            }, 500);
        }, 3000);
    }
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.game = new BibleScrambleGame();
});