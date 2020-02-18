# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import faster_rcnn_pb2 as protos_dot_faster__rcnn__pb2
from protos import ssd_pb2 as protos_dot_ssd__pb2
from protos import rssd_pb2 as protos_dot_rssd__pb2
from protos import rfaster_rcnn_pb2 as protos_dot_rfaster__rcnn__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x12protos/model.proto\x12\x17object_detection.protos\x1a\x18protos/faster_rcnn.proto\x1a\x10protos/ssd.proto\x1a\x11protos/rssd.proto\x1a\x19protos/rfaster_rcnn.proto\"\xef\x01\n\x0e\x44\x65tectionModel\x12:\n\x0b\x66\x61ster_rcnn\x18\x01 \x01(\x0b\x32#.object_detection.protos.FasterRcnnH\x00\x12+\n\x03ssd\x18\x02 \x01(\x0b\x32\x1c.object_detection.protos.SsdH\x00\x12-\n\x04rssd\x18\x03 \x01(\x0b\x32\x1d.object_detection.protos.RssdH\x00\x12<\n\x0crfaster_rcnn\x18\x04 \x01(\x0b\x32$.object_detection.protos.RfasterRcnnH\x00\x42\x07\n\x05model')
  ,
  dependencies=[protos_dot_faster__rcnn__pb2.DESCRIPTOR,protos_dot_ssd__pb2.DESCRIPTOR,protos_dot_rssd__pb2.DESCRIPTOR,protos_dot_rfaster__rcnn__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DETECTIONMODEL = _descriptor.Descriptor(
  name='DetectionModel',
  full_name='object_detection.protos.DetectionModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faster_rcnn', full_name='object_detection.protos.DetectionModel.faster_rcnn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssd', full_name='object_detection.protos.DetectionModel.ssd', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rssd', full_name='object_detection.protos.DetectionModel.rssd', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rfaster_rcnn', full_name='object_detection.protos.DetectionModel.rfaster_rcnn', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='model', full_name='object_detection.protos.DetectionModel.model',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=138,
  serialized_end=377,
)

_DETECTIONMODEL.fields_by_name['faster_rcnn'].message_type = protos_dot_faster__rcnn__pb2._FASTERRCNN
_DETECTIONMODEL.fields_by_name['ssd'].message_type = protos_dot_ssd__pb2._SSD
_DETECTIONMODEL.fields_by_name['rssd'].message_type = protos_dot_rssd__pb2._RSSD
_DETECTIONMODEL.fields_by_name['rfaster_rcnn'].message_type = protos_dot_rfaster__rcnn__pb2._RFASTERRCNN
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['faster_rcnn'])
_DETECTIONMODEL.fields_by_name['faster_rcnn'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['ssd'])
_DETECTIONMODEL.fields_by_name['ssd'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['rssd'])
_DETECTIONMODEL.fields_by_name['rssd'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
_DETECTIONMODEL.oneofs_by_name['model'].fields.append(
  _DETECTIONMODEL.fields_by_name['rfaster_rcnn'])
_DETECTIONMODEL.fields_by_name['rfaster_rcnn'].containing_oneof = _DETECTIONMODEL.oneofs_by_name['model']
DESCRIPTOR.message_types_by_name['DetectionModel'] = _DETECTIONMODEL

DetectionModel = _reflection.GeneratedProtocolMessageType('DetectionModel', (_message.Message,), dict(
  DESCRIPTOR = _DETECTIONMODEL,
  __module__ = 'protos.model_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.DetectionModel)
  ))
_sym_db.RegisterMessage(DetectionModel)


# @@protoc_insertion_point(module_scope)
