#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-win
Version  : 1.2.1
Release  : 10
URL      : http://tarballs.openstack.org/os-win/os-win-1.2.1.tar.gz
Source0  : http://tarballs.openstack.org/os-win/os-win-1.2.1.tar.gz
Summary  : Windows / Hyper-V library for OpenStack projects.
Group    : Development/Tools
License  : Apache-2.0
Requires: os-win-python
BuildRequires : Jinja2
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.service-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : repoze.lru-python
BuildRequires : setuptools
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

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
Requires: oslo.service-python

%description python
python components for the os-win package.


%prep
%setup -q -n os-win-1.2.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
