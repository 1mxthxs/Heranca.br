from django.core.management import call_command
from googletrans import Translator
import polib
import os

# Função para traduzir uma mensagem de source_lang para target_lang
def translate_message(message, source_lang, target_lang):
    translator = Translator()
    try:
        translated_text = translator.translate(message, src=source_lang, dest=target_lang).text
        return translated_text
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return None

# Diretórios para os arquivos .po
pt_po_dir = 'locale/pt/LC_MESSAGES/'
en_po_dir = 'locale/en/LC_MESSAGES/'

# Criar arquivos .po com o comando makemessages para português
call_command('makemessages', '-l', 'pt', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')
call_command('makemessages', '-l', 'en', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')

# Iterar pelos arquivos .po em ambos os diretórios
for root, dirs, files in os.walk(pt_po_dir):
    for filename in files:
        if filename.endswith('.po'):
            pt_po_path = os.path.join(root, filename)
            en_po_path = os.path.join(en_po_dir, filename)

            pt_po_file = polib.pofile(pt_po_path)
            en_po_file = polib.pofile(en_po_path)

            for pt_entry in pt_po_file:
                if not pt_entry.msgstr and not pt_entry.fuzzy:
                    original_text = pt_entry.msgid
                    # Traduzir do português (pt) para o inglês (en)
                    translated_text = translate_message(original_text, 'pt', 'en')
                    if translated_text:
                        pt_entry.msgstr = translated_text
                        pt_entry.fuzzy = False

                        # Adicionar a tradução também ao arquivo em inglês
                        en_entry = en_po_file.find(pt_entry.msgid)
                        if en_entry:
                            en_entry.msgstr = translated_text
                            en_entry.fuzzy = False

            # Salvar os arquivos .po
            pt_po_file.save(pt_po_path)
            en_po_file.save(en_po_path)

try:
    os.system("python manage.py compilemessages")
except Exception as e:
    print(f"Erro ao executar o comando compile: {e}")

os.system("python manage.py runserver")
