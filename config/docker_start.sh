#!/usr/bin/env bash
# 绑定hosts
echo "139.199.206.110 cute.leveryd.top" >> /etc/hosts

# supervisor重启任务
/usr/bin/supervisord -c /data/lady/config/supervisord.conf

# 满足docker
/usr/bin/tail -f /dev/null