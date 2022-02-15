import requests
# 下面url为华为云获取token的接口，这个接口基本一致，需要注意的是“iam.cn-north-4.myhuaweicloud.com”这个需要根据具体需求进行修改，不同区域项目不同
url = "https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens"
# 头部信息
headers = {'Content-Type': 'application/json'}
# json内容，需要上传进行做验证
payload = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                        # name值为你的IAM账号名
                            "name": ,
                            # password值为你的IAM密码
                            "password": ,
                            "domain": {
                            # name值为你的主账号的账号名
                                "name": 
                            }
                        }
                    }
                },
                "scope": {
                    "project": {
                    # name值为你的项目ID
                        "name": 
                    }
                }
            }
        }
# 使用POST上传头部内容和body内容
response = requests.post(url, headers=headers, json=payload)
# 获取token值
token = response.headers['X-Subject-Token']
# 打印token值
print(token)
