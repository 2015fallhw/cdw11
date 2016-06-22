# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template, make_response

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag2_40323122 = Blueprint('ag2_40323122', __name__, url_prefix='/ag2_40323122', template_folder='templates')




@ag2_40323122.route('/A4')
def A4():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
</head>
<body>
<script>
window.onload=function(){
brython(1);
}
</script>
<canvas id="plotarea" width="800" height="800"></canvas>
<script type="text/python">
from javascript import JSConstructor
from browser import alert
from browser import window
import math
 
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
 
cgo.setWorldCoords(-250, -250, 500, 500) 
 
# 畫軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
 
deg = math.pi/180  

class chain():
    # 輪廓的外型設為成員變數
    chamber = "M -6.8397, -1.4894 \
            A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
            A 40, 40, 0, 0, 1, 6.8397, -18.511 \
            A 7, 7, 0, 1, 0, -6.8397, -18.511 \
            A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    # 利用鏈條起點與終點定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic(self, x1, y1, x2, y2, color="green", border=True, linewidth=4, scale=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.border = border
        self.linewidth = linewidth
        self.scale = scale
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": color,
                "border": border,
                "strokeColor": "tan",
                "lineWidth": linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4), "PATH")
        cmbr.appendPath(hole)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(math.atan2(y2-y1, x2-x1)/deg+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, scale, 0)
 
    # 利用鏈條起點與旋轉角度定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic_rot(self, x1, y1, rot, color="green", border=True, linewidth=4, scale=1):
        self.x1 = x1
        self.y1 = y1
        self.rot = rot
        self.color = color
        self.border = border
        self.linewidth = linewidth
        self.scale = scale
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": color,
                "border": border,
                "strokeColor": "tan",
                "lineWidth": linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4), "PATH")
        cmbr.appendPath(hole)
        # 根據旋轉角度, 計算 x2 與 y2
        x2 = x1 + 20*math.cos(rot*deg)
        y2 = y1 + 20*math.sin(rot*deg)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(rot+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, scale, 0)
 
        return x2, y2

# 利用 chain class 建立案例, 對應到 mychain 變數
mychain = chain()
 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="blue")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="blue")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="blue")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="blue")
mychain.basic(x10, y10, x1, y1, color="blue")


cgo.setWorldCoords(-315, -250, 500, 500) 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="blue")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="blue")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="blue")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="blue")
mychain.basic(x10, y10, x1, y1, color="blue")

cgo.setWorldCoords(-385, -250, 500, 500) 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="blue")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="blue")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="blue")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="blue")
mychain.basic(x10, y10, x1, y1, color="blue")

