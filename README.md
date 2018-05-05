# lady

## 项目介绍
分布式任务worker端

## 适用以下场景
1. 异步任务
2. 需要分布式

## 开发环境
1. 启动rabbitmq
2. 启动cute项目webapp (因为任务结果通过web api保存)
3. 启动flower监控
```bash
flower --port=9999 --broker="amqp://"
```
4. 启动worker
```bash
celery -A app worker -l info
```

## 线上部署
### worker
1. 创建项目目录，并pull代码
```bash
mkdir -p /data/lady
cd /data/lady
git clone git@gitee.com:looklook/lady.git
```
1. 安装supervisor，配置见config/supervisord.conf文件
```bash
apt-get install -y supervisord-server
```
2. 安装nmap
```bash
apt-get install -y nmap
```
3. 安装项目依赖
```bash
pip2 install -r requrements.txt
```
4. 绑定hosts
```bash
139.199.206.110 cute.leveryd.top
```
5. supervisor重启任务