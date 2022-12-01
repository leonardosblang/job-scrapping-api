import json
from unittest import TestCase
from src.data_manip import DataManip
from src.connector import Connector
from tests.constants import *


class TestDataManipulation(TestCase):
    maxDiff: int | None = None

    def setUp(self):
        self.connector_mock = Connector()
        self.connector_mock.get_jobs_json = lambda: SAMPLE_JOBS
        self.connector_mock.get_jobs_json_by_type = lambda job_type: SAMPLE_JOBS_BY_TYPE
        self.data_manip = DataManip(self.connector_mock)

    def test_get_all_jobs(self):
        job_list = self.data_manip.get_all_jobs()
        self.assertEqual(job_list, EXPECTED_JOBS)

    def test_get_jobs_by_type(self):
        jobs_json = self.data_manip.get_jobs_by_type("backend")
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
