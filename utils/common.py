# coding:utf-8
import requests
import socket
import getpass
import datetime
import uuid
import json
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from config.main import *


class CuteApi(object):
    host = host

    @staticmethod
    def _convert_dict(dict_input):
        """
        字典转换成url参数
        :param dict_input:
        :return:
        """
        templist = []
        if not isinstance(dict_input, dict):
            raise ValueError("not a dict", dict_input)
        for key in dict_input:
            value = dict_input[key]
            if isinstance(value, unicode):
                value = value.encode("utf-8")
            tempstr = "{0}={1}".format(key, value)
            templist.append(tempstr)
        return "&".join(templist)

    def post(self, uri, params):
        url = "%s%s" % (self.host, uri)
        ret = requests.post(url, json=params, verify=False)
        return ret

    def get(self, uri, params):
        """
        查询操作
        :param uri:
        :param params:
        :return:
        """
        params = self._convert_dict(params)
        url = "%s%s?%s" % (self.host, uri, params)
        ret = requests.get(url, verify=False)
        jsondata = json.loads(ret.text)
        return jsondata["rows"]

    def get_rootdomain_info(self):
        """
        从兄弟域名表中获取所有的根域名、公司名、子公司名,去重后返回
        :return:
        """
        ret_rootdomain_list = []
        rows = self.get("/api/info/brotherdomain/query", {})
        for row in rows:
            ret_rootdomain_list.append((row["rootdomain"], row["corpname"], row["subcorpname"]))
        return list(set(ret_rootdomain_list))

    def save_exception_message(self, message):
        params = {
            "message": message,
            "owner": get_owner(),
        }
        self.post("/api/info/exceptionmessage/add", params)

    def is_items_exists_in_table(self, tablename, prikey, value):
        prikey = convert_utf8(prikey)
        value = convert_utf8(value)
        params = {
            prikey: value,
            "fuzzyquery": 0
        }
        url = "/api/info/%s/query" % tablename
        rows = self.get(url, params)
        if len(rows) > 0:
            return True
        return False

    def get_assets_corpinfo(self):
        params = {}
        return self.get("/api/assets/corp/query", params)

    def get_info_subdomain(self):
        params = {}
        return self.get("/api/info/subdomain/query", params)


def get_owner():
    hostname = socket.gethostname()
    username = getpass.getuser()
    return "%s-%s" % (hostname, username)


def now(formatstr="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(formatstr)


def randomuid():
    return str(uuid.uuid1())


def convert_utf8(inputstr):
    if isinstance(inputstr, unicode):
        inputstr = inputstr.encode("utf-8")
    return inputstr


def get_dnsserver_list_from_config():
    dns_server_list = []
    for key in dns_server:
        dns_server_list.append(dns_server[key])
    dns_server_list = list(set(dns_server_list))
    return dns_server_list


def mysleep(condition):
    """
    上一次计划任务开启的扫描进程若还没有结束，则休眠等它结束
    :param condition:
    :return:
    """
    # ps aux|grep -i hostscan|grep -i '/home/work/scan/scanlog/StandardScan/'|grep -v grep|wc -l
    sleepflag = True
    while sleepflag:
        with os.popen(condition) as f:
            num = f.read()
            if int(num.strip('\n')) == 1:
                sleepflag = False
            else:
                time.sleep(5 * 60)


class Email(object):
    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def sendmail(self, title, message):
        if isinstance(title, str):
            title = title.decode("utf-8")

        msg = MIMEText(message, 'html', 'utf-8')
        msg['From'] = self._format_addr(u'<%s>' % from_addr)
        msg['To'] = self._format_addr(u'<%s>' % to_addr)
        msg['Subject'] = Header(title, 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr.split(","), msg.as_string())
        server.quit()
