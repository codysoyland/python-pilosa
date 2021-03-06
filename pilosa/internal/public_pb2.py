# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='public.proto',
  package='internal',
  syntax='proto3',
  serialized_pb=_b('\n\x0cpublic.proto\x12\x08internal\"5\n\x06\x42itmap\x12\x0c\n\x04\x42its\x18\x01 \x03(\x04\x12\x1d\n\x05\x41ttrs\x18\x02 \x03(\x0b\x32\x0e.internal.Attr\"\"\n\x04Pair\x12\x0b\n\x03Key\x18\x01 \x01(\x04\x12\r\n\x05\x43ount\x18\x02 \x01(\x04\"9\n\x03\x42it\x12\r\n\x05RowID\x18\x01 \x01(\x04\x12\x10\n\x08\x43olumnID\x18\x02 \x01(\x04\x12\x11\n\tTimestamp\x18\x03 \x01(\x03\":\n\rColumnAttrSet\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x1d\n\x05\x41ttrs\x18\x02 \x03(\x0b\x32\x0e.internal.Attr\"o\n\x04\x41ttr\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\x0c\n\x04Type\x18\x02 \x01(\x04\x12\x13\n\x0bStringValue\x18\x03 \x01(\t\x12\x10\n\x08IntValue\x18\x04 \x01(\x03\x12\x11\n\tBoolValue\x18\x05 \x01(\x08\x12\x12\n\nFloatValue\x18\x06 \x01(\x01\"(\n\x07\x41ttrMap\x12\x1d\n\x05\x41ttrs\x18\x01 \x03(\x0b\x32\x0e.internal.Attr\"c\n\x0cQueryRequest\x12\r\n\x05Query\x18\x01 \x01(\t\x12\x0e\n\x06Slices\x18\x02 \x03(\x04\x12\x13\n\x0b\x43olumnAttrs\x18\x03 \x01(\x08\x12\x0f\n\x07Quantum\x18\x04 \x01(\t\x12\x0e\n\x06Remote\x18\x05 \x01(\x08\"u\n\rQueryResponse\x12\x0b\n\x03\x45rr\x18\x01 \x01(\t\x12&\n\x07Results\x18\x02 \x03(\x0b\x32\x15.internal.QueryResult\x12/\n\x0e\x43olumnAttrSets\x18\x03 \x03(\x0b\x32\x17.internal.ColumnAttrSet\"j\n\x0bQueryResult\x12 \n\x06\x42itmap\x18\x01 \x01(\x0b\x32\x10.internal.Bitmap\x12\t\n\x01N\x18\x02 \x01(\x04\x12\x1d\n\x05Pairs\x18\x03 \x03(\x0b\x32\x0e.internal.Pair\x12\x0f\n\x07\x43hanged\x18\x04 \x01(\x08\"s\n\rImportRequest\x12\r\n\x05Index\x18\x01 \x01(\t\x12\r\n\x05\x46rame\x18\x02 \x01(\t\x12\r\n\x05Slice\x18\x03 \x01(\x04\x12\x0e\n\x06RowIDs\x18\x04 \x03(\x04\x12\x11\n\tColumnIDs\x18\x05 \x03(\x04\x12\x12\n\nTimestamps\x18\x06 \x03(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BITMAP = _descriptor.Descriptor(
  name='Bitmap',
  full_name='internal.Bitmap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Bits', full_name='internal.Bitmap.Bits', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Attrs', full_name='internal.Bitmap.Attrs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=79,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='internal.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Key', full_name='internal.Pair.Key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Count', full_name='internal.Pair.Count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=115,
)


_BIT = _descriptor.Descriptor(
  name='Bit',
  full_name='internal.Bit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RowID', full_name='internal.Bit.RowID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ColumnID', full_name='internal.Bit.ColumnID', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='internal.Bit.Timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=174,
)


_COLUMNATTRSET = _descriptor.Descriptor(
  name='ColumnAttrSet',
  full_name='internal.ColumnAttrSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='internal.ColumnAttrSet.ID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Attrs', full_name='internal.ColumnAttrSet.Attrs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=234,
)


_ATTR = _descriptor.Descriptor(
  name='Attr',
  full_name='internal.Attr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Key', full_name='internal.Attr.Key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='internal.Attr.Type', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StringValue', full_name='internal.Attr.StringValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IntValue', full_name='internal.Attr.IntValue', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BoolValue', full_name='internal.Attr.BoolValue', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FloatValue', full_name='internal.Attr.FloatValue', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=347,
)


