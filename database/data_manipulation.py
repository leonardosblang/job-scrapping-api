import json

import pymongo


def connect_bd():
    client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.bqedr.mongodb.net/?retryWrites=true&w=majority")
    db = client.web
    jobs = db.vagas
    jobs_json = jobs.find()
    jobs_json = (list(jobs_json))
    return jobs_json


def update_json_file():
    jobs_json = connect_bd()
    with open('jobs2.json', 'w') as outfile:
        json.dump(jobs_json, outfile, default=str)


def read_json_file():
    update_json_file()
    with open('jobs2.json') as file:
        file_data = json.load(file)
    return file_data




def get_jobs_by_type(job_type):
    client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.bqedr.mongodb.net/?retryWrites=true&w=majority")
    db = client.web
    jobs = db.vagas

    jobs_json = jobs.find({"type": job_type})
    jobs_json = (list(jobs_json))

    for job in jobs_json:
        try:
            job['technology'] = job.pop('tecnology')
        except KeyError:
            pass

    for job3 in jobs_json:
        del job3['type']
        del job3['companies']
        del job3['date']
    print(jobs_json)

    for job in jobs_json:
        count = 0
        for job2 in jobs_json:

            if job['technology'] == job2['technology']:
                print(job['technology'])
                print(job2['vacancies'])
                print(job2['technology'])
                print(job['vacancies'])
                job['vacancies'] += job2['vacancies']
                print(job['vacancies'])
                count = count + 1
                print("count" + str(count))
        #       jobs_json.remove(job2)

        if count == 0:
            count = 1

        job['vacancies'] = job['vacancies'] / count
        print("vagas" + str(job['vacancies']))
    count = 0

    for job5 in jobs_json:

        for job6 in jobs_json:

            if job5['technology'] == job6['technology'] and job5['_id'] != job6['_id']:
                print(job5['technology'] + " remove -> " + job6['technology'])
                jobs_json.remove(job6)


    for job7 in jobs_json:
        del job7['_id']
        for job8 in jobs_json:
            if job7['technology'] == job8['technology'] and job7['vacancies'] != job8['vacancies']:
                jobs_json.remove(job8)


    print(jobs_json)
    return jobs_json


def return_all_jobs():
    job_list = read_json_file()

    for job in job_list:
        del job['type']
        del job['companies']
        del job['_id']
        job['date'] = job['date'][:10]

    return job_list


print(get_jobs_by_type('backend'))
update_json_file()
