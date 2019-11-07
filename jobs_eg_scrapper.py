from bs4 import BeautifulSoup
import requests

def make_request():
    url='https://www.jobs.ge/?page=1&q=&cid=6&lid=&jid='
    responce=requests.get(url,headers={"Accept":"text"})
    data=responce.text
    return data

def parse_jobs_ge():
    soup=BeautifulSoup(make_request(),"html.parser")
    table=soup.find("table",{"id":"job_list_table"})
    jobs=table.find_all("tr")

    job_names=[]
    links=[]

    for item in range(1,len(jobs)):
         if jobs[item].find_all("img")[2]["alt"]=="გამოქვეყნებულია ბოლო 2 დღის განმავლობაში":
            job_names.append(jobs[item].find("a").get_text())
            links.append(jobs[item].find("a")["href"]) # for description
    return job_names

