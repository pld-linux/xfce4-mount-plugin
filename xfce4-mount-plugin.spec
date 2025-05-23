Summary:	mount/umount utility for Xfce panel
Summary(pl.UTF-8):	Narzędzie do montowania/odmontowywania dla panelu Xfce
Name:		xfce4-mount-plugin
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	77324f512ce82e4c63f2fe0a5a0fa192
Patch0:		%{name}-label-uuid.patch
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmount.so
%{_datadir}/xfce4/panel/plugins/xfce4-mount-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*
