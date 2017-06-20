pyinstaller nhmfm.py
xcopy /E /I static dist\nhmfm\static
xcopy /E /I templates dist\nhmfm\templates
xcopy db.sqlite3 dist\nhmfm\
xcopy nhmfm.conf dist\nhmfm\