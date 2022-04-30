# JWT认证

## 1. JWT & JWS & JWE

### Json Web Token(JWT)

JSON Web Token（JWT）是一个非常轻巧的规范。这个规范允许我们使用JWT在两个组织之间传递安全可靠的信息。

> 官方定义:JSON Web Token (JWT) is a compact URL-safe means of representing claims to be transferred between two parties



![img](images/jwt.png)

现在网上大多数介绍JWT的文章实际介绍的都是JWS(JSON Web Signature),也往往导致了人们对于JWT的误解，但是JWT并不等于JWS，JWS只是JWT的一种实现，除了JWS外，JWE(JSON Web Encryption)也是JWT的一种实现。

 下面就来详细介绍一下JWT与JWE的两种实现方式：



![img](images/jwt&jws&jwe.png)

### JSON Web Signature(JWS)

JSON Web Signature是一个有着简单的统一表达形式的字符串：



![img](images/jws.png)

##### 头部（Header）

头部用于描述关于该JWT的最基本的信息，例如其类型以及签名所用的算法等。
 JSON内容要经Base64 编码生成字符串成为Header。

##### 载荷（PayLoad）

payload的五个字段都是由JWT的标准所定义的。

1. iss: 该JWT的签发者
2. sub: 该JWT所面向的用户
3. aud: 接收该JWT的一方
4. **exp(expires): 什么时候过期，这里是一个Unix时间戳**
5. iat(issued at): 在什么时候签发的

后面的信息可以按需补充。
 JSON内容要经Base64 编码生成字符串成为PayLoad。

##### 签名（signature）

这个部分header与payload通过header中声明的加密方式，使用密钥secret进行加密，生成签名。
 JWS的主要目的是保证了数据在传输过程中不被修改，验证数据的完整性。但由于仅采用Base64对消息内容编码，因此不保证数据的不可泄露性。所以不适合用于传输敏感数据。

### JSON Web Encryption(JWE)

相对于JWS，JWE则同时保证了安全性与数据完整性。
 JWE由五部分组成：

![img](images/jwe.png)

JWE组成

具体生成步骤为：

1. JOSE含义与JWS头部相同。
2. 生成一个随机的Content Encryption Key （CEK）。
3. 使用RSAES-OAEP 加密算法，用公钥加密CEK，生成JWE Encrypted Key。
4. 生成JWE初始化向量。
5. 使用AES GCM加密算法对明文部分进行加密生成密文Ciphertext,算法会随之生成一个128位的认证标记Authentication Tag。
    6.对五个部分分别进行base64编码。

可见，JWE的计算过程相对繁琐，不够轻量级，因此适合与数据传输而非token认证，但该协议也足够安全可靠，用简短字符串描述了传输内容，兼顾数据的安全性与完整性。

## 2. 独立的JWT Python库

* itsdangerous

  * JSONWebSignatureSerializer
  * TimedJSONWebSignatureSerializer  （可设置有效期）

* pyjwt

  <https://pyjwt.readthedocs.io/en/latest/>

  ### 安装

	```shell
	$ pip install pyjwt
	```
	
	### 用例
	
	```python
	>>> import jwt
	
	>>> encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
	>>> encoded_jwt
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'
	
	>>> jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
	{'some': 'payload'}
	```

## 3. 头条项目的实施方案

设置有效期，但有效期不宜过长，需要刷新。

如何解决刷新问题？

* 手机号+验证码（或帐号+密码）验证后颁发接口调用token与refresh_token（刷新token）

* Token 有效期为2小时，在调用接口时携带，每2小时刷新一次 
* 提供refresh_token，refresh_token 有效期14天 
*  在接口调用token过期后凭借refresh_token 获取新token

* 未携带token 、错误的token或接口调用token过期，返回401状态码

* refresh_token 过期返回403状态码，前端在使用refresh_token请求新token时遇到403状态码则进入用户登录界面从新认证。

* token的携带方式是在请求头中使用如下格式：

  ```http
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
  ```

  注意：Bearer前缀与token中间有一个空格

## 4. 代码实现

* token生成
* 中间件验证
* token刷新
* 装饰器强制

## 5. 扩展-token禁用问题

token颁发给用户后，在有效期内服务端都会认可，但是如果在token的有效期内需要让token失效，该怎么办？

此问题的应用场景：

* 用户修改密码，需要颁发新的token，禁用还在有效期内的老token
* 后台封禁用户

解决方案：

在redis中使用set类型保存新生成的token

```python
key = 'user:{}:token'.format(user_id)
pl = redis_client.pipeline()
pl.sadd(key, new_token)
pl.expire(key, token有效期)
pl.execute()
```

| 键                   | 类型 | 值      |
| -------------------- | ---- | ------- |
| user:{user_id}:token | set  | 新token |

客户端使用token进行请求时，如果验证token通过，则从redis中判断是否存在该用户的user:{}:token记录：

* 若不存在记录，放行，进入视图进行业务处理

* 若存在，则对比本次请求的token是否在redis保存的set中：

  * 若存在，则放行
  * 若不在set的数值中，则返回403状态码，不再处理业务逻辑

```python
key = 'user:{}:token'.format(user_id)
valid_tokens = redis_client.smembers(key, token)
if valid_tokens and token not in valid_tokens:
  return {'message': 'Invalid token'.}, 403
```

##### 说明：

1. redis记录设置有效期的时长是一个token的有效期，保证旧token过期后，redis的记录也能自动清除，不占用空间。

2. 使用set保存新token的原因是，考虑到用户可能在旧token的有效期内，在其他多个设备进行了登录，需要生成多个新token，这些新token都要保存下来，既保证新token都能正常登录，又能保证旧token被禁用



