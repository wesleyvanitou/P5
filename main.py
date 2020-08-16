import requests as rq


def counter():
    # Count the pro
    counter = int(
        rq.get(
            url=url,
            params={
                'action': 'process',
                'json': True}
        ).json()['count'])
