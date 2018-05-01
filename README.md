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

## 部署
线上环境使用supervisord来管理ceelry进程，配置见config/supervisord.conf文件