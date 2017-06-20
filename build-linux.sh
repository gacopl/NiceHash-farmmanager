pyinstaller nhmfm.py
cp -R static dist/nhmfm/static
cp -R templates dist/nhmfm/templates
cp db.sqlite3 dist/nhmfm/
cp nhmfm.conf dist/nhmfm/