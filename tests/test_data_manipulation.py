import json
from unittest import TestCase
from database.data_manipulation import DataManipulation as DataManip
from database.database_connection import DatabaseConnection as DBConnection
from tests.sample_json import *


class TestDataManipulation(TestCase):
    def setUp(self):
        self.db_connection_mock = DBConnection()
        self.db_connection_mock.get_jobs_json = lambda: SAMPLE_JSON
        self.db_connection_mock.get_jobs_json_by_type = lambda job_type: SAMPLE_JSON_BY_TYPE
        self.data_manip = DataManip(self.db_connection_mock)

    def test_get_jobs_by_type(self):
        jobs_json = self.data_manip.get_jobs_by_type("mobile")
        self.assertEqual(jobs_json, EXPECTED_JSON_BY_TYPE)

    def test_update_json_file(self):
        self.data_manip.update_json_file()
        with open('jobs2.json') as file:
            file_data = json.load(file)
        self.assertEqual(file_data, SAMPLE_JSON)

    def test_read_json_file(self):
        self.data_manip.read_json_file()
        with open('jobs2.json') as file:
            file_data = json.load(file)
        self.assertEqual(file_data, SAMPLE_JSON)
    
    def test_return_all_jobs(self):
        job_list = self.data_manip.return_all_jobs()
        self.assertEqual(job_list, EXPECTED_JSON)