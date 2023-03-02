# rollback ubuntu kernel version

- check kernel version
    - uname -r

- install example (linux 5.15.20)

    - download package
    - https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.15.20/
        - amd64/linux-headers-5.15.20-051520-generic_5.15.20-051520.202202050734_amd64.deb
        - amd64/linux-headers-5.15.20-051520_5.15.20-051520.202202050734_all.deb
        - amd64/linux-image-unsigned-5.15.20-051520-generic_5.15.20-051520.202202050734_amd64.deb
        - amd64/linux-modules-5.15.20-051520-generic_5.15.20-051520.202202050734_amd64.deb 
    - sudo dpkg -i *.deb

    - reboot(if can't press esc when open reboot and enter GURB and select advanced Ubuntu and select correct kernel verison)