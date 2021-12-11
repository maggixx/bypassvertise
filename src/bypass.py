import requests

link = "https://bypass.bot.nu/bypass2?url="

def bypass(bypasserlink):
    new = link + bypasserlink
    a = requests.get(new).json()
    return a["destination"]
