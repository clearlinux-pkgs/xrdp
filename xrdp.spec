#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9F72CDBC01BF10EB (meta@vmeta.jp)
#
Name     : xrdp
Version  : 0.9.6
Release  : 23
URL      : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.6/xrdp-0.9.6.tar.gz
Source0  : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.6/xrdp-0.9.6.tar.gz
Source99 : https://github.com/neutrinolabs/xrdp/releases/download/v0.9.6/xrdp-0.9.6.tar.gz.asc
Summary  : An open source Remote Desktop Protocol (RDP) server
Group    : Development/Tools
License  : Apache-2.0
Requires: xrdp-bin
Requires: xrdp-config
Requires: xrdp-lib
Requires: xrdp-data
Requires: xrdp-license
Requires: xrdp-man
BuildRequires : FreeRDP-dev
BuildRequires : Linux-PAM-dev
BuildRequires : libXfixes-dev
BuildRequires : libXrandr-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(x11)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras
Patch1: 0001-Remove-RC4-support-for-OpenSSL.patch
Patch2: stateless.patch

%description


%package bin
Summary: bin components for the xrdp package.
Group: Binaries
Requires: xrdp-data
Requires: xrdp-config
Requires: xrdp-license
Requires: xrdp-man

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


%package lib
Summary: lib components for the xrdp package.
Group: Libraries
Requires: xrdp-data
Requires: xrdp-license

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


%prep
%setup -q -n xrdp-0.9.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531257331
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-painter \
--disable-rfxcodec \
--enable-pixman \
--enable-jpeg
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1531257331
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xrdp
cp COPYING %{buildroot}/usr/share/doc/xrdp/COPYING
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/share/defaults
mv %{buildroot}/etc/* %{buildroot}/usr/share/defaults/
mv %{buildroot}/usr/share/defaults/pam.d %{buildroot}/usr/share
## make_install_append end

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
%exclude /usr/share/defaults/xrdp/cert.pem
%exclude /usr/share/defaults/xrdp/key.pem
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
/usr/lib64/pkgconfig/xrdp.pc

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

%files license
%defattr(-,root,root,-)
/usr/share/doc/xrdp/COPYING

%files man
%defattr(-,root,root,-)
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
