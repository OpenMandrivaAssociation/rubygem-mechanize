%define oname mechanize

Name:       rubygem-%{oname}
Version:    1.0.0
Release:    %mkrel 1
Summary:    The Mechanize library is used for automating interaction with websites
Group:      Development/Ruby
License:    GPLv2+ or Ruby
URL:        http://mechanize.rubyforge.org
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(nokogiri) >= 1.2.1
Requires:   rubygem(hoe) >= 2.3.3
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
The Mechanize library is used for automating interaction with websites. 
Mechanize automatically stores and sends cookies, follows redirects,
can follow links, and submit forms.  Form fields can be populated and
submitted.  Mechanize also keeps track of the sites that you have visited as
a history.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/examples/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/EXAMPLES.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/FAQ.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/GUIDE.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
