% 此页已完成
# 在本地部署文档


在您编辑内容时，可以选择使用本地部署来预览效果。<br>

本篇教程将会告诉您如何在本地部署本项目。

本篇教程仅演示 Windows 环境下的部署。<br>
其他环境下的部署您可以参考 [使用 Sphinx](https://www.sphinx-doc.org/zh_CN/master/usage/index.html) 。


````{note}
本篇属于进阶教程，您不一定需要进行此操作。
````
***
## 克隆 Repo

如果您并不熟悉 Git 的使用方法，我们推荐您使用 [GitHub Desktop](https://desktop.github.com/) 对文件进行管理。

本篇教程就使用 GitHub Desktop 进行演示。<br>

在此之前，您应该先 Fork 我们的仓库。

````{seealso}
您可以在这里查看 [如何 Fork](暂无)
````

在您 Fork 完成之后，您就可以打开您的 GitHub Desktop 软件。  

在您的软件登录 GitHub 账号之后，使用快捷键```CTRL+SHIFT+O```即可打开 Clone a repository 窗口。

在窗口中找到您 Fork 的项目，并在 Local Path 一栏选择您的本地路径。
````{note}
您需要牢记此路径，后续还需要这个路径。
````

完成之后单击 Clone 即可。

***

## 安装本地环境

为了在本地部署本项目，您需要先下载 [Python](https://www.python.org/downloads/windows/) 。

在 Python 的下载页面选择 ```Download Windows installer (64-bit)``` 即可，尽量选择较新版本的进行下载。

````{note}
如果您安装的是 Python3.4 以下版本，您可能还需要手动安装 pip 。
````

安装完成之后，使用 ```Windows 徽标键+X```，选择 ```Windows PowerShell (管理员)```。

在打开的命令行中输入：
```
pip install -U sphinx
```

如果您在中国大陆地区，您也可以使用清华镜像源来加速安装：
```
pip install -U sphinx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

安装完成之后，使用版本查询来检查安装是否成功：
```
sphinx-build --version
```
如果您得到的结果是 ```sphinx-build X.X.X```，即为安装成功。

***

## 构建本地项目并预览

在项目的 ```docs``` 文件夹下，我们为为您提供了一键构建脚本，您只需要双击 ```build.bat``` 即可自动安装前置并构建启动。

您只需要在浏览器中输入 ```127.0.0.1:8000``` 即可访问您的本地构建。

````{note}
在您本地构建时，可能遇到报错、构建失败等问题。<br>
如果您无法解决，您可以复制 cmd 窗口全部内容并尝试联系项目管理员。
````