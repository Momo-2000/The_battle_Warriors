#coding=utf-8 
from flask import Flask, request, render_template, url_for, send_from_directory, redirect,session,json, jsonify
import os
import numpy
import matplotlib.pyplot as plt
import datetime
import random 
from werkzeug import secure_filename
from datetime import timedelta
from glob import glob
import time
import pymysql



def qurry_for_result(sql):
    conn = pymysql.connect(host="47.102.116.56",user ="3DWeb", passwd ="3DWeb",db ="3DWeb",charset ="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 执行完毕返回的结果集默认以元组显示
    res = cursor.execute(sql)
    dict=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return res

def qurry_for_data(sql):
    conn = pymysql.connect(host="47.102.116.56",user ="3DWeb", passwd ="3DWeb",db ="3DWeb",charset ="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 执行完毕返回的结果集默认以元组显示
    res = cursor.execute(sql)
    dict=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return dict

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #限制上传文件大小



@app.before_request
def print_request_info():
    # print(request.path)
    # print("请求方法：" + str(request.method))
    # print("---请求headers--start--")
    # print(str(request.headers).rstrip())
    # print("---请求headers--end----")
    # print("GET参数：" + str(request.args))
    # print("POST参数：" + str(request.form))
    if (request.path=='/reg' or request.path=='/login' or request.path=='/reg.html' or request.path=='/login.html' or request.path.find("/static/")>=0):
       return None
    if session.get("role")==None:
        return redirect('login.html')
    if (request.path.find('/zs')>=0):
        if session.get("role")==1:
            return None
        else:
            return jsonify({'status': '-1', 'msg': '权限不足'})


@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password=  request.form['password']
    res=qurry_for_data("select * from user where username='%s' and password='%s'"%(username,password))
    if len(res)>0:
        session['username'] = username
        session['role'] = res[0]["role"]
        return jsonify({'status': '0', 'msg': '登录成功!'})
    else:
        return jsonify({'status': '-1', 'msg': '账号密码错误'})

@app.route('/reg',methods=['POST'])
def reg():
    username = request.form['username']
    password=  request.form['password']
    phone = request.form['phone']
    res=qurry_for_data("select * from user where username='%s'"%(username))
    if len(res)>0:
        return jsonify({'status': '-1', 'msg': '用户已存在!'})
    else:
        res = qurry_for_result("insert into user (`username`,`password`,`phone`) values ('%s','%s','%s')" % (username,password,phone))
        if res==1:
            return jsonify({'status': '0', 'msg': '注册成功'})
        else:
            return jsonify({'status': '-1', 'msg': '数据库错误，请联系管理员'})

@app.route('/login.html')
def login_html():
    return render_template('login.html')

@app.route('/reg.html')
def reg_html():
    return render_template('reg.html')

@app.route('/')
def test():
    return render_template('test.html')
    
@app.route('/kz')
def kz():
    return render_template('kz.html')
    
@app.route('/fangsuo1')
def fangsuo1():
    return render_template('fangsuo_test.html')
	
@app.route('/fangsuo')
def fangsuo():
    return render_template('fangsuo.html')
	

ALLOWED_OBJS = set(['drc'])
def allowed_upload(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_OBJS
           
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename) 
    
    
@app.route('/zs', methods=['GET', 'POST'])
def zs():
    showObj = []
    length=0
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_upload(file.filename):
            filename = secure_filename(file.filename)
            print(filename.split('.')[-1])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            print(file_url)
        
    files = glob("static/uploads/*.drc")
    files = sorted(files, key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=True)
    length = len(files)
    for f in files:
        a = f.split('\\')[-1]
        showObj.append("../static/uploads/" +a)
    return render_template('zs.html', showObj=showObj, length=length)

ALLOWED_EXTENSIONS = set(['obj', 'off', 'drc', 'txt'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/search1')
def search1():
    return render_template('search_index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        
        file = request.files['file']
        filename = ''
        if file and allowed_file(file.filename):
            filename = file.filename
            filename = filename.rsplit('.', 1)[0]#拿到模型名字
        suanfa = request.values.get("sf")
        print(suanfa)
        itemindex = int(filename[1:])#拿到模型序号
        print(itemindex)
        showObj = []
        showPng = []
        showSim = []
        if suanfa == 'ermianjiao':
            a = numpy.loadtxt('ermianjiao_shrec2015_INDEX.txt')
            showObj.append("../static/SHREC15/T" + str(itemindex) + ".drc")
            feature = numpy.loadtxt('shrec2015_hist_105_3_255_feature.txt')
            similarity = numpy.loadtxt('similarity_ermianjiao.txt')
            x = range(51)
        if suanfa == 'siwks':
            a = numpy.loadtxt('siwks_shrec2010_INDEX.txt')
            showObj.append("../static/Test-database/T" + str(itemindex) + ".drc")
            feature = numpy.loadtxt('Test_SIwks_shrec2010_faeture.txt')
            similarity = numpy.loadtxt('similarity_SIwks.txt')
            x = range(100)
        if suanfa == 'suanfa3':
            a = numpy.loadtxt('shrec2015_geoImage_1024_new_INDEX.txt')
            showObj.append("../static/SHREC15/T" + str(itemindex) + ".drc")
            feature = numpy.loadtxt('mul_feature_1024_new.txt')
            similarity = numpy.loadtxt('similarity_geoImage.txt')
            x = range(1024)
        
        #生成模型特征的png文件
        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")#生成当前时间  
        randomNum=random.randint(0,100)#生成的随机整数n，其中0<=n<=100  
        if randomNum<=10:  
            randomNum=str(0)+str(randomNum)
        uniqueNum=str(nowTime)+str(randomNum)
        
#        feature = numpy.loadtxt('mul_feature_1024_new.txt')
        plt.figure() 
#        x = range(a.shape[1])
        y = feature[itemindex]
        plt.plot(x, y, mfc='w')
        plt.legend()  # 让图例生效
        plt.margins(0)
        plt.subplots_adjust(bottom=0.15)
        name_feature = './static/img/retrieval'+ uniqueNum +'.png'
        showPng.append('.'+name_feature)
        plt.savefig(name_feature)
        print(similarity.shape)
        for i in range(14):#拿到检索结果前14个模型序号，在index文件中，T7模型相似的模型是第8行（a数组下标为7）
            resultindex = int(a[itemindex][i])
            
            showSim.append(round(similarity[itemindex][i+1],3)) 
            if suanfa == 'ermianjiao':
                show = "../static/SHREC15/T" + str(resultindex) + ".drc"
            if suanfa == 'siwks':
                show = "../static/Test-database/T" + str(resultindex) + ".drc"
            if suanfa == 'suanfa3':
                show = "../static/SHREC15/T" + str(resultindex) + ".drc"
            plt.figure()
            #x = range(1024)
            y = feature[resultindex]
            plt.plot(x, y, mfc='w')
            plt.legend()  # 让图例生效
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            name_feature = './static/img/result'+str(i)+ '_' + uniqueNum +'.png'
            showPng.append('.'+name_feature)
            plt.savefig(name_feature)
            showObj.append(show)
        
        print(showSim)
        print(showObj)
        
        return render_template('search-test.html',filename=filename,suanfa=suanfa,showObj=showObj,showPng=showPng,uniqueNum=uniqueNum,showSim=showSim)
    else:
        return 0

@app.route('/fenlei1', methods=['GET'])
def fenlei1():
    if request.method == 'GET':
        cla = request.values.get("class")
        print(cla)
        showObj = []
        length = 0
        if cla:
            files = glob("static/ModelNet10/" +cla+"/test/*.drc")
            # print files
            for f in files:
                a = f.split('\\')[-1]
                print("static/ModelNet10/" +cla+"/test" + a)
                showObj.append("../static/ModelNet10/" +cla+"/test/" +a)
            length = len(showObj)
    return render_template('fenlei_test.html', showObj=showObj, length=length)


@app.route('/del', methods=['GET'])
def delete():
    if request.method == 'GET':
        object = request.values.get("obj")
        print(object)
        showObj = []
        if object:
            os.remove("static/uploads/"+object);
            files = glob("static/uploads/*.drc")
            print(files)
            for f in files:
                a = f.split('\\')[-1]
                showObj.append("../static/uploads/"+a)
                
    return render_template('zs.html', showObj=showObj)

       
        
       

if __name__ == '__main__':
    app.run()
	
