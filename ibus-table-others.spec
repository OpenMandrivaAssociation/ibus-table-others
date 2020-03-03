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
%{_datadir}/ibus-table/icons/ipa-x-sampa.svg
%{_datadir}/ibus-table/icons/rusle.png
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/telex.png
%{_datadir}/ibus-table/icons/vni.png
%{_datadir}/ibus-table/icons/yawerty.png
%{_datadir}/ibus-table/tables/cns11643.db
%{_datadir}/ibus-table/tables/emoji-table.db
%{_datadir}/ibus-table/tables/ipa-x-sampa.db
%{_datadir}/ibus-table/tables/rusle.db
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/telex.db
%{_datadir}/ibus-table/tables/vni.db
%{_datadir}/ibus-table/tables/yawerty.db

%package -n ibus-table-compose
Group: System/Internationalization
Summary: ibus-compose table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-compose
ibus-table-compose provides compose input method on IBus Table under IBus framework.

%files -n ibus-table-compose
#%{_datadir}/ibus-table/icons/compose.svg
#%{_datadir}/ibus-table/tables/compose.db

%package -n ibus-table-latex
Group: System/Internationalization
Summary: ibus-latex table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-latex
ibus-table-latex provides latex input method on IBus Table under IBus framework.

%files -n ibus-table-latex
%{_datadir}/ibus-table/icons/latex.svg
%{_datadir}/ibus-table/tables/latex.db

%package -n ibus-table-mathwriter
Group: System/Internationalization
Summary: ibus-mathwriter table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-mathwriter
ibus-table-mathwriter provides mathwriter input method on IBus Table under IBus framework.

%files -n ibus-table-mathwriter
%{_datadir}/ibus-table/icons/mathwriter.png
%{_datadir}/ibus-table/tables/mathwriter-ibus.db

%package -n ibus-table-th
Summary:   Thai language support via ibus-table
Group:     System/Internationalization
Requires:  ibus-table >= 1.3.0
Requires:  locales-th
Requires(post,preun): GConf2
Obsoletes: ibus-table-thai

%description -n ibus-table-th
ibus-table-th provides Thai input method on IBus Table under IBus framework.

%files -n ibus-table-th
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

%files -n ibus-table-vi
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/tables/viqr.db

%package -n ibus-table-translit
Group: System/Internationalization
Summary: ibus-translit - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-translit
ibus-table-translit provides Translit input method on IBus Table under IBus framework.

%files -n ibus-table-translit
%{_datadir}/ibus-table/icons/translit-ua.svg
%{_datadir}/ibus-table/icons/translit.svg
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/tables/translit.db

%package -n ibus-table-hu-rovas
Summary:   Hungarian language support via ibus-table
Group:     System/Internationalization
Requires:  ibus-table >= 1.3.0
Requires(post,preun): GConf2
Requires:  locales-hu

%description -n ibus-table-hu-rovas
ibus-table-hu-rovas provides old Hungarian rovas input method on IBus Table under IBus framework.

%files -n ibus-table-hu-rovas
%{_datadir}/ibus-table/icons/hu-old-hungarian-rovas.svg
%{_datadir}/ibus-table/tables/hu-old-hungarian-rovas.db



#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --disable-compose --disable-latex
%make_build

%install
%make_install

