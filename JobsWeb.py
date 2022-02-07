from bs4 import BeautifulSoup
import requests
import SaveDataToCSV as sv


def getInfo(url : str, isRecent : bool, lookingFor : str):
    #html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml');
    jobs = soup.findAll('li', class_ = 'clearfix job-bx wht-shd-bx')

    jobsList = []

    for job in jobs:
        list = []
        few = "Posted 3 days ago" #.replace(' ', '')
        Publis_Date = job.find('span', class_ = 'sim-posted').span.text #.replace(' ', '');

        if isRecent:
            if few in Publis_Date:
                Job_Profile = job.header.h2.a.strong.text.replace(' ', '')
                more_info = job.find('ul', class_='list-job-dtl clearfix').li.a['href']
                Company_Name = job.find('h3', class_='joblist-comp-name').text
                Skills_Set = job.find('span', class_='srp-skills').text.replace(' ', '').replace(',', ', ')
                location = job.find('ul', class_='top-jd-dtl clearfix').text.split()[-1]

                list.append(Job_Profile)
                list.append(Company_Name.strip())
                list.append(Skills_Set.strip())
                list.append(location.strip())
                list.append(Publis_Date.strip())
                list.append(more_info.strip())

                jobsList.append(list)
        else:
            Job_Profile = job.header.h2.a.strong.text  #.replace(' ', '')
            more_info = job.find('ul', class_='list-job-dtl clearfix').li.a['href']
            Company_Name = job.find('h3', class_='joblist-comp-name').text
            Skills_Set = job.find('span', class_='srp-skills').text.replace(' ', '').replace(',', ', ')
            location = job.find('ul', class_='top-jd-dtl clearfix').text.split()[-1]

            list.append(Job_Profile)
            list.append(Company_Name.strip())
            list.append(Skills_Set.strip())
            list.append(location.strip())
            list.append(Publis_Date.strip())
            list.append(more_info.strip())

            jobsList.append(list)


    # sv.saveToCSV(jobsList)
    sv.validate_Info(jobsList, isRecent, lookingFor)

#https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer

def valiDating_Input(lookingFor, experience, isRecentPost):
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='\
          +str(lookingFor)+'&txtLocation=&cboWorkExp1='\
          +str(experience)
    getInfo(url, isRecentPost, lookingFor)

if __name__ == '__main__':
    pass