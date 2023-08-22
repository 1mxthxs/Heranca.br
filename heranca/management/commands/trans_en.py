import os
from googletrans import Translator
import polib
from django.core.management import BaseCommand
from pathlib import Path

class Command(BaseCommand):

    def handle(self, *args, **options ):
        BASE_DIR = Path(__file__).resolve().parent.parent
        if __name__ == "__main__":
            # Caminho do arquivo PO para o idioma inglês (en)
            #caminho_po_en = BASE_DIR / 'locale/en/LC_MESSAGES/django.po'
            caminho_po = os.path.join(BASE_DIR, 'locale/en/LC_MESSAGES/django.po')

            idioma_destino = options.get('lang')
            print(options.get('lang'))

            
            translator = Translator()
            po = polib.pofile(caminho_po)

            for entry in po:
                if entry.msgstr == "":
                    # Apenas traduz mensagens que não possuem tradução
                    traducao = translator.translate(entry.msgid, dest=idioma_destino)
                    entry.msgstr = traducao.text

            # Salva as alterações no arquivo PO
            po.save()    
            