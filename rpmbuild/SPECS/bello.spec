Name:           dnf5-autosnapper
Version:        0.1
Release:        1%{?dist}
Summary:        A dnf5 plugin that automatically creates snapper btrfs snapshots.

License:        GPLv3+
URL:            https://github.com/douglascdev/dnf5-autosnapper

Requires:       dnf5, libdnf5-plugin-actions
BuildArch:      noarch

%description
A dnf5 plugin that automatically creates snapper btrfs snapshots
%prep
%autosetup
%build
%configure
%make_build
%install

export FOLDER=%{buildroot}/etc/dnf/libdnf5-plugins/actions.d
export FILE=$FOLDER/snapper.actions
mkdir -p $FOLDER
cat %{sourcesroot}/snapshot > $FILE

%make_install
%files
$FILE
%license LICENSE
%changelog
* Mon Oct 20 2025 douglas <douglasc.dev@gmail.com>
- First autosnapper package
