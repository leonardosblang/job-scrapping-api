import json
import pandas as pd
import pymongo
from src.connector import Connector


class DataManip:
    def __init__(self, connector: Connector):
        self.__connector = connector

    def update_json_file(self) -> None:
        jobs_json = self.__connector.get_jobs_json()
        with open('docs/jobs.json', 'w') as outfile:
            json.dump(jobs_json, outfile, default=str)

    def read_json_file(self):
        self.update_json_file()
        with open('docs/jobs.json') as file:
            file_data = json.load(file)
        for job in file_data:
            try:
                job['technology'] = job.pop('tecnology')
            except KeyError:
                pass
            try:
                job['name'] = job.pop('technology')
            except KeyError:
                pass
        return file_data

    def get_jobs_by_type(self, job_type: str):
        job_list = self.read_json_file()
        df = pd.DataFrame(job_list)
        df = df[df['type'] == job_type]
        df = df.drop(['type', 'companies', '_id', 'date'], axis=1)
        df = df.rename(columns={'vacancies': 'y', 'name': 'x'})
        df = df.groupby('x').apply(
            lambda x: x['y'].sum() / x['y'].count()).reset_index(name='y')
        df = df.to_json(orient='records')
        df = json.loads(df)
        return df

    def get_all_jobs(self):
        job_list = self.read_json_file()
        df = pd.DataFrame(job_list)
        df = df.drop(['type', 'companies', '_id'], axis=1)
        df['date'] = df['date'].str[8:10]
        df = df.rename(columns={'vacancies': 'y', 'date': 'x'})
        df['x'] = df['x'].astype(int)
        df = df.drop_duplicates(subset=['x', 'name'], keep='first')
        df = df.groupby('name').apply(lambda x: x[['x', 'y']].to_dict(
            orient='records')).reset_index(name='vagas')
        df = df.to_json(orient='records')
        df = json.loads(df)
        return df
