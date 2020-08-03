# =============================================================================
# Copyright 2020 NVIDIA. All Rights Reserved.
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
# =============================================================================

from nemo.collections.nlp import callbacks, data, nm, utils
from nemo.collections.nlp.neural_types import *
from nemo.package_info import __version__ as nemo_version

# Set collection version equal to NeMo version.
__version__ = nemo_version

# Authorship.
__author__ = "NVIDIA Corporation"

# Set collection name.
__description__ = "Natural Language Processing collection"
