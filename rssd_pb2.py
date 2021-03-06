# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/rssd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import anchor_generator_pb2 as protos_dot_anchor__generator__pb2
from protos import box_coder_pb2 as protos_dot_box__coder__pb2
from protos import box_predictor_pb2 as protos_dot_box__predictor__pb2
from protos import hyperparams_pb2 as protos_dot_hyperparams__pb2
from protos import image_resizer_pb2 as protos_dot_image__resizer__pb2
from protos import matcher_pb2 as protos_dot_matcher__pb2
from protos import losses_pb2 as protos_dot_losses__pb2
from protos import post_processing_pb2 as protos_dot_post__processing__pb2
from protos import region_similarity_calculator_pb2 as protos_dot_region__similarity__calculator__pb2
from protos import ssd_pb2 as protos_dot_ssd__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/rssd.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x11protos/rssd.proto\x12\x17object_detection.protos\x1a\x1dprotos/anchor_generator.proto\x1a\x16protos/box_coder.proto\x1a\x1aprotos/box_predictor.proto\x1a\x18protos/hyperparams.proto\x1a\x1aprotos/image_resizer.proto\x1a\x14protos/matcher.proto\x1a\x13protos/losses.proto\x1a\x1cprotos/post_processing.proto\x1a)protos/region_similarity_calculator.proto\x1a\x10protos/ssd.proto\"\xfd\x04\n\x04Rssd\x12\x13\n\x0bnum_classes\x18\x01 \x01(\x05\x12<\n\rimage_resizer\x18\x02 \x01(\x0b\x32%.object_detection.protos.ImageResizer\x12G\n\x11\x66\x65\x61ture_extractor\x18\x03 \x01(\x0b\x32,.object_detection.protos.SsdFeatureExtractor\x12\x34\n\tbox_coder\x18\x04 \x01(\x0b\x32!.object_detection.protos.BoxCoder\x12\x31\n\x07matcher\x18\x05 \x01(\x0b\x32 .object_detection.protos.Matcher\x12R\n\x15similarity_calculator\x18\x06 \x01(\x0b\x32\x33.object_detection.protos.RegionSimilarityCalculator\x12<\n\rbox_predictor\x18\x07 \x01(\x0b\x32%.object_detection.protos.BoxPredictor\x12\x42\n\x10\x61nchor_generator\x18\x08 \x01(\x0b\x32(.object_detection.protos.AnchorGenerator\x12@\n\x0fpost_processing\x18\t \x01(\x0b\x32\'.object_detection.protos.PostProcessing\x12+\n\x1dnormalize_loss_by_num_matches\x18\n \x01(\x08:\x04true\x12+\n\x04loss\x18\x0b \x01(\x0b\x32\x1d.object_detection.protos.Loss\"\x98\x01\n\x14RssdFeatureExtractor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1b\n\x10\x64\x65pth_multiplier\x18\x02 \x01(\x02:\x01\x31\x12\x15\n\tmin_depth\x18\x03 \x01(\x05:\x02\x31\x36\x12>\n\x10\x63onv_hyperparams\x18\x04 \x01(\x0b\x32$.object_detection.protos.Hyperparams')
  ,
  dependencies=[protos_dot_anchor__generator__pb2.DESCRIPTOR,protos_dot_box__coder__pb2.DESCRIPTOR,protos_dot_box__predictor__pb2.DESCRIPTOR,protos_dot_hyperparams__pb2.DESCRIPTOR,protos_dot_image__resizer__pb2.DESCRIPTOR,protos_dot_matcher__pb2.DESCRIPTOR,protos_dot_losses__pb2.DESCRIPTOR,protos_dot_post__processing__pb2.DESCRIPTOR,protos_dot_region__similarity__calculator__pb2.DESCRIPTOR,protos_dot_ssd__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RSSD = _descriptor.Descriptor(
  name='Rssd',
  full_name='object_detection.protos.Rssd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='object_detection.protos.Rssd.num_classes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_resizer', full_name='object_detection.protos.Rssd.image_resizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_extractor', full_name='object_detection.protos.Rssd.feature_extractor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_coder', full_name='object_detection.protos.Rssd.box_coder', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matcher', full_name='object_detection.protos.Rssd.matcher', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='similarity_calculator', full_name='object_detection.protos.Rssd.similarity_calculator', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_predictor', full_name='object_detection.protos.Rssd.box_predictor', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchor_generator', full_name='object_detection.protos.Rssd.anchor_generator', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_processing', full_name='object_detection.protos.Rssd.post_processing', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalize_loss_by_num_matches', full_name='object_detection.protos.Rssd.normalize_loss_by_num_matches', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss', full_name='object_detection.protos.Rssd.loss', index=10,
      number=11, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=318,
  serialized_end=955,
)


_RSSDFEATUREEXTRACTOR = _descriptor.Descriptor(
  name='RssdFeatureExtractor',
  full_name='object_detection.protos.RssdFeatureExtractor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='object_detection.protos.RssdFeatureExtractor.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth_multiplier', full_name='object_detection.protos.RssdFeatureExtractor.depth_multiplier', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_depth', full_name='object_detection.protos.RssdFeatureExtractor.min_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='object_detection.protos.RssdFeatureExtractor.conv_hyperparams', index=3,
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
  ],
  serialized_start=958,
  serialized_end=1110,
)

_RSSD.fields_by_name['image_resizer'].message_type = protos_dot_image__resizer__pb2._IMAGERESIZER
_RSSD.fields_by_name['feature_extractor'].message_type = protos_dot_ssd__pb2._SSDFEATUREEXTRACTOR
_RSSD.fields_by_name['box_coder'].message_type = protos_dot_box__coder__pb2._BOXCODER
_RSSD.fields_by_name['matcher'].message_type = protos_dot_matcher__pb2._MATCHER
_RSSD.fields_by_name['similarity_calculator'].message_type = protos_dot_region__similarity__calculator__pb2._REGIONSIMILARITYCALCULATOR
_RSSD.fields_by_name['box_predictor'].message_type = protos_dot_box__predictor__pb2._BOXPREDICTOR
_RSSD.fields_by_name['anchor_generator'].message_type = protos_dot_anchor__generator__pb2._ANCHORGENERATOR
_RSSD.fields_by_name['post_processing'].message_type = protos_dot_post__processing__pb2._POSTPROCESSING
_RSSD.fields_by_name['loss'].message_type = protos_dot_losses__pb2._LOSS
_RSSDFEATUREEXTRACTOR.fields_by_name['conv_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['Rssd'] = _RSSD
DESCRIPTOR.message_types_by_name['RssdFeatureExtractor'] = _RSSDFEATUREEXTRACTOR

Rssd = _reflection.GeneratedProtocolMessageType('Rssd', (_message.Message,), dict(
  DESCRIPTOR = _RSSD,
  __module__ = 'protos.rssd_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Rssd)
  ))
_sym_db.RegisterMessage(Rssd)

RssdFeatureExtractor = _reflection.GeneratedProtocolMessageType('RssdFeatureExtractor', (_message.Message,), dict(
  DESCRIPTOR = _RSSDFEATUREEXTRACTOR,
  __module__ = 'protos.rssd_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RssdFeatureExtractor)
  ))
_sym_db.RegisterMessage(RssdFeatureExtractor)


# @@protoc_insertion_point(module_scope)
