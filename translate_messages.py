from mtranslate import translate
import polib

def translate_po_file(input_po_file, target_language):
    input_po = polib.pofile(input_po_file)

    for entry in input_po:
        if entry.msgstr:
            if not entry.translated():
                translated_text = translate(entry.msgstr, target_language, 'auto')
                entry.msgstr = translated_text

    input_po.save()

if __name__ == "__main__":
    input_po_file = "locale/en/LC_MESSAGES/django.po"
    target_language = "en" 

    translate_po_file(input_po_file, target_language)
