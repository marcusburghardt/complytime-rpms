Name:           complytime
Version:        0.0.2
Release:        1%{?dist}
Summary:        ComplyTime leverages OSCAL to perform compliance assessment activities, using plugins for each stage of the lifecycle.

License:        Apache-2.0
URL:            https://github.com/complytime/complytime
Source0:        https://github.com/complytime/complytime/archive/refs/tags/v0.0.2.tar.gz

BuildRequires:  golang
BuildRequires:  make
Requires:       scap-security-guide

%description
ComplyTime leverages OSCAL to perform compliance assessment activities, using plugins for each stage of the lifecycle.

%prep
%setup -q

%undefine _missing_build_ids_terminate_build

%build
make build

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 bin/complytime %{buildroot}/usr/bin/complytime
install -m 0755 bin/openscap-plugin %{buildroot}/usr/bin/openscap-plugin

%check
make test-unit

%files
%license LICENSE
%doc README.md
/usr/bin/complytime
/usr/bin/openscap-plugin

%changelog
* Tue Apr 08 2025 Marcus Burghardt <maburgha@redhat.com>
- Initial RPM
