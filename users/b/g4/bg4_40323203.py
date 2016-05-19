# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template, make_response

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
bg4_40323203 = Blueprint('bg8_40323203', __name__, url_prefix='/bg4_40323203', template_folder='templates')




@bg4_40323203.route('/task4A')
def task4A():
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
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="purple")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="purple")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="purple")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="purple")
mychain.basic(x10, y10, x1, y1, color="purple")


cgo.setWorldCoords(-315, -250, 500, 500) 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="purple")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="purple")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="purple")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="purple")
mychain.basic(x10, y10, x1, y1, color="purple")

cgo.setWorldCoords(-385, -250, 500, 500) 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="purple")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="purple")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="purple")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="purple")
mychain.basic(x10, y10, x1, y1, color="purple")

cgo.setWorldCoords(-445, -250, 500, 500) 
# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="purple")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="purple")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="purple")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="purple")
mychain.basic(x10, y10, x1, y1, color="purple")
</script>
</body></html>
'''
    return outstring
    

@bg4_40323203.route('/taskBADC')
def taskBADC():
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
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="purple")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="purple")
# 右上垂直向下單元
x7, y7 = mychain.basic_rot(x6, y6, -90, color="purple")
# 右斜 240 度
x8, y8 = mychain.basic_rot(x7, y7, 210, color="purple")
# 中間水平
mychain.basic(x8, y8, x2, y2, color="purple")
# 右下斜 -30 度
x10, y10 = mychain.basic_rot(x8, y8, -30, color="purple")
# 右下垂直向下單元
x11, y11 = mychain.basic_rot(x10, y10, -90, color="purple")
# 右下斜 240 度
x12, y12 = mychain.basic_rot(x11, y11, 210, color="purple")
# 水平接回起點
mychain.basic(x12,y12, 0, 0, color="purple")

cgo.setWorldCoords(-50, -250, 500, 500) 

# 畫 A
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(50,0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="purple")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="purple")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="purple")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="purple")
mychain.basic(x10, y10, x1, y1, color="purple")

cgo.setWorldCoords(-107.5, -250, 500, 500) 


# 畫 D
# 左邊四個垂直單元
x1, y1 = mychain.basic_rot(0+60, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="purple")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜 -40 度
x6, y6 = mychain.basic_rot(x5, y5, -40, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -60, color="purple")
# 右中垂直向下單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
# -120 度
x9, y9 = mychain.basic_rot(x8, y8, -120, color="purple")
# -140
x10, y10 = mychain.basic_rot(x9, y9, -140, color="purple")
# 水平接回原點
mychain.basic(x10, y10, 0+60, 0, color="purple")

# 畫 C
# 上半部
# 左邊中間垂直起點, 圓心位於線段中央, y 方向再向上平移兩個鏈條圓心距單位
x1, y1 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), 90, color="purple")
# 上方轉 80 度
x2, y2 = mychain.basic_rot(x1, y1, 80, color="purple")
# 上方轉 30 度
x3, y3 = mychain.basic_rot(x2, y2, 30, color="purple")
# 上方水平
x4, y4 = mychain.basic_rot(x3, y3, 0, color="purple")
# 下半部, 從起點開始 -80 度
x5, y5 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), -80, color="purple")
# 下斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="purple")
# 下方水平單元
x7, y7 = mychain.basic_rot(x6, y6, -0, color="purple")

cgo.setWorldCoords(-55, -250, 500, 500) 
</script>
</body></html>
'''
    return outstring

@bg4_40323203.route('/taskABCD')
def taskABCD():
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
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="purple")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="purple")
# 右上垂直向下單元
x7, y7 = mychain.basic_rot(x6, y6, -90, color="purple")
# 右斜 240 度
x8, y8 = mychain.basic_rot(x7, y7, 210, color="purple")
# 中間水平
mychain.basic(x8, y8, x2, y2, color="purple")
# 右下斜 -30 度
x10, y10 = mychain.basic_rot(x8, y8, -30, color="purple")
# 右下垂直向下單元
x11, y11 = mychain.basic_rot(x10, y10, -90, color="purple")
# 右下斜 240 度
x12, y12 = mychain.basic_rot(x11, y11, 210, color="purple")
# 水平接回起點
mychain.basic(x12,y12, 0, 0, color="purple")


cgo.setWorldCoords(-247.5, -350, 500, 500) 
# 畫 B
# 左邊兩個垂直單元
x1, y1 = mychain.basic_rot(0, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
# 左斜邊兩個單元
x3, y3 = mychain.basic_rot(x2, y2, 80, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 71, color="purple")
# 最上方水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜邊兩個單元
x6, y6 = mychain.basic_rot(x5, y5, -71, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -80, color="purple")
# 右邊兩個垂直單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
x9, y9 = mychain.basic_rot(x8, y8, -90, color="purple")
# 中間兩個水平單元
x10, y10 = mychain.basic_rot(x8, y8, -180, color="purple")
mychain.basic(x10, y10, x1, y1, color="purple")

cgo.setWorldCoords(-55, -50, 500, 500) 
# 畫 C
# 左邊四個垂直單元
x1, y1 = mychain.basic_rot(0+65*3, 0, 90, color="purple")
x2, y2 = mychain.basic_rot(x1, y1, 90, color="purple")
x3, y3 = mychain.basic_rot(x2, y2, 90, color="purple")
x4, y4 = mychain.basic_rot(x3, y3, 90, color="purple")
# 上方一個水平單元
x5, y5 = mychain.basic_rot(x4, y4, 0, color="purple")
# 右斜 -40 度
x6, y6 = mychain.basic_rot(x5, y5, -40, color="purple")
x7, y7 = mychain.basic_rot(x6, y6, -60, color="purple")
# 右中垂直向下單元
x8, y8 = mychain.basic_rot(x7, y7, -90, color="purple")
# -120 度
x9, y9 = mychain.basic_rot(x8, y8, -120, color="purple")
# -140
x10, y10 = mychain.basic_rot(x9, y9, -140, color="purple")
# 水平接回原點
mychain.basic(x10, y10, 0+65*3, 0, color="purple")

cgo.setWorldCoords(-120, -150, 500, 500) 
# 畫 D
# 上半部
# 左邊中間垂直起點, 圓心位於線段中央, y 方向再向上平移兩個鏈條圓心距單位
x1, y1 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), 90, color="purple")
# 上方轉 80 度
x2, y2 = mychain.basic_rot(x1, y1, 80, color="purple")
# 上方轉 30 度
x3, y3 = mychain.basic_rot(x2, y2, 30, color="purple")
# 上方水平
x4, y4 = mychain.basic_rot(x3, y3, 0, color="purple")
# 下半部, 從起點開始 -80 度
x5, y5 = mychain.basic_rot(0+65*2, -10+10+20*math.sin(80*deg)+20*math.sin(30*deg), -80, color="purple")
# 下斜 -30 度
x6, y6 = mychain.basic_rot(x5, y5, -30, color="purple")
# 下方水平單元
x7, y7 = mychain.basic_rot(x6, y6, -0, color="purple")
</script>
</body></html>
'''
    return outstring



