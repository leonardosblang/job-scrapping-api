import datetime
from bson.objectid import ObjectId

SAMPLE_JOBS = [
    {
        "_id": "6364ee60ce535cccc45406e8",
        "date": "2022:11:04:10:50:08.474000",
        "vacancies": 124,
        "companies": 64,
        "type": "mobile",
        "technology": "React Native"
    },
    {
        "_id": "6364ee6ece535cccc45406e9",
        "date": "2022:11:04:10:50:22.177000",
        "vacancies": 442,
        "companies": 292,
        "type": "web",
        "technology": "React"
    },
    {
        "_id": "6364ee7bce535cccc45406ea",
        "date": "2022:11:04:10:50:35.746000",
        "vacancies": 283,
        "companies": 205,
        "type": "backend",
        "technology": "Node"
    }
]

SAMPLE_JOBS_BY_TYPE = [
    {
        "_id": "6364ee60ce535cccc45406e8",
        "date": "2022:11:04:10:50:08.474000",
        "vacancies": 124,
        "companies": 64,
        "type": "mobile",
        "technology": "React Native"
    }
]


EXPECTED_JOBS = [
    {
        "name": "React Native",
        "vagas": [
            {
                "x": 124,
                "y": "04"
            }
        ]
    },
    {
        "name": "React",
        "vagas": [
            {
                "x": 442,
                "y": "04"
            }
        ]
    },
    {
        "name": "Node",
        "vagas": [
            {
                "x": 283,
                "y": "04"
            }
        ]
    }
]

EXPECTED_JOBS_BY_TYPE = [
    {
        "name": "React Native",
        "vagas": [
            {
                "x": 124,
                "y": "04"
            }
        ]
    }
]
