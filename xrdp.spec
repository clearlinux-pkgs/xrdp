#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x03993B4065E7193B (meta@vmeta.jp)
#
%define keepstatic 1
Name     : xrdp
Version  : 0.9.21.1
Release  : 53
URL      : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.21.1/xrdp-0.9.21.1.tar.gz
Source0  : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.21.1/xrdp-0.9.21.1.tar.gz
Source1  : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.21.1/xrdp-0.9.21.1.tar.gz.asc
Summary  : An open source Remote Desktop Protocol (RDP) server
Group    : Development/Tools
License  : Apache-2.0
Requires: xrdp-bin = %{version}-%{release}
Requires: xrdp-data = %{version}-%{release}
Requires: xrdp-lib = %{version}-%{release}
Requires: xrdp-license = %{version}-%{release}
Requires: xrdp-man = %{version}-%{release}
Requires: xrdp-services = %{version}-%{release}
BuildRequires : FreeRDP-dev
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-configure
BuildRequires : libXfixes-dev
BuildRequires : libXrandr-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libvpx-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : opus-dev
BuildRequires : opusfile-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(imlib2)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(x11)
BuildRequires : yasm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Remove-RC4-support-for-OpenSSL.patch
Patch2: 0002-Fix-stateless.patch
Patch3: xfce.patch

