import pymongo
import json


def connect_bd():
    client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.bqedr.mongodb.net/?retryWrites=true&w=majority")
    db = client.web
    jobs = db.vagas
    jobs_json = jobs.find()
    jobs_json = (list(jobs_json))
    return jobs_json


def update_json_file():
    jobs_json = connect_bd()
    with open('jobs.json', 'w') as outfile:
        json.dump(jobs_json, outfile, default=str)


def read_json_file():
    update_json_file()
    with open('jobs.json') as file:
        file_data = json.load(file)
    return file_data


def get_jobs_by_technology(technology_type):
    job_list = read_json_file()
    jobs_by_technology = []
    for job in job_list:
        if technology_type in job['technology']:
            jobs_by_technology.append(job)
    return jobs_by_technology


def get_jobs_by_type(job_type):
    job_list = read_json_file()

    for job in job_list:
        job['average'] = 0
    jobs_by_type = []

    for job in job_list:
        if job_type == job['type']:
            jobs_by_type.append(job)

    for job in jobs_by_type:
        del job['type']
        del job['companies']
        del job['_id']
        job['date'] = job['date'][:10]

    for job in jobs_by_type:
        for job2 in jobs_by_type:
            if job['technology'] == job2['technology'] and job != job2:
                job['vacancies'] += job2['vacancies']
                job['average'] = (job['average'] + job2['average']) / 2
                jobs_by_type.remove(job2)
    return jobs_by_type


def return_all_jobs():
    job_list = read_json_file()

    for job in job_list:
        del job['type']
        del job['companies']
        del job['_id']
        job['date'] = job['date'][:10]

    return job_list
