#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parse-RecDescent
Version  : 1.967015
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/J/JT/JTBRAUN/Parse-RecDescent-1.967015.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JT/JTBRAUN/Parse-RecDescent-1.967015.tar.gz
Summary  : 'Generate Recursive-Descent Parsers'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Parse-RecDescent-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Parse::RecDescent version 1.967015
NAME
Parse::RecDescent - generate recursive-descent parsers

%package dev
Summary: dev components for the perl-Parse-RecDescent package.
Group: Development
Provides: perl-Parse-RecDescent-devel = %{version}-%{release}
Requires: perl-Parse-RecDescent = %{version}-%{release}

%description dev
dev components for the perl-Parse-RecDescent package.


%package perl
Summary: perl components for the perl-Parse-RecDescent package.
Group: Default
Requires: perl-Parse-RecDescent = %{version}-%{release}

%description perl
perl components for the perl-Parse-RecDescent package.


%prep
%setup -q -n Parse-RecDescent-1.967015
cd %{_builddir}/Parse-RecDescent-1.967015

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parse::RecDescent.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
