"""
Replicate MCP - AI Media Generation for Claude Code
By Daniel Fleuren
"""

__version__ = "1.0.0"
__author__ = "Daniel Fleuren"
__email__ = "daniel@example.com"

# Import main components when available
try:
    from .complete_catalog import COMPLETE_MODEL_CATALOG
    
    __all__ = [
        "COMPLETE_MODEL_CATALOG",
        "__version__",
        "__author__",
        "__email__"
    ]
except ImportError:
    # Basic imports for testing without dependencies
    __all__ = [
        "__version__",
        "__author__", 
        "__email__"
    ]