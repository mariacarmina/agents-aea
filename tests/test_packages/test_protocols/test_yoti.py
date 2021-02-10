# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the tests of the yoti protocol package."""
from uuid import uuid4

from packages.fetchai.protocols.yoti.message import YotiMessage


def test_encode_decode_get_profile():
    """Test encode decode get profile."""
    msg = YotiMessage(
        performative=YotiMessage.Performative.GET_PROFILE,
        token=str(uuid4()),
        dotted_path="a",
        args=tuple(),
    )
    assert YotiMessage.decode(msg.encode()) == msg


def test_encode_decode_profile():
    """Test encode decode profile."""
    msg = YotiMessage(performative=YotiMessage.Performative.PROFILE, info={},)
    assert YotiMessage.decode(msg.encode()) == msg


def test_encode_decode_error():
    """Test encode decode error."""
    msg = YotiMessage(
        performative=YotiMessage.Performative.ERROR, error_code=500, error_msg="msg"
    )
    assert YotiMessage.decode(msg.encode()) == msg
