Summary:	mount/umount utility for Xfce panel
Summary(pl):	Narzêdzie do montowania/odmontowywania dla panelu Xfce
Name:		xfce4-mount-plugin
Version:	0.1
Release:	0.1
License:	GPL
Group:		X11/Applications	
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	2dc989aadd349d6d248cd3d64cdfb93a
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.1.90
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
