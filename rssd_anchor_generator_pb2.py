# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/rssd_anchor_generator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/rssd_anchor_generator.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n\"protos/rssd_anchor_generator.proto\x12\x17object_detection.protos\"\xde\x01\n\x13RssdAnchorGenerator\x12\x15\n\nnum_layers\x18\x01 \x01(\x05:\x01\x36\x12\x16\n\tmin_scale\x18\x02 \x01(\x02:\x03\x30.2\x12\x17\n\tmax_scale\x18\x03 \x01(\x02:\x04\x30.95\x12\x15\n\raspect_ratios\x18\x04 \x03(\x02\x12*\n\x1creduce_boxes_in_lowest_layer\x18\x05 \x01(\x08:\x04true\x12\x0e\n\x06\x61ngles\x18\x06 \x03(\x02\x12,\n!num_aspect_ration_of_middle_scale\x18\x07 \x01(\x05:\x01\x31')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RSSDANCHORGENERATOR = _descriptor.Descriptor(
  name='RssdAnchorGenerator',
  full_name='object_detection.protos.RssdAnchorGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_layers', full_name='object_detection.protos.RssdAnchorGenerator.num_layers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_scale', full_name='object_detection.protos.RssdAnchorGenerator.min_scale', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_scale', full_name='object_detection.protos.RssdAnchorGenerator.max_scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.95),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aspect_ratios', full_name='object_detection.protos.RssdAnchorGenerator.aspect_ratios', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reduce_boxes_in_lowest_layer', full_name='object_detection.protos.RssdAnchorGenerator.reduce_boxes_in_lowest_layer', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angles', full_name='object_detection.protos.RssdAnchorGenerator.angles', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_aspect_ration_of_middle_scale', full_name='object_detection.protos.RssdAnchorGenerator.num_aspect_ration_of_middle_scale', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
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
  ],
  serialized_start=64,
  serialized_end=286,
)

DESCRIPTOR.message_types_by_name['RssdAnchorGenerator'] = _RSSDANCHORGENERATOR

RssdAnchorGenerator = _reflection.GeneratedProtocolMessageType('RssdAnchorGenerator', (_message.Message,), dict(
  DESCRIPTOR = _RSSDANCHORGENERATOR,
  __module__ = 'protos.rssd_anchor_generator_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RssdAnchorGenerator)
  ))
_sym_db.RegisterMessage(RssdAnchorGenerator)


# @@protoc_insertion_point(module_scope)
