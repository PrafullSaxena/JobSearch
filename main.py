import JobsWeb as st
import enum


SearchFor : str = '';
Experience: str = '';
ResentPost: bool = False;
Wait_Time = 0;


class SkillToSearch (enum.Enum):
    def __str__(self):
        return str(self.value)

    JAVA = 'java'
    PYTHON = 'python'
    DEVELOPER = 'Software+Developer'
    STORAGE = 'Storage+Engineer'
    NET_ADMIN = 'Network+Admin'
    DBA = "Database+Administrator"

def set_ResentPost():
    global ResentPost
    check_isResentPost = input("Do you wish to look for most recent posts <less then 3 days> [defalut: n] : y/n> ")
    if(check_isResentPost == 'y'):
        ResentPost = True
    else:
        ResentPost = False

def set_Experience():
    global Experience
    exp = int(input("Please enter your experiece <1...10> [Default - 2] > "))
    if(exp >= 1 and exp <= 10):
        Experience = exp;
    else:
        Experience = 2;

def set_SkillToSearch():
    global SkillToSearch, SearchFor;
    print(f'''

Select Your Job Profile/Skills

1. Java
2. Python
3. Network Admin
4. Storage Engineer
5. Software Developer
6. Database Administrator

    ''')
    index = int(input("Enter the Index > "))

    if(index == 1):
        SearchFor = SkillToSearch.JAVA
    elif(index == 2):
        SearchFor = SkillToSearch.PYTHON
    elif(index == 3):
        SearchFor = SkillToSearch.NET_ADMIN
    elif(index == 4):
        SearchFor = SkillToSearch.STORAGE
    elif(index == 5):
        SearchFor = SkillToSearch.DEVELOPER
    elif(index == 6):
        SearchFor = SkillToSearch.DBA
    else:
        print("Please enter Correct Information")
        exit(0)

def set_WaitTime():
    global Wait_Time
    getTime = int(input("Enter time if you want to get updates after given minute [default: disabled] > "))
    Wait_Time = getTime


def Starting_Script():
    global Wait_Time;
    # if (Wait_Time)
    st.valiDating_Input(SearchFor, Experience, ResentPost)



def print_Info():
    global SearchFor, Experience, ResentPost
    print(f'SearchFor = {SearchFor}')
    print(f'Experience = {Experience}')
    print(f'showRecent = {ResentPost}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    set_SkillToSearch();
    set_Experience();
    set_ResentPost();
    Starting_Script();

