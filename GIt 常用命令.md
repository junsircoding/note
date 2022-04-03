Git 常用命令

### 合并单个文件
把 v_juunwang_pro 分支的 file.py 文件合并到 dev 分支
```shell
git checkout dev
git checkout --patch v_juunwang_pro file.py
```

### 配置免输密码
```shell
# commit, push 均免输密码
git config --global credential.helper store
```

### 创建一个新分支并且直接切换到该分支
```shell
git checkout -b newBranch
```

### 完全覆盖当前分支
将 dataplatform 分支完全覆盖 v_juunwang 分支

```shell
# 保证本地的 v_juunwang 和 dataplatform 分支均和远程保持一致

git checkout dataplatform
git pull

git checkout v_juunwang
git pull

# 本地 dataplatform 分支完全覆盖本地 v_juunwang 分支
git reset --hard origin/dataplatform

# 将本地 v_juunwang 分支强行推到远程 v_juunwang 分支
git push -f
```

git 的每一次 commit 都有一个 parent，就是相对于它的上一次 commit。
git 的 branch 其实就是指向 commit 的指针。
所谓 merge 其实是一个特殊的 commit，这个 commit 有两个指针，分别指向当前分支和 master 分支。

### 开发标准流程

开发全程在 v_juunwang 分支，在此分支调试完毕之后合并入 dataplatform 分支

```python
# 初始化，保证两个分支均和远程保持一致
git checkout dataplatform
git pull
git checkout v_juunwang
git pull

# 开发调试完毕

git add .
git commit -m 'msg'
git push

# 同步 dataplatform
git checkout dataplatform
git pull

# 将 v_juunwang 合并到 dataplatform
git merge v_juunwang
git push

# 最后保证分支回到 v_juunwang
git checkout v_juunwang
```
