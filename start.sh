#!/usr/bin/env bash
project_dir = "/data/lady"
# 创建项目目录
mkdir -p $project_dir

# 安装supervisor，配置见config/supervisord.conf文件
# 安装nmap
apt-get update && apt-get install -y python-pip nmap supervisor

# 安装项目依赖
pip2 install -r $project_dir/requrements.txt

# 绑定hosts
echo "139.199.206.110 cute.leveryd.top" >> /etc/hosts

# supervisor重启任务
/usr/bin/supervisord -c $project_dir/config/supervisord.conf