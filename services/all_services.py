from changelanguage_service import ChangeLanguage



class AllServices:
    def __init__(self,event,context):
        self.event = event
        self.context = context

    def change_language(self):
        translator = ChangeLanguage(self.event['language'],self.event['content'])
        result = translator.translate_content()
        return result
