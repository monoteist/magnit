from house import api
from flask_restful import Resource, reqparse
from house.models import House, db


class HouseAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('latitude', type=float, required=True,
                                   help='Отсутвует значение поля latitude',
                                   location='json')
        self.reqparse.add_argument('longitude', type=float, required=True,
                                   help='Отсутвует значение поля provided',
                                   location='json')
        self.reqparse.add_argument('family_count', type=int, required=True,
                                   help='Отсутвует значение поля provided',
                                   location='json')

    def post(self, house_id):
        args = self.reqparse.parse_args()
        house = House.query.get(house_id)
        if house:
            house.latitude = args.latitude
            house.longitude = args.longitude
            house.family_count = args.family_count
            db.session.commit()
            return {'message': 'Данные дома обновлены!'}
        else:
            house = House(**args)
            db.session.add(house)
            db.session.commit()
            return {'message': 'Новый дом добавлен с переданными данными!'}


api.add_resource(HouseAPI, '/api/v1/houses/<int:house_id>',
                 endpoint='house')
