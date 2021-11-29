

高鸿成 | 重庆大学计算机学院

Gao Hongcheng | College of Computer Science, Chongqing University

# IDE远程服务器连接使用教程

本文介绍了VScode与Pycharm上进行远程连接后的文件管理与编程等操作，包括了基础连接的使用方法与各种附加的细节功能。从笔者经验来看，更推荐使用vscode进行远程连接。

## 1 VScode 远程连接服务器

### 1.1 安装远程连接插件

 1. 打开VScode

<img src="pic/image-20211110205126634.png" alt="image-20211110205126634" style="zoom: 33%;" />

2. 点击左边的扩展中心（Extensions） 

   > 快捷键：ctrl+shift+x

   <img src="pic/image-20211110205226236.png" alt="image-20211110205226236" style="zoom:50%;" />

   此时会弹出扩展中心的界面

   <img src="pic/image-20211110205424647.png" alt="image-20211110205424647" style="zoom:50%;" />

3. 在搜索栏输入ssh，我们可以看到有一个名为 Romote -SSH的插件

   <img src="pic/image-20211110205616167.png" alt="image-20211110205616167" style="zoom:50%;" />

4. 点击右下角蓝色的Install便进入安装

   ![image-20211110210408791](pic/image-20211110210408791.png)

5. 安装完成后，左侧将出现如下标志，即安装完成。

   > 如果没有出现该标志，可以关闭VScode再重启

   <img src="pic/image-20211110210548314.png" alt="image-20211110210548314" style="zoom:50%;" />

### 1.2 配置远程服务器

1. 点击进入上图（第一阶段第5步）的插件，然后在远程资源管理器中选中SSH target（如下图）。

   <img src="pic/image-20211110211323071.png" alt="image-20211110211323071" style="zoom:50%;" />

2. 点击设置按钮

   > 需要把鼠标放到SSH TARGETS这一行他才会显示设置按钮

   ![image-20211110211107230](pic/image-20211110211107230.png)

3. 右边会跳出下图所示的下拉栏，点击第一个即可

   <img src="pic/image-20211110211200366.png" alt="image-20211110211200366" style="zoom:33%;" />

4. 进入该文件后，将内容改成如下

   ![image-20211110211552076](pic/image-20211110211552076.png)

   （1）Host为我们想给主机取的名，随便取就好，我这里取的华为；

   （2）Hostname是主机地址，这个可以在华为服务器的控制台里看到，复制下来粘贴进来就好；

   <img src="pic/image-20211110212228057.png" alt="image-20211110212228057" style="zoom:33%;" />

   （3）user是你登录的用户名，从实验1到现在，如果没有自己新增用户，应该只有root和hadoop。建议用hadoop就行。

   然后 ctrl+s 保存即可。

5. 此时左边会弹出你新增的服务器名称，即配置成功

   <img src="pic/image-20211110212611680.png" alt="image-20211110212611680" style="zoom:50%;" />

6. 你也可以添加多个服务器，如下：

   ![image-20211110212816741](pic/image-20211110212816741.png)

   添加端口号的方法如下：

   ![image-20211110212939355](pic/image-20211110212939355.png)

### 1.3 连接服务器

1. 鼠标放在服务器名字栏上，点击右边的如下符号（注意，鼠标放上去才会出现该符号）

<img src="pic/image-20211110213107911.png" alt="image-20211110213107911" style="zoom:67%;" />

2. 此时会弹出新界面并让你在上方输入该服务器账户的密码

   <img src="pic/image-20211110213252416.png" alt="image-20211110213252416" style="zoom: 33%;" />

3. 输入完成后点击Enter，稍等几秒钟。登陆成功之后会是如下界面

   <img src="pic/image-20211110213443225.png" alt="image-20211110213443225" style="zoom: 33%;" />

   注意下面是TERMINAL（终端）窗口。

### 1.4 玩转Remote SSH

