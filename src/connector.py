import pymongo

CONNECTION_STRING = "mongodb+srv://root:root@cluster0.bqedr.mongodb.net/?retryWrites=true&w=majority"


class Connector:
    def __init__(self):
        pass

    def __connect_to_bd(self):
        client = pymongo.MongoClient(CONNECTION_STRING)
        database = client.web
        return database

    def get_jobs_json(self):
        database = self.__connect_to_bd()
        jobs = database.vagas
        jobs_json = jobs.find()
        jobs_json = list(jobs_json)
        return jobs_json

    def get_jobs_json_by_type(self, job_type: str):
        database = self.connect_to_bd()
        jobs = database.vagas
        jobs_json = jobs.find({"type": job_type})
        jobs_json = list(jobs_json)
        return jobs_json
