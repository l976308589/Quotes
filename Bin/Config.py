# 配置账号信息
account = 'TEST001'

# 配置发布方式
publish = 0  # 0是打印;1是redis;2是socket;3是file

# 配置发布信息
# 如果publish==1,需要配置redis
redis = {'host': 'localhost',
         'port': 6379,
         'db': 0,
         'password': None
         }
# 如果publish==2,需要配置socket
socket = {'ip': '127.0.0.1',
          'port': 8080}
