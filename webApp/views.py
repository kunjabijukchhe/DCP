from django.shortcuts import render
from os import fdopen

# Create your views here.

f = open('access.log')
lines = f.readlines()

def timeLog():
   listDate = []
   dates = []
   time = []
   for line in lines:
       ip = line.split()[3]
       listDate.append(ip)

   for dateTime in listDate:
       import re
       line = re.sub('[[]', '', dateTime)
       dates.append(line)

   for date in dates:
       temp = (date.split(':')[-5:-1])
       temp = "-".join(temp)
       time.append(temp)

   return time


def getOs():
   listOs = []
   for line in lines:
       os = line.split()[15]
       listOs.append(os)

   return listOs
def operatingSystem(request):
    os = getOs()
    osCount = {}
    name=[]
    num=[]
    for oses in os:
       if oses in osCount:
           osCount[oses] = osCount[oses]+1
       else:
           osCount[oses] = 1

    for i in osCount.keys():
        name.append(i)
    

    for j in osCount.values():
        num.append(j)
    return render(request,'os.html',{'a':osCount,'b':os,'c':name,'d':num})

def getBrowser():
   listBrowser = []
   for line in lines:
       browser = line.split()[12]
       listBrowser.append(browser)
   return listBrowser
def browser(request):
    browsers = getBrowser()
    browserCount = {}
    name=[]
    num=[]
    for browser in browsers:
       if browser in browserCount:
           browserCount[browser] = browserCount[browser]+1
       else:
           browserCount[browser] = 1
    for i in browserCount.keys():
        name.append(i)
    

    for j in browserCount.values():
        num.append(j)
    return render(request,'browser.html',{'a':browserCount,'b':browsers,'c':name,'d':num})

def getIP():

   listIP = []
   for line in lines:
       ip = line.split()[0]
       listIP.append(ip)
   return listIP

def getCountry():
    import requests
    import json
    ips = getIP()
    countries = []
    # apiKey = 'b67567fd8a344bd88f011e4d1b865c5d'
    apiKey = '04d1d69a46a846fb97fb92a8d9f0476d'

    
    for ip in ips:
        url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + \
            apiKey+'&ip='+ip + '&fields=country_name'
        response = requests.get(url)
        a = response.text
        data = json.loads(a)
        countries.append(data['country_name'])
        print(response)
    return countries

def country(request):
    country = getCountry()
    Countrycount = {}

    name=[]
    num=[]
    for cou in country:
        if cou in Countrycount:
            Countrycount[cou] = Countrycount[cou]+1
        else:
            Countrycount[cou] = 1

    for i in Countrycount.keys():
        name.append(i)
    

    for j in Countrycount.values():
        num.append(j)
    return render(request,'country.html',{'a':Countrycount,'b':country,'c':name,'d':num})
def times(request):
    count={}
    name=[]
    num=[]
    time=timeLog()
    for cou in time:
        if cou in count:
            count[cou] = count[cou]+1
        else:
            count[cou] = 1
    for i in count.keys():
        name.append(i)
    

    for j in count.values():
        num.append(j)

    return render(request,'time.html',{'a':name,'b':num})

def index(request):
    country = getCountry()
    browsers = getBrowser()
    os = getOs()
    time= timeLog()
    return render(request,'index.html',{'a':country,'b':browsers,'c':os,'d':time})

def UserInput(ip):
    import requests
    import json
    ips = ip
    countries = []
    # apiKey = 'b67567fd8a344bd88f011e4d1b865c5d'
    apiKey = '04d1d69a46a846fb97fb92a8d9f0476d'

    # url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + \
    #         apiKey+'&ip='+ip 
   
    url = 'https://api.ipgeolocation.io/ipgeo?apiKey=' + \
            apiKey+'&ip='+ip + '&fields=country_name,continent_name,country_capital,state_prov,district,city,zipcode,latitude,longitude,calling_code,country_tld,isp'

    response = requests.get(url)
    a = response.text
    data = json.loads(a)
    # countries.append(data['country_name'])
    print(response)
    # print(countries)
    
    return data

def search(request):
    
    name=[]
    num=[]
    if request.method=="POST":
        userip=request.POST.get('userInput')
        print(userip)
        record=UserInput(userip)
    else:
        print("error")
    for i in record.keys():
        name.append(i)
    
    for j in record.values():
        num.append(j)
    return render(request,'search.html',{'a':name,'b':num,'c':record})

