Summary:	Real-time, text-based, serverless LAN chat program
Summary(pl):	Dzia�aj�cy w czasie rzeczywistym, tekstowy, bezserwerowy program do pogaw�dek sieciowych
Name:		vyqchat
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://linux.bydg.org/~yogin/%{name}-%{version}.tar.gz
# Source0-md5:	89731e26467dfd2d33c5703dc4b839a7
URL:		http://linux.bydg.org/~yogin/#vyqchat
BuildRequires:	qt-devel >= 3.1.0
BuildRequires:	arts-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VyQChat is a real-time, text-based, serverless chat program dedicated
to LANs, that runs on Linux using Qt/X11 library. It is almost 100%
compatible with Vypress Chat(TM) for Windows. It allows you to chat
with friends on public or private channels, send and recieve messages
etc.

%description -l pl
VyQChat jest dzia�aj�cym w czasie rzeczywistym, tekstowym, nie
wymagaj�cym serwera program do pogaw�dek przeznaczonym dla sieci
lokalnych, kt�ry dzia�a w Linuksie korzystaj�c z biblioteki Qt/X11.
Jest on niemal w 100% zgodny z programem Vypress Chat(TM) dla Windows.
Pozwala on na rozmowy z przyjaci�mi na kana�ach publicznych lub
prywatnych, wysy�anie i otrzymywanie wiadomo�ci itp.

%prep
%setup  -q

%build
%configure \
	--with-Qt-include-dir=%{_includedir}/qt \
	--with-Qt-lib-dir=%{_libdir} \
	--with-arts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}