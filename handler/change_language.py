import json
from services.changelanguage import ChangeLanguage

def changeLanguage(event, context):
    
    response = {"statusCode": 200, "body": json.dumps(event)}

    return response
