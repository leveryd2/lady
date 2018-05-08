# lady

## 项目介绍
分布式任务worker端

## 适用以下场景
1. 异步任务
2. 需要分布式处理任务

## 开发环境
1. 启动rabbitmq
2. 启动cute项目webapp (因为任务结果通过web api保存)
3. 启动worker
```bash
celery -A app worker -l info
```
4. 启动flower监控
```bash
flower --port=9999 --broker="amqp://"
```

## 线上部署
### 腾讯云容器部署
只需要push代码，云上会自动构建镜像，并重启使用此镜像的服务

### 虚机部署
运行start.sh脚本

## 监控 && 管理
1. flower监控web页面
本地启动flower
```bash
flower --port=9999 --broker="amqp://rabbituser1:xjifajijiwx@139.199.206.110/"
```

```bash
http://139.199.206.110:9999/
```

2. rabbitmq监控web页面
```bash
http://139.199.206.110:15672/#/
```
3. 管理集群服务
```bash
登陆https://console.cloud.tencent.com/ccs/service
账号密码因为安全原因另外使用文档记录
```