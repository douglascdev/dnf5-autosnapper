# dnf5-autosnapper
A dnf5 plugin that automatically creates snapper btrfs snapshots

## Install
```
sudo dnf copr enable douglascdev/dnf5-autosnapper && sudo dnf install dnf5-autosnapper
```

## Recommended dev environment
To avoid cluttering my actual fedora install with packages and files, I develop the package like this:
```
distrobox create --name fedora -i fedora:42 -H ~/dnf5-autosnapper
# runs in ~/dnf5-autosnapper instead of your real home
distrobox enter fedora -nw
```
In the box you'll need tito
```
sudo dnf install tito
```
Build the spec:
```
tito build --rpm
```
Install the package and check the results:
```
[douglas@fedora ~]$ sudo dnf install /tmp/tito/noarch/dnf5-autosnapper-0.4-1.fc42.noarch.rpm
Updating and loading repositories:
Repositories loaded.
Package                                    Arch        Version                                     Repository                  Size
Installing:
 dnf5-autosnapper                          noarch      0.4-1.fc42                                  @commandline             1.4 KiB
Installing dependencies:
 libdnf5-plugin-actions                    x86_64      5.2.16.0-1.fc42                             updates                269.1 KiB

Transaction Summary:
 Installing:         2 packages

Total size of inbound packages is 170 KiB. Need to download 162 KiB.
After this operation, 270 KiB extra will be used (install 270 KiB, remove 0 B).
Is this ok [y/N]: y
[1/1] libdnf5-plugin-actions-0:5.2.16.0-1.fc42.x86_64                                      100% | 693.4 KiB/s | 161.6 KiB |  00m00s
-----------------------------------------------------------------------------------------------------------------------------------
[1/1] Total                                                                                100% | 468.3 KiB/s | 161.6 KiB |  00m00s
Running transaction
[1/4] Verify package files                                                                 100% |   2.0 KiB/s |   2.0   B |  00m00s
[2/4] Prepare transaction                                                                  100% |  48.0   B/s |   2.0   B |  00m00s
[3/4] Installing libdnf5-plugin-actions-0:5.2.16.0-1.fc42.x86_64                           100% |  38.1 MiB/s | 273.3 KiB |  00m00s
[4/4] Installing dnf5-autosnapper-0:0.4-1.fc42.noarch                                      100% |   8.4 KiB/s |   1.8 KiB |  00m00s
Warning: skipped OpenPGP checks for 1 package from repository: @commandline
Complete!
📦[douglas@fedora ~]$ ls /etc/dnf/libdnf5-plugins/actions.d/
snapper.actions
```
