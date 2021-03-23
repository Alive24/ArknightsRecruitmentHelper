# ArknightsRecruitmentHelper
ArknightsRecruitmentHelper

## 使用方法

0. 点击更新数据按钮获取最新的数据
1. 在句柄处选择浏览器，如果没有可选择的选项请点刷新按钮
2. 打开公开招募选择tag的界面后，点击手动识别分析
3. 右侧会显示单Tag或双Tag可以锁定四星或以上的招募方案


## 编译方法
1. 创建适合的python环境（开发环境下为conda建立的python3.7虚拟环境）
2. 使用`pip install -r requirements.txt`安装环境
3. 使用`pyinstaller .\main.spec`以文件夹形式编译（启动速度更快）或使用`pyinstaller .\main-onefile.spec`以单文件形式编译（启动速度稍慢）
4. 打包后需要添加若干dll文件，具体是`~\anaconda3\envs\ArknightsRecruitmentHelper\Lib\site-packages\mxnet`下的所有dll文件即可。