#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

# .la files needed to load modules
KeepSpecial = ["libtool"]

def setup():
    # ghostscript is better than dps
    # unstable fpx support disabled
    # trio is for old systems not providing vsnprintf
    autotools.configure("--enable-shared \
                         --enable-year2038 \
                         --disable-static \
                         --disable-openmp \
                         --with-threads \
                         --with-modules \
                         --with-magick-plus-plus \
                         --with-perl \
                         --with-bzlib \
                         --with-gslib \
                         --with-jbig \
                         --with-jpeg \
                         --with-jp2 \
                         --with-lcms2 \
                         --with-png \
                         --with-tiff \
                         --with-ttf \
                         --with-wmf \
                         --with-fontpath=/usr/share/fonts \
                         --with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --with-xml \
                         --with-zlib \
                         --with-x \
                         --with-tcmalloc \
                         --with-quantum-depth=16 \
                         --without-dps \
                         --without-fpx \
                         --without-trio")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make("perl-build")

def install():
    autotools.rawInstall("DESTDIR=%s doc_DATA='Copyright.txt NEWS.txt'" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C PerlMagick" % get.installDIR())
    for d in ("demo/", "README.txt"):
        pisitools.insinto("/usr/share/doc/PerlMagick", "PerlMagick/%s" % d)

    pisitools.remove("/usr/lib/*.la")
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
