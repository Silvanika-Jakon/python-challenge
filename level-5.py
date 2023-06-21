import pickle
import urllib.request
with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as resp:
    html = resp.read()
    data = pickle.loads(html)
    for line in data:
        print("".join([first * second for first, second in line]))