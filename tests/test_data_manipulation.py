import json
from unittest import TestCase
from database.data_manipulation import DataManipulation as DataManip
from database.db_connection import DatabaseConnection as DBConnection
from tests.jobs_json import *


class TestDataManipulation(TestCase):
    maxDiff: int | None = None

    def setUp(self):
        self.db_mock = DBConnection()
        self.db_mock.get_jobs_json = lambda: SAMPLE_JOBS
        self.db_mock.get_jobs_json_by_type = lambda job_type: SAMPLE_JOBS_BY_TYPE
        self.data_manip = DataManip(self.db_mock)

    def test_get_all_jobs(self):
        job_list = self.data_manip.get_all_jobs()
        self.assertEqual(job_list, EXPECTED_JOBS)

    def test_get_jobs_by_type(self):
        jobs_json = self.data_manip.get_jobs_by_type("mobile")
        self.assertEqual(jobs_json, EXPECTED_JOBS_BY_TYPE)

    def test_read_json_file(self):
        self.data_manip.read_json_file()
        with open('docs/jobs.json') as file:
            file_data = json.load(file)
        self.assertEqual(file_data, SAMPLE_JOBS)

    def test_update_json_file(self):
        self.data_manip.update_json_file()
        with open('docs/jobs.json') as file:
            file_data = json.load(file)
        self.assertEqual(file_data, SAMPLE_JOBS)
