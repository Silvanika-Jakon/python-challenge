import urllib.request
import re
nothing = '12345'
for i in range(400):
   with urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}') as resp:
      html = str(resp.read())
      try:
         nothing = re.findall('[\d]{1,}', html)[-1]
         if nothing == '16044':
            nothing = str(int(nothing) // 2)
         print(html)
         print(nothing, i)
      except:
         print(html) #that's the answer
         break

