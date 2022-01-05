<h1 align='center'>实验五：基于爬虫和华为云的命名实体识别</h1>

<h5 align='center'> Design by ZJY| Direct by Prof. Feng</h5>

## 1 实验目的

通过本次实验，你应该：

- 掌握基于爬虫`Spider` 的数据收集、数据清洗工作
- 通过`Python`编程来发送`POST`请求以及处理识别结果
- 可以通过华为云所提供的`API`接口调用相关服务
- 对自然语言处理相关内容有所了解，对文本分析与挖掘等相关内容有一定掌握

本次实验，你将根据代码相关提示完成整个数据集的收集构建以及调用相关接口进行命名实体识别。

## 2 实验准备

### 2.0 成绩说明

本次实验主要是**爬虫+华为云特色相关API**调用，难度不高。因此成绩组成和之前有所不同，**基础成绩给分较低，高分需自行完成扩展实验**：

- 基本成绩（80分）：完整本次实验所有流程即可，未完成部分按具体情况扣分；
- 扩展成绩（20分）：请查看文末扩展实验要求。

### 2.1 实验须知

本次实验基于华为云提供的组件以及同学们通过爬虫自行收集的数据集以进行后续实体识别，由于爬虫版本众多且特点各异：

1. 并不严格要求按照教程中的步骤完成数据集的收集；
2. 同样也不严格限制收集数据主题必须与电影相关，但是总体来说数据集所含文本条目应不少于1000条数据，并且要求数据集的收集应包含发起网页请求、网站解析、数据收集、数据清洗等流程；
3. 数据集的收集过程应在实验报告中有所体现。

:warning: 特别提醒：实验中使用爬虫的目的仅在于获取公开信息以搭建数据集，请勿使用爬虫技术作不正当用途！

### 2.2 包管理

命名实体识别属于自然语言处理领域的基本任务，它可以为我们辅助标注、积累数据，下游任务包括构建知识图谱、问答系统、机器翻译等，高质量的命名实体具有深远影响。

在本次实验中，你可能需要先对相关函数包进行安装，我们通过`pip3`指令进行下载：

```shell
pip3 install requests
pip3 install bs4
pip3 install lxml
pip3 install selenium	
```

为了防止后续版本变更使得指令失灵，我们特地在此给出相关文件的版本，请同学们尽量安装相同版本或者版本相近的文件：

- Python 3.8.5
- bs4 0.0.1、requests 2.26.0、lxml 4.7.1、selenium 4.1.0
- Chrome: 96.0.4664.110 (正式版本) （64 位） (cohort: Stable)

本次实验的数据集将由同学们自行收集，我们需要收集到的样例数据为短文本`txt`格式，以人物数据为例 ，内容示例如下：

    张三的生日是1990年1月1日，身高175cm，出生于北京。
    李四，著名导演，毕业于电影学院，代表作有《电影1》、《电影2》。


## 3 实验步骤
### 3.1 电影名称索引抓取

本次实验主题以电影为例，电影相关的短文本描述将在百度百科上利用爬虫爬取。

同时，在`NLP`的下游任务中所需要的基本数据级以千甚至以万计量，这样量级的电影集难以通过手工逐条收集。我们首先需要在电影门户网站上使用爬虫爬取电影名作为百科查询的索引，但常见的电影数据爬虫大多数是基于豆瓣TOP250进行，但是仅仅250条数据并不能满足数据集的需求。因此我们选择在电影门户网站上对全站的电影做爬虫，收集影库中所有电影名。

特别的：

- 为防止版权问题，<u>全文隐去目标网站</u>，请同学们自行寻找可爬取数据的网站，根据网站内容对代码进行修改；

- 注意，如果直接在百度百科上进行爬取，可能会陷入`A`中的超链指向`B`，再由`B`中的超链指向`A`，或者中间夹杂一些其他超链最终形成回环，从而来回反复收集重复信息的情况。

整体爬虫流程如下：

1. **调试准备**。在影库页面通过`F12`进如调试模式（注意如进行`Debug`时网站自动暂停，可以通过多次刷新解除影响），使用自带调试工具对网页内容进行分析（也可以通过`Ctrl+Shift+C`快捷键），电影名在`module-item-cover`类别下的`a`标签中，为`title`的属性值，也是本次需要爬取的目标。

