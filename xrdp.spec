#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9F72CDBC01BF10EB (meta@vmeta.jp)
#
%define keepstatic 1
Name     : xrdp
Version  : 0.9.10
Release  : 34
URL      : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.10/xrdp-0.9.10.tar.gz
Source0  : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.10/xrdp-0.9.10.tar.gz
Source99 : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.10/xrdp-0.9.10.tar.gz.asc
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
BuildRequires : buildreq-qmake
BuildRequires : e2fsprogs-dev
BuildRequires : libXfixes-dev
BuildRequires : libXrandr-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(x11)
BuildRequires : yasm
Patch1: 0001-Remove-RC4-support-for-OpenSSL.patch
Patch2: stateless.patch

%description
[![Build Status](https://travis-ci.org/neutrinolabs/xrdp.svg?branch=devel)](https://travis-ci.org/neutrinolabs/xrdp)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/neutrinolabs/xrdp)
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

%description services
services components for the xrdp package.


%package staticdev
Summary: staticdev components for the xrdp package.
Group: Default
Requires: xrdp-dev = %{version}-%{release}

%description staticdev
staticdev components for the xrdp package.


%prep
%setup -q -n xrdp-0.9.10
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563913800
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure  --enable-pixman \
--enable-jpeg \
--enable-fuse \
--enable-pam \
--enable-vsock
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1563913800
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xrdp
cp COPYING %{buildroot}/usr/share/package-licenses/xrdp/COPYING
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/defaults
mv %{buildroot}/etc/* %{buildroot}/usr/share/defaults/
mv %{buildroot}/usr/share/defaults/pam.d %{buildroot}/usr/share
## install_append end

%files
%defattr(-,root,root,-)
%exclude /usr/lib64/xrdp/libcommon.a
%exclude /usr/lib64/xrdp/libmc.a
%exclude /usr/lib64/xrdp/libscp.a
%exclude /usr/lib64/xrdp/libvnc.a
%exclude /usr/lib64/xrdp/libxrdp.a
%exclude /usr/lib64/xrdp/libxrdpapi.a
%exclude /usr/lib64/xrdp/libxup.a

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
%exclude /usr/share/defaults/xrdp/cert.pem
%exclude /usr/share/defaults/xrdp/key.pem
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
/usr/share/defaults/xrdp/pulse/default.pa
/usr/share/defaults/xrdp/reconnectwm.sh
/usr/share/defaults/xrdp/rsakeys.ini
/usr/share/defaults/xrdp/sesman.ini
/usr/share/defaults/xrdp/startwm.sh
/usr/share/defaults/xrdp/xrdp.ini
/usr/share/defaults/xrdp/xrdp.sh
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
/usr/include/*.h
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
/usr/share/package-licenses/xrdp/COPYING

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
