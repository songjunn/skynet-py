import google.protobuf.json_format as json_format

def dict2pb(adict, cls):
    obj = cls()
    json_format.ParseDict(adict, obj, ignore_unknown_fields=True)
    return obj

def pb2dict(pb):
    obj = json_format.MessageToDict(pb, including_default_value_fields=True, preserving_proto_field_name=True)
    return obj

def json2pb(json, cls):
    obj = cls()
    json_format.Parse(json, obj, ignore_unknown_fields=True)
    return obj

def pb2json(pb):
    obj = json_format.MessageToJson(pb, including_default_value_fields=True, preserving_proto_field_name=True, indent=None)
    return obj
