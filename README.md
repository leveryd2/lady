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
### worker
1. 启动worker
使用腾讯云容器服务，push代码以后自动构建镜像，并重启使用此镜像的服务
2. 启动flower监控
```bash
flower --port=9999 --broker="amqp://rabbituser1:xjifajijiwx@139.199.206.110/"
```
