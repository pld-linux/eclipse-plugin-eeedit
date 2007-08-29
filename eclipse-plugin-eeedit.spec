Summary:	eeedit - Eclipse External Editor
Summary(pl.UTF-8):	eeedit - zewnętrzny edytor dla eclipse
Name:		eclipse-plugin-eeedit
Version:	0.2.2
Release:	0.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://eeedit.googlecode.com/files/org.eeedit.vimclient_%{version}.jar
# Source0-md5:	042090eef835b5debe9fca9f6a91467b
URL:		http://code.google.com/p/eeedit/
Requires:	eclipse >= 3.1-2
Requires:	vim >= 4:7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
Integrates your favourite editor with Eclipse IDE.

%description -l pl.UTF-8
Integruje Twój ulubiony edytor ze środowiskiem Eclipse.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

install %{SOURCE0} $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/*
