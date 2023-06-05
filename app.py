from flask import  Flask,request,render_template

app = Flask(__name__)


class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email








@app.route('/')
def hello_world():
    user=User(username='治疗',email='sss@qq.com')
    user1={
        "username":"zs",
        "email":"qq"
    }
    return render_template("index.html",user=user1)

@app.route('/home')
def profile():
    return '我是个人中心'
#1. debug模式


@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return render_template("blog.html",blog_id=blog_id,username='知了')


@app.route('/book/list')
def booklist():
    page= request.args.get("page",default=1,type=int)
    return f"你获取的是第{page}页书单"




if __name__== '__main__':
    app.run(debug=True)
