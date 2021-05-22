# -1.前言  
`这些内容只是设想。SAE的开发需要大家的帮助，希望大家能够给点建议。内容还没写完。可能需要的帮助:除了下面的21种问题外，你希望SAE还能够检查出什么问题？你希望SAE应该怎么样帮助你发现作品中的不足？`  
# 0. 首页  
点击并粘贴 JSON / 其他选项  
## 发现潜在的问题  
通过积木分析和合理性检查快速发现可能的错误  
## 追踪变量的源头  
通过反向查找变量设定和积木引用找到问题所在  
## 看到清晰的结构  
通过绘制引用结构图来更加直观地展示深层逻辑  
## 获得极致的体验  
通过实时的提示和方便简单的操作提升使用体验  
## 现在，让 SAE 为你发现，帮你解决那些烦人的小问题，  
把你宝贵的精力更多地投入到想像与创作当中！  
# 1. 简介  
## 1.1. 为什么会有 SAE  
### 1  
(改编自某人主页的文章+个人体验)我觉得今天糟透了。  
看看这可悲的一天吧。  
晚上九点，我点开了 scratch，想要给我的作品加一些功能。  
加了一个，结果发现这功能不起作用。  
于是我回去检查了半天。发现好像有两个地方有问题。修复完成。  
好，我检查，修复了大约 10 分钟后，发现还是不行。  
于是我又检查了一次，可能是大于号不对要改成小于，结果还是不行。一点反应都没有。  
我疑惑再怎么不对也得有点反应啊，哪怕只是显示一堆乱七八糟也好。  
于是我尝试使用列表调试法，就是放置大量的把 xxx 加入列表，如果有没运行到的地方就检查。  
盯着列表对了半天后，我发现是 3，5 都被运行了，就 4 没被运行。为什么？  
真是费解。就在我即将使出大招——删掉重做——的时候，奇迹发生了——在我去掉调试用的积木时，我看到舞台里突然多了一块`((i)+(1))`{.scratch-inline}积木  
咦？  
直到我右键撤销后我才意识到那个积木是我不小心从某个积木里拖出来的，一直没有发现！  
于是我把那个积木拖了回去，yes，运行成功了  
现在是晚上十点，也就是说，我计划要加的全部功能除了那个之外也就全部 over 了   
scratch 是真的难用。  
### 2  
scratch 是壮哉我大 LLK 开发的一个直观的互动媒体设计工具。  
`scratch不是编程语言，是创作工具。`  
它以直观，简单的操作以及友好的逻辑结构为未接触过一行亿 error 的代码编程的小朋友们提供了简单，方便的创作互动内容的机会。得益于官方的社区和国内外各种本土化的社区，大家得以在各路社区发布作品，分享创意，发现志同道合的小伙伴。  
但是，scratch 虽然有效避免了代码编程中的大多数问题，但是有一些问题不是把代码变成积木就能解决的，积木在规避拼写错误，符号不规范的同时，还带来了拖放位置不正确等问题。尤其是在设计中存在的逻辑缺陷，根本无法通过积木来避免。无视越界错误，自定义积木的参数可以随意拼接，积木可以跨角色复制，找不到角色/造型/声音时自动跳过等特性在方便创作的同时也给错误的查找带来了困难。  
因此，我根据某人留下的 scratch 转编程猫工具的半成品制作出了 SAE 的一个 javascript 版本，它可以展现出项目中可能存在错误的地方，就像这样：  
```  
文件 1  
角色 编辑器  
4输入内容左/右端有空格   
  
0 定义 输出 〈x〉 长度 〈n〉   
1 将 「<编辑器>j」 设为 1   
2 将 「<编辑器>输出长度」 设为 〈n〉   
3 重复执行直到 「<编辑器>j」 > (〈x〉)的字数 或 「<编辑器>输出长度」 < 0  
[4] | 如果 <〔0123456789abcdefghijklmnopqrstuvwxyz`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>? 〕 包含 (〈x〉 的第 「<编辑器>j」 个字符)?> 那么   
5 | | 把 「<编辑器>输出长度」 增加 -1   
6 | 否则   
7 | | 把 「<编辑器>输出长度」 增加 -1.8   
8 | ＼————————   
9 | 如果 「<编辑器>输出长度」 > -1 那么   
10 | | 输出 (〈x〉 的第 「<编辑器>j」 个字符)  
  
  
文件 1  
角色 编辑器  
0未拼合的积木  
  
