%define upstream_name    Throwable
%define upstream_version 0.102080

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	An easy-to-use class for error objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Throwable/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
Requires:	perl(Devel::StackTrace)

BuildArch:	noarch


%description
Throwable is a role for classes that are meant to be thrown as exceptions
to standard program flow. It is very simple and does only two things: saves
any previous value for '$@' and calls 'die $self'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.102.80-2mdv2011.0
+ Revision: 653623
- rebuild for updated spec-helper

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.80-1mdv2011.0
+ Revision: 563002
- update to 0.102080

* Thu Apr 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.110-1mdv2011.0
+ Revision: 537885
- update to 0.101110

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.90-2mdv2010.1
+ Revision: 490632
- adding missing requires:

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.90-1mdv2010.1
+ Revision: 490491
- import perl-Throwable


* Wed Jan 13 2010 cpan2dist 0.100090-1mdv
- initial mdv release, generated with cpan2dist
