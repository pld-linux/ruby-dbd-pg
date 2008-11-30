Summary:	Ruby Database driver for PostgreSQL
Name:		ruby-dbd-pg
Version:	0.3.6
Release:	1
License:	Ruby License
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/47540/dbd-pg-%{version}.tar.gz
# Source0-md5:	82167a3a06112e6113d4d76d869b79ad
URL:		http://rubyforge.org/projects/ruby-dbi/

%description
Ruby Database driver for PostgreSQL.

%prep
%setup -n dbd-pg-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/dbd/pg
%{ruby_rubylibdir}/dbd/Pg.rb

%clean
rm -rf $RPM_BUILD_ROOT
