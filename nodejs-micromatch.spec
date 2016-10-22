%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name micromatch

Summary:       Glob matching for javascript/node.js
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.3.5
Release:       7%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/micromatch
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch
#Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Glob matching for javascript/node.js. 
A drop-in replacement and faster alternative to minimatch and multimatch. 
Just use micromatch.isMatch() instead of minimatch(), 
or use micromatch() instead of multimatch().

%prep
%setup -q -n package

%nodejs_fixdep lazy-cache
#%nodejs_fixdep optimist
%nodejs_fixdep normalize-path

chmod 644 index.js LICENSE package.json README.md

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%doc LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Mar 03 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.5-7
- Remove redundant dependency

* Wed Feb 24 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.5-6
- Fix dependency on collection metapackage

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 2.3.5-3
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 2.3.5-2
- Fix dependencies

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.3.5-1
- Initial package
