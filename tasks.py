# coding:utf-8
import json
from IPy import IP

from libnmap.parser import NmapParser
from libnmap.process import NmapProcess

from app import app
from utils.common import CuteApi
from config.celery import global_options, global_log_states


@app.task
def collect_service_info(jsondata):
    """
    >>> collect_service_info('{"target":"127.0.0.1"}')

    扫描主机获取服务信息后通过HTTP API入库
    :param jsondata:
    :return:
    """
    ret = []
    jsondata = json.loads(jsondata)
    target = jsondata.get("target", "")
    options = jsondata.get("options", global_options)
    log_states = jsondata.get("log_states", global_log_states)

    # 忽略内网IP
    ip = IP(target)
    if ip.iptype() == "PRIVATE":
        return "内网IP"
    if target.strip() == "":
        return "无IP"

    nmap_proc = NmapProcess(targets=str(target), options=options, safe_mode=False)
    nmap_proc.sudo_run_background()  # nmap -O 参数需要root权限

    while nmap_proc.is_running():
        pass
    if nmap_proc.is_successful():
        nmap_report = NmapParser.parse(nmap_proc.stdout)
        # 开始处理扫描结果
        for host in nmap_report.hosts:
            # 处理主机开放的服务和端口
            for serv in host.services:
                serv.address = host.address
                serv.endtime = host.endtime
                if serv.state in log_states:
                    service = dict()
                    service['address'] = serv.address
                    service['port'] = serv.port
                    service['service'] = serv.service
                    service['state'] = serv.state
                    service['protocol'] = serv.protocol
                    service['product'] = serv.product if "product" in dir(serv) else None
                    service['product_version'] = serv.product_version if "product_version" in dir(serv) else None
                    service['product_extrainfo'] = serv.product_extrainfo if "product_extrainfo" in dir(serv) else None

                    # HTTP API保存到远端服务器
                    CuteApi().post("/api/info/hostserviceinfo/add", service)
                    ret.append(service)
    return json.dumps(ret)