%description
[![Build Status](https://github.com/neutrinolabs/xrdp/actions/workflows/build.yml/badge.svg)](https://github.com/neutrinolabs/xrdp/actions)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/neutrinolabs/xrdp-questions)
![Apache-License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

%package bin
Summary: bin components for the xrdp package.
Group: Binaries
Requires: xrdp-data = %{version}-%{release}
Requires: xrdp-license = %{version}-%{release}
Requires: xrdp-services = %{version}-%{release}

%description bin
bin components for the xrdp package.


%package data
Summary: data components for the xrdp package.
Group: Data

%description data
data components for the xrdp package.


%package dev
Summary: dev components for the xrdp package.
Group: Development
Requires: xrdp-lib = %{version}-%{release}
Requires: xrdp-bin = %{version}-%{release}
Requires: xrdp-data = %{version}-%{release}
Provides: xrdp-devel = %{version}-%{release}
Requires: xrdp = %{version}-%{release}

%description dev
dev components for the xrdp package.


%package lib
Summary: lib components for the xrdp package.
Group: Libraries
Requires: xrdp-data = %{version}-%{release}
Requires: xrdp-license = %{version}-%{release}

%description lib
lib components for the xrdp package.


%package license
Summary: license components for the xrdp package.
Group: Default

%description license
license components for the xrdp package.


%package man
Summary: man components for the xrdp package.
Group: Default

%description man
man components for the xrdp package.


%package services
Summary: services components for the xrdp package.
Group: Systemd services
Requires: systemd

%description services
services components for the xrdp package.


%package staticdev
Summary: staticdev components for the xrdp package.
Group: Default
Requires: xrdp-dev = %{version}-%{release}

%description staticdev
staticdev components for the xrdp package.


%prep
%setup -q -n xrdp-0.9.21.1
cd %{_builddir}/xrdp-0.9.21.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681745431
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure  --enable-pixman \
--enable-jpeg \
--enable-fuse \
--enable-pam \
--enable-vsock \
--enable-opus
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export GCC_IGNORE_WERROR=1
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1681745431
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xrdp
cp %{_builddir}/xrdp-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xrdp/490afe7aa564c6be23045021284706e4710336f6 || :
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/share/xrdp/xrdp/cert.pem
rm -f %{buildroot}*/usr/share/xrdp/xrdp/key.pem
rm -f %{buildroot}*/usr/share/xrdp/cert.pem
rm -f %{buildroot}*/usr/share/xrdp/key.pem
rm -f %{buildroot}*/usr/lib64/xrdp/libcommon.a
rm -f %{buildroot}*/usr/lib64/xrdp/libmc.a
rm -f %{buildroot}*/usr/lib64/xrdp/libscp.a
rm -f %{buildroot}*/usr/lib64/xrdp/libvnc.a
rm -f %{buildroot}*/usr/lib64/xrdp/libxrdp.a
rm -f %{buildroot}*/usr/lib64/xrdp/libxrdpapi.a
rm -f %{buildroot}*/usr/lib64/xrdp/libxup.a
## install_append content
mkdir -p %{buildroot}/usr/share/defaults
mv %{buildroot}/etc/* %{buildroot}/usr/share/defaults/
mv %{buildroot}/usr/share/defaults/pam.d %{buildroot}/usr/share
rm -f %{buildroot}/usr/share/defaults/xrdp/cert.pem
rm -f %{buildroot}/usr/share/defaults/xrdp/key.pem
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xrdp
/usr/bin/xrdp-chansrv
/usr/bin/xrdp-dis
/usr/bin/xrdp-genkeymap
/usr/bin/xrdp-keygen
/usr/bin/xrdp-sesadmin
/usr/bin/xrdp-sesman
/usr/bin/xrdp-sesrun

%files data
%defattr(-,root,root,-)
/usr/share/defaults/xrdp/km-00000406.ini
/usr/share/defaults/xrdp/km-00000407.ini
/usr/share/defaults/xrdp/km-00000409.ini
/usr/share/defaults/xrdp/km-0000040a.ini
/usr/share/defaults/xrdp/km-0000040b.ini
/usr/share/defaults/xrdp/km-0000040c.ini
/usr/share/defaults/xrdp/km-00000410.ini
/usr/share/defaults/xrdp/km-00000411.ini
/usr/share/defaults/xrdp/km-00000412.ini
/usr/share/defaults/xrdp/km-00000414.ini
/usr/share/defaults/xrdp/km-00000415.ini
/usr/share/defaults/xrdp/km-00000416.ini
/usr/share/defaults/xrdp/km-00000419.ini
/usr/share/defaults/xrdp/km-0000041d.ini
/usr/share/defaults/xrdp/km-00000807.ini
/usr/share/defaults/xrdp/km-00000809.ini
/usr/share/defaults/xrdp/km-0000080a.ini
/usr/share/defaults/xrdp/km-0000080c.ini
/usr/share/defaults/xrdp/km-00000813.ini
/usr/share/defaults/xrdp/km-00000816.ini
/usr/share/defaults/xrdp/km-0000100c.ini
/usr/share/defaults/xrdp/km-00010409.ini
/usr/share/defaults/xrdp/km-19360409.ini
/usr/share/defaults/xrdp/pulse/default.pa
/usr/share/defaults/xrdp/reconnectwm.sh
/usr/share/defaults/xrdp/rsakeys.ini
/usr/share/defaults/xrdp/sesman.ini
/usr/share/defaults/xrdp/startwm.sh
/usr/share/defaults/xrdp/xrdp.ini
/usr/share/defaults/xrdp/xrdp_keyboard.ini
/usr/share/pam.d/xrdp-sesman
/usr/share/xrdp/ad24b.bmp
/usr/share/xrdp/ad256.bmp
/usr/share/xrdp/cursor0.cur
/usr/share/xrdp/cursor1.cur
/usr/share/xrdp/sans-10.fv1
/usr/share/xrdp/xrdp24b.bmp
/usr/share/xrdp/xrdp256.bmp
/usr/share/xrdp/xrdp_logo.bmp

%files dev
%defattr(-,root,root,-)
/usr/include/ms-erref.h
/usr/include/ms-fscc.h
/usr/include/ms-rdpbcgr.h
/usr/include/ms-rdpeclip.h
/usr/include/ms-rdpedisp.h
/usr/include/ms-rdpefs.h
/usr/include/ms-rdpegdi.h
/usr/include/ms-rdpele.h
/usr/include/ms-rdperp.h
/usr/include/ms-smb2.h
/usr/include/painter.h
/usr/include/rfxcodec_common.h
/usr/include/rfxcodec_decode.h
/usr/include/rfxcodec_encode.h
/usr/include/xrdp_client_info.h
/usr/include/xrdp_constants.h
/usr/include/xrdp_rail.h
/usr/include/xrdp_sockets.h
/usr/lib64/libpainter.so
/usr/lib64/librfxencode.so
/usr/lib64/pkgconfig/libpainter.pc
/usr/lib64/pkgconfig/rfxcodec.pc
/usr/lib64/pkgconfig/xrdp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpainter.so.0
/usr/lib64/libpainter.so.0.0.0
/usr/lib64/librfxencode.so.0
/usr/lib64/librfxencode.so.0.0.0
/usr/lib64/xrdp/libcommon.so
/usr/lib64/xrdp/libcommon.so.0
/usr/lib64/xrdp/libcommon.so.0.0.0
/usr/lib64/xrdp/libmc.so
/usr/lib64/xrdp/libscp.so
/usr/lib64/xrdp/libscp.so.0
/usr/lib64/xrdp/libscp.so.0.0.0
/usr/lib64/xrdp/libvnc.so
/usr/lib64/xrdp/libxrdp.so
/usr/lib64/xrdp/libxrdp.so.0
/usr/lib64/xrdp/libxrdp.so.0.0.0
/usr/lib64/xrdp/libxrdpapi.so
/usr/lib64/xrdp/libxrdpapi.so.0
/usr/lib64/xrdp/libxrdpapi.so.0.0.0
/usr/lib64/xrdp/libxup.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xrdp/490afe7aa564c6be23045021284706e4710336f6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xrdp-dis.1
/usr/share/man/man5/sesman.ini.5
/usr/share/man/man5/xrdp.ini.5
/usr/share/man/man8/xrdp-chansrv.8
/usr/share/man/man8/xrdp-genkeymap.8
/usr/share/man/man8/xrdp-keygen.8
/usr/share/man/man8/xrdp-sesadmin.8
/usr/share/man/man8/xrdp-sesman.8
/usr/share/man/man8/xrdp-sesrun.8
/usr/share/man/man8/xrdp.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/xrdp-sesman.service
/usr/lib/systemd/system/xrdp.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libpainter.a
/usr/lib64/librfxencode.a
