"""
Compatibility entry point.

Runtime moved to `simple.editor.runtime`, but we keep `python -m simple.editor_runtime`
working for existing projects/editor versions.
"""

from .editor.runtime import main

if __name__ == "__main__":
    main()

