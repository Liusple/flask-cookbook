第一章将会帮助你去理解不同配置Flask的方法来满足每个项目各式各样的需求。
在这一章，将会涉及到以下方面：
* 用virtualenv搭建环境
* 处理基本的配置
* 基于类的设置
* 静态文件的组织
* 实例文件夹？
* 视图和模型的布置？
* 用蓝本创建一个模块化的web应用
* 使用setuptools使Flask应用可安装

### 介绍
> "Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions."

何为微小？是不是意味着Flask在功能性上有所欠缺或者强制性的只能用一个文件来完成web应用？并不是这样！它说明的事实是Flask目的在于保持核心框架的微小但是高度可扩展。这使得编写应用或者扩展非常的容易和灵活，同时也给了开发者为他们应用选择他们想要配置的余地，没有在数据库，模板引擎和其他方面做出强制性的限制。通过这一章你将会学到一些建立和配置Flask的方法。
开始Flask几乎不需要2分钟。建立一个简单的Hello World应用就和烤派一样简单：
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello to the World of Flask!'

if __name__ == '__main__':
	app.run()
```
现在需要安装Flask，这可以通过pip实现：
```
$ pip install Flask
```
前一小段就是完整的基于Flask的web应用。被导入的Flask类是一个web服务器网关接口(WSGI)应用。所以代码里的app成为了我们的WSGI应用，因为这个一个独立模块，我们用`__name__` 和`'__main__'` 字符串做比较。如果我们将这些保存为名字是app.py的文件，这个应用可以使用下面的命令来运行：

```
$ python app.py 
 * Running on http://127.0.0.1:5000/
```
现在如果在浏览器中输入http:/127.0.0.1:5000/，将会看见程序在运行。

###### Tips
不要将你的文件保存为flask.py，如果你这样做了，将会和导入的Flask冲突。

### 用virtualenv搭建环境
Flask能够通过使用pip或者easy_install进行全局安装，但我们应该使用virtualenv来搭建应用环境。通过为应用创建一个单独的环境可以防止全局Python被自定义的安装影响。单独的环境是有用的，因为你可以有同一个库的多个版本被用于多个应用程序，或者一些包可能有不同版本的相同库作为依赖。virtualenv管理这些在单独的环境里，不会让任何错误版本的库影响到任何其他应用。
##### 怎么做
我们将会使用pip安装virtualenv，然后在我们运行第一个命令的文件里创建一个名为my_flask_env的新的环境。这将会创建一个同样名字的文件夹：
```
$ pip install virtualenv
$ virtualenv my_flask_env
```
现在在my_flask_env文件中，运行以下命令：
```
$ cd my_flask_env
$ source bin/activate
$ pip install flask
```
这将会激活环境并且在其中安装Flask。现在可以在这个环境中对我们的应用做任何事情，而不会影响到任何其他Python环境。
##### 它是如何工作的
直到现在，我们已经使用pip install flask多次了。顾名思义，这个命令安装Flask就像安装其他Python包。如果我们仔细的观察一下通过pip安装Flask的过程，我们将会看到一些包被安装了。下面是Flask包安装过程的一些摘要：
```
$ pip install -U flask
Downloading/unpacking flask
......
......
Many more lines......
......
Successfully installed flask Werkzeug Jinja2 itsdangerous markupsafe
Cleaning up...
```
###### Tips

```
在前面的命令中，-U指的是安装与升级。这将会用最新的版本覆盖已经存在的安装。
```

如果观察的够仔细，总共有五个包被安装了，分别是flask，Werkzeug，Jinja2，itsdangerous，markupsafe。Flask依赖这些包，如果这些包缺失了，Flask将不会工作。
##### 更多
为了更美好的生活，我们可以使用virtualenvwrapper。顾名思义，这是virtualenv的包装，使得处理多个virtualenv更容易。
###### Tips

```
记住应该通过全局的方式安装virtualenvwrapper。所以需要停用还处在激活状态的virtualenv。可以用个下面的命令来停用它：
$ deactivate
同时，你可能因为权限问题不被允许在全局环境安装包。这种情况下切换到超级用户或者使用sudo。
```

可以用个下面的命令来安装virtualenvwrapper：
```
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/workspace
$ source /usr/local/bin/virtualenvwrapper.sh
```
在上面的代码里，我们已经安装了virtualenvwrapper，
！！！！
安装Flask可以使用下面的命令：
```
$ mkvirtualenv flask
$ pip install flask
```
停用虚拟环境，只需运行下面的命令：
```
$ deactivate
```
激活已经存在的使用virtualenvwrapper的virtualenv，可以运行下面的命令：
```
$ workon flask
```
##### 其它
参考和安装链接如下：
* https://pypi.python.org/pypi/virtualenv
* https://pypi.python.org/pypi/virtualenvwrapper
* https://pypi.python.org/pypi/Flask
* https://pypi.python.org/pypi/Werkzeug
* https://pypi.python.org/pypi/Jinja2
* https://pypi.python.org/pypi/itsdangerous
* https://pypi.python.org/pypi/MarkupSafe

### 处理基本配置
首先想到的应该是根据需要去配置Flask应用。这一小节，我们将会去理解Flask不同的配置方法。
##### 准备
在Flask中，配置是用名为config的属性完成的。config属性是字典数据类型的子集，我们能够像字典一样修改它。
##### 怎么做
举个例子，在调试模式下运行我们的程序，需要写出下面这样的代码：
```python
app = Flask(__name__)
app.config['DEBUG'] = True
```
###### Tips

```
debug布尔变量可以从Flask对象而不是config角度来设置：
app.debug = True
同样也可以使用下面这行代码：
app.run(debug=True)
使能调试模将会使服务器在有代码改变的时候重新装载，同时它也在出错的时候提供了非常有用的Werkzeug调试器。
```

Flask还提供了一些配置变量，我们将会在相关的章节接触他们。
当应用越来越大的时候，就产生了在一个文件中管理这些应用配置的需要。在大部分案例中特定于机器基础的设置都不是版本控制系统的一部分。因为这些，Flask提供了多种方式去获取配置。常用的几种是：
* 通过一个pyhton配置文件，使用

  `app.config.from_pyfile('myconfig.cfg')`可以获取到配置

* 通过一个对象，使用 `app.config.from_object('myapplication.default_settings')`

  可以获取到配置。或者也可以使用`app.config.from_object(__name__)`

* 通过环境变量，使用`app.config.from_envvar('PATH_TO_CONFIG_FILE')`

  可以获取到配置
##### 它是如何工作的
Flask足够智能去找到上面例子里我们写的配置变量。同时这也允许我们在配置文件/对象里定义任何本地变量，剩下的就交给Flask。
###### Tips

```
最好的使用配置方式是在app.py里定义一些默认配置，或者通过应用本身的任何对象，然后从配置文件里加载同样的去覆盖它们。所以代码看起来像这样：
app = Flask(__name__)
DEBUG = True
TESTING = True
app.config.from_object(__name__)
app.config.from_pyfile('/path/to/config/file')
```

### 基于类的配置
一种配置诸如生产，测试等不同发布模式的方式是通过使用类继承模式。当项目越来越大，可以有不同的发布模式，比如开发环境，stag，生产等等，每种模式都有一些不同的配置，也会存在一些相同的配置。
##### 怎么做
我们可以拥有一个默认配置基类，其他类可以继承基类也可以覆盖或者增加特定发布环境的配置变量。
下面默认配置基类的例子：
```python
class BaseConfig(object):
	'Base config class'
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'
class ProductionConfig(BaseConfig):
	'Production specific config'
    DEBUG = False
    SECRET_KEY = open('/path/to/secret/file').read()
