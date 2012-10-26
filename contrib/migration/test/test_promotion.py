##
# Copyright (c) 2012 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

import twistedcaldav.test.util
from contrib.migration.calendarpromotion import updatePlist

class PromotionTests(twistedcaldav.test.util.TestCase):
    """
    Calendar Server Promotion Tests
    """

    def test_updatePlist(self):
        """
        Verify XMPPNotifier is disabled and DSN is updated
        """

        orig = {
            "ignored" : "ignored",
        }
        expected = {
            "ignored" : "ignored",
            "DSN" : "/Library/Server/PostgreSQL For Server Services/Socket:caldav:caldav:::",
        }
        updatePlist(orig)
        self.assertEquals(orig, expected)

        orig = {
            "Notifications" : {
                "Services" : {
                    "XMPPNotifier" : {
                        "Enabled" : True
                    }
                }
            }
        }
        expected = {
            "Notifications" : {
                "Services" : {
                    "XMPPNotifier" : {
                        "Enabled" : False
                    }
                }
            },
            "DSN" : "/Library/Server/PostgreSQL For Server Services/Socket:caldav:caldav:::",
        }
        updatePlist(orig)
        self.assertEquals(orig, expected)
