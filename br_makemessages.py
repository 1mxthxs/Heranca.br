from django.core.management import call_command
import os
from googletrans import Translator
import polib



#python manage.py makemessages -l en -i  account/* -i openid/* -i socialaccount/*
call_command('makemessages', '-l', 'en', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')

#python manage.py makemessages -l br -i  account/* -i openid/* -i socialaccount/*
call_command('makemessages', '-l', 'br', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')


try:
    po_file = polib.pofile('locale/pt/LC_MESSAGES/django.po')

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

    po_file.save('locale/pt/LC_MESSAGES/django.po')

    try:
        os.system("python manage.py compilemessages")
    except Exception as e:
        print(f"Erro ao executar o comando compile: {e}")
except Exception as e:
    print(f"Erro ao executar o arquivo: {e}")

 
os.system("python manage.py runserver")