class StagingConfig(BaseConfig):
	'Staging specific config'
    DEBUG = True
class DevelopmentConfig(BaseConfig):
	'Development environment specific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Another random secret key'
```

###### Tips

```
私密键应该被存储在单独的文件里，因为从安全角度考虑，它不应该是版本控制系统的一部分。应该被保存在机器自身的本地文件系统，或者个人电脑或者服务器。
```

##### 它是如何工作的
现在，当我通过from_object()导入应用配置的时候可以使用任意一个刚才写的类。前提是我们将刚才基于类的配置保存在了名字为configuration.py的文件里：
```
app.config.from_object('configuration.DevelopmentConfig')
```
###静态文件组织
将JavaScript，stylesheets，图像等静态文件高效的组织起来是所有web框架需要考虑的事情。
#####怎么做
Flask推荐一个特定的方式去组织静态文件：
```
my_app/
	- app.py
	- config.py
	- __init__.py
	- static/
		- css/
		- js/
		- images/
			- logo.png
```
当需要在模板中渲染他们的时候（比如logo.png），我们可以通过下面方式使用静态文件：
```
<img src='/static/images/logo.png'>
```
#####它是如何工作的
如果在应用根目录存在一个名字为static的文件夹，就像和app.py在同一层目录，Flask会自动的去读这个文件夹下的内容，而不需要任何其他配置。
##### 其它

与此同时，我们可以在app.py定义应用的时候为应用对象提供一个名为static_folder的参数：

`app=Flask(__name__, static_folder='/path/to/static/folder')`

在它是如何工作一节提到的img src路径中，static指的是这个应用static_url_path的值。可以通过下面方法修改：

```python
app = Flask(
	__name__, static_url_path='/differentstatic',
	static_folder='/path/to/static/folder'
)
```

现在，去获取静态文件，可以使用：

` <img src='/differentstatic/logo.png'>`

###### Tips

```
通常是一个好的方式是使用url_for去创建静态文件URLs，而不是明确的定义他们：
<img src='{{ url_for('static', filename="logo.png") }}'>
将会在下面章节看到更多这样的用法。
```

### 使用实例文件夹进行特定部署



### 使用蓝图创建一个模块化的web应用

蓝图是Flask的一个概念用来帮助大型应用模块化。通过在应用中一个中心位置注册所有的组件来保持应用分离。蓝本看起来像是一个应用对象，但却不是。一个蓝本更像是一个操作集合，能够被注册到应用上，和说明如果构建一个应用。

##### 准备

我们将会利用视图和模型构建一章的应用做为例子，通过使用蓝图修改它，使它正常工作。

##### 怎么做

