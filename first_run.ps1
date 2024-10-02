python -m venv venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip freeze > requirements.txt
Move-Item .\.gitignore_ph .\.gitignore