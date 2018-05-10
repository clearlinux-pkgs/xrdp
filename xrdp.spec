#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9F72CDBC01BF10EB (meta@vmeta.jp)
#
Name     : xrdp
Version  : 0.9.6
Release  : 17
URL      : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.6/xrdp-0.9.6.tar.gz
Source0  : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.6/xrdp-0.9.6.tar.gz
Source99 : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.6/xrdp-0.9.6.tar.gz.asc
Summary  : An open source Remote Desktop Protocol (RDP) server
Group    : Development/Tools
License  : Apache-2.0
Requires: xrdp-bin
Requires: xrdp-config
Requires: xrdp-lib
Requires: xrdp-doc
Requires: xrdp-data
BuildRequires : FreeRDP-dev
BuildRequires : Linux-PAM-dev
BuildRequires : libXfixes-dev
BuildRequires : libXrandr-dev
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(x11)
BuildRequires : qtbase-dev
Patch1: 0001-Remove-RC4-support-for-OpenSSL.patch

%description


%package bin
Summary: bin components for the xrdp package.
Group: Binaries
Requires: xrdp-data
Requires: xrdp-config

%description bin
bin components for the xrdp package.


%package config
Summary: config components for the xrdp package.
Group: Default

%description config
config components for the xrdp package.


%package data
Summary: data components for the xrdp package.
Group: Data

%description data
data components for the xrdp package.


%package dev
Summary: dev components for the xrdp package.
Group: Development
Requires: xrdp-lib
Requires: xrdp-bin
Requires: xrdp-data
Provides: xrdp-devel

%description dev
dev components for the xrdp package.


%package doc
Summary: doc components for the xrdp package.
Group: Documentation

%description doc
doc components for the xrdp package.


%package lib
Summary: lib components for the xrdp package.
Group: Libraries
Requires: xrdp-data

%description lib
lib components for the xrdp package.


%prep
%setup -q -n xrdp-0.9.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522107054
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
%configure --disable-static --sysconfdir=/usr/share/defaults/xrdp \
--disable-painter \
--disable-rfxcodec
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522107054
rm -rf %{buildroot}
%make_install

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

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/xrdp-sesman.service
/usr/lib/systemd/system/xrdp.service

%files data
%defattr(-,root,root,-)
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
/usr/lib64/pkgconfig/xrdp.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
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
