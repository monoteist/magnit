from house import api
from flask_restful import Resource, reqparse


class HouseAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('latitude', type=float, required=True,
                                   help='No latitude provided', location='json')
        self.reqparse.add_argument('longitude', type=float, required=True,
                                   help='No longitude provided', location='json')
        self.reqparse.add_argument('family_count', type=int, required=True,
                                   help='No family_count provided', location='json')
        super(HouseAPI, self).__init__()

    def post(self, house_id):
        args = self.reqparse.parse_args()
        return {house_id: args}


api.add_resource(HouseAPI, '/api/v1/houses/<int:house_id>',
                 endpoint='house')
