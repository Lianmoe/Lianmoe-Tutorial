# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '联萌社区教程项目'
#项目名
copyright = '2022, 联萌及所有贡献者'
#社区项目版权当然是属于所有人咯
author = '社区贡献者们'

release = '1.0'
#release 版本
version = '1.0.0'
#版本
# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinx_togglebutton',
    'sphinx_tabs.tabs'
]

myst_enable_extensions = [
    "deflist",
    "colon_fence",
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist"
    ]
    #有的可能会拖慢加载，但我也不知道哪个能派上用场啊喂

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'
#book theme 超好看有没有）
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/Lianmoe/Lianmoe-Tutorial",
    "use_repository_button": True,
    "extra_navbar": "<a rel='license' href='images/CC-BY-NC-SA.png'><img alt='知识共享许可协议' style='border-width:0' src='https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png' /></a>",
    "home_page_in_toc": True,
    "show_navbar_depth": 1,
    "use_edit_page_button": True,
    "use_issues_button": True,
     "announcement": (
        "⚠️部分地区受 CloudFlare 及 运营商 网络"
        "波动影响，加载速度可能较慢，望互相转告⚠️"
        #banner 公告
    ),
}
html_logo = "images/Bookicon.png"#sidebar 上的 Logo
html_favicon = "images/Bookicon.ico"#浏览器页面图标
html_title = "联萌社区教程项目"#Logo 下面显示的项目名
html_last_updated_fmt = ""#自动更新页脚 Last Update 日期

# -- Options for EPUB output
epub_show_urls = 'footnote'
#不知道干什么用的（