2. **网页分析**。通过对网页内容进行分析可知，所有电影标题被统一放在`module-items`的`div`标签下，之后各个电影被分配到不同的`module-item`的`div`标签下，而电影标题则属于各个电影`module-item-cover`下的子内容。

   ![电影名](https://blog-imgs-1256686095.cos.ap-guangzhou.myqcloud.com/1.png)

3. **爬虫准备**。在使用爬虫之前，我们先进行`UA`伪装，将我们的访问请求包装成在浏览器环境下的正常访问，相关代码如下：

   ```python
   # UA伪装
   headers = {
       'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
   }
   ```

   我们还需使用`requests`包装我们的访问请求，通过`requests.get()`函数得到响应的html文本内容：

   ```python
   response = requests.get(url, headers=headers)    #url即访问的目标网站，headers为我们之前定义的UA伪装
   html = response.text      #获得响应文件的文本，即目标url的html内容
   ```

   **为了防止目标网站进行反爬虫处理**，导致后续实验失败，我们可以在此时通过`print(html)`命令对获得的`html`文件进行打印，若能够输出`html`文本，再进行后续处理。

4. **爬取信息**。之后需要通过正则匹配对`html`文本进行清洗以获得爬取目标。然而由于`html`文档往往结构复杂、内容繁多，手写的正则表达式稍有差池便需要反复修改，因此我们采用`BeautifulSoup`辅助我们对网页内容进行抓取，关于`BeatifulSoup`，官方文档的解释如下：

   > Beautiful Soup 提供一些简单的、python 式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。 Beautiful Soup 自动将输入文档转换为 Unicode 编码，输出文档转换为 utf-8 编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup 就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。 Beautiful Soup 已成为和 lxml、html6lib 一样出色的 python 解释器，为用户灵活地提供不同的解析策略或强劲的速度。

   我们先创建`BeautifulSoup`对象对`html`文本进行解析，解析器采用`lxml`：

   	soup = BeautifulSoup(html, 'lxml')

   按照我们之前分析的网页源码内容，我们需要对所有`div`标签下的`module-item-cover`进行抓取，我们首先选定内容范围在`module-items`的`div`标签内，之后在该标签内抓取全部类别为`module-item-cover`的`div`标签内容：

   ```python
   all_div = soup.find('div', {'class': 'module-items'}).find_all('div', {'class': 'module-item-cover'})
   ```

   之后我们遍历提取到的`all_div`标签，将`a`标签中的`title`进行内容提取，为了防止反复抓取对目标网站造成不必要的流量浪费，我们直接将影片名称存储到`movies.txt`文件中：

   ```python
   for item in all_div:
       # 提取影片名称
       name = item.find('a')['title']
       # 存储影片名称
       print(name, file=open("movies.txt", "a"))
   ```

   以上步骤即可完成对一个目标`url`所有包含的电影标题进行爬虫获取。

5. **爬取完整信息**。之后我们观察目标网站可知，网站所有的影库页的`url`命名规律为：*”前缀网址 + page页 + ---“*，因此我们对`page`进行循环，按照`page`拼接目标`url`，同时为了防止请求过于频繁引发网站的反爬虫机制，我们在每次发起请求后调用`time.sleep()`函数模拟休眠，将上述对单页的抓取集合成`onepage`函数，对该函数反复调用：

   ```python
   for i in range(n):  #此处n为拟抓取页数，抓取的电影标题足够即可停止，同时也需要注意不要超过了网站总页数
   	url += str(page) + '---/'     #url的前缀取决于选取的目标网址
   	onepage(url)		#抓取该目标url的内容
   	time.sleep(1)		#防止过快的爬虫抓取触发反爬虫机制，具体的休眠时间取决于目标网址反爬虫力度
   ```

   由此，我们获得了足够的电影名称作为百度百科查询索引，相关内容存储在`movies.txt`文本中。


### 3.2 电影描述百科抓取

1. **selenium使用**。对于百度百科内容的抓取，我们使用`selenium`模拟`Chrome`浏览器进行访问，首先需要确保电脑已安装`Chrome浏览器`，之后，通过`webdriver`启动模拟的`Chrome`浏览器:

   ```python
   driver = webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
   ```

   注意，如果启动失败且报错信息为：

   	Message: 'chromedriver' executable needs to be in PATH.

   你需要先在[这个网站](http://chromedriver.storage.googleapis.com/index.html)下载浏览器对应版本的`chromedriver.exe`驱动，若需要查看当前使用的`Chrome`版本，在`Chrome`浏览器中输入`chrome://version/ `即可查看版本号。将下载好的驱动放在`Chrome`对应目录中，之后在环境变量中添加`Chrome`根目录到`PATH`中即可（当然，你也可以修改参数换用其他浏览器进行模拟）。

   成功启动后，模拟浏览器会显示`Chrome`正受到自动测试软件的控制：

   ![成功启动的模拟浏览器](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/4.png)

2. **分析网站**。由于百度百科可以通过`https://baike.baidu.com/item/`+`搜索目标名`直接访问，我们将存储在`movies.txt`中的电影名称按行读出作为查询索引进行组合：

   ```python
   with open("movies2.txt",'r') as f:
   	names = f.read().splitlines()
   ```

   在`names`中存储了所有待查询的电影名，我们同样通过前缀`url`+待查询目标组合作为目标`url`，通过`driver.get()`函数进行页面跳转，我们同样先按`F12`进入调试模式，对网页分析可知，对于查询的内容的基本信息描述均放在`lemma-summary`类下的`div`标签中：

   ![对百科内容进行分析](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/5.png)

   我们只需要对该标签中的文本内容进行提取即可。此外，由于某些热门电影百度百科还会在该标签下的文本内容中编辑部分关于电影剧情等介绍，通过分析可知，在绝大多数情况下，我们需要爬取的目标内容只需要包含基本简介的第一句话，因此我们设置`split`分割，以句号作为文本切割标识符，提取首句返回作为电影描述：
    

   ```python
   desc = driver.find_element_by_class_name('lemma-summary').text.split('。')[0]
   ```

   

   

3. **数据清洗**。由于我们所选取的电影数量级较大，其中不可避免的会存在以该电影作为索引在百度百科中搜索时返回的页面不是所需要查询的电影，比如我们用”分水岭“作为关键词查询，首先返回的页面为将”分水岭“作为地理科学术语查询的结果，而这并不是我们所需要的内容：

   ![分水岭查询返回页面](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/6.png)

   因此我们还需要对不相干内容进行清洗，通过分析可知，绝大多数电影词条内容首句都会将电影名称用"《》"括起，因此我们将所有首句中不含'《'的进行排除，只写入符合条件的短文本，我们将之前取一条描述的代码形成函数`get_one_detail()`，用`i`代表为电影标题：

   ```python
   	one_movie_list = get_one_detail(i)
       if '《' in one_movie_list:
           with open("des.txt", 'a') as f:
                   f.write(one_movie_list+'\n')
   ```

4. **异常处理**。同时，为了防止部分电影过于冷门导致百科没有收录，导致中途报错影响整体实验，我们使用`try except`板块包裹整体代码，如果查询结果出错，则跳转到下一条查询索引，整体代码框架为：

   

   ```python
   for i in names[：500]： #作为演示，此处仅查询前500条内容作为返回值
   	try:
   		'''
   		返回一条短文本结果
   		符合规范则写入txt文本中
   		'''
   	except:
   		continue
   ```

   最终我们将所有得到的短文本描述存入`des.txt`文件中。

   ![部分结果一览](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/7.png)

   

### 3.3 基于华为云的命名实体识别

### 3.3.1 开通服务

我们首先在华为云产品页面开启命名实体识别服务，具体路径为：产品->人工智能->自然语言处理基础，之后在点击“立即体验”按钮跳转到对应界面开启服务：

![开通服务](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/8.png)

#### 3.3.2 获取账号token

在进行调用相关服务的接口之前，我们首先需要完成令牌认证，其目的在于告诉服务器，调用该服务接口的用户是哪一位。我们通过`python`进行相关接口认证，利用`requests`函数包打包我们的`POST`请求以及获取返回的`token`值。相关服务为`IAM`，为默认开通状态，因此不需要再自行开通。

我们首先需要找到进行请求的`URL`地址，相关帮助文档中给出地址的组成结构为`URL-scheme`+`Endpoint`+`resource-path`，对于`token`获取步骤，`resource-path`部分均为`/v3/auth/tokens`，`URL-scheme`部分为`https`，而对于`Endpoint`的内容则会因为获取区域的不同而发生改变，查看自身区域的步骤为：进入控制台、选择右上角用户名、点击'统一身份认证'，点击左侧项目栏，即可知当前已开通的项目所属区域以及项目名：

![已开通服务](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/9.png)

以图中内容为例，所属项目为`cn-north-4`。因此我们需要请求的`URL`地址为：

```python
url = "https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens"
```


华为云中的相关文档给出了请求`token`的头部信息为：

```python
headers = {'Content-Type': 'application/json'}
```

以及对应的验证内容，注意两处的`name`一个对应默认分配的`ID`（即`hw`开头的默认账号），一个对应登录用的账户名：

```json
{
"auth": {
    "identity": {
        "methods": [
            "password"
        ],
        "password": {
            "user": {
                "name": "username",
                "password": "password",
                "domain": {
                    "name": "domianname"
                }
            }
        }
    },
    "scope": {
        "project": {
            "id": "xxxxxxxxxxxxxxxxxx"
        }
    }
}
```
}

注意在`scope`部分的项目`ID`即为之前的项目名，即`cn-north-4`。我们在填入相关内容后进行`POST`请求，打印返回内容的`token`部分：

	response = requests.post(url, headers=headers, json=payload)
	token = response.headers['X-Subject-Token']
	print(token)

请同学们保存好此token信息，为下一步的实验做身份验证。


#### 3.3.3 调用API进行命名实体识别

此步的调用的`API`与上一步的不同，因此我们需要对`URL`进行修改，在其中加入项目`ID`，其具体格式为：

```python
POST /v1/{project_id}/nlp-fundamental/ner
```

其中`project_id`会根据每个账户随机生成，请各位同学在“控制台”、“我的凭证”中查看，然后对所需要访问的`URL`进行拼接，同时修改该`POST`请求的头部信息为：

```python
header = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
}
```

我们在`body`中填入需要进行处理的文本实体，以单条信息为例：

```python
body = {
    'text': '《最佳拍档之女皇密令》是由新艺城出品的《最佳拍档》系列的第三部，由徐克担任执导，许冠杰，麦嘉，张艾嘉主演的一部喜剧片',
    'lang': 'zh'
}
```

之后我们对整个`POST`通过`requests`函数包进行封装，再将返回文本进行`utf-8`再编码（否则可能打印的为`unicode`的编码）：

```python
resp = requests.post(url, data=json.dumps(body), headers=header)
print(resp.text.encode('utf-8').decode("unicode_escape"))
```

即可看到所识别的实体信息：

![部分实体识别结果](https://zjy-fig-1308535101.cos.ap-chengdu.myqcloud.com/%E6%9C%AC%E7%A7%91%E7%94%9F%E5%AE%9E%E9%AA%8Cex5/10.png)

将之前爬虫获取的`des.txt`文档逐条遍历输入，再将打印信息存入相关文件即可。


## 4 扩展实验

在本次实验中，我们给予学有余力的同学，在完成本次实验的基础上提出了扩展要求。
【注】总分不超过100分。


| 扩展要求 | 加分 | 备注 |
| :-----:| :-----: | :-----: |
| 1.使用更细粒度的数据清洗方法 | +5~+10 | 根据清洗数据的质量、清洗思路给分 |
| 2.在此基础上构建知识图谱 | +5~+10 | 根据创建的图谱给分，具体教程请参考[此处](https://support.huaweicloud.com/bestpractice-kg/kg_04_0002.html#section8) |
| 4. 使用分布式爬虫或其它方式获取更优质的数据集 | +5~+10 | 根据分布式框架、性能给分；根据数据集规模、质量给分 |
| 5.**创新的数据场景（华为云特色API应用不限于知识图谱**） | +10~+15 | 根据场景创新程度、工作量给分 |
| 6.在云服务器上搭建网页，调用相关API集成功能 |+5~+10 | 根据网站的功能及美观程度给分 |


当然，**如果你有更好的idea**来完善更新本次实验，请联系老师或助教，我们还会考虑为你申请本年度的优秀课设（每一年都有同学通过该方式获得优秀课设）。

详情你可参考：[CQU_bigdata-开源贡献](https://github.com/Wanghui-Huang/CQU_bigdata)。

## 5 实验小结

在本次实验中，你使用了爬虫爬取了一个不错的数据集，还利用金主华为云特色API构建了一个知识图谱（当然，优秀的你可能是做了点什么其它很棒的事）。

不管怎样，你应该对爬虫开始得心应手，也了解了知识图谱一些很有意思的知识。通过前面的实验学习，你也肯定了解并应用了不少大数据工具、算法等。相信有些过程一定让你印象深刻。这为你后续的大数据课程，打下了还不错的基础。

最后，恭喜你完成所有大数据的课程实验！

