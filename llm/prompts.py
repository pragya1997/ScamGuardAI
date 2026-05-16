from pathlib   import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))
from utils import load_file

PROMPT_DIR = Path(__file__).parent / "prompts"

#load prompt templates from external files
def load_prompt(file_name: str) -> str:
    """Load a prompt template from a file."""
    return load_file(PROMPT_DIR / file_name)

#Available prompts
PROMPT = load_prompt("react.md")

def generate_prompt(user_input: str) -> str:
    """
    Generate a prompt for scam detection - choose your strategy here!
    
    Available strategies:
    - REACT_PROMPT: Step-by-step reasoning 
    - FEWSHOT_PROMPT: Learning from examples
    - STRICT_JSON_PROMPT: Clean JSON output
    - SIMPLIFIED_PROMPT: Quick classification
    
    Args:
        user_input: The message to analyze
        use_react: Legacy parameter, defaults to ReAct strategy
        
    Returns:
        A formatted prompt string ready for LLM execution
    """
    template = PROMPT
    return f"{template}\n\nUser Message:\n{user_input.strip()}"