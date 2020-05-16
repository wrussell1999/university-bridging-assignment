virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cat creds-template.json > creds.json