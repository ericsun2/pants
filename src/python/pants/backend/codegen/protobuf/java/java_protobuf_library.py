# coding=utf-8
# Copyright 2019 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from pants.backend.jvm.targets.jvm_target import JvmTarget


class JavaProtobufLibrary(JvmTarget):
  """A Java library generated from Protocol Buffer IDL files."""
