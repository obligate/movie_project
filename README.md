## 前台布局搭建
+ 静态文件引入 {{ url_for('static',filename='文件路径')}}
+ 定义路由 {{ url_for('模块名.视图名',变量=参数)}}
+ 定义数据块 {% block 数据块名称 %} ... {% endblock %}



## Refer
[flask-sqlalchemy 分页](http://www.pythondoc.com/flask-sqlalchemy/api.html#id4)

## QA
+ 1.新版本会遇到这样的问题，到flask_sqlalchemy的__init__.py里面修改init_app方法，修改下面的一行： track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True) 然后保存，重新运行程序
+ 2.{"useexisting": True}
```
sqlalchemy.exc.InvalidRequestError: Table 'comment' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
```
解决方案: 为所有的models添加__table_args__ = {"useexisting": True}
+ 引入models中的模型时没有采用全量路径，而是采用了很短的路径
```
sqlalchemy.exc.InvalidRequestError: Multiple classes found for path "Userlog" in the registry of this declarative base. Please use a fully module-qualified path.
```
解决方案： `from models import Admin# 改为from app.models import Admin`