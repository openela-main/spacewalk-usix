%if 0%{?rhel} && 0%{?rhel} < 6
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%if 0%{?fedora} >= 23 || 0%{?rhel} >= 8
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%global python3rhnroot %{python3_sitelib}/spacewalk
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%global build_py3   1
%global default_py3 1
%endif

%define pythonX %{?default_py3: python3}%{!?default_py3: python2}

%global pythonrhnroot %{python_sitelib}/spacewalk

Name:	    spacewalk-usix
Version:	2.8.1
Release:	5%{?dist}
Summary:	Spacewalk server and client nano six library

License:	GPLv2
URL:		  https://github.com/spacewalkproject/spacewalk
Source0: https://github.com/spacewalkproject/spacewalk/archive/%{name}-%{version}.tar.gz
Patch0: spacewalk-usix-2.8.1-1-to-spacewalk-usix-2.8.1-2-el8.patch
Patch1: spacewalk-usix-2.8.1-2-el8-to-spacewalk-usix-2.8.1-3-el8.patch
Patch2: spacewalk-usix-2.8.1-3-el8-to-spacewalk-usix-2.8.1-4-el8.patch
Patch3: spacewalk-usix-2.8.1-4-el8-to-spacewalk-usix-2.8.1-5-el8.patch
BuildArch: noarch

Provides:	spacewalk-backend-usix = %{version}-%{release}
Requires: %{pythonX}-%{name} = %{version}-%{release}
Obsoletes: spacewalk-backend-usix < 2.8

%description
Library for writing code that runs on Python 2 and 3

%package -n python3-%{name}
Summary: Spacewalk client micro six library
Provides: python3-spacewalk-backend-usix = %{version}-%{release}
Obsoletes: python3-spacewalk-backend-usix < 2.8
BuildRequires: python3-devel

%description -n python3-%{name}
Library for writing code that runs on Python 2 and 3

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%define debug_package %{nil}

%install
install -m 0755 -d $RPM_BUILD_ROOT%{python3rhnroot}/common
install -m 0644 __init__.py $RPM_BUILD_ROOT%{python3rhnroot}/__init__.py
install -m 0644 common/__init__.py $RPM_BUILD_ROOT%{python3rhnroot}/common/__init__.py
install -m 0644 common/usix.py* $RPM_BUILD_ROOT%{python3rhnroot}/common/usix.py


%clean

%files

%files -n python3-%{name}
%dir %{python3rhnroot}
%dir %{python3rhnroot}/common
%{python3rhnroot}/__init__.py
%{python3rhnroot}/common/__init__.py
%{python3rhnroot}/common/usix.py*
%{python3rhnroot}/common/__pycache__/*
%exclude %{python3rhnroot}/__pycache__/*
%exclude %{python3rhnroot}/common/__pycache__/__init__.*

%changelog
* Mon Apr 16 2018 Tomas Kasparek <tkasparek@redhat.com> 2.8.1-5
- build spacewalk-usix just on python3 (tkasparek@redhat.com)

* Thu Mar 01 2018 Tomas Kasparek <tkasparek@redhat.com> 2.8.1-4
- empty %%files section is required for a package to build as a metapackage
  (tkasparek@redhat.com)

* Wed Feb 28 2018 Tomas Kasparek <tkasparek@redhat.com> 2.8.1-3
- split spacewalk-usix into python2 and python3 variants (tkasparek@redhat.com)
- build python3-spacewalk-usix also on rhel8 (tkasparek@redhat.com)

* Wed Feb 28 2018 Tomas Kasparek <tkasparek@redhat.com> 2.8.1-2
- rebuild for rhel8

* Fri Feb 09 2018 Michael Mraka <michael.mraka@redhat.com> 2.8.1-1
- remove install/clean section initial cleanup
- removed Group from specfile
- removed BuildRoot from specfiles

* Wed Aug 09 2017 Michael Mraka <michael.mraka@redhat.com> 2.7.8-1
- 1477753 - precompile py3 bytecode

* Mon Jul 31 2017 Eric Herget <eherget@redhat.com> 2.7.7-1
- update copyright year

* Mon Jul 17 2017 Jan Dobes 2.7.6-1
- Updated links to github in spec files
- Migrating Fedorahosted to GitHub

* Fri Feb 24 2017 Tomas Kasparek <tkasparek@redhat.com> 2.7.5-1
- Revert "do checks to match latest __init__.py from spacewalk-backend-libs"
- don't package pyc and pyo files

* Thu Feb 23 2017 Tomas Kasparek <tkasparek@redhat.com> 2.7.4-1
- do checks to match latest __init__.py from spacewalk-backend-libs
- don't rely on module initialization on backend-libs

* Fri Feb 17 2017 Tomas Kasparek <tkasparek@redhat.com> 2.7.3-1
- require python3 version of backend-libs on fedoras

* Fri Feb 17 2017 Tomas Kasparek <tkasparek@redhat.com> 2.7.2-1
- require spacewalk-backend-libs for usix functionality

* Wed Feb 15 2017 Tomas Kasparek <tkasparek@redhat.com> 2.7.1-1
- new package built with tito


