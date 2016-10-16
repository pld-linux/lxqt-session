#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-session
Name:		lxqt-session
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	bfc0553d4afbaddf55fa10b674991202
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	xdg-user-dirs
BuildRequires:	xdg-utils >= 1.1.0
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-session

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	-DBUNDLE_XDG_UTILS=No \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-session
%attr(755,root,root) %{_bindir}/lxqt-leave
%attr(755,root,root) %{_bindir}/lxqt-session
%{_desktopdir}/lxqt-config-session.desktop
%{_desktopdir}/lxqt-hibernate.desktop
%{_desktopdir}/lxqt-leave.desktop
%{_desktopdir}/lxqt-lockscreen.desktop
%{_desktopdir}/lxqt-logout.desktop
%{_desktopdir}/lxqt-reboot.desktop
%{_desktopdir}/lxqt-shutdown.desktop
%{_desktopdir}/lxqt-suspend.desktop
%{_mandir}/man1/lxqt-config-session.1*
%{_mandir}/man1/lxqt-leave.1*
%{_mandir}/man1/lxqt-session.1*
#%dir %{_datadir}/lxqt/translations/lxqt-config-session
#%dir %{_datadir}/lxqt/translations/lxqt-leave
#%dir %{_datadir}/lxqt/translations/lxqt-session
