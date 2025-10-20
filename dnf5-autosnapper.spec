Name:           dnf5-autosnapper
Version:        0.2
Release:        1%{?dist}
Summary:        A dnf5 plugin that automatically creates snapper btrfs snapshots.

License:        GPLv3+
URL:            https://github.com/douglascdev/dnf5-autosnapper
Source0:        snapper.conf
Source1:        LICENSE

Requires:       dnf5, libdnf5-plugin-actions
BuildArch:      noarch

%description
A dnf5 plugin that automatically creates snapper btrfs snapshots

%install
mkdir -p %{buildroot}/etc/dnf/libdnf5-plugins/actions.d
cp %{SOURCE0} %{buildroot}/etc/dnf/libdnf5-plugins/actions.d/

mkdir -p %{buildroot}/usr/share/doc/%{name}/
cp %{SOURCE1} %{buildroot}/usr/share/doc/%{name}/

%files
/etc/dnf/libdnf5-plugins/actions.d/snapper.conf

%license /usr/share/doc/%{name}/LICENSE

%changelog
* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com> 0.2-1
- new package built with tito

* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com>
- First autosnapper package
