Name:           vdpauinfo
Version:        1.5
Release:        1%{?dist}
Summary:        Tool to query the capabilities of a VDPAU implementation
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/VDPAU/

Source0:        https://gitlab.freedesktop.org/vdpau/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:         https://gitlab.freedesktop.org/vdpau/%{name}/-/commit/da66af25aa327d21179d478f3a6d8c03b6c7f574.diff

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(vdpau) >= 1.5

%description
Tool to query the capabilities of a VDPAU implementation.

%prep
%autosetup -p1
autoreconf -vif

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/vdpauinfo

%changelog
* Fri Oct 07 2022 Simone Caronni <negativo17@gmail.com> - 1.5-1
- Update to 1.5.

* Tue Feb 15 2022 Simone Caronni <negativo17@gmail.com> - 1.4-10
- Clean up SPEC file.
- Add latest patch to show AV1 information.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
