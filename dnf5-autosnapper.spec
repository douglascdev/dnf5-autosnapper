Name:           dnf5-autosnapper
Version:        0.4
Release:        1%{?dist}
Summary:        A dnf5 plugin that automatically creates snapper btrfs snapshots.

License:        GPLv3+
URL:            https://github.com/douglascdev/dnf5-autosnapper
Source0:        %{name}-%{version}.tar.gz

Requires:       dnf5, libdnf5-plugin-actions
BuildArch:      noarch

%description
A dnf5 plugin that automatically creates snapper btrfs snapshots

%prep
# This automatically unpacks the source tarball and changes directory
%autosetup -n %{name}-%{version}

%install
# Copy from the unpacked source directory

mkdir -p %{buildroot}/etc/dnf/libdnf5-plugins/actions.d
cp snapper.conf %{buildroot}/etc/dnf/libdnf5-plugins/actions.d/

mkdir -p %{buildroot}/usr/share/doc/%{name}/
cp LICENSE %{buildroot}/usr/share/doc/%{name}/

%files
/etc/dnf/libdnf5-plugins/actions.d/snapper.conf

%license /usr/share/doc/%{name}/LICENSE

%changelog
* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com> 0.4-1
- test (douglasc.dev@gmail.com)

* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com> 0.3-1
- test (douglasc.dev@gmail.com)
- move back to rpmbuild (douglasc.dev@gmail.com)

* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com> 0.2-1
- new package built with tito

* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com>
- First autosnapper package
