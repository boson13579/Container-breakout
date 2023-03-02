# Dirty Pipe (CVE-2022-0847)

- imapct
    - write thing into file that with read permission but write
    - some limitation
        - the offset must not be on a page boundary (because at least one byte of that page must have been spliced into the pipe)
        - the write cannot cross a page boundary (because a new anonymous buffer would be created for the rest)
        - the file cannot be resized (because the pipe has its own page fill management and does not tell the page cache how much data has been appended)

- linux kernel version
    - below : 5.16.11 5.15.25 5.10.102 (not include)

- action
    - (on host)
    - docker cp write 96f7f14e99ab2:/
    - (in container)
    - /write /etc/shells 1 $'\nHello World\n'
    
    
- write.c compile command
    - gcc write.c -o write

- reference
    - https://dirtypipe.cm4all.com/