# Installation Guide

Complete installation guide for Replicate MCP by Daniel Fleuren.

## 📋 Prerequisites

### System Requirements

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **Claude Code CLI** ([Install](https://claude.ai/code))
- **Replicate API Key** ([Get yours](https://replicate.com/account/api-tokens))

### Supported Platforms

- ✅ **Linux** (Ubuntu 20.04+, CentOS 8+, Debian 11+)
- ✅ **macOS** (10.15+, both Intel and Apple Silicon)
- ✅ **Windows** (10/11 with WSL2 recommended)

## 🚀 Quick Installation

### Method 1: Automated Installation (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nuptul/replicate-mcp.git
   cd replicate-mcp
   ```

2. **Run the installer**
   ```bash
   ./scripts/install.sh
   ```

3. **Follow the prompts**
   - The installer will check dependencies
   - Configure MCP settings automatically
   - Prompt for your Replicate API key
   - Test the installation

That's it! 🎉

### Method 2: Manual Installation

1. **Clone and setup**
   ```bash
   git clone https://github.com/Nuptul/replicate-mcp.git
   cd replicate-mcp
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Configure MCP settings**
   
   Create or edit `~/.config/claude-code/mcp_settings.json`:
   ```json
   {
     "mcpServers": {
       "replicate-media": {
         "command": "python",
         "args": ["/path/to/replicate-mcp/src/replicate_mcp/server.py"],
         "env": {
           "REPLICATE_API_TOKEN": "your_token_here",
           "REPLICATE_BUDGET_LIMIT": "100.0"
         }
       }
     }
   }
   ```

5. **Set API key**
   ```bash
   export REPLICATE_API_TOKEN="your_token_here"
   ```

## 🔧 Configuration

### Environment Variables

```bash
# Required
export REPLICATE_API_TOKEN="your_token_here"

# Optional
export REPLICATE_BUDGET_LIMIT="100.0"          # Monthly budget limit ($)
export REPLICATE_CACHE_ENABLED="true"          # Enable result caching
export REPLICATE_QUALITY_PREFERENCE="balanced" # quality|speed|cost
export REPLICATE_LOG_LEVEL="INFO"              # DEBUG|INFO|WARNING|ERROR
```

### MCP Configuration

The MCP settings file location depends on your OS:

- **Linux**: `~/.config/claude-code/mcp_settings.json`
- **macOS**: `~/Library/Application Support/claude-code/mcp_settings.json`
- **Windows**: `%APPDATA%/claude-code/mcp_settings.json`

## 🧪 Testing Installation

### Run the test suite
```bash
python scripts/test_installation.py
```

Expected output:
```
🚀 Running comprehensive installation tests...

✅ Python Version: 3.11.0 ✓
✅ Required Modules: All available
✅ Project Structure: Complete
✅ MCP Server Import: Success
✅ Model Catalog: 50+ models loaded
✅ Environment Configuration: Valid
✅ MCP Configuration: Found and valid
✅ Basic Functionality: Working

📊 TEST SUMMARY
Tests Passed: 8/8
Success Rate: 100.0%
Status: READY ✅

🎉 Installation is ready to use!
```

### Test with Claude Code

1. **Restart Claude Code** to load the MCP server
2. **Try a simple command**:
   ```
   Generate a professional logo for my tech startup
   ```
3. **Check the response** for media generation

## 🐛 Troubleshooting

### Common Issues

#### Python Version Error
```bash
❌ Python 3.8+ required, found 3.7.x
```
**Solution**: Upgrade Python to 3.8 or higher

#### Missing Dependencies
```bash
❌ Missing required modules: aiohttp, pydantic
```
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

#### API Key Not Set
```bash
⚠️ REPLICATE_API_TOKEN not set
```
**Solution**: Set your API key
```bash
export REPLICATE_API_TOKEN="your_token_here"
```

#### Claude Code Not Found
```bash
⚠️ Claude Code not found
```
**Solution**: Install Claude Code from https://claude.ai/code

#### MCP Server Not Loading
```bash
❌ MCP server not found in configuration
```
**Solution**: Check MCP settings file and restart Claude Code

### Advanced Troubleshooting

#### Enable Debug Logging
```bash
export REPLICATE_LOG_LEVEL="DEBUG"
python src/replicate_mcp/server.py
```

#### Check MCP Server Manually
```bash
# Test server startup
python src/replicate_mcp/server.py --help

# Test with sample input
echo '{"method": "tools/list"}' | python src/replicate_mcp/server.py
```

#### Verify API Connection
```bash
# Test API key
python -c "
import replicate
replicate.api_token = 'your_token_here'
try:
    models = replicate.models.list()
    print('✅ API connection successful')
except Exception as e:
    print(f'❌ API error: {e}')
"
```

### Platform-Specific Issues

#### Windows WSL2
- Use WSL2 for best compatibility
- Install Python in WSL2, not Windows
- Use Linux paths in MCP configuration

#### macOS Apple Silicon
- Use native Python installation
- Avoid Rosetta emulation for better performance
- Install via Homebrew if needed:
  ```bash
  brew install python@3.11
  ```

#### Linux Package Managers
- **Ubuntu/Debian**: `sudo apt install python3 python3-pip python3-venv`
- **CentOS/RHEL**: `sudo yum install python3 python3-pip`
- **Arch**: `sudo pacman -S python python-pip`

## 🔄 Updating

### Update to Latest Version
```bash
cd replicate-mcp
git pull origin main
pip install -r requirements.txt --upgrade
```

### Update MCP Configuration
```bash
# Backup existing config
cp ~/.config/claude-code/mcp_settings.json ~/.config/claude-code/mcp_settings.json.backup

# Run installer to update config
./scripts/install.sh
```

## 🚀 Next Steps

After successful installation:

1. **Try basic commands** in Claude Code
2. **Explore examples** in `examples/` directory
3. **Read the user guide** in `docs/usage.md`
4. **Check out workflows** in `docs/workflows.md`
5. **Join the community** on GitHub Discussions

## 💬 Getting Help

- **Documentation**: Check all files in `docs/`
- **Issues**: [GitHub Issues](https://github.com/Nuptul/replicate-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Nuptul/replicate-mcp/discussions)
- **Email**: daniel@example.com

## 📋 Installation Checklist

- [ ] Python 3.8+ installed and working
- [ ] Claude Code CLI installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] MCP configuration created
- [ ] API key configured
- [ ] Installation tests pass
- [ ] Claude Code restarted
- [ ] Basic functionality tested
- [ ] Ready to create amazing media! 🎨

---

*Having trouble? Don't worry! Check the troubleshooting section above or reach out for help.*