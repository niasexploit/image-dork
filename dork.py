## You must used a python3.*
## Usage : python namefile.py or python3 namefile.py
## 4NDR0 R4T
import urllib.request
import re

banner = """
                                                                                    .-'''-.                            
                                                                   _______         '   _    \                          
.--. __  __   ___                          __.....__               \  ___ `'.    /   /` '.   \              .          
|__||  |/  `.'   `.            .--./)  .-''         '.              ' |--.\  \  .   |     \  '            .'|          
.--.|   .-.  .-.   '          /.''\\  /     .-''"'-.  `.            | |    \  ' |   '      |  '.-,.--.  .'  |          
|  ||  |  |  |  |  |    __   | |  | |/     /________\   \           | |     |  '\    \     / / |  .-. |<    |          
|  ||  |  |  |  |  | .:--.'.  \`-' / |                  |           | |     |  | `.   ` ..' /  | |  | | |   | ____     
|  ||  |  |  |  |  |/ |   \ | /("'`  \    .-------------'           | |     ' .'    '-...-'`   | |  | | |   | \ .'     
|  ||  |  |  |  |  |`" __ | | \ '---. \    '-.____...---.           | |___.' /'                | |  '-  |   |/  .      
|__||__|  |__|  |__| .'.''| |  /'""'.\ `.             .'           /_______.'/                 | |      |    /\  \     
                    / /   | |_||     ||  `''-...... -'             \_______|/                  | |      |   |  \  \    
                    \ \._,\ '/\'. __//                                                         |_|      '    \  \  \   
                     `--'  `"  `'---'                                                                  '------'  '---'                                                                        
     
     Github : github.com/hidayat-code
     Blog : www.hidayatcode.com
"""
print(banner)


def scrap(args):
  args = args.split()
  url = 'https://www.google.co.id/search?ei=c_uHW87hBc_p9QO-6I7wBg&safe=strict&yv=3&tbm=isch&q=' + "+" .join(args)  +'&vet=10ahUKEwiO58Pk-pTdAhXPdH0KHT60A24QuT0IMSgB.c_uHW87hBc_p9QO-6I7wBg.i&ved=0ahUKEwiO58Pk-pTdAhXPdH0KHT60A24QuT0IMSgB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc'
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request(url, headers = headers)
  resp = urllib.request.urlopen(req)
  respData = resp.read()
  paragraphs = re.findall(r'"ou":"(.*?)"',str(respData))
  for eachP in paragraphs:
    print(eachP)

print("--- Google Search Images ---\nCreated By : 4NDRO R4t")
dorks = input("DORK : ")

for kntl in dorks:
  scrap(dorks)
