import asyncio
from .utils import Utils

utils = Utils()

class ChangeLanguage():
    def __init__(self,language:str,contents:list):
        self.language = language
        self.contents = contents

    def get_translate_content(self):
        return_content = []
        for content in self.contents:
            result  = asyncio.run(utils.translate_content(self.language,content))
            return_content.append(result)
        return return_content