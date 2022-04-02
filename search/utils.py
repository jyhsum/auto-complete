from .models import FrequencyTable


def get_auto_complete_suggestions(keyword):
    pipeline = [
        {
            '$search': {
                'index': 'default',
                'autocomplete': {
                    'query': keyword,
                    'path': 'query',
                    'tokenOrder': 'sequential',
                    'fuzzy': {
                        'maxEdits': 2,
                        'prefixLength': 3,
                        'maxExpansions': 3
                    }
                }
            }
        },
        {
            '$match': {
                '$expr' : {'$gte': [{'$strLenCP': "$query"}, len(keyword)]}
            }
        },
        {
            '$sort': {
                'score': -1,
                'frequency': -1
            }
        },
        {
            '$project': {
                "_id": 0,
                "frequency": 1,
                "query": 1,
                "score": { "$meta": "searchScore" },
            }
        },
        { "$limit": 10 }
    ]
    result = FrequencyTable.objects().aggregate(pipeline)
    return list(result)