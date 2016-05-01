import os
# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
    static_dir = os.environ['OPENSHIFT_REPO_DIR']+"/static"
else:
    # 表示程式在近端執行
    data_dir = _curdir + "/local_data/"
    static_dir = _curdir + "/static"
class Init(object):
    def __init__(self):
        # hope to create downloads and images directories　
        if not os.path.isdir(data_dir+"downloads"):
            try:
                os.makedirs(data_dir+"downloads")
            except:
                print("mkdir error")
        if not os.path.isdir(data_dir+"images"):
            try:
                os.makedirs(data_dir+"images")
            except:
                print("mkdir error")


