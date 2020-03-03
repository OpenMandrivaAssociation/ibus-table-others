Summary:	ibus-table-others - table-based engine
Name:		ibus-table-others
Version:	1.3.11
Release:	1
License:	GPLv2+
Group:		System/Internationalization
URL:       https://github.com/moebiuscurve/ibus-table-others
Source0:   https://github.com/moebiuscurve/ibus-table-others/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(ibus-table)
Requires:	ibus-table
BuildArch:	noarch

%description
Provides the following input methods on IBus-Table on IBus framework:

    * CNS11643
    * Emoji
    * IPA-X-SAMPA
    * RussianTraditional
    * Yawerty

%files
%{_datadir}/ibus-table/icons/cns11643.png
%{_datadir}/ibus-table/icons/ibus-emoji.svg
#%{_datadir}/ibus-table/icons/ipa-x-sampa.png
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/yawerty.png
%{_datadir}/ibus-table/tables/cns11643.db
%{_datadir}/ibus-table/tables/emoji-table.db
%{_datadir}/ibus-table/tables/ipa-x-sampa.db
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/yawerty.db

#----------------------------------------------------------------------------

%package -n ibus-table-th
Summary:	Thai language support via ibus-table
Group:		System/Internationalization
Requires:	ibus-table
Requires:	locales-th
Requires(post,preun):	GConf2

%description -n ibus-table-th
Thai input method on IBus Table under IBus framework.

%files -n ibus-table-th
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/tables/thai.db

#----------------------------------------------------------------------------

%package -n ibus-table-vi
Summary:	Vietnamese language support via ibus-table
Group:		System/Internationalization
Requires:	ibus-table
Requires(post,preun):	GConf2
Requires:	locales-vi

%description -n ibus-table-vi
Vietnamese input method on IBus Table under IBus framework.

%files -n ibus-table-vi
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/tables/viqr.db

#----------------------------------------------------------------------------

%package -n ibus-table-translit
Summary:	ibus-translit - table-based engine
Group:		System/Internationalization
Requires:	ibus-table
Requires(post,preun):	GConf2

%description -n ibus-table-translit
Translit input method on IBus Table under IBus framework.

%files -n ibus-table-translit
#%{_datadir}/ibus-table/icons/translit-ua.png
#%{_datadir}/ibus-table/icons/translit.png
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/tables/translit.db

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --disable-compose --disable-latex
%make_build

%install
%make_install

