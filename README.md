# Wi-Fi Reconnector

### 功能

每隔一段时间检测网络连接是否正常。
如果不正常（无法访问百度），断开wifi，重连。

### 用法

1. 安装 `git clone https://github.com/froyog/wifi-reconnector.git`
2. 执行 `python index.py`
3. 选项 设置 `reconnector = Reconnector(ssid, timeout)`
    - ssid: 要断开重连的路由器ssid，无默认值
    - timeout: 轮询时间，默认为30秒