# -*- mode: python -*-

block_cipher = None


a = Analysis(['manage.py'],
             pathex=['C:\\Users\\gaco\\Desktop\\NHM-farmmanager\\nhmfarmmanager'],
             binaries=[],
             datas=[],
             hiddenimports=['nhmfm.apps', 'django.contrib.auth.apps', 'django.contrib.auth.apps', 'django.contrib.contenttypes.apps', 'django.contrib.sessions.apps', 'django.contrib.messages.apps', 'django.contrib.staticfiles.apps', 'django.contrib.admin.apps', 'nhmfm.urls', 'django.contrib.messages.middleware', 'django.contrib.auth.middleware', 'django.middleware.security', 'django.contrib.sessions.middleware', 'django.middleware.common', 'django.middleware.csrf', 'django.contrib.auth.middleware', 'django.contrib.messages.middleware', 'django.middleware.clickjacking'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='manage',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='manage')
