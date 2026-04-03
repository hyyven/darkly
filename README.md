# Darkly
## Setup
- Open **Virtual Machine Manager**
- File -> Add Connection...
- Hypervisor -> `QEMU/KVM user session` -> Connect
- File -> New Virtual Machine
- Install normally (choose `Ubuntu 24.04 LTS`) and check `Customize configuration before install` -> Finish
- Overview -> XML
- See `setup.xml` for changes
  - Add `xmlns:qemu="http://libvirt.org/schemas/domain/qemu/1.0"` in `<domain>`
  - Remove the entire `<interface>` tag
  - Add the following lines at the end before the closing tag of `<domain>`:
```
  <qemu:commandline>
    <qemu:arg value="-netdev"/>
    <qemu:arg value="user,id=mynet.0,net=10.0.10.0/24,hostfwd=tcp::8080-:80"/>
    <qemu:arg value="-device"/>
    <qemu:arg value="rtl8139,netdev=mynet.0"/>
  </qemu:commandline>
```
    
- Boot options -> Details -> Check ONLY `SATA CDROM 1` -> Apply -> Begin Installation
- Open a browser and access `127.0.0.1:8080`

## Notes
CHECK ROBOTS.TXT
