Summary:	The Universal Plug and Play (UPnP) SDK for Linux
Name:		libupnp
Version:	1.2.1a
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/upnp/%{name}-%{version}.tar.gz
# Source0-md5:	e72b3550bf064eedf080f16f09688891
URL:		http://upnp.sourceforge.net/
Requires(pre,post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an
API and open source code for building control points, devices, and
bridges that are compliant with Version 1.0 of the Universal Plug and
Play Device Architecture Specification.

%package devel
Summary:	Header files for libupnp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for the Linux SDK for UPnP Devices
(libupnp).

%prep
%setup -q

%build
cd ixml
%{__make} \
	CC="%{__cc}" \
	%{?!debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DNDEBUG"} \
	%{?debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DDEBUG"}
cd ../threadutil
%{__make} \
	CC="%{__cc}" \
	%{?!debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DNDEBUG"} \
	%{?debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DDEBUG"}
cd ../upnp
%{__make} \
	CC="%{__cc}" \
	%{?!debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DNDEBUG"} \
	%{?debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DDEBUG"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/upnp

cd ixml
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT
install -m 644 inc/* $RPM_BUILD_ROOT%{_includedir}/upnp
cd ../threadutil
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT
install -m 644 inc/* $RPM_BUILD_ROOT%{_includedir}/upnp
cd ../upnp
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libupnp.so.*.* libupnp.so

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libupnp.so.*.*
%attr(755,root,root) %{_libdir}/libixml.so
%attr(755,root,root) %{_libdir}/libthreadutil.so

%files devel
%defattr(644,root,root,755)
%doc upnp/doc/UPnP_Programming_Guide.pdf
%{_libdir}/libupnp.so
%{_includedir}/*
