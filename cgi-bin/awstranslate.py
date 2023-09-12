#!/usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import boto3


# Create an Amazon Translate client
translate = boto3.client('translate', aws_access_key_id="AWS ACCESS KEY",
    aws_secret_access_key="AWS SECRET KEY", region_name="ap-south-1")

print(translate)

# Get form data
form = cgi.FieldStorage()

source_lang = form.getvalue('source_lang', 'en')  # Default to 'auto' for automatic language detection
target_lang = form.getvalue('target_lang', 'hi')    # Default to English
text_to_translate = form.getvalue('text_to_translate', '')

print(source_lang)
print(target_lang)
# Perform translation only if text is provided
if text_to_translate:
    response = translate.translate_text(
        Text=text_to_translate,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    translated_text = response['TranslatedText']

   