[0] 输出 〔 ▇ 〕   
1 输出 〔 ┃ 〕   
```  
但我的最终目的是希望能够在 scratch 上实现它。创作者们可以在少量的脚本的帮助下快速获得 json 并在 SAE 项目中粘贴，获得实时，直观的提示和详细的帮助，甚至在 SAE 无法主动发现错误的情况下，通过 SAE 的引导，找到错误所在。  
这真的非常困难，但是这个项目一但实现，不仅会是一个值得永久纪念的作品，还将会是帮助更多创造者进步的实用工具。  
### 3  
scratch 的世界很危险，希望 SAE 能够带你避开这些坑，让你在有限的时间里创造出更加丰富的内容。你的宝贵精力本不该被白白消耗在因为 scratch 的缺陷而产生的 bug 中。  
HOPE IT WORK.  
`当然，也可能最后的结局是该项目被停止，什么都没有发生`  
## 1.2. 定价  
`你看看隔壁六年级小朋友画幅画就能卖￥10+你搁这搞什么SAE搞它几个月连个￥0.01的红包都没有这合理吗?`  
||基本版|高级版|定制版|  
|-|-|-|-|  
|积木检查|√|√|√|  
|直观显示|√|√|√|  
|积木搜索|√|√|√|  
|帮助文档|√|√|√|  
|实时提示|√|√|√|  
|允许改编|√|√|√|  
|允许下载项目文件|√|√|√|  
|保存设定和进度|×|√|√|  
|自定义功能|×|×|√|  
|价格|￥ 0.00|￥ 0.00|￥ 0.00|  
|特殊需求|无|把作品保存到电脑或者改编|在这里催奥波多普加功能，或者自行改编原作品|  
`如果SAE真的有用，可以在你的作品上给它打个广告么`  
# 2. SAE 积木检查会发现什么  
## 2.1. 相同的积木  
` scratch-blocks把x坐标设为 (鼠标的x坐标::sensing)::motion把x坐标设为 (鼠标的y坐标::sensing)::motion`  
当功能相同的积木被放在一起时  
## 2.2. 无意义的积木  
`把 [x v] 增加 (0)::variables`{.scratch-inline}  
`把 [i v] 设为 (i)::variables`{.scratch-inline}  
增加 0，设定变量为自己  
## 2.3. 空白的数字  
`将 [k v] 设为 ((i)+())::variables`{.scratch-inline}  
当计算积木里的数字忘记填写的时候  
## 2.4. 空白的积木  
`等待<<(i)>(10)>和<>::operators>::control`{.scratch-inline}  
当六边形空格缺少积木，或者 C 形积木内空白的时候  
## 2.5. 未接上的积木当有积木没被正确和开头积木接上的时候  
## 2.6. 不合理的积木针对特效设定的值的范围。  
`大多数情况下画笔/声音特效的范围是0到100但是也有例外  
颜色特效是0到200  
亮度，左右平衡是-100到100  
鱼眼和像素化和马赛克只要是非负数就行  
貌似马赛克是10的整数倍`  
以及使用列表的第 0 项，或者第 0 个字符(scratch 中项目数从 1 开始)  
## 2.7. 不存在的角色/造型/背景/声音/变量  
复制积木，删除造型，编辑自定义积木后，部分保留了原名称的积木将会失效  
## 2.8. 克隆时没有角色变量条件控制  
` scratch-blocks当作为克隆体启动时::control hat克隆(自己 v)::control`  
在广播，克隆启动时，如果克隆自己时没有角色变量条件加以控制，将会产生不受控制的克隆现象。  
## 2.9. 循环条件未在循环体中改变  
` scratch-blocks将[i v]设为(0)::variables重复执行直到<(i)>(5)>时{把(i)加入[列表 v]::list}::control`  
## 2.10. 循环条件未在循环体中改变方向不正确  
` scratch-blocks将[i v]设为(5)::variables重复执行直到<(i)<(1)>时{把(i)加入[列表 v]::list把(i)增加(1)::variables}::control`  
这类错误会导致死循环的出现  
## 2.11. 删除克隆体积木后仍有可执行积木  
` scratch-blocks如果<(生命)=(0)>那么{删除此克隆体::control cap}::control广播(胜利 v)::events`  
在本体执行这类积木时，删除此克隆体不会停止积木进行，下面的广播会被执行  
## 2.12. 停止当前积木所处的位置不正确  
` scratch-blocks重复执行直到<……::#0F0>时{...::#FF0如果<……::#0F0>那么{...::#F0F}::control停止[当前积木 v]::control cap}::control`  
停止当前积木应该在如果/否则里的积木之后，在其他地方出现这类积木则可能是因为拖动时的错误导致  
## 2.13. 注意 2000 积木的时区问题  
`(从2000年起的天数::sensing)`{.scratch-inline}  
正如这个积木所说，返回 2000 年起的天数，但是要注意，这里的 2000 年是指 0° 经线所在时区的 2000 年。这个积木事实上会返回从 2000 年 1 月 1 日 08:00:00(北京时间)起的天数。  
## 2.14. 注意星期数问题  
`(当前时间的[星期 v]::sensing)`{.scratch-inline}  
在这个积木中，1 表示星期日，2 表示星期一，3 表示星期二，以此类推。  
`这么明显的BUG，scratch为什么不修复?  
在中国我们已经习惯了从'星期一'叫到'星期天'这样的叫法，我们第一感觉会认为星期一到星期天理所当然应该是1234567，但其实不是。按照惯例星期日是一周的第一天，因此星期日会返回1。  
可是这很明显会产生误解，严重影响创作者的使用!!!!!!!!!!!!!!!  
按照惯例，星期日确实是第一天，而且在英语里星期一到星期天并没有和数字相似，不会引发这类误会。scratch本身是一个国际性的软件，不太可能因为某一种语言的习惯来改变一个积木的运行方式。更何况这是一个只需要减去一就能解决的问题。`  
## 2.15. 不合理的计算  
`((x)+(0))`{.scratch-inline} `((x)*(1))`{.scratch-inline} `((x)/(0))`{.scratch-inline}  
加零，减零，乘零，乘一……都会被认为是不合理的计算。  
## 2.16. 直接使用列表  
`(列表::list)`{.scratch-inline}  
直接使用列表会带来不确定的行为，带来创作困难  
`当你直接使用(列表)时，会得到列表的每一项用空格连接起来的文本，例如  
1 2 3 4 5 10 12 19  
但是当列表里全都是单个字符的文本时，空格就会被省略，而且这里的单个字符里还有一个很智能的判断：通过加减乘除等运算产生的一位数不是字符。但是通过连接或者取第几个字符产生的单个字符是字符。从外观上完全看不出来，就很坑人。  
强烈不建议使用这样的方式使用列表，做一个功能明确的循环，可以避免很多相关的问题。`  
## 2.17. 自定义积木参数没被使用  
在自定义积木的参数没被使用的时候。多半是因为你把它忘记了。  
## 2.18. 在一步执行(运行时不刷新屏幕)里使用造成等待的积木  
由于设计缺陷，这会导致运行卡顿。  
`  
这类积木包括  
等待xxx  
xxx并等待  
说/思考xxx秒  
xxxx x拍  
load/save variable/list  
发送JSON`  
## 2.19. 建议使用一步执行  
在循环中没有改变画面的积木时建议使用一步执行(运行时不刷新屏幕)。这可以避免大部分变量冲突带来的影响。  
## 2.20. 并排如果变量冲突  
` scratch-blocks询问[需要什么操作?1.吃 2.扔掉]并等待::sensing把[i v]设为(回答::sensing)::variables如果<(i)=(1)>那么{询问[需要什么操作?1.全部吃光 2.吃一半]并等待::sensing把[i v]设为(回答::sensing)::variables如果<(i)=(1)>那么{全部吃光::#0F0}::control如果<(i)=(2)>那么{吃一半::#00F}::control}::control如果<(i)=(2)>那么{扔掉::#F00}::control`  
这是一个不那么容易发现的错误。如图。如果第一次询问时输入 1 并且第二次询问时输入 2，那么最后一个如果也会被运行。  
解决方法是使用如果/否则积木  
` scratch-blocks询问[需要什么操作?1.吃 2.扔掉]并等待::sensing把[i v]设为(回答::sensing)::variables如果<(i)=(1)>那么{询问[需要什么操作?1.全部吃光 2.吃一半]并等待::sensing把[i v]设为(回答::sensing)::variables如果<(i)=(1)>那么{全部吃光::#0F0}否则{如果<(i)=(2)>那么{吃一半::#00F}::control}::control}否则{如果<(i)=(2)>那么{扔掉::#F00}::control}::control`  
## 2.21. 输入内容左/右端有空格  
` scratch-blocks把[名字 v]设为[a]::variables...::#00F如果<(名字)=[a ]>那么{...::#F0F}::control`  
你肯定一眼看不到问题在哪。但是你在选中了如果那里的名字后面的 a 后，会发现后面有空格!!!!!!!!!!  
## 2.22. 等于号比较不区分大小写  
例如`<[A]=[a]>`{.scratch-inline}是成立的  
但是角色名，变量名，造型名，声音名是区分大小写的  
例如`把造型切换为(A v)::looks`{.scratch-inline}和`把造型切换为(a v)::looks`{.scratch-inline}不同。  
`可以利用造型名为字母的角色来区分大小写`  
# 3. 拓展积木  
## 3.1. javascript   
写点什么……  
# 4. 更好地与 SAE 合作  
# 5. SAE 是怎么工作的  
## 5.1. 处理  
## 5.2. 显示  
## 5.3. 检查  
## 5.4. 绘图  
## 5.5. 搜索  
  