% 此页已完成
# 指引

为了教程的可读性和规范性，请您在编写内容之前通读本页。  

***

## 规范
请确保您使用的是规范的通用语言，避免出现方言词汇等。<br>
对于格式，请您不要使用难以理解的、糟糕的排版逻辑。  

```{seealso}
您可以参考 [中文文案排版指北](https://tutorial.lianmoe.cn/zh_CN/latest/contributing/paiban.html) 。  
```

对于不规范的语言，我们将给您提出修改建议并由您再次进行完善。  

对于文件命名，请使用**有意义**的**英文**文件名。   
错误的例子：<br>

> 原版红石教程.md<br>

正确的示范：<br>

> vanilla-redstone-tutorial.md<br>

如果您不知道对应英文，您也可以使用中文拼音，例如： <br>

> YuanBanHongShi.md<br>

***

## 语法

您在编写内容的过程中可以使用 **Markdown 语法**或 **reStructuredText 语法**，  
当然，您也可以使用 **HTML**。

我们**推荐您使用 Markdown 语法**。

````{tip}
对这三种语言都不了解？您可以尝试[**StackEdit**](https://stackedit.cn/)。  
它可以帮助您像编辑 Word 文档一样编辑 Markdown。
````

[CommonMark syntax specification](https://spec.commonmark.org/) 详细介绍了 Markdown 语法。
在这里，我们列举了部分常用语法：

元素            | 语法
--------------- | -------------------------------------------
标题            | `# H1` to `###### H6`
加粗            | `**bold**`
斜体            | `*italic*`
代码行          | `` `code` ``
可点击的链接    | `<https://www.example.com>`
超链接          | `[title](https://www.example.com)`
图片            | `![alt](https://www.example.com/image.png)`
引用类型链接    | `[title][link]`
被引用链接      | `[link]: https://www.example.com`
分隔线          | `---`
引用            | `> quote`
有序列表        | `1. item`
无序列表        | `- item`
代码块          | 开始 ```` ```lang ````  结束 ```` ``` ````

````{seealso}
由于我们使用了 Myst-parser，所以您可以通过查阅 [特殊语法表](https://tutorial.lianmoe.cn/zh_CN/latest/contributing/extension.html) 来了解部分元素的使用方法。
````

***

## 图片
对于图片，请您上传到**第三方图床**。  

````{tip}
您可以使用 [路过图床](https://imgse.com/) 。
````

***

## 提交内容
您可以通过 GitHub 来提交您编辑的相关内容。  

在您修改之前，请 Fork 本项目。  
在您的仓库内修改完成后提交 Pull Request 即可完成提交。  

***

### 具体步骤
1. 您需要在我们的仓库内选择右上角的 Fork 按钮将我们的库复刻到您的账号下；
2. 您需要在上传您的内容到您复刻之后的仓库的 docs 文件夹当中，并按对应文件夹进行分类；

````{important}
请您一定要按照分类在各文件夹里进行上传，如果您不认为您的内容属于任何一类，请联系项目管理员。
````
3. 上传完成后，您需要在 Pull Request 中填写您的教程的相关信息，如标题、内容概括等；
4. 上述内容完成后提交 Pull Request 即可。

````{seealso}
您也可以查看 [内容提交详细指引](https://tutorial.lianmoe.cn/zh_CN/latest/contributing/pr-guide.html) 获得详细指引。
````
