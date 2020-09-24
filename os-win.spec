#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : os-win
Version  : 5.1.0
Release  : 42
URL      : http://tarballs.openstack.org/os-win/os-win-5.1.0.tar.gz
Source0  : http://tarballs.openstack.org/os-win/os-win-5.1.0.tar.gz
Source1  : http://tarballs.openstack.org/os-win/os-win-5.1.0.tar.gz.asc
Summary  : Windows / Hyper-V library for OpenStack projects.
Group    : Development/Tools
License  : Apache-2.0
Requires: os-win-license = %{version}-%{release}
Requires: os-win-python = %{version}-%{release}
Requires: os-win-python3 = %{version}-%{release}
Requires: Babel
Requires: eventlet
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: pbr
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.utils
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package license
Summary: license components for the os-win package.
Group: Default

%description license
license components for the os-win package.


%package python
Summary: python components for the os-win package.
Group: Default
Requires: os-win-python3 = %{version}-%{release}

%description python
python components for the os-win package.


%package python3
Summary: python3 components for the os-win package.
Group: Default
Requires: python3-core
Provides: pypi(os_win)
Requires: pypi(babel)
Requires: pypi(eventlet)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)

%description python3
python3 components for the os-win package.


%prep
%setup -q -n os-win-5.1.0
cd %{_builddir}/os-win-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594140785
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-win
cp %{_builddir}/os-win-5.1.0/LICENSE %{buildroot}/usr/share/package-licenses/os-win/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-win/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
