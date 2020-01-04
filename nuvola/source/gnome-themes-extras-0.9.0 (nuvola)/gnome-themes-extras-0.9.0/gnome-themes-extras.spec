Summary: Additional themes collection for GNOME
Name: gnome-themes-extras
Version: 0.9.0
Release: 0
License: Various
Group: User Interface/Desktop
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires:  glib2-devel >= 0:2.0.0
BuildRequires:  libxml2-devel >= 0:2.5.0
BuildRequires:  librsvg2-devel >= 0:2.1.3
Requires:	gnome-panel >= 2.2.2.2
Requires:	librsvg2 >= 2.2.0
Requires:	gtk-engines >= 2.6.0
Obsoletes:	Nuvola

%description
Additional SVG themes collection for GNOME

%prep
%setup

%build
%configure
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall
### Remove files not to be installed
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/@GTK_BINARY_VERSION@/engines/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/@GTK_BINARY_VERSION@/engines/*.a

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%{_datadir}/icons/*
%{_datadir}/themes/*
%{_datadir}/locale/*
%doc AUTHORS MAINTAINERS ChangeLog COPYING README license_dsg license_lgpl license_gpl TODO

%changelog
* Fri Feb 11 2005 Christian Schaller <uraeus@gnome.org>
- Update for dependency on new gtk-engines

* Sat Jun 05 2004 Christian Schaller <uraeus@gnome.org>
- Re-add translations

* Mon Jul 14 2003 Håvard Wigtil <havardw@stud.ntnu.no>
- Add translations to files section

* Thu May 01 2003 Yanko Kaneti <yaneti@declera.com>
- use the GTK_BINARY_VERSION autoconf variable

* Thu May 01 2003 Christian Schaller <Uraeus@gnome.org>
- Added buildreqs
- Added obsoletes Nuvola

* Wed Apr 02 2003 Yanko Kaneti <yaneti@declera.com>
- First spec
