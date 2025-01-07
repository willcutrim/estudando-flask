from marshmallow import Schema, fields


class UserSchemaUser(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    created_at = fields.DateTime()
    is_active = fields.Bool()
    address = fields.Nested('AddressSchema', many=True)


class AddressSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    address = fields.Str()
    city = fields.Str()
    state = fields.Str()
    country = fields.Str()
