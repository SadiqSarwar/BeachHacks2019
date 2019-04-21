# Imports the Google Cloud client library
from google.cloud import translate
import cgi
import cgitb
cgitb.enable()

inputData = cgi.FieldStorage()

print "Content-Type: text/html"
print

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = inputData["review"].value
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print "<TITLE>TRANSLATION</TITLE>"
print "<H1>Translation Generated</H1>"
print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
