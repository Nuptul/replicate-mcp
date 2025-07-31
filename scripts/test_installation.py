#!/usr/bin/env python3
"""
Replicate MCP - Installation Test Script
By Daniel Fleuren

This script runs comprehensive tests to verify the installation is working correctly.
"""

import os
import sys
import json
import importlib.util
from pathlib import Path

# ANSI color codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # No Color

# Test results
tests_passed = 0
tests_failed = 0
test_results = []

def print_header():
    """Print test header"""
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{CYAN}🚀 Replicate MCP Installation Test Suite{NC}")
    print(f"{CYAN}   By Daniel Fleuren{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

def test_start(name):
    """Start a test"""
    print(f"{BLUE}[TEST]{NC} {name}...", end='', flush=True)

def test_pass(message=""):
    """Mark test as passed"""
    global tests_passed
    tests_passed += 1
    if message:
        print(f" {GREEN}✅ {message}{NC}")
    else:
        print(f" {GREEN}✅{NC}")
    test_results.append(True)

def test_fail(message):
    """Mark test as failed"""
    global tests_failed
    tests_failed += 1
    print(f" {RED}❌ {message}{NC}")
    test_results.append(False)

def test_python_version():
    """Test Python version"""
    test_start("Python Version")
    
    python_version = sys.version_info
    if python_version.major == 3 and python_version.minor >= 8:
        test_pass(f"Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        test_fail(f"Python 3.8+ required, found {python_version.major}.{python_version.minor}")

def test_required_modules():
    """Test required Python modules"""
    test_start("Required Modules")
    
    required_modules = [
        'aiohttp',
        'pydantic',
        'typing_extensions',
        'replicate'
    ]
    
    missing_modules = []
    for module in required_modules:
        spec = importlib.util.find_spec(module)
        if spec is None:
            missing_modules.append(module)
    
    if not missing_modules:
        test_pass("All modules available")
    else:
        test_fail(f"Missing modules: {', '.join(missing_modules)}")

def test_project_structure():
    """Test project directory structure"""
    test_start("Project Structure")
    
    required_paths = [
        'src/replicate_mcp',
        'scripts',
        'docs',
        'examples',
        'assets'
    ]
    
    base_path = Path(__file__).parent.parent
    missing_paths = []
    
    for path in required_paths:
        if not (base_path / path).exists():
            missing_paths.append(path)
    
    if not missing_paths:
        test_pass("All directories present")
    else:
        test_fail(f"Missing directories: {', '.join(missing_paths)}")

def test_mcp_server_import():
    """Test MCP server can be imported"""
    test_start("MCP Server Import")
    
    try:
        # Add src to path
        src_path = Path(__file__).parent.parent / 'src'
        sys.path.insert(0, str(src_path))
        
        # Try to import
        import replicate_mcp
        test_pass(f"Version {replicate_mcp.__version__}")
    except Exception as e:
        test_fail(f"Import error: {str(e)}")

def test_model_catalog():
    """Test model catalog loading"""
    test_start("Model Catalog")
    
    try:
        from replicate_mcp.complete_catalog import COMPLETE_MODEL_CATALOG
        model_count = len(COMPLETE_MODEL_CATALOG)
        
        if model_count > 0:
            test_pass(f"{model_count} models loaded")
        else:
            test_fail("No models in catalog")
    except Exception as e:
        test_fail(f"Catalog error: {str(e)}")

def test_environment_config():
    """Test environment configuration"""
    test_start("Environment Configuration")
    
    api_token = os.environ.get('REPLICATE_API_TOKEN')
    
    if api_token:
        if api_token.startswith('r8_'):
            test_pass("API token format valid")
        else:
            test_fail("Invalid API token format")
    else:
        test_fail("REPLICATE_API_TOKEN not set")

def test_mcp_configuration():
    """Test MCP configuration file"""
    test_start("MCP Configuration")
    
    # Determine config path based on OS
    home = Path.home()
    config_paths = [
        home / '.config' / 'claude-code' / 'mcp_settings.json',  # Linux
        home / 'Library' / 'Application Support' / 'claude-code' / 'mcp_settings.json',  # macOS
        Path(os.environ.get('APPDATA', '')) / 'claude-code' / 'mcp_settings.json'  # Windows
    ]
    
    config_found = False
    valid_config = False
    
    for config_path in config_paths:
        if config_path.exists():
            config_found = True
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    
                if 'mcpServers' in config and 'replicate-media' in config['mcpServers']:
                    valid_config = True
                    break
            except:
                pass
    
    if config_found and valid_config:
        test_pass("Configuration valid")
    elif config_found:
        test_fail("Configuration incomplete")
    else:
        test_fail("Configuration not found")

def test_basic_functionality():
    """Test basic functionality"""
    test_start("Basic Functionality")
    
    try:
        from replicate_mcp.complete_catalog import COMPLETE_MODEL_CATALOG
        
        # Check if we can access model info
        if 'sdxl' in COMPLETE_MODEL_CATALOG:
            sdxl_info = COMPLETE_MODEL_CATALOG['sdxl']
            if 'version' in sdxl_info:
                test_pass("Model access working")
            else:
                test_fail("Model data incomplete")
        else:
            test_fail("SDXL model not found")
    except Exception as e:
        test_fail(f"Functionality error: {str(e)}")

def run_optional_tests():
    """Run optional advanced tests"""
    print(f"\n{BLUE}Running optional tests...{NC}\n")
    
    # Test API connection (if token is set)
    if os.environ.get('REPLICATE_API_TOKEN'):
        test_start("API Connection")
        try:
            import replicate
            client = replicate.Client(api_token=os.environ['REPLICATE_API_TOKEN'])
            # Try to list models (will fail if token is invalid)
            list(client.models.list())
            test_pass("API connection successful")
        except Exception as e:
            test_fail(f"API error: {str(e)}")

def print_summary():
    """Print test summary"""
    total_tests = tests_passed + tests_failed
    success_rate = (tests_passed / total_tests * 100) if total_tests > 0 else 0
    
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{CYAN}📊 TEST SUMMARY{NC}")
    print(f"{BLUE}{'='*60}{NC}")
    
    print(f"Tests Passed: {GREEN}{tests_passed}{NC}/{total_tests}")
    print(f"Tests Failed: {RED}{tests_failed}{NC}/{total_tests}")
    print(f"Success Rate: {GREEN if success_rate == 100 else YELLOW}{success_rate:.1f}%{NC}")
    
    if tests_failed == 0:
        print(f"\nStatus: {GREEN}READY ✅{NC}")
        print(f"\n{GREEN}🎉 Installation is ready to use!{NC}")
        print(f"\nNext steps:")
        print(f"1. Restart Claude Code")
        print(f"2. Try: 'Generate a logo for my startup'")
    else:
        print(f"\nStatus: {RED}NEEDS ATTENTION ⚠️{NC}")
        print(f"\n{YELLOW}Please fix the failed tests above.{NC}")
        print(f"Run './scripts/install.sh' to complete setup.")

def main():
    """Main test runner"""
    print_header()
    
    # Core tests
    print(f"{BLUE}Running core tests...{NC}\n")
    test_python_version()
    test_required_modules()
    test_project_structure()
    test_mcp_server_import()
    test_model_catalog()
    test_environment_config()
    test_mcp_configuration()
    test_basic_functionality()
    
    # Optional tests
    run_optional_tests()
    
    # Summary
    print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if tests_failed == 0 else 1)

if __name__ == "__main__":
    main()