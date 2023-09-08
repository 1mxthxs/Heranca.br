from django.core.management import call_command
from googletrans import Translator
import polib
import os

# Função para traduzir uma mensagem de source_lang para target_lang
def translate_message(message, source_lang, target_lang):
    translator = Translator()
    try:
        # Traduz primeiro do source_lang para o espanhol
        translated_text_es = translator.translate(message, src=source_lang, dest='en').text
        # Em seguida, traduz do espanhol para o target_lang
        translated_text = translator.translate(translated_text_es, src='en', dest=target_lang).text
        return translated_text
    except Exception as e:
        print(f"Erro ao traduzir: {e}")
        return None

# Diretórios para os arquivos .po
br_po_dir = 'locale/br/LC_MESSAGES/'
en_po_dir = 'locale/en/LC_MESSAGES/'

# Criar arquivos .po com o comando makemessages
call_command('makemessages', '-l', 'en', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')
call_command('makemessages', '-l', 'br', '-i', 'account/*', '-i' ,'openid/*','-i','socialaccount/*')

# Iterar pelos arquivos .po em ambos os diretórios
for root, dirs, files in os.walk(br_po_dir):
    for filename in files:
        if filename.endswith('.po'):
            br_po_path = os.path.join(root, filename)
            en_po_path = os.path.join(en_po_dir, filename)

            br_po_file = polib.pofile(br_po_path)
            en_po_file = polib.pofile(en_po_path)

            for br_entry in br_po_file:
                if not br_entry.msgstr and not br_entry.fuzzy:
                    original_text = br_entry.msgid
                    # Traduzir do inglês (en) para o espanhol (es) e, em seguida, para o português (pt)
                    translated_text = translate_message(original_text, 'en', 'pt')
                    if translated_text:
                        br_entry.msgstr = translated_text
                        br_entry.fuzzy = False

                        # Adicionar a tradução também ao arquivo em inglês
                        en_entry = en_po_file.find(br_entry.msgid)
                        if en_entry:
                            en_entry.msgstr = translated_text
                            en_entry.fuzzy = False

            # Salvar os arquivos .po
            br_po_file.save(br_po_path)
            en_po_file.save(en_po_path)

try:
    os.system("python manage.py compilemessages")
except Exception as e:
    print(f"Erro ao executar o comando compile: {e}")

os.system("python manage.py runserver")
