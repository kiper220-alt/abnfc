%define _unpackaged_files_terminate_build 1

Name: abnfc
Version: 0.4.0
Release: alt1

Summary: ABNF compiler
License: GPLv2
Group: Development/C 
Url: https://github.com/zinid/abnfc
Vcs: https://github.com/zinid/abnfc

BuildRequires: ragel
BuildRequires: man2web
BuildRequires: make
BuildRequires: gcc

Source0: %name-%version.tar

%description
ABNF compiler

%prep
%setup -q

%build
%make_build all

%install
%__mkdir -p %buildroot%_bindir
%__install abnfc %buildroot%_bindir

%files 
%_bindir/abnfc 

%changelog
* Wed Jul 24 2024 Korney Gedert <kiper@altlinux.org> 0.4.0-alt1 
- Initial build.
