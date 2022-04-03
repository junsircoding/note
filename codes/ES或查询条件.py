"""
{
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "shape": "round"
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "term": {"color": "red"}
                            },
                            {
                                "term": {"color": "blue"}
                            }
                        ]
                    }
                }
            ]
        }
    }
}
"""