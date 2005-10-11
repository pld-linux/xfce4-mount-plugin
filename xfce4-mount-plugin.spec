Summary:	mount/umount utility for Xfce panel
Summary(pl):	Narzêdzie do montowania/odmontowywania dla panelu Xfce
Name:		xfce4-mount-plugin
Version:	0.3.2
Release:	1
License:	GPL v2+
Group:		X11/Applications	
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	0bcf4717a78d70e81f1b332535a87e74
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2:2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.1.90
Requires:	gtk+2 >= 2:2.6.0
Requires:	xfce4-panel >= 4.1.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin let's you easy mount/umount and check space uvailable on
destdevice.

%description -l pl
Ta wtyczka umo¿liwia ³atwe montowanie/odmontowywanie oraz sprawdzanie
miejsca dostêpnego na urz±dzeniu.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
