# Scam Detection System

An AI-powered scam detection system built with Google Gemini and Streamlit.

## Project Structure

```
scam-detection-system/
│
├── config.py               # Central configuration
├── main.py                 # CLI interface
├── requirements.txt        # Dependencies
├── .env                    # Environment variables (not committed)
├── utils.py                # Common helper functions
│
├── llm/                    # LLM integration layer
│   ├── client.py           # Gemini API client
│   ├── prompts.py          # Prompt management
│   ├── validator.py        # Response validation
│   └── prompts/            # Prompt templates
│       └── scam_detection.txt
│
├── pipeline/               # Core detection pipeline
│   └── scam_detector/
│       ├── detector.py     # Main orchestration
│       ├── builder.py      # Prompt building
│       ├── executor.py     # LLM execution
│       └── parser.py       # Result parsing
│
└── streamlit/              # Web interface
    └── app.py
```

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd scam-detection-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and set your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

### CLI

```bash
# Analyse a text string
python main.py analyse -t "Congratulations! You've won a $1000 gift card. Click here."

# Analyse a text file
python main.py analyse -f message.txt

# Output raw JSON
python main.py analyse -t "Your account has been suspended." --json
```

### Web UI

```bash
streamlit run streamlit/app.py
```

## Configuration

All settings are controlled via environment variables (`.env`):

| Variable | Default | Description |
|---|---|---|
| `GEMINI_API_KEY` | — | Your Google Gemini API key (required) |
| `GEMINI_MODEL` | `gemini-1.5-flash` | Gemini model to use |
| `GEMINI_TEMPERATURE` | `0.2` | Model temperature (0.0–1.0) |
| `GEMINI_MAX_OUTPUT_TOKENS` | `2048` | Max tokens in response |
| `SCAM_CONFIDENCE_THRESHOLD` | `0.7` | Confidence threshold for scam verdict |
| `LOG_LEVEL` | `INFO` | Logging verbosity |

## License

MIT
