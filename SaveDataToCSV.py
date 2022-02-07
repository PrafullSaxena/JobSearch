import csv
from datetime import date

def printOnScreen(jobResult: list, filename):
    print(f'Filename - {filename}')
    for job in jobResult:
        print(f'JobProfile = {job[0]}')
        print(f'Company Name = {job[1]}')
        print(f'Skills Required = {job[2]}')
        print(f'Location = {job[3]}')
        print(f'Job Publish Date = {job[4]}')
        print(f'MoreInfo = {job[5]}')
        print(f' ')

def saveToCSV(jobsResult : list, Filename : str):

    fields = ['JobProfile', 'Company Name' ,'Skills Required', 'Location', 'Job Publish Date' ,'MoreInfo']
    with open(Filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(jobsResult)


def validate_Info(jobsResult : list, isRecent : bool, lookingFor: str):
    today = date.today();
    Filename = str(lookingFor).replace('+', '_') + '-' + 'Jobs' + '-' + str(today) + '.csv'
    if isRecent:
        Filename = 'lastest-only' + Filename;

    saveToCSV(jobsResult, Filename)





if __name__ == '__main__':
    pass
