# Contributing to Bible Book Scramble

We love contributions! This document provides guidelines for contributing to the Bible Book Scramble project.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/bible-book-scramble.git
   cd bible-book-scramble
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🤝 How to Contribute

### Areas where we welcome contributions:
- 🐛 **Bug fixes** and issue resolution
- ✨ **New features** and enhancements
- 📚 **Documentation** improvements
- 🧪 **Test coverage** expansion
- 🌍 **New language support** (Spanish, German, etc.)
- 🎨 **UI/UX improvements** for the web version
- ♿ **Accessibility** enhancements

## 🛠️ Development Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git

### Setup Steps
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test the CLI version:**
   ```bash
   cd anagram/
   python3 bible_scrambler_cli.py
   ```

3. **Test the web version:**
   ```bash
   cd web/
   python3 app.py
   ```

### Project Structure
```
bible-book-scramble/
├── anagram/          # CLI application
├── web/              # Web application
├── docs/             # Documentation
├── README.md         # Main project documentation
└── requirements.txt  # Python dependencies
```

## 🎨 Code Style

### Python Code
- Follow **PEP 8** style guidelines
- Use **meaningful variable names** and **clear function names**
- Add **docstrings** to all functions and classes
- Keep lines under **88 characters** when possible

### Example:
```python
def scramble_bible_book(book_name: str, language: str) -> str:
    """
    Generate a scrambled version of a Bible book name.

    Args:
        book_name: The Bible book name to scramble
        language: 'english' or 'french'

    Returns:
        Scrambled version of the book name

    Raises:
        ValueError: If book_name or language is invalid
    """
    # Implementation here
```

### Web Code (HTML/CSS/JS)
- Use **semantic HTML** elements
- Follow **CSS BEM** methodology for class naming
- Use **modern JavaScript** (ES6+)
- Ensure **mobile-first** responsive design

## 🧪 Testing

### Running Tests
```bash
# Test CLI functionality
cd anagram/
python3 test_bible_scrambler.py

# Test web application
cd web/
python3 -m pytest  # If you add pytest tests
```

### Writing Tests
- Add tests for **all new features**
- Test **both English and French** functionality
- Include **edge cases** and **error conditions**
- Ensure tests are **clear and maintainable**

## 📝 Pull Request Process

1. **Update documentation** if you're adding features
2. **Add or update tests** for your changes
3. **Run the test suite** to ensure nothing is broken
4. **Update the README** if needed
5. **Submit your pull request** with:
   - Clear title and description
   - Reference to any related issues
   - Screenshots for UI changes

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] I have tested this thoroughly
- [ ] I have added/updated tests as needed
- [ ] All tests pass

## Screenshots (if applicable)
[Add screenshots for UI changes]
```

## 🐛 Issue Guidelines

### Before Creating an Issue
1. **Search existing issues** to avoid duplicates
2. **Try the latest version** to see if it's already fixed
3. **Gather relevant information** (Python version, OS, error messages)

### Creating a Good Issue
- Use a **clear, descriptive title**
- Provide **steps to reproduce** the problem
- Include **expected vs. actual behavior**
- Add **screenshots** if helpful
- Include **system information**

### Issue Labels
We use these labels:
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to docs
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed

## 🌍 Adding New Language Support

To add support for a new language (e.g., Spanish):

1. **Add language data** to `anagram/bible_books_data.py`:
   ```python
   def get_spanish_bible_books() -> Dict[str, Dict[str, Any]]:
       return {
           "genesis": {
               "display_name": "Génesis",
               "testament": "antiguo",
               "category": "ley",
               "book_number": 1
           },
           # ... continue for all 66 books
       }
   ```

2. **Update the scrambler** in `bible_book_scrambler.py`
3. **Add web interface support** in `web/app.py`
4. **Update UI** in `web/templates/index.html`
5. **Add tests** for the new language
6. **Update documentation**

## 🎯 Feature Request Process

1. **Open an issue** describing the feature
2. **Discuss the approach** with maintainers
3. **Get approval** before starting work
4. **Implement and test** the feature
5. **Submit a pull request**

## 📞 Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: Check README files in each directory

## 🙏 Recognition

All contributors will be recognized in our README file. Thank you for making this project better!

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Happy coding!** 🎮 Thank you for contributing to Bible Book Scramble!