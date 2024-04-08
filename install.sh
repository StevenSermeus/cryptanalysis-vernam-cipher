sudo apt install python3.10-venv

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the requirements
pip install -r requirements.txt