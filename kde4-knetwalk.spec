%define		_state		stable
%define		orgname		knetwalk
%define		qtver		4.8.0

Summary:	KDE knetwalk
Summary(pl.UTF-8):	knetwalk dla KDE
Name:		kde4-%{orgname}
Version:	4.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d429fad03cb9a97c4f9a05d7b71e1493
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of this game is to connect the network with a minimum amount
of clicks.

%description -l pl.UTF-8
Celem tej gry jest połączenie sieci minimalną liczbą kliknięć.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knetwalk
%{_desktopdir}/kde4/knetwalk.desktop
%{_datadir}/apps/knetwalk
%{_iconsdir}/*/*/apps/knetwalk.png
%{_iconsdir}/hicolor/scalable/apps/knetwalk.svgz
