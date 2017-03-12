#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : os-win
Version  : 1.2.1
Release  : 17
URL      : http://tarballs.openstack.org/os-win/os-win-1.2.1.tar.gz
Source0  : http://tarballs.openstack.org/os-win/os-win-1.2.1.tar.gz
Source99 : http://tarballs.openstack.org/os-win/os-win-1.2.1.tar.gz.asc
Summary  : Windows / Hyper-V library for OpenStack projects.
Group    : Development/Tools
License  : Apache-2.0
Requires: os-win-python
Requires: Babel
Requires: eventlet
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
BuildRequires : configparser-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
======
os-win
======
Windows / Hyper-V library for OpenStack projects.
This library contains Windows / Hyper-V specific code commonly used in
OpenStack projects. The library can be used in any other OpenStack projects
where it is needed.

%package python
Summary: python components for the os-win package.
Group: Default

%description python
python components for the os-win package.


%prep
%setup -q -n os-win-1.2.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489282402
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489282402
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
