Summary:	mount/umount utility for Xfce panel
Summary(pl.UTF-8):	Narzędzie do montowania/odmontowywania dla panelu Xfce
Name:		xfce4-mount-plugin
Version:	1.1.7
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	46e9725946c9167bb3becc10c115d85b
Patch0:		%{name}-label-uuid.patch
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin let's you easy mount/umount and check space uvailable on
destdevice.

%description -l pl.UTF-8
Ta wtyczka umożliwia łatwe montowanie/odmontowywanie oraz sprawdzanie
miejsca dostępnego na urządzeniu.

%prep
%setup -q
%patch -P 0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmount.so
%{_datadir}/xfce4/panel/plugins/xfce4-mount-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*
