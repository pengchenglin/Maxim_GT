# Maxim_GT
通过GT实现app的性能数据采集，结合maxim实现高速monkey

参考：

[[广播方式使用GT]](https://github.com/Tencent/GT/blob/master/android/GT_APP/app/docs/UseGtWithBroadcast.txt)

[(无需 Root) 基于 Android Monkey 二次开发，实现高速点击的 Android Monkey 自动化工具 fastmonkey - 代号 Maxim](https://testerhome.com/topics/11719)



#### **工程说明**

*-Public*		

  ​*command.py*       		adb_shell相关的命令方法

  ​	*gt.py*			   	GT通过广播方式实现性能的采集

  ​	*Maxim_monkey.py*	    	Maxim fast monkey的一些功能配置

*-Maxim*  		（maxim的一些配置文件）

  ​	*awl.strings*：			存放activity白名单

  ​	*max.xpath.actions*：	特殊事件序列 

  ​	*max.xpath.selecto*r：	TROY模式（支持特殊事件、黑控件等） 配置 

  ​	*max.xpath.selector*：	 troy控件选择子来定制自有的控件选择优先级

  ​	*max.widget.black*：	黑控件 黑区域屏蔽

  ​	*max.strings* ：		随机输入字符，内容可自定义配置

*-GT-Report*	（GThtml报告的模板，替换data/data.js即可）

  *-example*		（自动化执行脚本，Run_monkey.py）

  *-apk*		        （存放一些必须的apk）



#### **操作说明**

**注意**：手机安装好GT App    被测app需要集成GT SDk才能采集到数据！！！！

1、编辑`example/Run_monkey.py`修改被测试app的包名后，直接运行`Run_monkey.py`或者Windows直接执行`run.bat`      *Maxim().command*的相关参数设置 请参照*Maxim_monkey.py*中的注释

2、等待执行完成后，打开手机的GT App 导出数据 ，选择指定的文件夹

3、导出成功过后，执行`get_report.py`或者直接运行`get_repor.bat`









