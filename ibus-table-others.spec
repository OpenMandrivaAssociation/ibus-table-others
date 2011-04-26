%define	version 1.3.0.20100528
%define	release %mkrel 4

Name:      ibus-table-others
Summary:   ibus-table-others - table-based engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ibus-table-devel >= 1.3.0
BuildRequires: ibus-devel >= 1.3.9-5
Requires:  ibus-table >= 1.3.0
BuildArch:	noarch

%description
ibus-table-others provides the following input methods on IBus-Table on IBus framework:

    * CNS11643
    * Compose
    * Emoji
    * IPA-X-SAMPA
    * LaTex
    * RussianTraditional
    * Thai
    * Translit
    * Ua-Translit
    * Viqr
    * Yawerty

%files
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/cns11643.png
%{_datadir}/ibus-table/icons/ibus-emoji.svg
%{_datadir}/ibus-table/icons/ipa-x-sampa.png
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/yawerty.png
%{_datadir}/ibus-table/tables/cns11643.db
%{_datadir}/ibus-table/tables/emoji-table.db
%{_datadir}/ibus-table/tables/ipa-x-sampa.db
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/yawerty.db

%package -n ibus-table-th
Summary:   Thai language support via ibus-table
Group:     System/Internationalization
Requires:  ibus-table >= 1.3.0
Requires:  locales-th
Requires(post,preun): GConf2
Obsoletes: ibus-table-thai

%description -n ibus-table-th
ibus-table-th provides Thai input method on IBus Table under IBus framework.

%post -n ibus-table-th
%post_ibus_register_engine thai th

%preun -n ibus-table-th
%preun_ibus_unregister_engine thai

%files -n ibus-table-th
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/tables/thai.db

%package -n ibus-table-vi
Summary:   Vietnamese language support via ibus-table
Group:     System/Internationalization
Requires:  ibus-table >= 1.3.0
Requires(post,preun): GConf2
Requires:  locales-vi

%description -n ibus-table-vi
ibus-table-vi provides Vietnamese input method on IBus Table under IBus framework.

%post -n ibus-table-vi
%post_ibus_register_engine viqr vi

%preun -n ibus-table-vi
%preun_ibus_unregister_engine viqr

%files -n ibus-table-vi
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/tables/viqr.db

%package -n ibus-table-translit
Group: System/Internationalization
Summary: ibus-translit - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-translit
ibus-table-translit provides Translit input method on IBus Table under IBus framework.

%post -n ibus-table-translit
%post_ibus_register_engine translit ru
%post_ibus_register_engine translit-ua uk

%preun -n ibus-table-translit
%preun_ibus_unregister_engine translit
%preun_ibus_unregister_engine translit-ua

%files -n ibus-table-translit
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/translit-ua.png
%{_datadir}/ibus-table/icons/translit.png
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/tables/translit.db

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-compose --disable-latex
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT
