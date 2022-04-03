Conda 使用

conda 创建环境
```shell
conda create -n [环境名称] python=[2.7|3.6]
```

conda 删除环境
```shell
conda remove -n [环境名称] --all
```

列出当前环境所有包
```shell
conda list
```

列出所有环境
```shell
conda env list
```

根据 yaml 创建
```shell
conda env create -n ${env_name} -f ./environment.yaml
```
