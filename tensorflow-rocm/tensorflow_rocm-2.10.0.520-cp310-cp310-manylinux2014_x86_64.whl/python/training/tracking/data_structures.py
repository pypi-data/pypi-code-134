"""Trackable data structures."""
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# TODO(kathywu): Delete this file after all imports have been moved to the path
# below.
from tensorflow.python.trackable import data_structures
from tensorflow.python.util import deprecation

__getattr__ = deprecation.deprecate_moved_module(
    __name__, data_structures, "2.11")
