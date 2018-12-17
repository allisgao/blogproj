# blogproj
a blog based on django(1.11.12, with python3.6)

# 项目背景
托管在腾讯云主机上的基于wordpress的博客系统所在机器受到攻击，成为肉鸡，导致博客系统无法使用。
在备份完数据后，重新部署了操作系统。鉴于此，决定运用自己所学，从头开始写一个博客系统。
演示地址：http://blogtest.cloxk.com/

# 项目概况
## 环境信息
### 开发环境
Win10 + python3.6 + django1.11.12 + mysql5.7.21，pycharm2018
django目前最新版本是2.+，最新LTS版本是1.11.x。django2版本的于2019年4月会有一版LTS。
根据调查，1.11.x版本的是目前使用量比较广的版本，兼容性也很好。1.11.x目前最新版本是1.11.17。
之所以选择1.11.12，这个比较新的LTS版本，是从如下角度考虑的：
* 相对于之前的版本，更稳定；
* 可以继续向后升级。

### 测试环境
VirtualBox + CentOS7.4 + python3.6 + mysql5.7.21

### 线上环境
腾讯云 + CentOS7.4 + python3.6 + mysql5.7.24

# 项目说明（待完善）
目录结构
~~~
├─blog
│  ├─migrations
│  ├─static
│  │  └─blog
│  │      ├─css
│  │      │  └─highlights
│  │      └─js
│  ├─templatetags
├─blogproj
├─comments
│  ├─migrations
└─templates
    └─blog
~~~

## 博客架构设计及实现
### 数据库设计
数据库
### python环境
采用Virtual-Environment，保证与本机的其他环境独立

## 博客的编码实现


## 博客的部署

## 博客使用介绍
### 访客
访客访问博客主页，在主页选择文章阅读，或从侧边栏过滤，选择感兴趣的内容。
### 管理员
管理员可以在后台添加文章、修改文章、统计访问量和评论。


# 附录
## 待添加功能
### 分页
#### 分页部分添加手工指定页面跳转
#### 可自定义每页显示的数量
## Bugs/待解决问题
## FAQ

## 参考资料
* django官方文档：https://docs.djangoproject.com/en/1.11/
* 追梦任务的博客：https://www.zmrenwu.com/
* python核心编程（第三版）
