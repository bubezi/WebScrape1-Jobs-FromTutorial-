from bs4 import BeautifulSoup as BF
import requests
import time
import os

website = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

print(f'\nThis bot generates files with Jobs available on {website[:25]} for python\n')
unfamiliar_skill = input("Input some Skill that you are not familar with: ")
print(f'Filtering out {unfamiliar_skill}')

dir_list = os.listdir()
if 'posts' not in dir_list:
    os.mkdir('posts')

def find_jobs():
    html_text = requests.get(website).text
    soup = BF(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text


        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find('span', class_='srp-skills').text
            experience = job.li.text.replace('card_travel', '')
            more_info = job.header.h2.a['href']
            
            if unfamiliar_skill not in skills:
                with open(f'posts/{company_name.strip()}.txt', 'w') as f:
                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"Required Experience: {experience.strip()}\n")
                    f.write(f'More Info: {more_info}\n')
                
                print(f'The file saved in the posts folder: {company_name.strip()}.txt ')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)