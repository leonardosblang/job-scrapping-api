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
    },
    {
        "_id": "6364ee6ece535cccc45406e7",
        "date": "2022:11:04:10:50:57.850000",
        "vacancies": 384,
        "companies": 236,
        "type": "backend",
        "technology": "Python"
    }
]

SAMPLE_JOBS_BY_TYPE = [
    {
        "_id": "6364ee6ece535cccc45406e9",
        "date": "2022:11:04:10:50:22.177000",
        "vacancies": 442,
        "companies": 292,
        "type": "web",
        "technology": "React"
    },
    {
        "_id": "6364ee6ece535cccc45406e7",
        "date": "2022:11:04:10:50:57.850000",
        "vacancies": 384,
        "companies": 236,
        "type": "backend",
        "technology": "Python"
    }
]


EXPECTED_JOBS = [
    {
        "name": "Node",
        "vagas": [
            {
                "x": 4,
                "y": 283
            }
        ]
    },
    {
        "name": "Python",
        "vagas": [
            {
                "x": 4,
                "y": 384
            }
        ]
    },
    {
        "name": "React",
        "vagas": [
            {
                "x": 4,
                "y": 442
            }
        ]
    },
    {
        "name": "React Native",
        "vagas": [
            {
                "x": 4,
                "y": 124
            }
        ]
    }
]

EXPECTED_JOBS_BY_TYPE = [
    {
        "x": "Node",
        "y": 283
    },
    {
        "x": "Python",
        "y": 384
    }
]
