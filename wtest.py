import wikipedia as wiki
from googletrans import Translator

tarjimon = Translator()
wiki.set_lang("en")
print(wiki.search("backed"))
#wiki.summary("Toshkent")
# pip install googletrans==3.1.0a0

def getTarjimon(word_id):
  lang = tarjimon.detect(word_id).lang
  dest = "en" if lang == "uz" else "uz"
  tarjima = tarjimon.translate(word_id, dest)
  return tarjima

#m = input()
#search = getTarjimon(m)
#res = wiki.summary(m)
#print(res)
#w = getTarjimon(res)
#print(w.text,w.src)