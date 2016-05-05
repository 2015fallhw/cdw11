# coding: utf-8
from flask import Flask, send_from_directory, request, redirect, render_template, session, make_response
import random
import math
import os
# init.py 為自行建立的起始物件
import init

import users.a.g10.ag10_40323139
import users.a.g4.ag4_40323138
import users.a.g8.ag8_40323131_task1
import users.b.g101.b40323299_cdw11
#import users.b.g9.bg9_40323218
import users.b.g9.bg9_40323250
#import users.b.g11.bg11_40323245
# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
    static_dir = os.environ['OPENSHIFT_REPO_DIR']+"/static"
    download_dir = os.environ['OPENSHIFT_DATA_DIR']+"/downloads"
else:
    # 表示程式在近端執行
    data_dir = _curdir + "/local_data/"
    static_dir = _curdir + "/static"
    download_dir = _curdir + "/local_data/downloads/"

# 利用 init.py 啟動, 建立所需的相關檔案
initobj = init.Init()

# 必須先將 download_dir 設為 static_folder, 然後才可以用於 download 方法中的 app.static_folder 的呼叫
app = Flask(__name__)
#app.config['download_dir'] = download_dir

# 使用 session 必須要設定 secret_key
# In order to use sessions you have to set a secret key
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T'








@app.route("/")
def index():
    #這是猜數字遊戲的起始表單, 主要在產生答案, 並且將 count 歸零
    # 將標準答案存入 answer session 對應區
    theanswer = random.randint(1, 100)
    thecount = 0
    # 將答案與計算次數變數存進 session 對應變數
    session['answer'] = theanswer
    session['count'] = thecount

    return render_template("index.html", answer=theanswer, count=thecount)
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)
@app.route('/red')
def red():
    # 重新導向 google
    return redirect("http://www.google.com")
@app.route('/guessform')
def guessform():
    session["count"] += 1
    guess = session.get("guess")
    theanswer = session.get("answer")
    count = session.get("count")
    return render_template("guessform.html", guess=guess, answer=theanswer, count=count)
@app.route('/docheck', methods=['POST'])
def docheck():
    # session[] 存資料
    # session.get() 取 session 資料
    # 利用 request.form[] 取得表單欄位資料, 然後送到 template
    guess = request.form["guess"]
    session["guess"] = guess
    # 假如使用者直接執行 doCheck, 則設法轉回根方法
    if guess is None:
        redirect("/")
    # 從 session 取出 answer 對應資料, 且處理直接執行 docheck 時無法取 session 值情況
    try:
        theanswer = int(session.get('answer'))
    except:
        redirect("/")
    # 經由表單所取得的 guess 資料型別為 string
    try:
        theguess = int(guess)
    except:
        return redirect("/guessform")
    # 每執行 doCheck 一次,次數增量一次
    session["count"] += 1
    count = session.get("count")
    # 答案與所猜數字進行比對
    if theanswer < theguess:
        return render_template("toobig.html", guess=guess, answer=theanswer, count=count)
    elif theanswer > theguess:
        return render_template("toosmall.html", guess=guess, answer=theanswer, count=count)
    else:
        # 已經猜對, 從 session 取出累計猜測次數
        thecount = session.get('count')
        return "猜了 "+str(thecount)+" 次, 終於猜對了, 正確答案為 "+str(theanswer)+": <a href='/'>再猜</a>"
    return render_template("docheck.html", guess=guess)
 
@app.route('/option', methods=["GET", "POST"])
def option():
    # 各組選出組長的方式, 若採遞增, 則各組內學號最小者為組長
    option_list1 = ["遞增", "遞減"]
    # 各組組長間的排序定組序, 若採遞增, 則學號最小的組長為第1組
    option_list2 = ["遞增", "遞減"]
    # 電腦教室共有 9 排電腦
    column = 9
    # 加上班級選擇
    option_list3 = ["2a", "2b"]
    # 根據班級的總人數, 以 9 去除, 算出需要排幾列才能夠容納的下, 而且若列數超過 7
    # 表示這些學員必須與其他同組學員共用電腦

    return render_template('option.html', option_list1=option_list1, option_list2=option_list2, option_list3=option_list3, column=column)
