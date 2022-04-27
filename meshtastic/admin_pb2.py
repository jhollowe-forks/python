# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64min.proto\x1a\rchannel.proto\x1a\nmesh.proto\x1a\x11radioconfig.proto\"\xa1\x08\n\x0c\x41\x64minMessage\x12!\n\tset_radio\x18\x01 \x01(\x0b\x32\x0c.RadioConfigH\x00\x12\x1a\n\tset_owner\x18\x02 \x01(\x0b\x32\x05.UserH\x00\x12\x1f\n\x0bset_channel\x18\x03 \x01(\x0b\x32\x08.ChannelH\x00\x12\x1b\n\x11get_radio_request\x18\x04 \x01(\x08H\x00\x12*\n\x12get_radio_response\x18\x05 \x01(\x0b\x32\x0c.RadioConfigH\x00\x12\x1d\n\x13get_channel_request\x18\x06 \x01(\rH\x00\x12(\n\x14get_channel_response\x18\x07 \x01(\x0b\x32\x08.ChannelH\x00\x12\x1b\n\x11get_owner_request\x18\x08 \x01(\x08H\x00\x12#\n\x12get_owner_response\x18\t \x01(\x0b\x32\x05.UserH\x00\x12\x1d\n\x13\x63onfirm_set_channel\x18  \x01(\x08H\x00\x12\x1b\n\x11\x63onfirm_set_radio\x18! \x01(\x08H\x00\x12\x18\n\x0e\x65xit_simulator\x18\" \x01(\x08H\x00\x12\x18\n\x0ereboot_seconds\x18# \x01(\x05H\x00\x12\x31\n\'get_canned_message_plugin_part1_request\x18$ \x01(\x08H\x00\x12\x32\n(get_canned_message_plugin_part1_response\x18% \x01(\tH\x00\x12\x31\n\'get_canned_message_plugin_part2_request\x18& \x01(\x08H\x00\x12\x32\n(get_canned_message_plugin_part2_response\x18\' \x01(\tH\x00\x12\x31\n\'get_canned_message_plugin_part3_request\x18( \x01(\x08H\x00\x12\x32\n(get_canned_message_plugin_part3_response\x18) \x01(\tH\x00\x12\x31\n\'get_canned_message_plugin_part4_request\x18* \x01(\x08H\x00\x12\x32\n(get_canned_message_plugin_part4_response\x18+ \x01(\tH\x00\x12)\n\x1fset_canned_message_plugin_part1\x18, \x01(\tH\x00\x12)\n\x1fset_canned_message_plugin_part2\x18- \x01(\tH\x00\x12)\n\x1fset_canned_message_plugin_part3\x18. \x01(\tH\x00\x12)\n\x1fset_canned_message_plugin_part4\x18/ \x01(\tH\x00\x12\x1a\n\x10shutdown_seconds\x18\x33 \x01(\x05H\x00\x42\t\n\x07variantBG\n\x13\x63om.geeksville.meshB\x0b\x41\x64minProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3')



_ADMINMESSAGE = DESCRIPTOR.message_types_by_name['AdminMessage']
AdminMessage = _reflection.GeneratedProtocolMessageType('AdminMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADMINMESSAGE,
  '__module__' : 'admin_pb2'
  # @@protoc_insertion_point(class_scope:AdminMessage)
  })
_sym_db.RegisterMessage(AdminMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\013AdminProtosH\003Z!github.com/meshtastic/gomeshproto'
  _ADMINMESSAGE._serialized_start=62
  _ADMINMESSAGE._serialized_end=1119
# @@protoc_insertion_point(module_scope)
