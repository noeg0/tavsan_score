import requests
import sys

def tamper (name, score) :
    url = 'http://www.littlebigplay.com/submitAir.php'
    values = { 'score' : score,
               'nickname' : name,
               'gameid' : '145',
               'gameMode' : '3'}
    r = requests.post(url, values)
    
tamper (sys.argv[1], sys.argv[2])
