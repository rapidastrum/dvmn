import requests

london = 'https://wttr.in/london?MnqT&lang=ru'
svo = 'https://wttr.in/svo?MnqT&lang=ru'
cher = 'https://wttr.in/череповец?MnqT&lang=ru'

print(requests.get(london).text)
print(requests.get(svo).text)
print(requests.get(cher).text)