"uvicorn src.main:app" 
#command to start the program.

#can also use:
"fast api run"
#or
"fast api dev"

"pip install uv"
#install uv for dependencies management

"uv sync"
#install dependencies

# 1. Navigate into the project folder
cd MemeAppPython

# 2. Sync the project (This creates the .venv and installs all dependencies)
uv sync

# 3. Run your app
uv run uvicorn src.main:app --reload