cgo.setWorldCoords(-445, -250, 500, 500) 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="blue")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="blue")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="blue")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="blue")
mychain.basic(x10, y10, x1, y1, color="blue")
</script>
</body></html>
'''
    return outstring
@ag2_40323122.route('/BADC')
def BADC():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
</head>
<body>
<script>
window.onload=function(){
brython(1);
}
</script>
<canvas id="plotarea" width="800" height="800"></canvas>
<script type="text/python">
from javascript import JSConstructor
from browser import alert
from browser import window
import math
 
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
 
cgo.setWorldCoords(-40, -250, 500, 500) 
 
# 畫軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
 
deg = math.pi/180  

class chain():
    # 輪廓的外型設為成員變數
    chamber = "M -6.8397, -1.4894 \
            A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
            A 40, 40, 0, 0, 1, 6.8397, -18.511 \
            A 7, 7, 0, 1, 0, -6.8397, -18.511 \
            A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    # 利用鏈條起點與終點定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic(self, x1, y1, x2, y2, color="green", border=True, linewidth=4, scale=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.border = border
        self.linewidth = linewidth
        self.scale = scale
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": color,
                "border": border,
                "strokeColor": "tan",
                "lineWidth": linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4), "PATH")
        cmbr.appendPath(hole)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(math.atan2(y2-y1, x2-x1)/deg+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, scale, 0)
 
    # 利用鏈條起點與旋轉角度定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic_rot(self, x1, y1, rot, color="green", border=True, linewidth=4, scale=1):
        self.x1 = x1
        self.y1 = y1
        self.rot = rot
        self.color = color
        self.border = border
        self.linewidth = linewidth
        self.scale = scale
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": color,
                "border": border,
                "strokeColor": "tan",
                "lineWidth": linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4), "PATH")
        cmbr.appendPath(hole)
        # 根據旋轉角度, 計算 x2 與 y2
        x2 = x1 + 20*math.cos(rot*deg)
        y2 = y1 + 20*math.sin(rot*deg)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(rot+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, scale, 0)
 
        return x2, y2
 
# 利用 chain class 建立案例, 對應到 mychain 變數
mychain = chain()
 
# 畫 B
# 左邊四個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="blue")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="blue")
# 右上垂直向下單元
x7, y7 = mychain.basic_rot(x6, y6, -90, color="blue")
# 右斜 240 度
x8, y8 = mychain.basic_rot(x7, y7, 210, color="blue")
# 中間水平
mychain.basic(x8, y8, x2, y2, color="blue")
# 右下斜 -30 度
x10, y10 = mychain.basic_rot(x8, y8, -30, color="blue")
# 右下垂直向下單元
x11, y11 = mychain.basic_rot(x10, y10, -90, color="blue")
# 右下斜 240 度
x12, y12 = mychain.basic_rot(x11, y11, 210, color="blue")
# 水平接回起點
mychain.basic(x12,y12, 0, 0, color="blue")

cgo.setWorldCoords(-50, -250, 500, 500) 

# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(50,0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="blue")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="blue")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="blue")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="blue")
mychain.basic(x10, y10, x1, y1, color="blue")

cgo.setWorldCoords(-107.5, -250, 500, 500) 


# 畫 D
# 左邊四個垂直單元
x1, y1 = mychain.basic_rot(0+60, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="blue")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜 -40 度
x6, y6 = mychain.basic_rot(x5, y5, -40, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -60, color="blue")
# 右中垂直向下單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
# -120 度
x9, y9 = mychain.basic_rot(x8, y8, -120, color="blue")
# -140
x10, y10 = mychain.basic_rot(x9, y9, -140, color="blue")
# 水平接回原點
mychain.basic(x10, y10, 0+60, 0, color="blue")

# 畫 C
# 上半部
# 左邊中間垂直起點, 圓心位於線段中央, y 方向再向上平移兩個鏈條圓心距單位
x1, y1 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), 90, color="blue")
# 上方轉 80 度
x2, y2 = mychain.basic_rot(x1, y1, 80, color="blue")
# 上方轉 30 度
x3, y3 = mychain.basic_rot(x2, y2, 30, color="blue")
# 上方水平
x4, y4 = mychain.basic_rot(x3, y3, 0, color="blue")
# 下半部, 從起點開始 -80 度
x5, y5 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), -80, color="blue")
# 下斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="blue")
# 下方水平單元
x7, y7 = mychain.basic_rot(x6, y6, -0, color="blue")

cgo.setWorldCoords(-55, -250, 500, 500) 
</script>
</body></html>
'''
    return outstring
@ag2_40323122.route('/abcd')
def abcd():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
</head>
<body>
<script>
window.onload=function(){
brython(1);
}
</script>
<canvas id="plotarea" width="800" height="800"></canvas>
<script type="text/python">
from javascript import JSConstructor
from browser import alert
from browser import window
import math
 
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
 
cgo.setWorldCoords(-250, -250, 500, 500) 
 
# 畫軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
 
deg = math.pi/180  
 
# 將繪製鏈條輪廓的內容寫成 class 物件
class chain():
    # 輪廓的外型設為成員變數
    chamber = "M -6.8397, -1.4894 \
            A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
            A 40, 40, 0, 0, 1, 6.8397, -18.511 \
            A 7, 7, 0, 1, 0, -6.8397, -18.511 \
            A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    # 利用鏈條起點與終點定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic(self, x1, y1, x2, y2, color="green", border=True, linewidth=4, scale=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.border = border
        self.linewidth = linewidth
        self.scale = scale
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": color,
                "border": border,
                "strokeColor": "tan",
                "lineWidth": linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4), "PATH")
        cmbr.appendPath(hole)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(math.atan2(y2-y1, x2-x1)/deg+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, scale, 0)
 
    # 利用鏈條起點與旋轉角度定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic_rot(self, x1, y1, rot, color="green", border=True, linewidth=4, scale=1):
        self.x1 = x1
        self.y1 = y1
        self.rot = rot
        self.color = color
        self.border = border
        self.linewidth = linewidth
        self.scale = scale
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": color,
                "border": border,
                "strokeColor": "tan",
                "lineWidth": linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4), "PATH")
        cmbr.appendPath(hole)
        # 根據旋轉角度, 計算 x2 與 y2
        x2 = x1 + 20*math.cos(rot*deg)
        y2 = y1 + 20*math.sin(rot*deg)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(rot+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, scale, 0)
 
        return x2, y2
 
# 利用 chain class 建立案例, 對應到 mychain 變數
mychain = chain()
 
