#!/usr/bin/python
# 導入 os 模組, 主要用來判斷是否在 OpenShift 上執行
import os
# 導入同目錄下的 myflaskapp.py
import myflaskapp
    
# 以下開始判斷在 OpenShift 或近端執行
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    application = myflaskapp.app
else:
    # 表示在近端執行, 以 python3 wsgi.py 執行,  若採 uwsgi 則與 Openshift 運作模式相同
    myflaskapp.app.run(debug=True)

