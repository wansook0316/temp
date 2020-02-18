# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/grid_rbbox_anchor_generator.proto

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
  name='protos/grid_rbbox_anchor_generator.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n(protos/grid_rbbox_anchor_generator.proto\x12\x17object_detection.protos\"\xe2\x01\n\x18GridRbboxAnchorGenerator\x12\x13\n\x06height\x18\x01 \x01(\x05:\x03\x32\x35\x36\x12\x12\n\x05width\x18\x02 \x01(\x05:\x03\x32\x35\x36\x12\x19\n\rheight_stride\x18\x03 \x01(\x05:\x02\x31\x36\x12\x18\n\x0cwidth_stride\x18\x04 \x01(\x05:\x02\x31\x36\x12\x18\n\rheight_offset\x18\x05 \x01(\x05:\x01\x30\x12\x17\n\x0cwidth_offset\x18\x06 \x01(\x05:\x01\x30\x12\x0e\n\x06scales\x18\x07 \x03(\x02\x12\x15\n\raspect_ratios\x18\x08 \x03(\x02\x12\x0e\n\x06\x61ngles\x18\t \x03(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GRIDRBBOXANCHORGENERATOR = _descriptor.Descriptor(
  name='GridRbboxAnchorGenerator',
  full_name='object_detection.protos.GridRbboxAnchorGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='object_detection.protos.GridRbboxAnchorGenerator.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='object_detection.protos.GridRbboxAnchorGenerator.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_stride', full_name='object_detection.protos.GridRbboxAnchorGenerator.height_stride', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width_stride', full_name='object_detection.protos.GridRbboxAnchorGenerator.width_stride', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_offset', full_name='object_detection.protos.GridRbboxAnchorGenerator.height_offset', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width_offset', full_name='object_detection.protos.GridRbboxAnchorGenerator.width_offset', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scales', full_name='object_detection.protos.GridRbboxAnchorGenerator.scales', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aspect_ratios', full_name='object_detection.protos.GridRbboxAnchorGenerator.aspect_ratios', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angles', full_name='object_detection.protos.GridRbboxAnchorGenerator.angles', index=8,
      number=9, type=2, cpp_type=6, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=296,
)

DESCRIPTOR.message_types_by_name['GridRbboxAnchorGenerator'] = _GRIDRBBOXANCHORGENERATOR

GridRbboxAnchorGenerator = _reflection.GeneratedProtocolMessageType('GridRbboxAnchorGenerator', (_message.Message,), dict(
  DESCRIPTOR = _GRIDRBBOXANCHORGENERATOR,
  __module__ = 'protos.grid_rbbox_anchor_generator_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.GridRbboxAnchorGenerator)
  ))
_sym_db.RegisterMessage(GridRbboxAnchorGenerator)


# @@protoc_insertion_point(module_scope)
