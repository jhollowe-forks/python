# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deviceonly.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2
from . import mesh_pb2 as mesh__pb2
from . import radioconfig_pb2 as radioconfig__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x65viceonly.proto\x1a\rchannel.proto\x1a\nmesh.proto\x1a\x11radioconfig.proto\"\x80\x01\n\x11LegacyRadioConfig\x12\x39\n\x0bpreferences\x18\x01 \x01(\x0b\x32$.LegacyRadioConfig.LegacyPreferences\x1a\x30\n\x11LegacyPreferences\x12\x1b\n\x06region\x18\x0f \x01(\x0e\x32\x0b.RegionCode\"\x8f\x02\n\x0b\x44\x65viceState\x12\'\n\x0blegacyRadio\x18\x01 \x01(\x0b\x32\x12.LegacyRadioConfig\x12\x1c\n\x07my_node\x18\x02 \x01(\x0b\x32\x0b.MyNodeInfo\x12\x14\n\x05owner\x18\x03 \x01(\x0b\x32\x05.User\x12\x1a\n\x07node_db\x18\x04 \x03(\x0b\x32\t.NodeInfo\x12\"\n\rreceive_queue\x18\x05 \x03(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07version\x18\x08 \x01(\r\x12$\n\x0frx_text_message\x18\x07 \x01(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07no_save\x18\t \x01(\x08\x12\x15\n\rdid_gps_reset\x18\x0b \x01(\x08J\x04\x08\x0c\x10\r\")\n\x0b\x43hannelFile\x12\x1a\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x08.ChannelBF\n\x13\x63om.geeksville.meshB\nDeviceOnlyH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3')



_LEGACYRADIOCONFIG = DESCRIPTOR.message_types_by_name['LegacyRadioConfig']
_LEGACYRADIOCONFIG_LEGACYPREFERENCES = _LEGACYRADIOCONFIG.nested_types_by_name['LegacyPreferences']
_DEVICESTATE = DESCRIPTOR.message_types_by_name['DeviceState']
_CHANNELFILE = DESCRIPTOR.message_types_by_name['ChannelFile']
LegacyRadioConfig = _reflection.GeneratedProtocolMessageType('LegacyRadioConfig', (_message.Message,), {

  'LegacyPreferences' : _reflection.GeneratedProtocolMessageType('LegacyPreferences', (_message.Message,), {
    'DESCRIPTOR' : _LEGACYRADIOCONFIG_LEGACYPREFERENCES,
    '__module__' : 'deviceonly_pb2'
    # @@protoc_insertion_point(class_scope:LegacyRadioConfig.LegacyPreferences)
    })
  ,
  'DESCRIPTOR' : _LEGACYRADIOCONFIG,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:LegacyRadioConfig)
  })
_sym_db.RegisterMessage(LegacyRadioConfig)
_sym_db.RegisterMessage(LegacyRadioConfig.LegacyPreferences)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

ChannelFile = _reflection.GeneratedProtocolMessageType('ChannelFile', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELFILE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:ChannelFile)
  })
_sym_db.RegisterMessage(ChannelFile)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nDeviceOnlyH\003Z!github.com/meshtastic/gomeshproto'
  _LEGACYRADIOCONFIG._serialized_start=67
  _LEGACYRADIOCONFIG._serialized_end=195
  _LEGACYRADIOCONFIG_LEGACYPREFERENCES._serialized_start=147
  _LEGACYRADIOCONFIG_LEGACYPREFERENCES._serialized_end=195
  _DEVICESTATE._serialized_start=198
  _DEVICESTATE._serialized_end=469
  _CHANNELFILE._serialized_start=471
  _CHANNELFILE._serialized_end=512
# @@protoc_insertion_point(module_scope)
