import json
import pandas as pd

vaccine_words_list = {'covidvaccine', 'vaccine', 'vaccines', 'vaccinate', 'vaccination', 'immunize', 'immunization',
                      'immunise', 'immunisation'}

vacinne_hashtag_list = {'#vaccine', '#vaccination', '#Vaccineswork', '#Vaccinesavelives',
                      '#Worldimmunization', '#Vax', '#VaxWithMe', '#Healthforall', '#WiW', '#ThankYouLaura',
                      '#LearnTheRisk', '#VaccineInjury', '#VaccineDeath', '#VaccineDamage', '#VaccinesCauseAutism',
                      '#CDCFraud', '#CDCWhistleBlower', '#CDCTruth', '#WakeUpAmerica', '#HearUs', '#HealthFreedom'}

# december
for i in range(1, 31, 1):
    with open("data/ready_december{}_december{}.jsonl".format(i, i + 1), 'r') as file:
        data = list(file)
        print(len(data))
        total = 0
    with open('data/US_revised_december{}_december{}.json'.format(i, i + 1), 'w') as outfile:
        for json_str in data:
            result = json.loads(json_str)
            try:
                place = result['place']['country_code']
                text = result['full_text']
                print(text)
                if place == 'US' and any(word in text for word in vaccine_words_list):
                    json.dump(result, outfile)
                    total = total + 1
                    print(total)
            except:
                pass

# new year
with open("data/ready_december31_january1.jsonl", 'r') as file:
    data = list(file)
    print(len(data))
    total = 0
with open('data/US_revised_december31_january1.json', 'w') as outfile:
    for json_str in data:
        result = json.loads(json_str)
        try:
            place = result['place']['country_code']
            text = result['full_text']
            if place == 'US' and any(word in text for word in vaccine_words_list):
                json.dump(result, outfile)
                total = total + 1
                print(total)
        except:
            pass

# january
for i in range(1, 9, 1):
    with open("data/ready_january{}_january{}.jsonl".format(i, i + 1), 'r') as file:
        data = list(file)
        print(len(data))
        total = 0
    with open('data/US_revised_january{}_january{}.json'.format(i, i + 1), 'w') as outfile:
        for json_str in data:
            result = json.loads(json_str)
            try:
                place = result['place']['country_code']
                text = result['full_text']
                if place == 'US' and any(word in text for word in vaccine_words_list):
                    json.dump(result, outfile)
                    total = total + 1
                    print(total)
            except:
                pass