@app.route('/optionaction', methods=['POST'])
def optionaction():
    # 最後傳回的字串為 out_string
    out_string = ""
    # 程式內需要暫時使用的 tmp_string
    tmp_string = ""
    # 傳回字串中, 用來說明排序原則的 desc_string
    desc_string = ""
    result = []
    group_sorted = []
    num_of_stud = 0
    # 每組至多 7 人
    max_num_in_one_group = 7
    # 電腦教室配置, 共有 9 排
    total_column = 9
    # 上面為相關變數的初始值設定, 以下開始取出 data_a 或 data_b 進行處理, 由 option3 傳回值決定
    if request.form["option3"]  == "2a":
        content = request.form["data_a"]
    else:
        content = request.form["data_b"]
    #result = content.splitlines()
    for line in content.splitlines():
        result.append(list(line.split(",")))
    # i 為行序
    for i in range(len(result)):
        # j 為組員序
        for j in range(len(result[i])):
            tmp_string += result[i][j] + ", "
        out_string += "第" + str(i+1) + "排資料:"+ tmp_string + "<br />"
        tmp_string = ""
    for i in range(len(result)):
        # 開始進入組內排序, 根據 request.form["option1"]  的值決定遞增或遞減
        if request.form["option1"]  == "遞增":
            group_list = sorted(list(filter(None, result[i])))
        else:
            group_list = sorted(list(filter(None, result[i])), reverse=True)
        group_sorted.append(group_list)
    if request.form["option1"]  == "遞增":
        desc_string += "組內學號最小者為組長."
    else:
         desc_string += "組內學號最大者為組長."
    # 開始進入組間組長學號排序, 根據 request.form["option2"] 的值決定遞增或遞減
    if request.form["option2"]  == "遞增":
        desc_string += "各組長中學號最小者為第1組."
        final_result = sorted(group_sorted)
    else:
        desc_string += "各組長中學號最大者為第1組."
        final_result = sorted(group_sorted, reverse=True)
    out_string += "<br />" + desc_string + "<br />"
    # i 為行序
    for i in range(len(final_result)):
        # j 為組員序
        for j in range(len(final_result[i])):
            num_of_stud += 1
            tmp_string += final_result[i][j] + ","
        out_string += "第" + str(i+1) + "組:"+ tmp_string + "<br />"
        tmp_string = ""
    #return "總共有" + str(i+) + "組"
    # group_num 為總組數
    group_num = i + 1
    # 截至這裡, 已經完成選組長, 以及定組序的工作 ,接下來要排座位, 並且印出座位表
    # 先算每班的總人數
    #return "總共有"+ str(num_of_stud) + "人"
    seat_by_column = []
    for row in range(max_num_in_one_group):
    # 每組最多 7 人
    #for row in range(7):
        # 這裡的 11 為總組數
        #for column in range(11):
        for column in range(group_num):
            # 因為各分組數列的長度並不相同, 但是最長的有 7 位組員, 因此若無法取得的資料 (因為索引超值), 就補上空字串
            try:
                seat_by_column.append(final_result[column][row])
            except:
                seat_by_column.append("")
    # seat_by_column 為去除空白字串前的座位數列
    # 然後利用 filter(None, seat_by_column) 去除空白字串, 就可以得到以 column 為主的座位排序
    seat_by_column = list(filter(None, seat_by_column))
    # 然後每 N 個取為 1 排, 即可得到以排為主的座位序列, 而 N 則視全班人數除以 9, 也就是 total_column 進位決定, 因為共有 9 排
    N = math.ceil(num_of_stud/total_col�l�$s y�4*0�G
�Fx�$k Fr�ĕm m�1�

�*1 k 6P 0 x�4�-uQ�b u�Ac�B.W��<����x�1   (  - {�@1@8 A c�%*-@c� f@1 j1@e@8��-U�
0@e�b@AdE@#3� c }�!T� M@b@Lf@GAVRNC�hn��a�@7n@r�$0^AR�r�
g�r�pn@F�-�XCC�*OC�*2�QW�*A�Q�:�\L�[d�e8��3 4 2D 3@oe 5�0�@Ate�-�b &F4`#'9 7`fU ?2`=7�}`	3U�B0bC7 b�c��?a- 
e` 8`Zb`a +�C4�
6U�6�c 5�
}�`�f`
-`��t6 �0 a �9Ub3 e�(2�e�`2� -`1�a�9ba��'ak�'�l��{�*a :d�
���'e�9`�;9���;2�;e�5�;�;�;��a�P`��&e�l�c`�  �@�	b��a�(y��  � �
0管�
btv�
jr`
.`lb�a���o �F`�e���
" �M I�N��R �u p�U�
 �e�
h �s�n
�
p �+
 �Zs`@r�e�td�lm�		���3 ^�
��l a`�c���a�q`�

`Ze"�e��w�n�b �.+
��t�^t`�f��hip.x�?p��
��}�t�sRpcD�a��s7qxE v��ZlpgP)S� jc�rtpp���PS-���kt�mp�
�1
xjA�p�i�
QiU�n

Up)P��k5`$  $0*xpe�zdp
X(  
PU�#n �Jrl :JV �xp�70��	0�Q*?
�(h�
w^q*�	P�
�
o�1�Qg) 
P
o0
�mpl�z
	
0��!p���
�p0��7���
p�-i\�12r�
m4Y�(�Vg
p�wP2l _�
psEQ0l����Evt
��Vs0�1o�
ePu�P
_	�Gc�f�
V'�3�-P2i-�P>o� nR�0l0�q
lP�-�1P�1 ="&__�Qq&^eQ
?WR
0	e�P9ocj_
�2i��Ѧ_
�*U
q r��4�
��t�	Q
�t\q+fP-m0 �T��__TnP&rP�aPi z�
l�7w�z��
��q�lU?a�
e�	
�.y]Pt_&P&��m0t���"%�
�
�
�'��;
(
0?Y!n�7� � �-�-_!q�Q�_[
�
�&a�j��sӱ$b�1M1%[��^e0B�ϱ1�d�u��0��sP�1�Qt���_�3Q`u�&W�s	�Sjr	 �iЙ��2�3���}bP	1����	
�o� ���Ip?	8m�N��s}2��    0    C o m p Ps i t e  B u s .
 
y 
�
 a �g |l |v �n
|
 r Bs l �2 �pzn d zjs 6a zizwk E
[
[p 9�ew={t #
��s� �

�-d�b�y�,   W�ZE��n�\e x�LU��g�@e�l�0P 0 1��
�1w���n�&m�
s ��� k��M	��=:�&L { 4 7�-e c 8 
3�1-��e 6 �f -�1�34�Zb�
-��E9�3U�	6�
7��}�%3�!0�8�6 bU�c�7@-�e�� 8��
e@0@U� 6@6@ c�
5m@}�&�'b@�2B
�'�'�  
]�nl@oA�AC.�li@�  A
@4A�c��p�
@
e v@z�b j�qd@l@>k��ls@�1�[Mn@
r@�a�
i z�L
�A�u@E�I�
@s�ks n�f��k�Vr@e�W4U�g@�2�

@4i�@�x�p@�K'��-"- w n�@�d�w`�~!-`�h �t�-`1 ua 0l	�
��
� 
s�I_0	��a�Qo
 Kh B`s[�+
��
�m��g���)0��m^h�
a�q
� l�i��'m0�:v`Nr�M�k

 ��r2
m��aTf,+��p�	4l��5!��
%�
�5a
�-:<o`:e��;!�r m`%!��((�
�k�Ia Sv�a>y�
�t��a�tl�Ԯd 
�k/H�pఽk#	 !\��Ee`
�t�4t`G��
&�
��
�a	�
y
'!�c'���

�El �c`Xt q,'�r�jp�*
ti�%L��Q3Qi�}9
P=�b�;;1�30b �hPbp	Ys
�yZr0x�	�}H�#A;pCo�т17c �l�4���Zk^uqzt�n�"�qo M�uP	t P� t0a�
�R�EQ1��D�ap
ae0dX  P $ Qp�rAt�
  
�yP   D�cP
mې��sp�	����'M� �q&��  q
P�+��Du�,e�	�jV�d�o��� A�[pp�aP!Zi0	n�	� a	5�opi�u
 �N� t H0opt  �
P��
�c0�� S1� d TP3 �[ ���Y]p �R��h�  ��p�o�mp
n�c  �(  ��
�
�#s0fP
0�)  Ёq�mQ
�&P
tt�*M�up<� @
z_Ɩs	}0	e�^��1� �16l0
t�{Q	q��
��q5�it�
4  �Q�o�a0 #�I)�'np
�
F��QMQP
�#
q+�d�
��qD��s�
1pT_(1��	 F�q�r��/���1�  STP�1�l�Y����Uq
f�u+tp
�
*�
3,58�+  �  "__��]-Q�1rp�7Rr�  1

�e�ap>l0"  UW�

��EupClu�c
������0�1
q�<�Q?-;-1�Ke)�	��	�
1!�=�?��?�3�?1$$��8q�
?4Q?4?4=4
��RM�1�qqT��q�W�
�Z�W�
?N�s+?N�-?N3N�!?N
.  V��  t   M e  n u     .   
z _Ɩ  � �  Lhb�,  [ ���Y] ̟R��h�  � F W i �d o w �s �n �
 S �(a r
Ƅ
��(  
 �E O �R Y . D 
jP E [
 Q[3 2 k s ya0 	 d x� a p }.  *   CE  F A U L VT K

. OP G 1�2�dF�*�P	 c�=rՀs�Oe�He��]�
r v�
d l��   �

 b�\zs��s����z�
lU��c�
l�
.��l�=  ��
�f��-�l��z�t�o�   �/  	 �z h -��W�H*n�GxD+H   40  
P6. �m@�i�
ADg�)��Ai
�i@ju@)Vb�
Ip
�c�!a��AP�p�1AXe�UAQ�e�Wt�$�E@-@uo g@ T ��@}e@[uU�C�a�Bn@Nl��e��l�
�)�5Zs�	d��T@�p��P�Rc@  L퀌
�4�um�A�A�Rd�  C=m@iu/@
�>G�A-	Bm �f@.� C�A

@W��ji�%o���

@�
N@nC@$C H �E@*D���A*�UAt�>��(m@n�@>A�u�
t@c@<�Iokk�7c�	d��"k%Xc
c�.g`#6.���[
 C _ k2 5 w. N��2S�!
�9`�0`f %nd
`N�v�a�	i`i�
#i�}p 1
 �4t 0�Bo�k�8}�e����!%
��.x` qv
�T�Da;Z.�Ox` e�p`=oo 
e��,�4t�4�`�p  R�;R 
�O�t� �K�9K B�a�U`��L�2  #+�a�t�&�E.�t�	�c	�"u ti�S+�
 a g`gn�K�f$9
jb Hc��ae�Sr �od!S���`g���V� 
�s j`k/
��
c�yt>
  <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
  <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
  </section></body></html>
  '''
@app.route('/imageaxupload', methods=['POST'])
# ajax jquery chunked file upload for flask
def imageaxupload():
    '''
    if not session.get('logged_in'):
        #abort(401)
        return redirect(url_for('login'))
    '''
    # need to consider if the uploaded filename already existed.
    # right now all existed files will be replaced with the new files
    filename = request.args.get("ax-file-name")
    flag = request.args.get("start")
    if flag == "0":
        file = open(data_dir+"images/"+filename, "wb")
    else:
        file = open(data_dir+"images/"+filename, "ab")
    file.write(request.stream.read())
    file.close()
    return "image file uploaded!"

    
    
@app.route('/imageuploadform')
def imageuploadform():
    '''
    if not session.get('logged_in'):
        #abort(401)
        return redirect(url_for('login'))
    '''
    return "<h1>file upload</h1>"+'''
  <script src="/static/jquery.js" type="text/javascript"></script>
  <script src="/static/axuploader.js" type="text/javascript"></script>
  <script>
  $(document).ready(function(){
  $('.prova').axuploader({url:'imageaxupload', allowExt:['jpg','png','gif','7z','pdf','zip','flv','stl','swf'],
  finish:function(x,files)
{
    alert('All files have been uploaded: '+files);
},
  enable:true,
  remotePath:function(){
  return 'images/';
  }
  });
  });
  </script>
  <div class="prova"></div>
  <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
  <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
  </section></body></html>
  '''
@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    #return send_from_directory(download_dir, filename=filename, as_attachment=True)
    return send_from_directory(download_dir, filename=filename)
    


# setup static directory
@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory(data_dir+"/images/", path)
# setup static directory
@app.route('/static/')
def send_static():
  return app.send_static_file('index.html')

# setup static directory
@app.route('/static/blog/')
def send_blog():
  return app.send_static_file('blog/index.html')

# setup static directory
@app.route('/static/<path:path>')
def send_file(path):
  return app.send_static_file(static_dir+path)

if __name__ == "__main__":
    app.run()
    
app.register_blueprint(users.a.g10.ag10_40323139.ag10_40323139)
app.register_blueprint(users.a.g8.ag8_40323131_task1.ag8_40323131)
app.register_blueprint(users.a.g4.ag4_40323138.ag4_40323138)
app.register_blueprint(users.b.g101.b40323299_cdw11.ag100)
#app.register_blueprint(users.b.g9.bg9_40323218.bg9_40323218)
app.register_blueprint(users.b.g9.bg9_40323250.bg9_40323250)
#app.register_blueprint(users.a.g11.bg11_40323245.bg11_40323245)




