#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
FocusWindow action
============================================================================

"""

from dragonfly.actions.action_base      import ActionBase, ActionError
from dragonfly.actions.action_startapp import StartApp
from dragonfly.windows  import Window
from dragonfly.actions.action_waitwindow import WaitWindow
import os.path
from subprocess           import Popen
import sys
import time

#---------------------------------------------------------------------------

class OpenWindow(StartApp):

    def __init__(self, executable=None, index=None):
        if executable:  self.executable = executable.lower()
        else:           self.executable = None
        self.index = index
        ActionBase.__init__(self)

        arguments = []
        if executable:  arguments.append("executable=%r" % executable)
        if index:       arguments.append("index=%r" % index)
        self._str = ", ".join(arguments)

    def _darwin_start_app(self, executable):
        # Try to use the macOS 'open' command-line program to start a new
        # instance of the specified application. Return False if this is
        # either not applicable or doesn't work.
        try_using_open = (
            sys.platform == "darwin" and
            not os.path.isabs(executable)
        )
        if try_using_open:
            process = Popen(['open', '-n', '-a', executable])
            return process.wait() == 0
        return False

    def _start_app_process(self, executable):
        try:
            return Popen(executable, cwd=None)
        except Exception as e:
            raise ActionError("Failed to start app %s: %s" % (executable, e))

    def _execute(self, data=None):
        executable = self.executable
        index = self.index
        if data and isinstance(data, dict):
            if executable:  executable = (executable % data).lower()
            if index:       index = (index % data).lower()

        index = int(index) if index else 0
        # Get the first matching window and bring it to the foreground.
        windows = Window.get_matching_windows(executable)

        if windows and (index < len(windows)):
            window = windows[index]
            window.set_foreground()
        else:
            if self._darwin_start_app(executable):
                pid = None
            else:
                # This either isn't macOS or the 'open' program didn't work, so
                # start the application as normal and get the process ID.
                pid = self._start_app_process(executable).pid
                if not pid:
                    raise ActionError("Failed to find window (%s)." % self._str)
