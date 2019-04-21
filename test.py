# Imports the Google Cloud client library
from flask import Flask, redirect, render_template, request
from google.cloud import translate

app = Flask(__name__)

@app.route('/run_translate', methods=['GET', 'POST'])
def run_translate():
    # Create a Cloud Translate client.
    client = translate.Client()

    # Retrieve Translate API's detect_language response for the input text
    form_text = request.form['text']
    ###detect_language_response = client.detect_language(form_text)
    ###confidence = detect_language_response.get('confidence')
    input_text = detect_language_response.get('textarea')
    language = detect_language_response.get('language')

    # Retrieve Translate API's translate to French response for the input text
    # See https://cloud.google.com/translate/docs/languages for supported target_language values.
    translate_response_french = client.translate(form_text, target_language='fr')
    translated_text_french = translate_response_french.get('translatedText')

    return render_template('reviewpage.html', input_text=input_text, language=language, translated_text_french=translated_text_french

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run()

'''    
# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = inputData["review"].value

# The target language
target = 'en'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
'''
