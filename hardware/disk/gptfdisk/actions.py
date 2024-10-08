#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -i '/^#include /s|ncursesw/||' gptcurses.cc")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # pisitools.dobin("cgdisk")
    # pisitools.dobin("fixparts")
    # pisitools.dobin("gdisk")
    # pisitools.dobin("sgdisk")

    # pisitools.doman("cgdisk.8")
    # pisitools.doman("fixparts.8")
    # pisitools.doman("gdisk.8")
    # pisitools.doman("sgdisk.8")
    for bin in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.dosym("/usr/bin/%s" % bin, "/usr/sbin/%s" % bin)

    pisitools.dodoc("COPYING", "NEWS", "README")
