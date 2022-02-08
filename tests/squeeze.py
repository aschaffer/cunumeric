# Copyright 2021-2022 NVIDIA Corporation
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
#

# import numpy as np
import cunumeric as np


def test():
    x = np.array([[[1, 2, 3]]])
    y = x.squeeze()
    assert y.ndim == 1
    assert y[0] == 1
    assert y[1] == 2
    assert y[2] == 3

    y = x.squeeze(axis=1)
    assert y.ndim == 2
    assert y[0, 0] == 1
    assert y[0, 1] == 2
    assert y[0, 2] == 3

    x = np.array([[[1], [2], [3]]])
    y = x.squeeze(axis=(0, 2))
    assert y.ndim == 1
    assert y[0] == 1
    assert y[1] == 2
    assert y[2] == 3


if __name__ == "__main__":
    test()
