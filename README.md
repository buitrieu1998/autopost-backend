# AutoPost Backend

This project provides a basic API and command line interface for generating images using AI, posting them to Instagram and performing bulk video edits.

## Installation

```bash
pip install -r requirements.txt
```

Set environment variables for required credentials:

```bash
export OPENAI_API_KEY=YOUR_KEY
export IG_ACCESS_TOKEN=YOUR_TOKEN
export IG_ACCOUNT_ID=YOUR_ACCOUNT
```

## Usage

Start the API server:

```bash
uvicorn autopost_backend.main:app --reload
```

Use the command line interface:

```bash
python -m autopost_backend.cli generate-image "A cute robot"
```

### Build executable

To build a Windows executable, install `pyinstaller` and run:

```bash
pyinstaller --onefile -n autopost autopost_backend/cli.py
```

The resulting file will be in the `dist/` directory as `autopost.exe`.
