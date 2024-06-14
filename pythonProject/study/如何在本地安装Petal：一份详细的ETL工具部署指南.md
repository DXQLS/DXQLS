# 如何在本地安装Petal：一份详细的ETL工具部署指南

## 引言

在企业中处理数据时，经常需要执行ETL（Extract, Transform, Load）流程。Petal是脉策科技后端开发的一个ETL工具，能够帮助我们高效地完成这一任务。本文将指引你如何在本地从零开始安装Petal，即使你是一个0基础小白也能轻松上手。

## 准备工作

### 第一步：配置Python环境

首先，我们需要确保本地安装有Python环境。推荐使用Anaconda来配置Python环境，因为它包含了数据科学所需的前沿工具和库。

Anaconda安装及配置教程请参考：[Python环境配置与系统变量设置](https://blog.csdn.net/qq_51872445/article/details/130023351)。

### 第二步：安装Python开发工具

为了方便进行开发和测试Petal是否安装成功，我们将使用Pycharm作为开发环境。

Pycharm安装教程请参考：[如何使用Conda环境](https://blog.csdn.net/Little_Carter/article/details/131031595)。文中也介绍了如何创建和使用虚拟环境，并更改conda的镜像源。

### 第三步：设置镜像源

由于我们要安装的一些库可能在国内下载较慢，这里我们使用国内镜像来提高安装速度。

1. **设置pip镜像**

    在用户文件夹（如：C:\Users\Administrator）下新建一个名为`pip`的文件夹，并在该文件夹中创建一个文本文件。将下面的代码复制进去，并将文件重命名为`pip.ini`。

    ```
    [global]
    index-url = https://pypi.douban.com/simple
    [install]
    trusted-host=pypi.douban.com
    timeout = 150
    ```

2. **设置conda镜像**

    在用户文件夹下新建一个文本文件，复制下方代码，将其重命名为`.condarc`。若已存在，则在原文件中替换以下内容。

    ```
    channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
    - https://nexus.idatatlas.com/repository/python-mdt/simple
    show_channel_urls: true
    always_yes: true
    ssl_verify: true
    ```

## 安装步骤

### 第一步：创建虚拟环境

如果Pycharm教程中你已经学会了如何创建虚拟环境，那么你可以跳过这一步。

否则，请将以下准备好的环境配置保存为`environment.yml`文件至用户文件夹下：

```yml
name: geopandas-dev
channels:
  - 以上相同的镜像源
dependencies:
  - python==3.8.2
  - 以上列出的依赖库
```

然后在Anaconda Powershell Prompt中执行下述命令来新建虚拟环境：

```shell
conda create -n 环境名 python=3.7.6 
```

接着，激活刚才创建的虚拟环境：

```shell
activate 环境名
```

### 第二步：在Pycharm中配置虚拟环境

打开Pycharm，按照指引`File -> Settings -> Project:pythonProject -> Python interpreter -> Add interpreter -> Add local interpreter -> Existing environment -> 选择你的虚拟环境路径 -> OK`，来设置虚拟环境。

之后，打开Pycharm的Terminal终端，输入以下命令，确保你在刚才创建的虚拟环境中：

```shell
activate 环境名
```

### 第三步：安装Petal所需的库

为了保证Petal的顺利运行，我们需要安装其依赖的库。在项目的根目录下创建一个`requirements.txt`文本文件，列出所有需要的库：(这里我会给一个文件)

```
# 这里放置Petal所需要的具体依赖库名称和版本
例如：
requests==2.25.1
Django==3.1.7
... 更多依赖项
```

在刚才打开的终端中，运行以下命令来安装所需的库：

```shell
pip install -r requirements.txt
```

### 第四步：验证Petal安装

为了确认Petal是否成功安装，我们将创建一个简单的Petal任务进行测试。

新建一个python文件，你可以将其命名为`petal_helloworld.py`或根据你的喜好来命名，然后添加以下内容并保存：

```python
from petal import Task

class HelloWorld(Task):
    """你的第一个Petal Task"""
    def run(self):
        (
            self
            .new_etl()
            .from_dict({
                'name': ['Tom', 'Lucy'],
                'age': [16, 18]
            })
            .to_console(pretty=True)
        )
```

确保命令行与该文件位于同一目录下，执行以下命令：

```shell
petal petal_helloworld.HelloWorld -e dev
```

如果命令行输出了如下内容，则说明Petal安装成功：

```
name  age
------  -----
Tom    16
Lucy   18
```

恭喜你！你已经成功安装了Petal，并运行了你的第一个Petal Task。现在你可以开始使用这个强大的ETL工具来进行数据处理了。

## 第五步：查阅官方文档

安装完成后，可以在 Petal 的官方文档中找到详细的安装说明和用法。请访问以下链接了解更多信息：
[Petal 官方文档](https://doc.idatatlas.com/petal/tutorial.html)
现在你已经成功安装了 Petal，可以开始在你的项目中使用它了。祝你学习愉快！

