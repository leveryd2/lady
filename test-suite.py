# coding:utf-8
import unittest

# 项目放到idc机器上直接运行测试用例:python tests/test_model.py
# 会爆模块路径相关的错误
suite = unittest.TestLoader().discover("tests")
unittest.TextTestRunner(verbosity=2).run(suite)
