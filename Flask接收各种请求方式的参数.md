对于 Flask POST 请求，Content-Type 用于指定资源的 MIME 类型。

1. application/json

**请求报文格式**

```
POST /login HTTP/1.1
Host: 127.0.0.1:30381
Content-Type: application/json
Content-Length: 59

{
    "user": "Mike",
    "password": "123456"
}
```

**curl 命令**

```shell
curl -H 'Content-Type: application/json' -d \
'{
    "user": "Mike",
    "password":"123456"
}' \
127.0.0.1:30381/login
```

2. application/x-www-form-urlencoded

**请求报文格式**

```
POST /login1 HTTP/1.1
Host: 127.0.0.1:30381
Content-Type: application/x-www-form-urlencoded
Content-Length: 38

user=Mike&password=123456
```

**curl 命令**

```shell
curl --data-urlencode 'user=Mike' --data-urlencode 'password=123456' 127.0.0.1:30381/login1
```

3. multipart/form-data

**请求报文格式**

```
curl --location --request POST '127.0.0.1:30381/login2' \
--form 'user="Mike"' \
--form 'password="123456"'
```

**curl 命令**

```shell
curl --location --request POST '127.0.0.1:30381/login2'\
--form 'user="Mike"' \
--form 'password="123456"'
```

4. text/plain

**请求报文格式**

```
POST /login3 HTTP/1.1
Host: 127.0.0.1:30381
Content-Type: text/plain
Content-Length: 59

{
    "user": "Mike",
    "password":"123456"
}
```

**curl 命令**

```shell
curl -H 'Content-Type: text/plain' --data \
'{
    "user": "Mike",
    "password":"123456"
}' \
127.0.0.1:30381/login3
```