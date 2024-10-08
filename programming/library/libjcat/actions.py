#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-D gtkdoc=true")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.removeDir("/usr/libexec/installed-tests")
    pisitools.removeDir("/usr/share/installed-tests")
    
    pisitools.dodoc("LICENSE", "NEWS", "README*")
