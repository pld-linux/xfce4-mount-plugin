Summary:	mount/umount utility for Xfce panel
Summary(pl.UTF-8):	Narzędzie do montowania/odmontowywania dla panelu Xfce
Name:		xfce4-mount-plugin
Version:	0.4.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-mount-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	1333adf1c76d8f8b4c6f58bbcf43b6c6
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin let's you easy mount/umount and check space uvailable on
destdevice.

%description -l pl.UTF-8
Ta wtyczka umożliwia łatwe montowanie/odmontowywanie oraz sprawdzanie
miejsca dostępnego na urządzeniu.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-mount-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-mount-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*
