#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    autotools.configure("--prefix=/usr")

#def build():
    #autotools.make()
    
def build():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/share/pkgconfig/mdds-2.0.pc", "/usr/share/pkgconfig/mdds-1.5.pc")
    
    pisitools.dodoc("AUTHORS", "LICENSE")
