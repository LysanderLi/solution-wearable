# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
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

from usr.common import *
from usr import EventMesh
import osTimer


class DeviceManager(Abstract):
    def __init__(self):
        self.timer = osTimer()

    def initialization(self, *args, **kwargs):
        self.timer.start(3000, 1, self.do_notify_time)

    def do_notify_time(self, *args):
        EventMesh.publish("topic_time")
