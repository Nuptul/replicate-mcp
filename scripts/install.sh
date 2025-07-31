#!/bin/bash

# Replicate MCP Installation Script
# By Daniel Fleuren
# 
# This script automates the installation of Replicate MCP for Claude Code
# Supports Linux, macOS, and Windows (via WSL)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                    Replicate MCP                          ║"
echo "║          AI Media Generation for Claude Code              ║"
echo "║                  By Daniel Fleuren                        ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Function to print colored output
print_status() {
    echo -e "${BLUE}[*]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        OS="windows"
    else
        print_error "Unsupported operating system: $OSTYPE"
        exit 1
    fi
    print_success "Detected OS: $OS"
}

# Check Python installation
check_python() {
    print_status "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_error "Python not found. Please install Python 3.8 or higher."
        echo "Visit: https://www.python.org/downloads/"
        exit 1
    fi
    
    # Check Python version
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ $PYTHON_MAJOR -eq 3 ] && [ $PYTHON_MINOR -ge 8 ]; then
        print_success "Python $PYTHON_VERSION found"
    else
        print_error "Python 3.8 or higher required. Found: $PYTHON_VERSION"
        exit 1
    fi
}

# Check Claude Code installation
check_claude_code() {
    print_status "Checking Claude Code installation..."
    
    if command -v claude &> /dev/null; then
        print_success "Claude Code CLI found"
    else
        print_warning "Claude Code CLI not found"
        echo "Please install Claude Code from: https://claude.ai/code"
        echo "Continuing with installation..."
    fi
}

# Create virtual environment
setup_venv() {
    print_status "Setting up virtual environment..."
    
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists"
    else
        $PYTHON_CMD -m venv venv
        print_success "Virtual environment created"
    fi
    
    # Activate virtual environment
    if [ "$OS" == "windows" ]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    print_success "Virtual environment activated"
}

# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    pip install --upgrade pip > /dev/null 2>&1
    pip install -r requirements.txt
    pip install -e .
    
    print_success "Dependencies installed"
}

# Get MCP config path
get_mcp_config_path() {
    if [ "$OS" == "linux" ]; then
        MCP_CONFIG_PATH="$HOME/.config/claude-code/mcp_settings.json"
        MCP_CONFIG_DIR="$HOME/.config/claude-code"
    elif [ "$OS" == "macos" ]; then
        MCP_CONFIG_PATH="$HOME/Library/Application Support/claude-code/mcp_settings.json"
        MCP_CONFIG_DIR="$HOME/Library/Application Support/claude-code"
    elif [ "$OS" == "windows" ]; then
        MCP_CONFIG_PATH="$APPDATA/claude-code/mcp_settings.json"
        MCP_CONFIG_DIR="$APPDATA/claude-code"
    fi
}

# Configure MCP settings
configure_mcp() {
    print_status "Configuring MCP settings..."
    
    get_mcp_config_path
    
    # Create directory if it doesn't exist
    mkdir -p "$MCP_CONFIG_DIR"
    
    # Get current directory
    CURRENT_DIR=$(pwd)
    
    # Check if config exists
    if [ -f "$MCP_CONFIG_PATH" ]; then
        print_warning "MCP configuration already exists"
        echo -n "Do you want to update it? (y/n): "
        read -r UPDATE_CONFIG
        
        if [[ ! "$UPDATE_CONFIG" =~ ^[Yy]$ ]]; then
            print_status "Keeping existing configuration"
            return
        fi
        
        # Backup existing config
        cp "$MCP_CONFIG_PATH" "$MCP_CONFIG_PATH.backup"
        print_success "Backed up existing configuration"
    fi
    
    # Create new config
    cat > "$MCP_CONFIG_PATH" << EOF
{
  "mcpServers": {
    "replicate-media": {
      "command": "$PYTHON_CMD",
      "args": ["$CURRENT_DIR/src/replicate_mcp/server.py"],
      "env": {
        "REPLICATE_API_TOKEN": "",
        "REPLICATE_BUDGET_LIMIT": "100.0",
        "REPLICATE_CACHE_ENABLED": "true",
        "REPLICATE_QUALITY_PREFERENCE": "balanced"
      }
    }
  }
}
EOF
    
    print_success "MCP configuration created at: $MCP_CONFIG_PATH"
}

# Get API key
get_api_key() {
    print_status "Setting up Replicate API key..."
    
    # Check if already set
    if [ ! -z "$REPLICATE_API_TOKEN" ]; then
        print_success "API key already set in environment"
        return
    fi
    
    echo ""
    echo "To use Replicate MCP, you need a Replicate API key."
    echo "Get your key at: https://replicate.com/account/api-tokens"
    echo ""
    echo -n "Enter your Replicate API key (or press Enter to skip): "
    read -s API_KEY
    echo ""
    
    if [ ! -z "$API_KEY" ]; then
        # Update MCP config with API key
        if [ "$OS" == "macos" ]; then
            sed -i '' "s/\"REPLICATE_API_TOKEN\": \"\"/\"REPLICATE_API_TOKEN\": \"$API_KEY\"/" "$MCP_CONFIG_PATH"
        else
            sed -i "s/\"REPLICATE_API_TOKEN\": \"\"/\"REPLICATE_API_TOKEN\": \"$API_KEY\"/" "$MCP_CONFIG_PATH"
        fi
        
        # Also set in current environment
        export REPLICATE_API_TOKEN="$API_KEY"
        
        # Add to shell profile
        SHELL_PROFILE=""
        if [ -f "$HOME/.bashrc" ]; then
            SHELL_PROFILE="$HOME/.bashrc"
        elif [ -f "$HOME/.zshrc" ]; then
            SHELL_PROFILE="$HOME/.zshrc"
        elif [ -f "$HOME/.bash_profile" ]; then
            SHELL_PROFILE="$HOME/.bash_profile"
        fi
        
        if [ ! -z "$SHELL_PROFILE" ]; then
            echo "" >> "$SHELL_PROFILE"
            echo "# Replicate MCP API Key" >> "$SHELL_PROFILE"
            echo "export REPLICATE_API_TOKEN=\"$API_KEY\"" >> "$SHELL_PROFILE"
            print_success "API key added to $SHELL_PROFILE"
        fi
        
        print_success "API key configured"
    else
        print_warning "No API key provided. You'll need to set it later."
    fi
}

# Test installation
test_installation() {
    print_status "Testing installation..."
    
    # Run test script
    if $PYTHON_CMD scripts/test_installation.py; then
        print_success "All tests passed!"
    else
        print_error "Some tests failed. Please check the output above."
    fi
}

# Final instructions
show_instructions() {
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║              Installation Complete! 🎉                    ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Restart Claude Code to load the MCP server"
    echo "2. Try: 'Generate a professional logo for my startup'"
    echo "3. Check examples in: examples/"
    echo "4. Read documentation in: docs/"
    echo ""
    
    if [ -z "$REPLICATE_API_TOKEN" ]; then
        echo -e "${YELLOW}Remember to set your API key:${NC}"
        echo "export REPLICATE_API_TOKEN='your_key_here'"
        echo ""
    fi
    
    echo "Need help? Visit: https://github.com/danielfleuren/replicate-mcp"
    echo ""
}

# Main installation flow
main() {
    echo "Starting Replicate MCP installation..."
    echo ""
    
    # Run checks
    detect_os
    check_python
    check_claude_code
    
    # Setup
    setup_venv
    install_dependencies
    configure_mcp
    get_api_key
    
    # Test
    test_installation
    
    # Done
    show_instructions
}

# Run main function
main