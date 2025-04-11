import json
from services.changelanguage_service import ChangeLanguage

def changeLanguage(event, context):
    content = event.body['content']
    language = event.body['language']
    changelanguage = ChangeLanguage(language=language,contents=content)
    tarnslated = changelanguage.get_translate_content()
    response = {"statusCode": 200, "body": json.dumps(tarnslated)}

    return response
