Summary:	The Universal Plug and Play (UPnP) SDK for Linux
Summary(pl):	Pakiet programistyczny Universal Plug and Play (UPnP) dla Linuksa
Name:		libupnp
Version:	1.2.1a
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/upnp/%{name}-%{version}.tar.gz
# Source0-md5:	e72b3550bf064eedf080f16f09688891
URL:		http://upnp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an
API and open source code for building control points, devices, and
bridges that are compliant with Version 1.0 of the Universal Plug and
Play Device Architecture Specification.

%description -l pl
Linuksowy pakiet programistyczny dla urz±dzeñ UPnP (libupnp) dostarcza
programistom API i kod z otwartymi ¼ród³ami s³u¿±ce do tworzenia
punktów kontrolnych, urz±dzeñ i mostków kompatybilnych z wersj± 1.0
specyfikacji architektury urz±dzeñ Universal Plug and Play.

%package devel
Summary:	Header files for libupnp
Summary(pl):	Pliki nag³ówkowe libupnp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for the Linux SDK for UPnP Devices
(libupnp).

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe dla linuksowego pakietu
programistycznego do urz±dzeñ UPnP (libupnp).

%prep
%setup -q

%build
%{__make} -C ixml \
	CC="%{__cc}" \
	%{?!debug:DEBUG=0 DEBUG_FLAGS="%{rpmcflags} -DNDEBUG"} \
	%{?debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DDEBUG"}
%{__make} -C threadutil \
	CC="%{__cc}" \
	%{?!debug:DEBUG=0 DEBUG_FLAGS="%{rpmcflags} -DNDEBUG"} \
	%{?debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DDEBUG"}
%{__make} -C upnp\
	CC="%{__cc}" \
	%{?!debug:DEBUG=0 DEBUG_FLAGS="%{rpmcflags} -DNDEBUG"} \
	%{?debug:DEBUG=1 DEBUG_FLAGS="%{rpmcflags} -DDEBUG"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/upnp}

cp upnp/inc/* $RPM_BUILD_ROOT%{_includedir}/upnp
cp upnp/bin%{?debug:/debug}/* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libupnp.so
%attr(755,root,root) %{_libdir}/libixml.so
%attr(755,root,root) %{_libdir}/libthreadutil*.so

%files devel
%defattr(644,root,root,755)
%doc upnp/doc/UPnP_Programming_Guide.pdf
%{_includedir}/*
