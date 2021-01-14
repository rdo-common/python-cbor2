# Created by pyp2rpm-3.3.4
%global pypi_name cbor2

Name:           python-%{pypi_name}
Version:        5.1.2
Release:        2%{?dist}
Summary:        Python CBOR (de)serializer with extensive tag support

License:        MIT
URL:            https://github.com/agronholm/cbor2
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 7049) serialization format.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  openstack-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 7049) serialization format.

%package -n python-%{pypi_name}-doc
Summary:        cbor2 documentation
BuildArch:      noarch

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%description -n python-%{pypi_name}-doc
Documentation for cbor2.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/_%{pypi_name}.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.2-2
- Make doc subpackage noarch (rhbz#1877691)

* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.2-1
- Initial package
