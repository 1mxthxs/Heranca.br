from googletrans import Translator
import polib
import os
from django.core.management import call_command

call_command('makemessages', '-l', 'br', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')
call_command('makemessages', '-l', 'en', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')


## makemessages -l br -i account/*  -i openid/* -i socialaccount/*
## makemessages -l en -i account/*  -i openid/* -i socialaccount/*

po_file = polib.pofile('locale/en/LC_MESSAGES/django.po')

translator = Translator()

for entry in po_file:
    if not entry.msgstr and not entry.fuzzy: 
        original_text = entry.msgid
        try:
            translated_text = translator.translate(original_text, src='pt', dest='en').text
            entry.msgstr = translated_text
            entry.fuzzy = False
        except Exception as e:
            print(f"Erro ao traduzir: {e}")

po_file.save('locale/en/LC_MESSAGES/django.po')

po_file = polib.pofile('locale/br/LC_MESSAGES/django.po')
translator = Translator()

for entry in po_file:
    if not entry.msgstr and not entry.fuzzy: 
        original_text = entry.msgid
        try:
            translated_text = translator.translate(original_text, src='en', dest='pt').text
            entry.msgstr = translated_text
            entry.fuzzy = False
        except Exception as e:
            print(f"Erro ao traduzir: {e}")

po_file.save('locale/br/LC_MESSAGES/django.po')

os.system("python manage.py compilemessages")
os.system("python manage.py runserver")