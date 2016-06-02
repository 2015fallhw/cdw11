# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag1_40323105 = Blueprint('ag1_40323105', __name__, url_prefix='/ag1_40323105', template_folder='templates')

# 展示傳回 Brython 程式
@ag1_40323105.route('/a')
def task1():
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

cgo.setWorldCoords(-150, -150, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 500, 0, 500, {
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
    basic11.rotate(170)
    basic11.translate(0, 20)
    
    basic12 = cmbr.dup()
    basic12.rotate(163)
    basic12.translate(3.5, 40)
    
    basic13 = cmbr.dup()
    basic13.rotate(90)
    basic13.translate(10, 59)
    
    basic14 = cmbr.dup()
    basic14.rotate(15)
    basic14.translate(30, 59)
    
    basic15 = cmbr.dup()
    basic15.rotate(10)
    basic15.translate(36, 39)
    
    basic16 = cmbr.dup()
    basic16.rotate(0)
    basic16.translate(40, 20)
    
    basic17 = cmbr.dup()
    basic17.rotate(0)
    basic17.translate(40, 0)
    
    basic18 = cmbr.dup()
    basic18.rotate(90)
    basic18.translate(0, 0)
    
    basic19 = cmbr.dup()
    basic19.rotate(90)
    basic19.translate(20, 0)
    
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(60, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(0)
    basic21.translate(60, 20)
    
    basic22 = cmbr.dup()
    basic22.rotate(170)
    basic22.translate(60, 20)
    
    basic23 = cmbr.dup()
    basic23.rotate(163)
    basic23.translate(63.5, 40)
    
    basic24 = cmbr.dup()
    basic24.rotate(90)
    basic24.translate(70, 59)
    
    basic25 = cmbr.dup()
    basic25.rotate(15)
    basic25.translate(90, 59)
    
    basic26 = cmbr.dup()
    basic26.rotate(10)
    basic26.translate(96, 39)
    
    basic27 = cmbr.dup()
    basic27.rotate(0)
    basic27.translate(100, 20)
    
    basic28 = cmbr.dup()
    basic28.rotate(0)
    basic28.translate(100, 0)
    
    basic29 = cmbr.dup()
    basic29.rotate(90)
    basic29.translate(60, 0)
    
    basic30 = cmbr.dup()
    basic30.rotate(90)
    basic30.translate(80, 0)
    
    basic31 = cmbr.dup()
    basic31.rotate(0)
    basic31.translate(120, 0)
    
    basic32 = cmbr.dup()
    basic32.rotate(0)
    basic32.translate(120, 20)
    
    basic33 = cmbr.dup()
    basic33.rotate(170)
    basic33.translate(120, 20)
    
    basic34 = cmbr.dup()
    basic34.rotate(163)
    basic34.translate(123.5, 40)
    
    basic35 = cmbr.dup()
    basic35.rotate(90)
    basic35.translate(130, 59)
    
    basic36 = cmbr.dup()
    basic36.rotate(15)
    basic36.translate(150, 59)
    
    basic37 = cmbr.dup()
    basic37.rotate(10)
    basic37.translate(156, 39)
    
    basic38 = cmbr.dup()
    basic38.rotate(0)
    basic38.translate(160, 20)
    
    basic39 = cmbr.dup()
    basic39.rotate(0)
    basic39.translate(160, 0)
    
    basic40 = cmbr.dup()
    basic40.rotate(90)
    basic40.translate(120, 0)
    
    basic41 = cmbr.dup()
    basic41.rotate(90)
    basic41.translate(140, 0)
    
    basic42 = cmbr.dup()
    basic42.rotate(0)
    basic42.translate(180, 0)
    
    basic43 = cmbr.dup()
    basic43.rotate(0)
    basic43.translate(180, 20)
    
    basic44 = cmbr.dup()
    basic44.rotate(170)
    basic44.translate(180, 20)
    
    basic45 = cmbr.dup()
    basic45.rotate(163)
    basic45.translate(183.5, 40)
    
    basic46 = cmbr.dup()
    basic46.rotate(90)
    basic46.translate(190, 59)
    
    basic47 = cmbr.dup()
    basic47.rotate(15)
    basic47.translate(210, 59)
    
    basic48 = cmbr.dup()
    basic48.rotate(10)
    basic48.translate(216, 39)
    
    basic49 = cmbr.dup()
    basic49.rotate(0)
    basic49.translate(220, 20)
    
    basic50 = cmbr.dup()
    basic50.rotate(0)
    basic50.translate(220, 0)
    
    basic51 = cmbr.dup()
    basic51.rotate(90)
    basic51.translate(180, 0)
    
    basic52 = cmbr.dup()
    basic52.rotate(90)
    basic52.translate(200, 0)
    
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    cmbr.appendPath(basic46)
    cmbr.appendPath(basic47)
    cmbr.appendPath(basic48)
    cmbr.appendPath(basic49)
    cmbr.appendPath(basic50)
    cmbr.appendPath(basic51)
    cmbr.appendPath(basic52)
    
    
     # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 20, 0, 0, 0, "black", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task1"></script>

</body>
</html>
'''
    return outstring
    
@ag1_40323105.route('/b')
def task2():
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

cgo.setWorldCoords(-150, -150, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 500, 0, 500, {
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
    
    basic01 = cmbr.dup()
    basic01.rotate(0)
    basic01.translate(0, 20)
    
    basic02 = cmbr.dup()
    basic02.rotate(0)
    basic02.translate(0, 40)
    
    basic03 = cmbr.dup()
    basic03.rotate(0)
    basic03.translate(0, 60)
    
    basic04 = cmbr.dup()
    basic04.rotate(90)
    basic04.translate(0, 60)
    
    basic05 = cmbr.dup()
    basic05.rotate(60)
    basic05.translate(20, 60)
    
    basic06 = cmbr.dup()
    basic06.rotate(180)
    basic06.translate(37, 30)
    
    basic07 = cmbr.dup()
    basic07.rotate(90)
    basic07.translate(0, 20)
    
    basic08 = cmbr.dup()
    basic08.rotate(120)
    basic08.translate(20, 20)
    
    basic09 = cmbr.dup()
    basic09.rotate(60)
    basic09.translate(20, 20)
    
    basic10 = cmbr.dup()
    basic10.rotate(0)
    basic10.translate(37, 10)
    
    basic11 = cmbr.dup()
    basic11.rotate(90)
    basic11.translate(0, -20)
    
    basic12 = cmbr.dup()
    basic12.rotate(120)
    basic12.translate(20, -20)
   
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(60, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(0)
    basic21.translate(60, 20)
    
    basic22 = cmbr.dup()
    basic22.rotate(170)
    basic22.translate(60, 20)
    
    basic23 = cmbr.dup()
    basic23.rotate(163)
    basic23.translate(63.5, 40)
    
    basic24 = cmbr.dup()
    basic24.rotate(90)
    basic24.translate(70, 59)
    
    basic25 = cmbr.dup()
    basic25.rotate(15)
    basic25.translate(90, 59)
    
    basic26 = cmbr.dup()
    basic26.rotate(10)
    basic26.translate(96, 39)
    
    basic27 = cmbr.dup()
    basic27.rotate(0)
    basic27.translate(100, 20)
    
    basic28 = cmbr.dup()
    basic28.rotate(0)
    basic28.translate(100, 0)
    
    basic29 = cmbr.dup()
    basic29.rotate(90)
    basic29.translate(60, 0)
    
    basic30 = cmbr.dup()
    basic30.rotate(90)
    basic30.translate(80, 0)
    
    basic60 = cmbr.dup()
    basic60.rotate(0)
    basic60.translate(120, 0)
    
    basic61 = cmbr.dup()
    basic61.rotate(0)
    basic61.translate(120, 20)
    
    basic62 = cmbr.dup()
    basic62.rotate(0)
    basic62.translate(120, 40)
    
    basic63 = cmbr.dup()
    basic63.rotate(0)
    basic63.translate(120, 60)
    
    basic64 = cmbr.dup()
    basic64.rotate(90)
    basic64.translate(120, 60)
    
    basic65 = cmbr.dup()
    basic65.rotate(55)
    basic65.translate(140, 60)
    
    basic66 = cmbr.dup()
    basic66.rotate(30)
    basic66.translate(156, 49)
    
    basic67 = cmbr.dup()
    basic67.rotate(0)
    basic67.translate(166, 32)
    
    basic68 = cmbr.dup()
    basic68.rotate(330)
    basic68.translate(166, 12)
    
    basic69 = cmbr.dup()
    basic69.rotate(90)
    basic69.translate(120,-20)
    
    basic70 = cmbr.dup()
    basic70.rotate(315)
    basic70.translate(155,-6)
    
    basic71 = cmbr.dup()
    basic71.rotate(90)
    basic71.translate(220,-20)
    
    basic72 = cmbr.dup()
    basic72.rotate(235)
    basic72.translate(220,-20)
    
    basic73 = cmbr.dup()
    basic73.rotate(200)
    basic73.translate(203,-8)
    
    basic74 = cmbr.dup()
    basic74.rotate(180)
    basic74.translate(196,10)
    
    basic75 = cmbr.dup()
    basic75.rotate(160)
    basic75.translate(196,30)
    
    basic76 = cmbr.dup()
    basic76.rotate(125)
    basic76.translate(203,49)
    
    basic77 = cmbr.dup()
    basic77.rotate(90)
    basic77.translate(220,60)
    
    cmbr.appendPath(basic01)
    cmbr.appendPath(basic02)
    cmbr.appendPath(basic03)
    cmbr.appendPath(basic04)
    cmbr.appendPath(basic05)
    cmbr.appendPath(basic06)
    cmbr.appendPath(basic07)
    cmbr.appendPath(basic08)
    cmbr.appendPath(basic09)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic60)
    cmbr.appendPath(basic61)
    cmbr.appendPath(basic62)
    cmbr.appendPath(basic63)
    cmbr.appendPath(basic64)
    cmbr.appendPath(basic65)
    cmbr.appendPath(basic66)
    cmbr.appendPath(basic67)
    cmbr.appendPath(basic68)
    cmbr.appendPath(basic69)
    cmbr.appendPath(basic70)
    cmbr.appendPath(basic71)
    cmbr.appendPath(basic72)
    cmbr.appendPath(basic73)
    cmbr.appendPath(basic74)
    cmbr.appendPath(basic75)
    cmbr.appendPath(basic76)
    cmbr.appendPath(basic77)
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 20, 0, 0, 0, "black", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task2"></script>

</body>
</html>
'''
    return outstring
    
@ag1_40323105.route('/C')
def task3():
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

cgo.setWorldCoords(-150, -300, 700, 700) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 300, 0, 500, {
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
    
    basic01 = cmbr.dup()
    basic01.rotate(0)
    basic01.translate(0, 20)
    
    basic02 = cmbr.dup()
    basic02.rotate(0)
    basic02.translate(0, 40)
    
    basic03 = cmbr.dup()
    basic03.rotate(0)
    basic03.translate(0, 60)
    
    basic04 = cmbr.dup()
    basic04.rotate(90)
    basic04.translate(0, 60)
    
    basic05 = cmbr.dup()
    basic05.rotate(60)
    basic05.translate(20, 60)
    
    basic06 = cmbr.dup()
    basic06.rotate(180)
    basic06.translate(37, 30)
    
    basic07 = cmbr.dup()
    basic07.rotate(90)
    basic07.translate(0, 20)
    
    basic08 = cmbr.dup()
    basic08.rotate(120)
    basic08.translate(20, 20)
    
    basic09 = cmbr.dup()
    basic09.rotate(60)
    basic09.translate(20, 20)
    
    basic10 = cmbr.dup()
    basic10.rotate(0)
    basic10.translate(37, 10)
    
    basic11 = cmbr.dup()
    basic11.rotate(90)
    basic11.translate(0, -20)
    
    basic12 = cmbr.dup()
    basic12.rotate(120)
    basic12.translate(20, -20)
   
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(0, 120)
    
    basic21 = cmbr.dup()
    basic21.rotate(0)
    basic21.translate(0, 140)
    
    basic22 = cmbr.dup()
    basic22.rotate(170)
    basic22.translate(0, 140)
    
    basic23 = cmbr.dup()
    basic23.rotate(163)
    basic23.translate(3.5, 160)
    
    basic24 = cmbr.dup()
    basic24.rotate(90)
    basic24.translate(10, 179)
    
    basic25 = cmbr.dup()
    basic25.rotate(15)
    basic25.translate(30, 179)
    
    basic26 = cmbr.dup()
    basic26.rotate(10)
    basic26.translate(36, 159)
    
    basic27 = cmbr.dup()
    basic27.rotate(0)
    basic27.translate(40, 140)
    
    basic28 = cmbr.dup()
    basic28.rotate(0)
    basic28.translate(40, 120)
    
    basic29 = cmbr.dup()
    basic29.rotate(90)
    basic29.translate(0, 120)
    
    basic30 = cmbr.dup()
    basic30.rotate(90)
    basic30.translate(20, 120)
    
    basic71 = cmbr.dup()
    basic71.rotate(90)
    basic71.translate(24,-130)
    
    basic72 = cmbr.dup()
    basic72.rotate(235)
    basic72.translate(24,-130)
    
    basic73 = cmbr.dup()
    basic73.rotate(200)
    basic73.translate(7,-118)
    
    basic74 = cmbr.dup()
    basic74.rotate(180)
    basic74.translate(0,-100)
    
    basic75 = cmbr.dup()
    basic75.rotate(160)
    basic75.translate(0,-80)
    
    basic76 = cmbr.dup()
    basic76.rotate(125)
    basic76.translate(7,-61)
    
    basic77 = cmbr.dup()
    basic77.rotate(90)
    basic77.translate(24,-50)
    
    basic60 = cmbr.dup()
    basic60.rotate(0)
    basic60.translate(0, -220)
    
    basic61 = cmbr.dup()
    basic61.rotate(0)
    basic61.translate(0, -200)
    
    basic62 = cmbr.dup()
    basic62.rotate(0)
    basic62.translate(0, -180)
    
    basic63 = cmbr.dup()
    basic63.rotate(0)
    basic63.translate(0, -160)
    
    basic64 = cmbr.dup()
    basic64.rotate(90)
    basic64.translate(0, -160)
    
    basic65 = cmbr.dup()
    basic65.rotate(55)
    basic65.translate(20, -160)
    
    basic66 = cmbr.dup()
    basic66.rotate(30)
    basic66.translate(36, -171)
    
    basic67 = cmbr.dup()
    basic67.rotate(0)
    basic67.translate(46, -188)
    
    basic68 = cmbr.dup()
    basic68.rotate(330)
    basic68.translate(46, -208)
    
    basic69 = cmbr.dup()
    basic69.rotate(90)
    basic69.translate(0,-240)
    
    basic70 = cmbr.dup()
    basic70.rotate(315)
    basic70.translate(35,-226)
    
    
    
    cmbr.appendPath(basic01)
    cmbr.appendPath(basic02)
    cmbr.appendPath(basic03)
    cmbr.appendPath(basic04)
    cmbr.appendPath(basic05)
    cmbr.appendPath(basic06)
    cmbr.appendPath(basic07)
    cmbr.appendPath(basic08)
    cmbr.appendPath(basic09)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic60)
    cmbr.appendPath(basic61)
    cmbr.appendPath(basic62)
    cmbr.appendPath(basic63)
    cmbr.appendPath(basic64)
    cmbr.appendPath(basic65)
    cmbr.appendPath(basic66)
    cmbr.appendPath(basic67)
    cmbr.appendPath(basic68)
    cmbr.appendPath(basic69)
    cmbr.appendPath(basic70)
    cmbr.appendPath(basic71)
    cmbr.appendPath(basic72)
    cmbr.appendPath(basic73)
    cmbr.appendPath(basic74)
    cmbr.appendPath(basic75)
    cmbr.appendPath(basic76)
    cmbr.appendPath(basic77)
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 20, 0, 0, 0, "black", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task3"></script>

</body>
</html>
'''
    return outstring
    
