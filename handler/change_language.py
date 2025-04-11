import json
from services.all_services import AllServices

def changeLanguage(event, context):
    service = AllServices(event,context)
    tarnslated = service.change_language()
    response = {"statusCode": 200, "body": json.dumps(tarnslated)}

    return response
