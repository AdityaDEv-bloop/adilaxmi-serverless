import json
from services.changelanguage_service import ChangeLanguage

def changeLanguage(event, context):
    content = event['content']
    language = event['language']
    changelanguage = ChangeLanguage(language=language,contents=content)
    tarnslated = changelanguage.translate_content()
    response = {"statusCode": 200, "body": json.dumps(tarnslated)}

    return response
