SAMPLE_JSON = [
    {
        "_id": 1,
        "date": datetime.datetime(2022, 11, 4, 10, 50, 8, 474000),
        "vacancies": 283,
        "companies": 205,
        "type": "backend",
        "technology": "Random Technology #01"
    },
    {
        "_id": 2,
        "date": 2,
        "vacancies": 87,
        "companies": 59,
        "type": "mobile",
        "technology": "Random Technology #02"
    },
    {
        "_id": 3,
        "date": 3,
        "vacancies": 34,
        "companies": 18,
        "type": "mobile",
        "technology": "Random Technology #03"
    }
]

SAMPLE_JSON_BY_TYPE = [
    {
        "_id": 2,
        "date": 2,
        "vacancies": 87,
        "companies": 59,
        "type": "mobile",
        "technology": "Random Technology #02"
    },
    {
        "_id": 3,
        "date": 3,
        "vacancies": 34,
        "companies": 18,
        "type": "mobile",
        "technology": "Random Technology #03"
    }
]

EXPECTED_JSON = [
    {
        "name": "Random Technology #01",
        "vagas": [
            {
                "x": 283,
                "y": "01"
            }
        ]
    },
    {
        "name": "Random Technology #02",
        "vagas": [
            {
                "x": 87,
                "y": "02"
            }
        ]
    },
    {
        "name": "Random Technology #03",
        "vagas": [
            {
                "x": 34,
                "y": "03"
            }
        ]
    }
]

EXPECTED_JSON_BY_TYPE = [
    {
        "name": "Random Technology #02",
        "vagas": [
            {
                "x": 87,
                "y": "02"
            }
        ]
    },
    {
        "name": "Random Technology #03",
        "vagas": [
            {
                "x": 34,
                "y": "03"
            }
        ]
    }
]