1. 终端就可以被认为是一个华为云ssh连接的界面，你可以在上面进行之前的所有操作。

   例如：

   <img src="pic/image-20211110214537719.png" alt="image-20211110214537719" style="zoom:50%;" />

2. 你可以同时开多个终端，点击下图的加号即可

   <img src="pic/image-20211110214657329.png" alt="image-20211110214657329" style="zoom:50%;" />

3. 打开文件夹：点击左边的“打开文件夹”，然后在右边选择你想打开的地址（注意是服务器上的地址）

   <img src="pic/image-20211110214755034.png" alt="image-20211110214755034" style="zoom: 33%;" />

   打开之后，左边就会显示此目录下的文件，你就可以像在本地使用vscode一样使用服务器来编程了。

   <img src="pic/image-20211110215014831.png" alt="image-20211110215014831" style="zoom:33%;" />

   例如：添加文件：

​		A.

<img src="pic/image-20211110215055817.png" alt="image-20211110215055817" style="zoom: 50%;" />

​		B. 

<img src="pic/image-20211110215130060.png" alt="image-20211110215130060" style="zoom: 33%;" />

4.  编写python代码：在左边添加py文件，右边就可以编写具体代码了。

   > 同时，你也可以编写jupyter类型的py文件，只需要左边新建.ipynb文件，然后右边会自动提示你安装相应插件，就能在vscode里玩转jupyter了

   <img src="pic/image-20211110215311930.png" alt="image-20211110215311930" style="zoom: 33%;" />

   到此，你就可以结合ssh终端与vscode强大的编辑能力完成接下来的实验了。



## 2. Pycharm 远程连接服务器

### 2.1 新建project

> 这一步不是必须的，可以跳过

1. 打开pycharm

<img src="pic/image-20211112134115792.png" style="zoom: 33%;" />

2. 在file里点击New Project

<img src="pic/image-20211112134143210.png" style="zoom:33%;" />

3. 设置新建位置并点击create便能建立一个新的project

<img src="pic/image-20211112134206476.png" style="zoom:33%;" />

### 2.2 SSH终端连接

1. 点击Tools→Start SSH Session

<img src="pic/image-20211112134454191.png" alt="image-20211112134454191" style="zoom:33%;" />

2.在弹出来的窗口点击第一行“Edit credentials”

<img src="pic/image-20211112134537040.png" alt="image-20211112134537040" style="zoom:33%;" />

3. 在弹出来的窗口输入主机地址，用户名（这些都是之前在华为云服务器上设置的），输入用户名对应的密码，端口一般用22。然后点击“OK”

   > 当然认证方式也可以不使用Password，例如公钥的方法也是ok的

<img src="pic/image-20211112134625648.png" alt="image-20211112134625648" style="zoom:33%;" />

4. 接下来就可以在下面的Terminal里看到与服务器的连接了，这里就可以视作之前的ssh窗口，可以进行在服务器上的所有操作

<img src="pic/image-20211112134638980.png" alt="image-20211112134638980" style="zoom: 33%;" />

### 2.3 远程主机目录显示

1. 点击右边的Remote Host

<img src="pic/image-20211112134838705.png" alt="image-20211112134838705" style="zoom:33%;" />

2. 输入对应host, 密码等信息，点击OK

   > 一般默认就填满了 只需要点OK。如果要自己填，就按如下来填就好

<img src="pic/image-20211112134853776.png" alt="image-20211112134853776" style="zoom:33%;" />

3. 此时就可以看到服务器上的文件目录了

   <img src="pic/image-20211112134943744.png" alt="image-20211112134943744" style="zoom:33%;" />

### 2.4 代码的编写、同步、运行

1. 点击File→Settings

<img src="pic/image-20211112135004380.png" alt="image-20211112135004380" style="zoom:33%;" />

2. 在弹出来的窗口找到左边的project interpreter并点击，然后在右边点击如下的设置按钮

