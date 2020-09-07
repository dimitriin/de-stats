import json

import boto3

from pkg.vacancy import *
from pkg.report import *
from pkg.skill_recognizer import *

if __name__ == '__main__':
    report = Report()
    provider = VacancyDataProvider()
    recognizer = SkillRecognizer(boto3.client(service_name='comprehend', region_name='eu-central-1'))

    i = 0
    for v in provider.provide('Data Engineer'):
        skill_set = recognizer.recognize(v.desc)

        for skill in skill_set:
            report.add_skill(skill)

        i += 1
        if i % 100 == 0:
            print('Vacancies processed: %d' % i)

            with open("top_skills.json", "w") as outfile:
                json.dump(report.get_top_skills(100), outfile, indent=4)

    print('Vacancies processed: %d' % i)

    with open("top_skills.json", "w") as outfile:
        json.dump(report.get_top_skills(100), outfile, indent = 4)