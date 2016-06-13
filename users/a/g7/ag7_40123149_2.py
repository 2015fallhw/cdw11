# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template, make_response

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag7_40123149_2 = Blueprint('ag7_40123149_2', __name__, url_prefix='/ag7_40123149', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag7_40123149_2.route('/ag7_40123149_2')
def one():
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
    # 輪廓的外型設為 class variable
    chamber = "M -6.8397, -1.4894             A 7, 7, 0, 1, 0, 6.8397, -1.4894             A 40, 40, 0, 0, 1, 6.8397, -18.511             A 7, 7, 0, 1, 0, -6.8397, -18.511             A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    #chamber = "M 0, 0 L 0, -20 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    def __init__(self, fillcolor="green", border=True, strokecolor= "tan", linewidth=2, scale=1):
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
        # 注意, cgoChamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole0 為原點位置
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

mychain = chain()
 
x1, y1 = mychain.basic_rot(50,0, 78, True)
#x1, y1 = mychain.basic_rot(50,0, 78)
x2, y2=mychain.basic_rot(x1, y1, 180-24, True) 
x3, y3=mychain.basic_rot(x2, y2, 180-36, True) 
x4, y4=mychain.basic_rot(x3, y3, 180-48, True) 
x5, y5=mychain.basic_rot(x4, y4, 180-60, True) 
x6, y6=mychain.basic_rot(x5, y5, 180-72, True) 
x7, y7=mychain.basic_rot(x6, y6, 180-84, True) 
x8, y8=mychain.basic_rot(x7, y7, 180-96) 
x9, y9=mychain.basic_rot(x8, y8, 180-108) 
x10, y10=mychain.basic_rot(x9, y9, 180-120) 
x11, y11=mychain.basic_rot(x10, y10, 180-132) 
x12, y12=mychain.basic_rot(x11, y11, 180-144) 
x13, y13=mychain.basic_rot(x12, y12, 180-156) 
x14, y14=mychain.basic_rot(x13, y13, 180-168) 
x15, y15=mychain.basic_rot(x14, y14, 180-180) 
x16, y16=mychain.basic_rot(x15, y15, 180-192) 
x17, y17=mychain.basic_rot(x16, y16, 180-204) 
x18, y18=mychain.basic_rot(x17, y17, 180-216) 
x19, y19=mychain.basic_rot(x18, y18, 180-228) 
x20, y20=mychain.basic_rot(x19, y19, 180-240) 
x21, y21=mychain.basic_rot(x20, y20, 180-252) 
x22, y22=mychain.basic_rot(x21, y21, 180-264) 
x23, y23=mychain.basic_rot(x22, y22, 180-276, True) 
x24, y24=mychain.basic_rot(x23, y23, 180-288, True) 
x25, y25=mychain.basic_rot(x24, y24, 180-300, True) 
x26, y26=mychain.basic_rot(x25, y25, 180-312, True) 
x27, y27=mychain.basic_rot(x26, y26, 180-324, True) 
x28, y28=mychain.basic_rot(x27, y27, 180-336, True) 
x29, y29=mychain.basic_rot(x28, y28, 180-348, True) 
x30, y30=mychain.basic_rot(x29, y29, 180-360, True) 

#mychain = chain()
 
p1, k1 = mychain.basic_rot(73.5,-185, 160)
p2, k2=mychain.basic_rot(p1, k1, 180-40) 
p3, k3=mychain.basic_rot(p2, k2, 180-60) 
p4, k4=mychain.basic_rot(p3, k3, 180-80) 
p5, k5=mychain.basic_rot(p4, k4, 180-100, True) 
p6, k6=mychain.basic_rot(p5, k5, 180-120, True) 
p7, k7=mychain.basic_rot(p6, k6, 180-140, True) 
p8, k8=mychain.basic_rot(p7, k7, 180-160, True) 
p9, k9=mychain.basic_rot(p8, k8, 180-180, True) 
p10, k10=mychain.basic_rot(p9, k9, 180-200, True) 
p11, k11=mychain.basic_rot(p10, k10, 180-220, True) 
p12, k12=mychain.basic_rot(p11, k11, 180-240, True) 
p13, k13=mychain.basic_rot(p12, k12, 180-260, True) 
p14, k14=mychain.basic_rot(p13, k13, 180-280) 
p15, k15=mychain.basic_rot(p14, k14, 180-300) 
p16, k16=mychain.basic_rot(p15, k15, 180-320) 
p17, k17=mychain.basic_rot(p16, k16, 180-340) 
p18, k18=mychain.basic_rot(p17, k17, 180-360) 

m1, n1 = mychain.basic_rot(p4, k4, 100)
m2, n2=mychain.basic_rot(m1, n1, 100)
m3, n3=mychain.basic_rot(m2, n2, 100)
m4, n4=mychain.basic_rot(m3, n3, 100)
m5, n5=mychain.basic_rot(m4, n4, 100)
m6, n6=mychain.basic_rot(m5, n5, 100)
m7, n7=mychain.basic_rot(m6, n6, 100)
m8, n8=mychain.basic_rot(m7, n7, 100)
m9, n9=mychain.basic_rot(m8, n8, 100)
m10, n10=mychain.basic_rot(m9, n9, 100)
m11, n11=mychain.basic_rot(m10, n10, 100)

r1, s1 = mychain.basic_rot(p13, k13, 80)
r2, s2=mychain.basic_rot(r1, s1, 80)
r3, s3=mychain.basic_rot(r2, s2, 80)
r4, s4=mychain.basic_rot(r3, s3, 80)
r5, s5=mychain.basic_rot(r4, s4, 80)
r6, s6=mychain.basic_rot(r5, s5, 80)
r7, s7=mychain.basic_rot(r6, s6, 80)
r8, s8=mychain.basic_rot(r7, s7, 80)
r9, s9=mychain.basic_rot(r8, s8, 80)
r10, s10=mychain.basic_rot(r9, s9, 80)
r11, s11=mychain.basic_rot(r10, s10, 80)
mychain.basic(x7, y7, m11, n11)
mychain.basic(x22, y22, r11, s11)

</script>
</body>
</html>

'''
    return outstring

