from marshmallow import Schema, fields


class Location(Schema):
    town = fields.String()
    latitude = fields.Float()
    longitude = fields.Float()
    iso_3166_1 = fields.String()
    country = fields.String()
