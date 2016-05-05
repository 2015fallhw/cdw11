# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
bg2_40123214 = Blueprint('bg2_40123214', __name__, url_prefix='/bg2_40123214', template_folder='templates')

# 展示傳回 Brython 程式
@bg2_40123214.route('/a')
def taskI():
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
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
   
    basic10 = cmbr.dup()
    basic10.rotate(0)
    basic10.translate(0, 20)
    
    basic11 = cmbr.dup()
    basic11.rotate(165)
    basic11.translate(0, 20)
    
    basic12 = cmbr.dup()
    basic12.rotate(145)
    basic12.translate(5, 40)
    
    basic13 = cmbr.dup()
    basic13.rotate(90)
    basic13.translate(16, 56)
    
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)

    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 0, 0, 0, 0, "black", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task1"></script>

</body>
</html>
'''
    return outstring
    
@bg2_40123214.route('/b')
def taskII():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 5000, 0, 5000, {
#    "strokeColor":"#aaaaaa",
#   "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0, 20)
    
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, 40)
    
    basic3 = cmbr.dup()
    basic3.rotate(90)
    basic3.translate(0, 0)
    
    basic4 = cmbr.dup()
    basic4.rotate(90)
    basic4.translate(20, 0)
    
    basic5 = cmbr.dup()
    basic5.rotate(0)
    basic5.translate(40, 0)
    
    basic6 = cmbr.dup()
    basic6.rotate(0)
    basic6.translate(40, 20)
    
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(40, 40)
    
    basic8 = cmbr.dup()
    basic8.rotate(150)
    basic8.translate(0, 40)
    
    basic9 = cmbr.dup()
    basic9.rotate(210)
    basic9.translate(40, 40)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(20*math.cos(60*deg), (20*math.sin(60*deg)+40))
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(350, 0, 0, 0, 0, "lightgreen", True, 4)
'''
    return outstring
    

    
@bg2_40123214.route('/d')
def task_III():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 5000, 0, 5000, {
#    "strokeColor":"#aaaaaa",
#   "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0, 20)
    
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, 40)
    
    basic3 = cmbr.dup()
    basic3.rotate(90)
    basic3.translate(0, 0)
    
    basic4 = cmbr.dup()
    basic4.rotate(90)
    basic4.translate(20, 0)
    
    basic5 = cmbr.dup()
    basic5.rotate(0)
    basic5.translate(40, 0)
    
    basic6 = cmbr.dup()
    basic6.rotate(0)
    basic6.translate(40, 20)
    
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(40, 40)
    
    basic8 = cmbr.dup()
    basic8.rotate(150)
    basic8.translate(0, 40)
    
    basic9 = cmbr.dup()
    basic9.rotate(210)
    basic9.translate(40, 40)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(20*math.cos(60*deg), (20*math.sin(60*deg)+40))
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(1050, 0, 0, 0, 0, "lightgreen", True, 4)
'''
    return outstring
    
