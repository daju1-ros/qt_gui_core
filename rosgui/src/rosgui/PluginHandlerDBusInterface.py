# Copyright (c) 2011, Dirk Thomas, Dorian Scholz, TU Darmstadt
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the TU Darmstadt nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from dbus.service import BusName, Object
import dbus

class PluginHandlerDBusInterface(Object):

    def __init__(self, plugin_handler, application_context, object_path):
        bus_name = BusName(application_context.dbus_unique_bus_name, dbus.SessionBus())
        super(PluginHandlerDBusInterface, self).__init__(bus_name, object_path)
        self._plugin_handler = plugin_handler

    @dbus.service.method('org.ros.rosgui.PluginHandlerXEmbed', in_signature='isi', out_signature='i')
    def embed_widget(self, pid, widget_object_name, area):
        return self._plugin_handler.embed_widget(pid, widget_object_name, area)

    @dbus.service.method('org.ros.rosgui.PluginHandlerXEmbed', in_signature='ss', out_signature='')
    def update_embedded_widget_title(self, widget_object_name, title):
        self._plugin_handler.update_embedded_widget_title(widget_object_name, title)

    @dbus.service.method('org.ros.rosgui.PluginHandlerXEmbed', in_signature='s', out_signature='')
    def unembed_widget(self, widget_object_name):
        self._plugin_handler.unembed_widget(widget_object_name)

    @dbus.service.method('org.ros.rosgui.PluginHandlerXEmbed', in_signature='', out_signature='')
    def close_plugin(self):
        self._plugin_handler.close_plugin()