# 畫 A
# 左邊四個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="blue")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="blue")
# 右上垂直向下單元
x7, y7 = mychain.basic_rot(x6, y6, -90, color="blue")
# 右斜 240 度
x8, y8 = mychain.basic_rot(x7, y7, 210, color="blue")
# 中間水平
mychain.basic(x8, y8, x2, y2, color="blue")
# 右下斜 -30 度
x10, y10 = mychain.basic_rot(x8, y8, -30, color="blue")
# 右下垂直向下單元
x11, y11 = mychain.basic_rot(x10, y10, -90, color="blue")
# 右下斜 240 度
x12, y12 = mychain.basic_rot(x11, y11, 210, color="blue")
# 水平接回起點
mychain.basic(x12,y12, 0, 0, color="blue")


cgo.setWorldCoords(-247.5, -350, 500, 500) 
# 畫 B
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="blue")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="blue")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="blue")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="blue")
mychain.basic(x10, y10, x1, y1, color="blue")

cgo.setWorldCoords(-55, -50, 500, 500) 
# 畫 C
# 左邊四個垂直單元
x1, y1 = mychain.basic_rot(0+65*3, 0, 90, color="blue")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="blue")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="blue")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="blue")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="blue")
# 右斜 -40 度
x6, y6 = mychain.basic_rot(x5, y5, -40, color="blue")
x7, y7 = mychain.basic_rot(x6, y6, -60, color="blue")
# 右中垂直向下單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="blue")
# -120 度
x9, y9 = mychain.basic_rot(x8, y8, -120, color="blue")
# -140
x10, y10 = mychain.basic_rot(x9, y9, -140, color="blue")
# 水平接回原點
mychain.basic(x10, y10, 0+65*3, 0, color="blue")

cgo.setWorldCoords(-120, -150, 500, 500) 
# 畫 D
# 上半部
# 左邊中間垂直起點, 圓心位於線段中央, y 方向再向上平移兩個鏈條圓心距單位
x1, y1 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), 90, color="blue")
# 上方轉 80 度
x2, y2 = mychain.basic_rot(x1, y1, 80, color="blue")
# 上方轉 30 度
x3, y3 = mychain.basic_rot(x2, y2, 30, color="blue")
# 上方水平
x4, y4 = mychain.basic_rot(x3, y3, 0, color="blue")
# 下半部, 從起點開始 -80 度
x5, y5 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), -80, color="blue")
# 下斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="blue")
# 下方水平單元
x7, y7 = mychain.basic_rot(x6, y6, -0, color="blue")
</script>
</body></html>
'''
    return outstring

@ag2_40323122.route('/ex/<x>/<y>')
@ag2_40323122.route('/ex', defaults={'x':0, 'y':0})
def ex(x,y):
    return head_str + chain_str + ex(int(x), int(y)) + tail_str

from flask import Blueprint, request
  
head_str = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 鏈條繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
 
</head>
<body>
 
<script>
window.onload=function(){
brython(1);
}
</script>
 
<canvas id="plotarea" width="800" height="800"></canvas>
'''
 
tail_str = '''
</script>
</body>
</html>
'''
 
chain_str = '''
<script type="text/python">
from javascript import JSConstructor
from browser import alert
from browser import window
import math
 
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
 
cgo.setWorldCoords(-250, -250, 500, 500) 
 
# 畫軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
 
deg = math.pi/180  
 
# 將繪製鏈條輪廓的內容寫成 class 物件
class chain():
    # 輪廓的外型設為 class variable
    chamber = "M -6.8397, -1.4894 \
            A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
            A 40, 40, 0, 0, 1, 6.8397, -18.511 \
            A 7, 7, 0, 1, 0, -6.8397, -18.511 \
            A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    def __init__(self, fillcolor="blue", border=True, strokecolor= "tan", linewidth=2, scale=1):
        self.fillcolor = fillcolor
        self.border = border
        self.strokecolor = strokecolor
        self.linewidth = linewidth
        self.scale = scale
 
    # 利用鏈條起點與終點定義繪圖
    def basic(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4*self.scale), "PATH")
        cmbr.appendPath(hole)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(math.atan2(y2-y1, x2-x1)/deg+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, self.scale, 0)
 
    # 利用鏈條起點與旋轉角度定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic_rot(self, x1, y1, rot, v=False):
        # 若 v 為 True 則為虛擬 chain, 不 render
        self.x1 = x1
        self.y1 = y1
        self.rot = rot
        self.v = v
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4*self.scale), "PATH")
        cmbr.appendPath(hole)
        # 根據旋轉角度, 計算 x2 與 y2
        x2 = x1 + 20*math.cos(rot*deg)*self.scale
        y2 = y1 + 20*math.sin(rot*deg)*self.scale
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(rot+90)
 
        # 放大 scale 倍
        if v == False:
            cgo.render(basic1, x1, y1, self.scale, 0)
 
        return x2, y2
'''
def circle2(x, y, degree=10):
    # 20 為鏈條兩圓距
    # chain 所圍之圓圈半徑為 20/2/math.asin(degree*math.pi/180/2)
    # degree = math.asin(20/2/radius)*180/math.pi
    #degree = 10
    first_degree = 90 - degree
    repeat = 360 / degree
 
    outstring = '''
mychain = chain()
 
x1, y1 = mychain.basic_rot('''+str(x)+","+str(y)+", "+str(first_degree)+''')
'''
    for i in range(2, int(repeat)+1):
        outstring += "x"+str(i)+", y"+str(i)+"=mychain.basic_rot(x"+str(i-1)+", y"+str(i-1)+", 90-"+str(i*degree)+") \n"
    return outstring
 
 
