import requests


class Vacancy:
    def __init__(self, desc):
        self.desc = desc


class VacancyDataProvider:

    def provide(self, text):
        page = 1

        while True:
            page_resp = requests.get('https://api.hh.ru/vacancies',
                                     params={'text': text, 'per_page': 100, 'page': page})

            if page_resp.status_code != 200:
                raise RuntimeError

            page_data = page_resp.json()

            for vacancy_data in page_data['items']:
                vacancy_resp = requests.get(vacancy_data['url'])

                if page_resp.status_code != 200:
                    raise RuntimeError

                vacancy_full_data = vacancy_resp.json()

                yield Vacancy(vacancy_full_data['description'])

            page += 1
            if page > page_data['pages']:
                break
