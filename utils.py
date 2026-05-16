import logging
import re
import json
from pathlib import Path

def get_logger(name: str) -> logging.Logger:
    """Get a logger with the specified name."""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] - %(name)s - %(levelname)s: %(message)s'
    )
    return logging.getLogger(name)


def extract_json_from_text(text: str) -> dict:
    """Extract JSON object from a string. Return empty dict if no valid JSON is found."""
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            json_str = match.group()
            return json.loads(json_str)
        else:
            return {}
    except json.JSONDecodeError:
        return {}
    

def load_file(file_path: str) -> str:
    """Load the content of a file and return it as a string."""
    return Path(file_path).read_text().strip()







