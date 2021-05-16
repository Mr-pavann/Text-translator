from translate import Translator
# enter the language you want to convert the text
translator=Translator(to_lang="telugu")
# enter the text that you want to convert
text="have a nice day"
translation=translator.translate(text)
print(translation)