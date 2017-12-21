# Python
<div>练习一：爬取知乎live</div>
<div>1.爬取知乎live要cookie登录，否则得不到所有的live。</div>
<div>2.知乎live页面是异步加载，需要获取异步加载链接。</div>
<div>3.打开链接发现“https://api.zhihu.com/lives/homefeed?limit=10&amp;offset=10”，得知每页限制10个，偏移也为10个。</div>
<div>4.把所有live数据显示在同一页（设置offset=0，limit=200）注意：live数要自己测（通过live）</div>
<div>5.把数据存入数据库Mysql</div>
