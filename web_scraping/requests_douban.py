import requests
import random


site = "https://dl.3dmgame.com/pc/127570.html"
site2 = "https://book.douban.com/people/pekingcat/wish?start=30&sort=time&rating=all&filter=all&mode=grid"
site3 = "https://book.douban.com/people/pekingcat/collect?start=105&sort=time&rating=all&filter=all&mode=grid"
site4 = "https://book.douban.com/people/pekingcat/collect"

headers = {
    "user-agent":"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)"
}
cookie={
    "__utma":"81379588.352940785.1565655500.1565655500.1565655500.1",
    "__utmb":"81379588.1.10.1565655500",
    "__utmc":"81379588",
    "__utmz":"81379588.1565655500.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "_pk_id.100001.3ac3":"a7561b55aa79516c.1565655500.1.1565655500.1565655500.",
    "_pk_ses.100001.3ac3":"*"
}
cookie2={
    # "ll":"108231",
    "bid":"arandomvalu"
}


pro = ['42.238.90.152', '163.204.245.219', '182.35.87.154','60.13.42.200','112.85.169.12','112.85.169.199','163.204.241.50','182.35.80.244','182.35.83.203','183.166.97.89','112.87.71.96']
num = 2
params = {
    "sort":"time",
    "filter":"all",
    # "mode":"grid",
    # "rating":"all",
    "start":num*15,
    }

resp = requests.get(site4,headers=headers,proxies={'http':random.choice(pro)},cookies=cookie2,params=params)
# re.encoding = 'utf-8'
print(resp.status_code)
with open("dou6.txt","w",encoding='utf-8') as f:
    f.write(resp.text)
    f.flush()
