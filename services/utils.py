from googletrans import Translator
import json

class Utils():
    async def translate_content(self,language:str,content:list):
        async with Translator() as translator:
            result = await translator.translate(content, dest=language)
            return result.text