_ATTRMAP = _descriptor.Descriptor(
  name='AttrMap',
  full_name='internal.AttrMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Attrs', full_name='internal.AttrMap.Attrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=389,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='internal.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Query', full_name='internal.QueryRequest.Query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Slices', full_name='internal.QueryRequest.Slices', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ColumnAttrs', full_name='internal.QueryRequest.ColumnAttrs', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Quantum', full_name='internal.QueryRequest.Quantum', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Remote', full_name='internal.QueryRequest.Remote', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=490,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='internal.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Err', full_name='internal.QueryResponse.Err', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Results', full_name='internal.QueryResponse.Results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ColumnAttrSets', full_name='internal.QueryResponse.ColumnAttrSets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=609,
)


_QUERYRESULT = _descriptor.Descriptor(
  name='QueryResult',
  full_name='internal.QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Bitmap', full_name='internal.QueryResult.Bitmap', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='N', full_name='internal.QueryResult.N', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pairs', full_name='internal.QueryResult.Pairs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Changed', full_name='internal.QueryResult.Changed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=717,
)


_IMPORTREQUEST = _descriptor.Descriptor(
  name='ImportRequest',
  full_name='internal.ImportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Index', full_name='internal.ImportRequest.Index', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Frame', full_name='internal.ImportRequest.Frame', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Slice', full_name='internal.ImportRequest.Slice', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RowIDs', full_name='internal.ImportRequest.RowIDs', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ColumnIDs', full_name='internal.ImportRequest.ColumnIDs', index=4,
      number=5, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamps', full_name='internal.ImportRequest.Timestamps', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=719,
  serialized_end=834,
)

_BITMAP.fields_by_name['Attrs'].message_type = _ATTR
_COLUMNATTRSET.fields_by_name['Attrs'].message_type = _ATTR
_ATTRMAP.fields_by_name['Attrs'].message_type = _ATTR
_QUERYRESPONSE.fields_by_name['Results'].message_type = _QUERYRESULT
_QUERYRESPONSE.fields_by_name['ColumnAttrSets'].message_type = _COLUMNATTRSET
_QUERYRESULT.fields_by_name['Bitmap'].message_type = _BITMAP
_QUERYRESULT.fields_by_name['Pairs'].message_type = _PAIR
DESCRIPTOR.message_types_by_name['Bitmap'] = _BITMAP
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['Bit'] = _BIT
DESCRIPTOR.message_types_by_name['ColumnAttrSet'] = _COLUMNATTRSET
DESCRIPTOR.message_types_by_name['Attr'] = _ATTR
DESCRIPTOR.message_types_by_name['AttrMap'] = _ATTRMAP
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT
DESCRIPTOR.message_types_by_name['ImportRequest'] = _IMPORTREQUEST

Bitmap = _reflection.GeneratedProtocolMessageType('Bitmap', (_message.Message,), dict(
  DESCRIPTOR = _BITMAP,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.Bitmap)
  ))
_sym_db.RegisterMessage(Bitmap)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), dict(
  DESCRIPTOR = _PAIR,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.Pair)
  ))
_sym_db.RegisterMessage(Pair)

Bit = _reflection.GeneratedProtocolMessageType('Bit', (_message.Message,), dict(
  DESCRIPTOR = _BIT,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.Bit)
  ))
_sym_db.RegisterMessage(Bit)

ColumnAttrSet = _reflection.GeneratedProtocolMessageType('ColumnAttrSet', (_message.Message,), dict(
  DESCRIPTOR = _COLUMNATTRSET,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.ColumnAttrSet)
  ))
_sym_db.RegisterMessage(ColumnAttrSet)

Attr = _reflection.GeneratedProtocolMessageType('Attr', (_message.Message,), dict(
  DESCRIPTOR = _ATTR,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.Attr)
  ))
_sym_db.RegisterMessage(Attr)

AttrMap = _reflection.GeneratedProtocolMessageType('AttrMap', (_message.Message,), dict(
  DESCRIPTOR = _ATTRMAP,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.AttrMap)
  ))
_sym_db.RegisterMessage(AttrMap)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQUEST,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.QueryRequest)
  ))
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESULT,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.QueryResult)
  ))
_sym_db.RegisterMessage(QueryResult)

ImportRequest = _reflection.GeneratedProtocolMessageType('ImportRequest', (_message.Message,), dict(
  DESCRIPTOR = _IMPORTREQUEST,
  __module__ = 'public_pb2'
  # @@protoc_insertion_point(class_scope:internal.ImportRequest)
  ))
_sym_db.RegisterMessage(ImportRequest)


# @@protoc_insertion_point(module_scope)
