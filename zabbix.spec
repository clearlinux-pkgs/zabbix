#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zabbix
Version  : 4.4.5
Release  : 4
URL      : https://github.com/zabbix/zabbix/archive/4.4.5.tar.gz
Source0  : https://github.com/zabbix/zabbix/archive/4.4.5.tar.gz
Source1  : zabbix-agent.service
Summary  : Network and application monitoring tool.
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: zabbix-bin = %{version}-%{release}
Requires: zabbix-data = %{version}-%{release}
Requires: zabbix-license = %{version}-%{release}
Requires: zabbix-man = %{version}-%{release}
Requires: zabbix-services = %{version}-%{release}
BuildRequires : mariadb-dev
BuildRequires : mariadb-extras-clientlib
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(libpcre)
BuildRequires : zlib-dev
Patch1: 0001-Use-default-hardcoded-config-files-with-Include-stat.patch

%description
Zabbix is free software, released under the GNU General Public License
(GPL) version 2.

%package bin
Summary: bin components for the zabbix package.
Group: Binaries
Requires: zabbix-data = %{version}-%{release}
Requires: zabbix-license = %{version}-%{release}
Requires: zabbix-services = %{version}-%{release}

%description bin
bin components for the zabbix package.


%package data
Summary: data components for the zabbix package.
Group: Data

%description data
data components for the zabbix package.


%package extras-client
Summary: extras-client components for the zabbix package.
Group: Default

%description extras-client
extras-client components for the zabbix package.


%package license
Summary: license components for the zabbix package.
Group: Default

%description license
license components for the zabbix package.


%package man
Summary: man components for the zabbix package.
Group: Default

%description man
man components for the zabbix package.


%package services
Summary: services components for the zabbix package.
Group: Systemd services

%description services
services components for the zabbix package.


%prep
%setup -q -n zabbix-4.4.5
cd %{_builddir}/zabbix-4.4.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582760292
export GCC_IGNORE_WERROR=1
export GOPROXY=file:///usr/share/goproxy
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static --enable-server \
--enable-proxy \
--with-mysql \
--enable-agent \
--disable-agent2 \
--disable-java \
--enable-ipv6
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1582760292
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zabbix
cp %{_builddir}/zabbix-4.4.5/COPYING %{buildroot}/usr/share/package-licenses/zabbix/26c435e19b7997e6327d77d52c4a510613c857d2
cp %{_builddir}/zabbix-4.4.5/templates/media/mattermost/LICENSE %{buildroot}/usr/share/package-licenses/zabbix/cca29330ec514dc3d67f2be9453e9e9986011936
cp %{_builddir}/zabbix-4.4.5/templates/media/mattermost/LICENSE-APACHE2 %{buildroot}/usr/share/package-licenses/zabbix/7be518eca9ce309f9a65999f72a4e331cf6d4243
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/zabbix-agent.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zabbix_get
/usr/bin/zabbix_js
/usr/bin/zabbix_proxy
/usr/bin/zabbix_sender
/usr/bin/zabbix_server

%files data
%defattr(-,root,root,-)
/usr/share/defaults/zabbix/zabbix_agentd.conf
/usr/share/defaults/zabbix/zabbix_server.conf

%files extras-client
%defattr(-,root,root,-)
/usr/bin/zabbix_agentd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zabbix/26c435e19b7997e6327d77d52c4a510613c857d2
/usr/share/package-licenses/zabbix/7be518eca9ce309f9a65999f72a4e331cf6d4243
/usr/share/package-licenses/zabbix/cca29330ec514dc3d67f2be9453e9e9986011936

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/zabbix_get.1
/usr/share/man/man1/zabbix_sender.1
/usr/share/man/man8/zabbix_agentd.8
/usr/share/man/man8/zabbix_proxy.8
/usr/share/man/man8/zabbix_server.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/zabbix-agent.service
