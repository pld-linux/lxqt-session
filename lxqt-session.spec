#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Main session for LXQt desktop suite
Summary(pl.UTF-8):	Główna sesja dla środowiska LXQt
Name:		lxqt-session
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-session/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	906806304592ba40b71b074c848d4e3e
URL:		http://www.lxqt.org/
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kwindowsystem-devel >= 6.0.0
BuildRequires:	kp6-layer-shell-qt-devel >= 6.0.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	libqtxdg-devel >= 4.3.0
BuildRequires:	procps-devel
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	udev-devel
BuildRequires:	xdg-user-dirs
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Main session for LXQt desktop suite.

%description -l pl.UTF-8
Główna sesja dla środowiska LXQt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-session
%attr(755,root,root) %{_bindir}/lxqt-leave
%attr(755,root,root) %{_bindir}/lxqt-session
%attr(755,root,root) %{_bindir}/startlxqt
/etc/xdg/autostart/lxqt-xscreensaver-autostart.desktop
%{_datadir}/xsessions/lxqt.desktop
%{_datadir}/lxqt/lxqt.conf
%{_datadir}/lxqt/session.conf
%{_datadir}/lxqt/waylandwindowmanagers.conf
%{_datadir}/lxqt/windowmanagers.conf
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
%{_mandir}/man1/startlxqt.1*
%dir %{_datadir}/lxqt/translations/lxqt-config-session
%dir %{_datadir}/lxqt/translations/lxqt-leave
%dir %{_datadir}/lxqt/translations/lxqt-session