<img src="pic/image-20211112135330815.png" alt="image-20211112135330815" style="zoom:33%;" />

3. 选择添加
4. <img src="pic/image-20211112135349765.png" alt="image-20211112135349765" style="zoom:33%;" />

4. 在弹出来的窗口里点击SSH Interpreter，输入主机号与用户名，点击Next

<img src="pic/image-20211112135403358.png" alt="image-20211112135403358" style="zoom:50%;" />

5. 输入密码（或通过Key pair方法），点击Next

   <img src="pic/image-20211112135423872.png" alt="image-20211112135423872" style="zoom:33%;" />

6. 在新的界面里，有两个地方要修改，修改完后应该呈现为第8步的样子，可以先到后面看一下。两个修改的地方，第一个是Interpreter，点击Interpreter最右边的文件夹图标，就会有下图的弹窗。

   一般来说，你的编译器都是在bin里的，因此在bin里找到python3即可，然后确认

<img src="pic/image-20211112135700024.png" alt="image-20211112135700024" style="zoom:33%;" />

7. 确认后，就需要第二个要修改的地方了，点击界面里Sync foders右边的文件夹图标，弹出下图

<img src="pic/image-20211112140024663.png" alt="image-20211112140024663" style="zoom:33%;" />

将remote path里修改为服务器上有的地址，我自己建了个test文件夹，所以就把地址改为的/tmp/test

8. 修改完后，就是如下如所示，点击finish

<img src="pic/image-20211112140036669.png" alt="image-20211112140036669" style="zoom:33%;" />

9. 到此界面，再次点击OK

<img src="pic/image-20211112140106110.png" alt="image-20211112140106110" style="zoom:33%;" />

10. 此时就会开始本地与服务器的同步了

<img src="pic/image-20211112140117706.png" alt="image-20211112140117706" style="zoom: 25%;" />

<img src="pic/image-20211112140228054.png" alt="image-20211112140228054" style="zoom: 25%;" />

<img src="pic/image-20211112140454101.png" alt="image-20211112140454101" style="zoom:33%;" />

10. 同步完成后，在project里建立一个python文件就可以开始编辑代码操作了

    <img src="pic/image-20211112140528214.png" alt="image-20211112140528214" style="zoom:33%;" />

11.编辑完后，在右上角选择编译器

<img src="pic/image-20211112140552911.png" alt="image-20211112140552911" style="zoom:33%;" />

12. 选择python

<img src="pic/image-20211112140611404.png" alt="image-20211112140611404" style="zoom:33%;" />

13. 右边上面的红框为你需要编译的python文件的地址，下面的红框为工程工作的地方，这两个地方都需要修改为服务器上他们分布的相对地址。

    > 这个相对地址是有技巧来得到的，你可以用我们之前2.3节在右边显示的文件目录来获得：
    >
    > 1. 首先我们知道存放此project的服务器里的隐射地址（前面第7步自己设的）
    > 2. 在右边目录树里进入该地址
    > 3. 右键选择复制相对地址就行

    我这里是把上面修改到“/tmp/test/venv/test.py“ 这是该程序在我的服务器上的地址。 下面修改为“/tmp/test/venv”，这是我希望在我服务器上工作的地址。 

<img src="pic/image-20211112140732450.png" alt="image-20211112140732450" style="zoom:33%;" />

14. 修改interpreter为我们前面设置的服务器上的编译器

<img src="pic/image-20211112140820912.png" alt="image-20211112140820912" style="zoom:33%;" />

15. 修改完成后如下，点击OK

<img src="pic/image-20211112140944955.png" alt="image-20211112140944955" style="zoom:33%;" />

16. 点击右上角的绿色三角形运行即可

<img src="pic/image-20211112141020689.png" alt="image-20211112141020689" style="zoom:33%;" />

现在就大功告成了，接下来就可以尽情使用了