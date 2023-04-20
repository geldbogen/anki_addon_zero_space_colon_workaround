from json import JSONDecodeError
from aqt import mw,gui_hooks,editor,addcards
from anki.hooks import addHook
import requests
import os
global editorWindow
english_field="english word"
english_definitions_field="english definition"
german_translation_field="german translation"
german_translation_field_alternative="alternative translations"
pronunciation_field="pronunciation (sound)"
etymology_field="etymology"
difficulty_score_field="difficulty/frequency"
slang_information_field="slang information"
slang_example_field="slang example sentences"
slang_url_field="urbandictionary-url"
example_sentences_entry="example sentences"
examples_prepared_field="prepared sentences"

# ankiusername="User 1"
# windowsusername="Julius"


def fill_the_fields(flag):
    global editorWindow
    n=editorWindow.editor.note
    word=""
    examples=""

    search_string=mw.col.media.strip(n[english_field])

    editorWindow.editor.loadNote()



def menu_popup(self,menu):
    
    global editorWindow
    editorWindow=self
    a=menu.addAction("Automatisch Ausfüllen")
    a.triggered.connect(fill_the_fields)

def your_function():
    addcards.add_current_note()
    pass

def setupButtons(buttons, editor): 
    [...]
    btn = editor.addButton(os.path.join(os.path.dirname(__file__), "banana.svg"),
                         'foo',
                         your_function,
                         tip='hover etxt')
    buttons.append(btn)



gui_hooks.editor_did_init_buttons.append(setupButtons)

addHook('EditorWebView.contextMenuEvent', menu_popup)