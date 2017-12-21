# Python
练习一：爬取知乎live
1.爬取知乎live要cookie登录，否则得不到所有的live。
2.知乎live页面是异步加载，需要获取异步加载链接。
3.打开链接发现“https://api.zhihu.com/lives/homefeed?limit=10&offset=10”，得知每页限制10个，偏移也为10个。
4.把所有live数据显示在同一页（设置offset=0，limit=200）注意：live数要自己测（通过live）
5.把数据存入数据库Mysql
