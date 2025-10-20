# dnf5-autosnapper
A dnf5 plugin that automatically creates snapper btrfs snapshots

## Recommended dev environment
To avoid cluttering my actual fedora install with packages and files, I develop the package like this:
```
distrobox create --name fedora -i fedora:42 -H ~/dnf5-autosnapper
# rpmbuild runs in ~/dnf5-autosnapper instead of your real home
distrobox enter fedora -nw
```
In the box you'll need rpmbuild
```
sudo dnf install rpmbuild
```
Build the spec:
```
rpmbuild -ba SPECS/dnf5-autosnapper.spec
```
Install the package and check the results:
```
📦[douglas@fedora rpmbuild]$ cd RPMS/noarch/
📦[douglas@fedora noarch]$ sudo dnf install dnf5-autosnapper-0.1-1.fc42.noarch.rpm 
Updating and loading repositories:
Repositories loaded.
Package                         Arch     Version                          Repository              Size
Reinstalling:
 dnf5-autosnapper               noarch   0.1-1.fc42                       @commandline         1.4 KiB
   replacing dnf5-autosnapper   src      0.1-1.fc42                       @commandline         1.4 KiB
Installing dependencies:
 libdnf5-plugin-actions         x86_64   5.2.16.0-1.fc42                  updates            269.1 KiB

Transaction Summary:
 Installing:         1 package
 Reinstalling:       1 package
 Replacing:          1 package

Total size of inbound packages is 169 KiB. Need to download 162 KiB.
After this operation, 269 KiB extra will be used (install 270 KiB, remove 1 KiB).
Is this ok [y/N]: y
[1/1] libdnf5-plugin-actions-0:5.2.16.0-1.fc42.x86_64         100% |   1.3 MiB/s | 161.6 KiB |  00m00s
------------------------------------------------------------------------------------------------------
[1/1] Total                                                   100% | 690.4 KiB/s | 161.6 KiB |  00m00s
Running transaction
[1/5] Verify package files                                    100% |   0.0   B/s |   2.0   B |  00m00s
[2/5] Prepare transaction                                     100% | 142.0   B/s |   3.0   B |  00m00s
[3/5] Installing libdnf5-plugin-actions-0:5.2.16.0-1.fc42.x86 100% |  20.5 MiB/s | 273.3 KiB |  00m00s
[4/5] Reinstalling dnf5-autosnapper-0:0.1-1.fc42.noarch       100% | 898.4 KiB/s |   1.8 KiB |  00m00s
[5/5] Removing dnf5-autosnapper-0:0.1-1.fc42.src              100% |  11.0   B/s |   2.0   B |  00m00s
Warning: skipped OpenPGP checks for 1 package from repository: @commandline
Complete!
📦[douglas@fedora noarch]$ ls /etc/dnf/libdnf5-plugins/actions.d/
snapper.conf
```
