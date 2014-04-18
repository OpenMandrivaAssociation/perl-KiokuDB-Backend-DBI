%define upstream_name    KiokuDB-Backend-DBI
%define upstream_version 1.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	L<KiokuDB::TypeMap::Entry>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/KiokuDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Core)
BuildRequires:	perl(DBIx::Class::ResultSource::Table)
BuildRequires:	perl(DBIx::Class::Schema)
BuildRequires:	perl(Data::Stream::Bulk)
BuildRequires:	perl(Data::Stream::Bulk::DBI)
BuildRequires:	perl(File::NFSLock)
BuildRequires:	perl(JSON)
BuildRequires:	perl(KiokuDB)
BuildRequires:	perl(KiokuDB::Backend)
BuildRequires:	perl(KiokuDB::Backend::Role::Clear)
BuildRequires:	perl(KiokuDB::Backend::Role::Concurrency::POSIX)
BuildRequires:	perl(KiokuDB::Backend::Role::GC)
BuildRequires:	perl(KiokuDB::Backend::Role::Query::GIN)
BuildRequires:	perl(KiokuDB::Backend::Role::Query::Simple)
BuildRequires:	perl(KiokuDB::Backend::Role::Scan)
BuildRequires:	perl(KiokuDB::Backend::Role::TXN)
BuildRequires:	perl(KiokuDB::Backend::Serialize::Delegate)
BuildRequires:	perl(KiokuDB::Test)
BuildRequires:	perl(KiokuDB::TypeMap)
BuildRequires:	perl(KiokuDB::TypeMap::Entry)
BuildRequires:	perl(KiokuDB::TypeMap::Entry::Naive)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Search::GIN)
BuildRequires:	perl(Search::GIN::Extract::Class)
BuildRequires:	perl(Search::GIN::Extract::Delegate)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::TempDir)
BuildRequires:	perl(Test::use::ok)
BuildRequires:  perl(Test::Requires)
BuildRequires:	perl(Throwable)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(ok)
BuildRequires:	perl(strictures)
BuildArch:	noarch

%description
This the DBIx::Class manpage component provides the code necessary for the
DBIx::Class::Row manpage objects to refer to the KiokuDB manpage objects
stored in the KiokuDB::Backend::DBI manpage.

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
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*
