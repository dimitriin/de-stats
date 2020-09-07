from botocore.client import BaseClient
from bs4 import BeautifulSoup
import lxml


class SkillRecognizer:
    def __init__(self, client: BaseClient):
        self.client = client

    def recognize(self, text):
        text = BeautifulSoup(text, "lxml").text

        if len(text.encode('utf-8')) > 5000:
            return set()

        data = self.client.detect_entities(Text=text, LanguageCode='en')

        if 'Entities' not in data:
            raise RuntimeError

        skills = set()
        for entity_data in data['Entities']:
            if entity_data['Score'] > 0.8 and entity_data['Type'] == 'TITLE':
                skills.add(entity_data['Text'])

        return skills
