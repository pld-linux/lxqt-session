#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-session
Name:		lxqt-session
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d1bdb44afd29974ac9362e9384296495
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	libqtxdg-devel >= 1.0.0
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
	-DBUNDLE_XDG_UTILS=No \
	-DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-session
%attr(755,root,root) %{_bindir}/lxqt-session
%{_desktopdir}/lxqt-config-session.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-config-session
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ar.qm
%lang(ca) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ca.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ja.qm
%lang(ja_JP) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ja_JP.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_zh_CN.GB2312.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-config-session/lxqt-config-session_zh_TW.qm

%dir %{_datadir}/lxqt-qt5/translations/lxqt-session
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ar.qm
%lang(ca) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ca.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ja.qm
%lang(ja_JP) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ja_JP.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_zh_CN.GB2312.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-session/lxqt-session_zh_TW.qm
