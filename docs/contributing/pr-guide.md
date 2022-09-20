% 此页已完成
# 内容提交详细指引



````{important}
此页图片较多，如果图片过小看不清，<br>
您可以右键**图片**选择**在新标签页中打开图片**后放大即可。
````

本篇教程将会以 GitHub 新手的视角详细介绍从 Fork 本项目到 Pull Request 提交完成的全部过程。

***

## Fork 本项目
在我们的 [GitHub 项目](https://github.com/Lianmoe/Lianmoe-Tutorial) 的页面右上角，一共有三个按钮。
[![xCRrU1.png](https://s1.ax1x.com/2022/09/20/xCRrU1.png)](https://imgse.com/i/xCRrU1)

这三个按钮依次是
- ```Watch``` 此按钮用来决定是否接收该项目的动态。
- ```Fork``` 此按钮是用来复刻我们的库到您的个人账号下的按钮，也是我们要用到的。
- ```Star``` 此按钮类似点赞功能，**记得给我们的项目点个 Star**~

在您点击完 ```Fork``` 按钮之后，就会跳转到对您的复刻后的项目的设置。

[![xCH7wT.png](https://s1.ax1x.com/2022/09/20/xCH7wT.png)](https://imgse.com/i/xCH7wT)

````{tip}
如果您没有特殊设置的需求或者完全不知道这步是用来干什么的，<br>
您就可以直接点击 ```Create Fork```。
````

***

## 上传您的修改

在 Fork 完成之后，您会跳转到您的复刻后的仓库。

在仓库中，您**只需要**修改 ```docs``` 文件夹下的内容。

````{important}
对于其他文件，请您**不要做任何修改**，否则我们可能不会通过您提交的内容。
````

[![xCbBh4.png](https://s1.ax1x.com/2022/09/20/xCbBh4.png)](https://imgse.com/i/xCbBh4)

单击 ```docs``` 进入 docs 目录，按文件夹分类上传您的内容。

下面这张表格简单介绍了各目录的分类情况：
目录  |  内容
----- |  -----
```contributing``` | 社区共建指南部分
```images``` | 前端图片部分，请您不要将图片上传至此文件夹
```tutorial``` | 教程内容部分
```tutorial / rumen``` | 入门教程部分
```tutorial / jinjie``` | 进阶教程部分

````{important}
如果您认为您的内容不属于任何一类，请您联系项目管理员。
````

进入对应文件夹后，您就可以上传您的相关内容了。

[![xCqYPe.png](https://s1.ax1x.com/2022/09/20/xCqYPe.png)](https://imgse.com/i/xCqYPe)

找到 ```Add file -> Upload files``` 

[![xCqwrt.png](https://s1.ax1x.com/2022/09/20/xCqwrt.png)](https://imgse.com/i/xCqwrt)

单击 ```choose your files``` 然后在弹出窗口中找到您要上传的文件。<br>

然后在 ```Commit changes``` 下方
第一个个框填写**相对于 docs 文件夹**的路径及文件名，<br>
第二个框中填写**标题及简介** (可选)。

示例如下图：

[![xCqXs1.png](https://s1.ax1x.com/2022/09/20/xCqXs1.png)](https://imgse.com/i/xCqXs1)

完成后单击 ```Commit changes``` 即可。

回到您的复刻项目首页，在中间部分看到 ```This branch is X commit ahead of Lianmoe:master.``` 即代表您的内容上传成功。

***

## 提交您的内容
在您的复刻项目首页的中间部分，找到 ```Contribute```，点击右侧小三角展开后点击 ```Open pull request```。

[![xCvbuj.png](https://s1.ax1x.com/2022/09/20/xCvbuj.png)](https://imgse.com/i/xCvbuj)

在新页面中您需要注意以下内容：
- 在标题处填写您的内容的标题（多个用中文顿号隔开）；
- 在描述中添加内容标题、简介（多个内容分开写）及作者 ID（留空使用 GitHub 用户名）；
- 请不要取消勾选 ```Allow edits by maintainers``` 项，这项可以让我们帮助您完善您的内容。

完成后点击 ```Create pull request``` 即可提交。<br>
示例：

[![xCvv5V.png](https://s1.ax1x.com/2022/09/20/xCvv5V.png)](https://imgse.com/i/xCvv5V)

***

## 完成及后续

[![xCxFbR.png](https://s1.ax1x.com/2022/09/20/xCxFbR.png)](https://imgse.com/i/xCxFbR)

出现这样的界面即为提交完成。

提交完成之后您只需要等待项目管理员处理即可。

后续如果您的内容存在一些问题，项目管理员会积极与您沟通、修改直至达到 Merge（可以理解为通过）标准。

**请您定期查看您的 PR 的状态，我们会在收到 PR 的第一时间查看您的内容并作出处理。**

```{tip}
我们强烈建议您加入我们的 [KOOK 频道](https://kook.top/wtPZIy)，有问题我们可以第一时间通知您，并且可以进行即时沟通。
```
