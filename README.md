## 特别声明: 

* 本仓库发布的MyActions项目中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断.

* 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。

sazs34对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害.

* 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, sazs34 对于由此引起的任何隐私泄漏或其他后果概不负责.

* 请勿将MyActions项目的任何内容用于商业或非法目的，否则后果自负.

* 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本.

* 任何以任何方式查看此项目的人或直接或间接使用该MyActions项目的任何脚本的使用者都应仔细阅读此声明。sazs34 保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或MyActions项目的规则，则视为您已接受此免责声明.

 **您必须在下载后的24小时内从计算机或手机中完全删除以上内容.**  </br>
> ***您使用或者复制了本仓库且本人制作的任何脚本，则视为`已接受`此声明，请仔细阅读*** 


![sazs34’s github stats](https://github-readme-stats.vercel.app/api?username=sazs34&show_icons=true&theme=vue)

# MyActions

### 本项目已可以实现自动同步上游更改！[具体点击](#自动同步)

目前[@lxk0301](https://github.com/lxk0301) 的代码都支持无限账号了，各位可以直接使用那边的了呢

> 更新时间2020-10-25
>
> **喜马拉雅支持开关时长任务+指定账号执行时长任务+执行时长任务上限(例如12小时)**
>
> **添加WebHook支持,具体[参考点击](backup/webhook.js)**
>
> **添加喜马拉雅极速版支持**(python版)

1. 支持手动执行，具体在Actions中选中要执行的Workflows后再在右侧可以看到Run workflow，点击即可运行此workflow。

2. 嫌上一步麻烦的，也可以直接点击一下star，你会发现所有的workflow都已执行。

3. **必须** - 请随便找个文件(例如`README.md`)，加个空格提交一下，否则可能会出现无法定时执行的问题

目前已支持[@NobyDa](https://github.com/NobyDa) 以及[@lxk0301](https://github.com/lxk0301) 中京东签到的内容,优点是支持无限数量的京东cookie

已支持[@Zero-S1](https://github.com/Zero-S1/xmly_speed)大佬的喜马拉雅极速版签到

# 特级注意事项

FORK后，如果actions没有定时执行，请随便找个文件，加个空格提交一下，就可以正常执行了

## 使用教程

1. 直接fork走
2. 再在`Settings`-`Secrets`里面添加`JD_COOKIE`
3. 多条cookie用`&`隔开，支持无数条cookie
4. 前三步之后，点击一下右上角的star（fork左边那个），让workflow运行一次。

上面四步搞定后就不用管了。

刚fork完可能在Actions中看不到对应的workflow

目前**已配置好自动执行时间**，到了指定时间会执行并且看到workflow

### Secrets全集合

#### 京东专用

| Name                    |   归属   | 属性   | 说明                                                         |
| ----------------------- | :------: | ------ | ------------------------------------------------------------ |
| `JD_COOKIE`             |   京东   | 必须   | 京东cookie,具体获取参考[lxk0301的获取教程](https://github.com/lxk0301/scripts/blob/master/githubAction.md#%E4%BA%AC%E4%B8%9Ccookie)或[点击直达](#Cookie获取和配置) |
| `JD_DEBUG`              |   脚本打印log   | 非必须   | 运行脚本时，是否显示log,默认显示。改成false表示不显示，注重隐私的人可以在设置secret -> `Name:JD_DEBUG,Value:false` |

##### 互助码系列

| Name                    |   归属   | 属性   | 说明                                                         |
| ----------------------- | :------: | ------ | ------------------------------------------------------------ |
| `FruitShareCodes`       |  东东农场互助码  | 非必须 | 填写规则请看 [jdFruitShareCodes.js](https://github.com/lxk0301/scripts/blob/master/jdFruitShareCodes.js) 里面的说明 |
| `PETSHARECODES`         |  东东萌宠互助码  | 非必须 | 填写规则请看 [jdPetShareCodes.js](https://github.com/lxk0301/scripts/blob/master/jdPetShareCodes.js) 里面的说明 |
| `PLANT_BEAN_SHARECODES` |  种豆得豆互助码  | 非必须 | 填写规则请看 [jdPlantBeanShareCodes.js](https://github.com/lxk0301/scripts/blob/master/jdPlantBeanShareCodes.js) 里面的说明 |
| `SUPERMARKET_SHARECODES`|  京小超商圈互助码  | 非必须 | 填写规则请看 [jdSuperMarketShareCodes.js](https://github.com/lxk0301/scripts/blob/master/jdSuperMarketShareCodes.js) 或见下方`互助码的填写规则` |

##### 其它控制

| Name                    |   归属   | 属性   | 说明                                                         |
| ----------------------- | :------: | ------ | ------------------------------------------------------------ |
| `JOY_FEED_COUNT`        | 宠汪汪喂食数量  | 非必须 | 控制jd_joy_feedPets.js脚本喂食数量  ,可以填的数字10,20,40,80 , 其他数字不可.              |
| `JOY_HELP_FEED`         | 宠汪汪帮好友喂食  | 非必须 | 控制jd_joy_steal.js脚本是否给好友喂食,`false`为否,`true`为是(给好友喂食)              |
| `JOY_RUN_FLAG`          | 宠汪汪参加双人赛跑  | 非必须 | 控制jd_joy.js脚本是否参加双人赛跑,`false`为否,`true`为是，脚本默认是`true`              |
| `MARKET_COIN_TO_BEANS`  | 京小超兑换京豆数量  | 非必须 | 控制jd_blueCoin.js兑换京豆数量,可输入值为1到20或者1000的数字，其他数字不可.              |
| `SUPERMARKET_UPGRADE`   |  京小超自动升级  | 非必须 | 自动升级,顺序:解锁升级商品、升级货架,`true`表示自动升级,`false`表示关闭自动升级 |
| `BUSINESS_CIRCLE_JUMP`  |  京小超自动更换商圈  | 非必须 | 小于对方300热力值自动更换商圈队伍,`true`表示运行,`false`表示禁止 |
| `SUPERMARKET_LOTTERY`   |  京小超抽奖  | 非必须 | 每天运行脚本是否使用金币去抽奖,`true`表示抽奖,`false`表示不抽奖 |
| `FRUIT_BEAN_CARD`       |  农场使用水滴换豆卡  | 非必须 | 农场使用水滴换豆卡(如果出现限时活动时100g水换20豆,此时比浇水划算,推荐换豆),`true`表示换豆(不浇水),`false`表示不换豆(继续浇水),脚本默认是浇水 |
| `UN_SUBSCRIBES`         |  jd_unsubscribe.js  | 非必须 | 共四个参数,换行隔开. 四个参数分别表示`取关商品数量`,`取关店铺数量`,`遇到此商品不再进行取关`, `遇到此店铺不再进行取关`，[具体使用往下看](#取关店铺secret的说明)|


#### 推送通知专用

| Name                    |   归属   | 属性   | 说明                                                         |
| ----------------------- | :------: | ------ | ------------------------------------------------------------ |
| `PUSH_KEY`              |   推送   | 非必须 | cookie失效推送[server酱的微信通知](http://sc.ftqq.com/3.version) |
| `BARK_PUSH`             |   推送   | 非必须 | cookie失效推送BARK这个APP,此token是https://api.day.app/后面的内容 |
| `BARK_SOUND`            |   推送   | 非必须 | bark推送声音设置，例如`choo`,具体值请在`bark`-`推送铃声`-`查看所有铃声` |
| `TG_BOT_TOKEN`          |   推送   | 非必须 | tg推送,填写自己申请[@BotFather](https://t.me/BotFather)的Token,如`10xxx4:AAFcqxxxxgER5uw` |
| `TG_USER_ID`            |   推送   | 非必须 | tg推送,填写[@getuseridbot](https://t.me/getuseridbot)中获取到的纯数字ID，[关于TG推送的说明](#关于TG推送的说明) |
| `DD_BOT_TOKEN`          |   钉钉推送   | 非必须 | 钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需`https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的XXX， 注：如果钉钉推送只填写`DD_BOT_TOKEN`，那么安全设置需勾选`自定义关键词`，内容输入输入`账号`即可，其他安全设置不要勾选 |
| `DD_BOT_SECRET`         |   钉钉推送   | 非必须 | 密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的字符串,填写了`DD_BOT_TOKEN`和`DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选 |
| `PET_NOTIFY_CONTROL`    | 东东萌宠推送开关  | 非必须 | 控制京东萌宠是否静默运行,`false`为否(发送推送通知消息),`true`为是(即：不发送推送通知消息)              |
| `FRUIT_NOTIFY_CONTROL`  | 东东农场推送开关  | 非必须 | 控制京东农场是否静默运行,`false`为否(发送推送通知消息),`true`为是(即：不发送推送通知消息)              |
| `JD_JOY_REWARD_NOTIFY`  | 宠汪汪兑换京豆推送开关  | 非必须 | 控制jd_joy_reward.js脚本是否静默运行,`false`为否(发送推送通知消息),`true`为是(即：不发送推送通知消息)              |
| `MARKET_REWARD_NOTIFY`  | 京小超兑换奖品推送开关  | 非必须 | 控制jd_blueCoin.js兑换奖品成功后是否静默运行, `false`为否(发送推送通知消息),`true`为是(即：不发送推送通知消息)             |


#### 喜马拉雅专用

| Name                    |   归属   | 属性   | 说明                                                         |
| ----------------------- | :------: | ------ | ------------------------------------------------------------ |
| `XMLY_SPEED_COOKIE`     | 喜马拉雅 | 非必须 | [Cookie获取请参考](https://github.com/Zero-S1/xmly_speed/blob/master/xmly_speed.md),仅支持git actions执行,多个Cookie用换行即可 |
| `XMLY_ANDROID_AGENT`     | 喜马拉雅 | 非必须 | 仅安卓用的Agent配置，不填的话也会默认用红米8的 |
| `XMLY_ACCUMULATE_TIME`     | 喜马拉雅 | 非必须 | 需要刷时长任务的话，填入`zero_s1`；可能会黑号，请知悉 |
| `XMLY_ACCUMULATE_INDEX`     | 喜马拉雅 | 非必须 | 需配合`XMLY_ACCUMULATE_TIME`使用，用于限定某个索引的账号不进行刷时长 |
| `XMLY_ACCUMULATE_HOURS`     | 喜马拉雅 | 非必须 | 需配合`XMLY_ACCUMULATE_TIME`使用，用于限定每天收听的小时数,尽量避免黑号 |

##### 关于`XMLY_ACCUMULATE_INDEX`

> 用于指定哪几个账号不执行时长任务

比如我有5个账号，我第1个和第5个不想执行刷时长任务，则填入内容为`1,5`
例如我只有两个号，第2个号不想执行刷时长，则直接填入`2`即可

##### 关于`XMLY_ACCUMULATE_HOURS`

> 用于指定时长任务最大时间，防止现在时长任务直接是24小时的，过于容易发生黑号情况

传入`1`~`24`之间的数字即可

#### 取关店铺参数的说明

> 格式为`取关商品数`,`取关店铺数`,`遇到此商品不再进行取关`,`遇到此店铺不再进行取关`

```javascript
// 例如我要取关10个商品，20个店铺，商品遇到商品关键字apple停止取关，店铺遇到apple不再取关
// 则填入的内容是10,20,apple,apple

//再例如我什么都不管，商品和店铺我都取关50个
// 则填入的内容为50,50,,

// 即 哪怕不填关键字，也要用英文逗号隔开
```

#### 关于TG推送的说明

> 需要`TG_BOT_TOKEN`和`TG_USER_ID`一起使用，前者用于调用bot，后者用于指定推送目标

私聊[@getuseridbot](https://t.me/getuseridbot)，点击start以后，收到的第一条纯数字消息就是你的userid了

<img src="https://user-images.githubusercontent.com/6993269/93156198-3b1ad700-f73a-11ea-8f51-5ee71d06ef8a.png" alt="获取userid" style="zoom:40%;" />

私聊[@BotFather](https://t.me/BotFather)，创建自己的bot

<img src="https://user-images.githubusercontent.com/6993269/93155923-b0d27300-f739-11ea-928a-803134f0f416.png" alt="获取bot的token" style="zoom:40%;" />



### Cookie获取和配置

> 具体如何取cookie如何配置,可参考 https://github.com/lxk0301/scripts/issues/8#issuecomment-675837338

```

针对京东cookie我们只需要
pt_key=****;
和
pt_pin=***;
的部分

我有两个京东账号,则我JD_COOKIE里面要填写的内容为
pt_key=****;pt_pin=***;&pt_key=****;pt_pin=***;
```

### 同步Fork后的代码

#### 手动同步

[手动同步 http://www.ibloger.net/article/3361.html](http://www.ibloger.net/article/3361.html)

#### 自动同步

##### 方案A - 强制远程分支覆盖自己的分支
1. 参考[这里](http://note.youdao.com/noteshare?id=6cd72de428957d593c129749194b4352)，安装[pull插件](https://github.com/apps/pull)，并确认此项目已在pull插件的作用下（参考文中1-d）。
2. 确保.github/pull.yml文件正常存在，yml内上游作者填写正确(此项目已填好，无需更改)。
3. 确保pull.yml里面是`mergeMethod: hardreset`(默认就是hardreset)。
4. ENJOY!上游更改三小时左右就会自动发起同步。

##### 方案B - 保留自己分支的修改

> 上游变动后pull插件会自动发起pr，但如果有冲突需要自行**手动**确认。
> 如果上游更新涉及workflow里的文件内容改动，需要自行**手动**确认。

1. 参考[这里](http://note.youdao.com/noteshare?id=6cd72de428957d593c129749194b4352)，安装[pull插件](https://github.com/apps/pull)，并确认此项目已在pull插件的作用下（参考文中1-d）。
2. 确保.github/pull.yml文件正常存在，yml内上游作者填写正确(此项目已填好，无需更改)。
3. 将pull.yml里面的`mergeMethod: hardreset`修改为`mergeMethod: merge`保存。
4. ENJOY!上游更改三小时左右就会自动发起同步。

## 鸣谢

[@NobyDa](https://github.com/NobyDa) - 京东每日签到

[@lxk0301](https://github.com/lxk0301)  - 京东系列其他签到

[@Zero-S1](https://github.com/Zero-S1/xmly_speed) - 喜马拉雅极速版签到