def ex(x, y):
    # 20 為鏈條兩圓距
    # chain 所圍之圓圈半徑為 20/2/math.asin(degree*math.pi/180/2)
    # degree = math.asin(20/2/radius)*180/math.pi
    x = 50
    y = 0
    degree = 12
    # 78, 66, 54, 42, 30, 18, 6度
    #必須有某些 chain 算座標但是不 render
    first_degree =90-degree
    repeat = 360 / degree
    # 第1節也是 virtual chain
    outstring = '''
mychain = chain()
 
x1, y1 = mychain.basic_rot('''+str(x)+","+str(y)+", "+str(first_degree)+''', True)
#x1, y1 = mychain.basic_rot('''+str(x)+","+str(y)+", "+str(first_degree)+''')
'''
    # 這裡要上下各多留一節虛擬 chain, 以便最後進行連接 (x7, y7) 與 (x22, y22)
    for i in range(2, int(repeat)+1):
        #if i < 7 or i > 23:        
        if i <= 7 or i >= 23:
            # virautl chain
            outstring += "x"+str(i)+", y"+str(i)+"=mychain.basic_rot(x"+str(i-1)+", y"+str(i-1)+", 90-"+str(i*degree)+", True) \n"
            #outstring += "x"+str(i)+", y"+str(i)+"=mychain.basic_rot(x"+str(i-1)+", y"+str(i-1)+", 90-"+str(i*degree)+") \n"
        else:
            outstring += "x"+str(i)+", y"+str(i)+"=mychain.basic_rot(x"+str(i-1)+", y"+str(i-1)+", 90-"+str(i*degree)+") \n"
 
    p = -150
    k = 0
    degree = 20
    # 70, 50, 30, 10
    # 從 i=5 開始, 就是 virautl chain
    first_degree = 90
    repeat = 360 / degree
    # 第1節不是 virtual chain
    outstring += '''
#mychain = chain()
 
p1, k1 = mychain.basic_rot('''+str(p)+","+str(k)+", "+str(first_degree)+''')
'''
    for i in range(2, int(repeat)+1):
        if i >= 5 and i <= 13:
            # virautl chain
            outstring += "p"+str(i)+", k"+str(i)+"=mychain.basic_rot(p"+str(i-1)+", k"+str(i-1)+", 90-"+str(i*degree)+", True) \n"
            #outstring += "p"+str(i)+", k"+str(i)+"=mychain.basic_rot(p"+str(i-1)+", k"+str(i-1)+", 90-"+str(i*degree)+") \n"
        else:
            outstring += "p"+str(i)+", k"+str(i)+"=mychain.basic_rot(p"+str(i-1)+", k"+str(i-1)+", 90-"+str(i*degree)+") \n"
 
    # 上段連接直線
    # 從 p5, k5 作為起點
    first_degree = 10
    repeat = 11
    outstring += '''
m1, n1 = mychain.basic_rot(p4, k4, '''+str(first_degree)+''')
'''
    for i in range(2, int(repeat)+1):
        outstring += "m"+str(i)+", n"+str(i)+"=mychain.basic_rot(m"+str(i-1)+", n"+str(i-1)+", "+str(first_degree)+")\n"
 
    # 下段連接直線
    # 從 p12, k12 作為起點
    first_degree = -10
    repeat = 11
    outstring += '''
r1, s1 = mychain.basic_rot(p13, k13, '''+str(first_degree)+''')
'''
    for i in range(2, int(repeat)+1):
        outstring += "r"+str(i)+", s"+str(i)+"=mychain.basic_rot(r"+str(i-1)+", s"+str(i-1)+", "+str(first_degree)+")\n"
 
    # 上段右方接點為 x7, y7, 左側則為 m11, n11
    outstring += "mychain.basic(x7, y7, m11, n11)\n"
    # 下段右方接點為 x22, y22, 左側則為 r11, s11
    outstring += "mychain.basic(x22, y22, r11, s11)\n"
 
    return outstring


