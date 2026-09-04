import re
from pathlib import Path

FENCE_LINE = re.compile(r'^\s*```[a-zA-Z]*\s*$')

def strip_markdown_fences(text: str) -> str:
    """Remove ANY line that is only a markdown fence marker, wherever it appears."""
    lines = text.split('\n')
    cleaned = [line for line in lines if not FENCE_LINE.match(line)]
    return '\n'.join(cleaned)

def clean_sandbox_py_files(sandbox_dir="sandbox"):
    for f in Path(sandbox_dir).glob("*.py"):
        content = f.read_text()
        cleaned = strip_markdown_fences(content)
        if cleaned != content:
            f.write_text(cleaned)
            print(f"Cleaned fences from {f}")

if __name__ == "__main__":
    clean_sandbox_py_files()



