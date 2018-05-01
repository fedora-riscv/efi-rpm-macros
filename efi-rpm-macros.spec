Summary: Common RPM Macros for building EFI-related packages
Name: efi-rpm-macros
Version: 2
Release: 2%{?dist}
Group: Development/System
License: GPLv3+
URL: https://github.com/rhboot/%{name}/
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86}
BuildRequires: git sed
Requires: rpm
BuildArch: noarch

Source0: https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0001: 0001-Simplify-efi_arch_upper.patch
Patch0002: 0002-Add-a-changelog-entry-to-the-.spec-for-version-2.patch
Patch0003: 0003-efi-rpm-macros.spec.in-use-autosetup.patch
Patch0004: 0004-Add-efi_alt_arch-and-efi_alt_arch_upper.patch
Patch0005: 0005-Return-nil-instead-of-on-unsupported-arches.patch
Patch0006: 0006-efi_arch-turns-out-nil-is-definitely-not-what-we-wan.patch

%global debug_package %{nil}
%global _efi_vendor_ %(eval sed -n -e 's/rhel/redhat/' -e 's/^ID=//p' /etc/os-release)

%description
%{name} provides a set of RPM macros for use in EFI-related packages.

%prep
%autosetup -S git

%build
%make_build EFI_VENDOR=%{_efi_vendor_} clean all

%install
%make_install EFI_VENDOR=%{_efi_vendor_}

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README
%{_rpmmacrodir}/*

%changelog
* Tue May 01 2018 Peter Jones <pjones@redhat.com> - 2-2
- Fix the non-efi and non-efi-alt-arch cases, hopefully.

* Tue May 01 2018 Peter Jones <pjones@redhat.com> - 2-1
- Lots of rpmlint fixups and the like.

* Mon Apr 30 2018 Peter Jones <pjones@redhat.com> - 1-1
- First shot at building it.
