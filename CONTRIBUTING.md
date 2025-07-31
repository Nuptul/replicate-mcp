# Contributing to Replicate MCP

Thank you for your interest in contributing to Replicate MCP! We welcome contributions from the community.

## 🤝 How to Contribute

### Reporting Issues

1. Check if the issue already exists
2. Create a new issue with a clear title
3. Provide detailed description and steps to reproduce
4. Include error messages and logs if applicable

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`python scripts/test_installation.py`)
5. Commit with clear message (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/replicate-mcp.git
cd replicate-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install in development mode
pip install -r requirements.txt
pip install -e .
```

## 📝 Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Write tests for new features

## 🧪 Testing

Run tests before submitting:

```bash
python scripts/test_installation.py
```

## 📚 Documentation

- Update README.md if needed
- Add docstrings to new functions
- Update examples if adding features
- Keep documentation clear and concise

## 🎯 Areas for Contribution

- **New Models**: Add support for new Replicate models
- **Workflows**: Create new workflow templates
- **Examples**: Add more usage examples
- **Documentation**: Improve guides and tutorials
- **Bug Fixes**: Fix reported issues
- **Performance**: Optimize code performance
- **Tests**: Add more test coverage

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 💬 Questions?

Feel free to open an issue or reach out to daniel@example.com

---

Thank you for contributing! 🎉