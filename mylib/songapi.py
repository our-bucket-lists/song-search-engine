import requests
import logging

COMPANY = '瑞影'
SERVER = 'https://song.corp.com.tw'
BASE_PATH = '/api/song.aspx'


def song_look_up(board: str = '', cus_type: str = '', keyword: str = '', 
                lang: str = '', len: str = '', min_id: str = '', oid: str = '', 
                sex: str = '', singer: str = '', song_date: str = 'null'):
    
    parameter = {
        'board': board,
        'cusType': cus_type,
        'keyword': keyword,
        'lang': lang,
        'Len': len,
        'minId': min_id,
        'oid': oid,
        'sex': sex,
        'singer': singer,
        'songDate': 'null' if song_date=='' else song_date,
    }

    url = f'{SERVER}{BASE_PATH}?company={COMPANY}'

    for key, value in parameter.items():
        url += f'&{key}={value}'

    logging.debug(f'Invoke the song lookup API {url}')
    response = requests.get(url)

    try:
        response.json()
    except ValueError as err:
        msg = 'Insufficient information, unable to search.'
        logging.error(msg)
        return requests.codes.bad

    return response.json()
