from flask import Flask
from flask_restx import Resource, Api, reqparse
from werkzeug.exceptions import BadRequest
from mylib.songapi import song_look_up
from mylib.logger import init_root_logger

init_root_logger()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('board', default='', type=str, help='')
parser.add_argument('cus_type', default='', type=str, help='')
parser.add_argument('keyword', default='', type=str, help='')
parser.add_argument('lang', default='', type=str, help='')
parser.add_argument('len', default='', type=str, help='')
parser.add_argument('min_id', default='', type=str, help='')
parser.add_argument('oid', default='', type=str, help='')
parser.add_argument('sex', default='', type=str, help='')
parser.add_argument('singer', default='', type=str, help='')
parser.add_argument('song_date', default='', type=str, help='')


@api.route('/api/v1/songs')
class Songs(Resource):
    @api.expect(parser)
    def get(self):
        args=parser.parse_args()
        if args['keyword']=='' and not(args['lang'] != '' and args['len'] !=''):
            raise BadRequest("Both of 'lang' and 'len' should have values when 'keyword' is not given.")

        result = song_look_up(
            board = args['board'],
            cus_type = args['cus_type'],
            keyword = args['keyword'], 
            lang = args['lang'], 
            len = args['len'], 
            min_id = args['min_id'], 
            oid = args['oid'], 
            sex = args['sex'], 
            singer = args['singer'], 
            song_date = args['song_date'])
        
        if result == 400:
            raise BadRequest
        
        return result


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
