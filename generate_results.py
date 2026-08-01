#!/usr/bin/env python3
"""生成 25 个城市匹配测试结果页 — 暖米色新中式风格"""

import os
import random

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
os.makedirs(output_dir, exist_ok=True)

element_config = {
    "wood": {
        "name": "木", "emoji": "🌲", "en": "Wood",
        "color": "#7CB342", "color_dark": "#558B2F",
        "traits": "生长 · 创新 · 仁爱",
        "personality": "你是一个充满生命力的人，像春天的树木一样不断向上生长。你天性善良温和，对世界充满好奇心，总是能在平凡中发现美好与诗意。你的创造力像新芽一样源源不断地涌现，你的耐心让身边的人感到安心。",
        "life_advice": "像树木扎根一般，找到让你安心的土壤，不急于求成。生长需要时间，你的每一次努力都会在未来的某一天开花结果。",
        "work_style": "你善于规划和构思长远之事，像建筑师般搭建未来。面对困难时，你会像树根般深扎，从逆境中汲取养分。"
    },
    "fire": {
        "name": "火", "emoji": "🔥", "en": "Fire",
        "color": "#E57373", "color_dark": "#C62828",
        "traits": "热情 · 活力 · 领导力",
        "personality": "你像一团永不熄灭的火焰，热情洋溢，充满感染力。你天生就是人群中的焦点，用你的光芒温暖和鼓舞身边的人。你有极强的行动力和领导力，想到就去做，从不拖泥带水。",
        "life_advice": "火焰最怕的不是风，而是没有燃料。记得给自己留一些空间充电，最好的光芒不是燃烧殆尽，而是温暖而持久。",
        "work_style": "你是行动派，善于快速决策和推动项目。你的激情能点燃整个团队。但偶尔也要慢下来，听听别人的意见。"
    },
    "earth": {
        "name": "土", "emoji": "🏔️", "en": "Earth",
        "color": "#BCAAA4", "color_dark": "#8D6E63",
        "traits": "稳重 · 包容 · 信任",
        "personality": "你像大地一样沉稳可靠，是身边人最信赖的依靠。你不急于表达，但每一步都走得扎实。你对待生活有自己坚定的节奏，不随波逐流，内心的秩序让你在混乱中依然从容。",
        "life_advice": "大地承载万物，却从不喧哗。你的力量不在于快，而在于稳。继续按自己的节奏走，不必与他人竞速。",
        "work_style": "你是团队中最可靠的后盾，善于统筹规划、稳扎稳打。你的务实精神让每个项目都有坚实的地基。"
    },
    "metal": {
        "name": "金", "emoji": "⚙️", "en": "Metal",
        "color": "#90A4AE", "color_dark": "#546E7A",
        "traits": "秩序 · 决断 · 精致",
        "personality": "你像精雕细琢的金属，理性而锐利。你追求卓越与精准，对事物有自己的高标准。你擅长分析与判断，在复杂问题面前总能找到最优雅的解决方案。你的自律令人钦佩。",
        "life_advice": "金属经过打磨才会发光。你的严谨与追求完美是宝贵的品质，但也要允许自己偶尔放松，人生不需要时刻都是满分的答卷。",
        "work_style": "你是天生的组织者和决策者，善于构建体系和流程。你的精确与效率让团队的工作如精密的齿轮般顺畅运转。"
    },
    "water": {
        "name": "水", "emoji": "💧", "en": "Water",
        "color": "#64B5F6", "color_dark": "#1E88E5",
        "traits": "智慧 · 灵活 · 适应",
        "personality": "你像水一样灵动智慧，善于随机应变。你的思维像流水般自由通透，能穿透复杂问题的每个缝隙。你有深刻的洞察力，能看到别人看不到的本质，你的优雅在于柔软中蕴含的力量。",
        "life_advice": "水无常形，因势利导。你的力量在于变通与适应，不必强迫自己成为某种固定的形状。顺流而行，终将汇入广阔的海洋。",
        "work_style": "你是天生的思考者和沟通者，善于处理复杂多变的情境。你的灵活思维能在困境中找到出人意料的突破点。"
    },
}

cities = {
    "wood": [
        { "id": "hangzhou", "name": "杭州", "emoji": "🏯",
          "tagline": "江南忆，最忆是杭州",
          "subtitle": "西湖潋滟 · 互联网创新 · 生活品质之城",
          "match_reason": "杭州的灵动温润、创业创新精神与木属性的生长开拓完美契合。西湖水的滋养让这座城市永远勃勃生机，正如你内心永不停歇的成长渴望。这里有阿里巴巴代表的创新力量，也有灵隐寺代表的宁静致远——你既能拥抱变革，又懂得沉淀。",
          "keywords": ["🌊 西湖", "💻 互联网", "🎨 文创", "🍵 龙井", "🏮 南宋"] },
        { "id": "chengdu", "name": "成都", "emoji": "🐼",
          "tagline": "来了就不想走的城市",
          "subtitle": "天府之国 · 美食天堂 · 慢生活典范",
          "match_reason": "成都的包容与自洽、悠闲中蕴含的蓬勃活力，与木属性的自由成长不谋而合。这座城市用一碗盖碗茶的节奏告诉你——好的生长不需要焦虑，自然而然地发生就好。这里有太古里的时尚先锋，也有人民公园的茶馆安逸，你在这里可以按照自己的节奏舒展枝叶。",
          "keywords": ["🐼 大熊猫", "🌶️ 火锅", "🏮 宽窄巷子", "🐉 都江堰", "🍵 茶馆"] },
        { "id": "kunming", "name": "昆明", "emoji": "🌸",
          "tagline": "天气常如二三月，花枝不断四时春",
          "subtitle": "春城花都 · 生态宜居 · 彩云之南",
          "match_reason": "昆明的四季如春是木属性最理想的气候形态——永远在生长的温度，永远有花开。你的内心如同这座春城，有着恒久的温暖和生机。这里远离喧嚣却充满活力，适合需要扎根、积淀和慢慢绽放的你。",
          "keywords": ["🕊️ 滇池", "🌸 鲜花", "🌿 石林", "🏔️ 西山", "🐘 民族风情"] },
        { "id": "nanning", "name": "南宁", "emoji": "🌴",
          "tagline": "半城绿树半城楼",
          "subtitle": "中国绿城 · 东盟门户 · 热带风情",
          "match_reason": "南宁的绿意盎然与木属性的生命力浑然一体，被誉为「中国绿城」。这座亚热带城市终年常青，正如你源源不断的创造力。作为面向东盟的门户，它还代表了开放与连接——你善于在不同文化之间搭桥，让新的可能性在这里生根。",
          "keywords": ["🌴 绿城", "🌍 东盟", "🏖️ 北海", "⛰️ 青秀山", "🎭 壮乡文化"] },
        { "id": "guilin", "name": "桂林", "emoji": "⛰️",
          "tagline": "桂林山水甲天下",
          "subtitle": "山水画廊 · 诗意栖居 · 自然杰作",
          "match_reason": "桂林的山水是大自然用千万年雕琢的木属性杰作——峰林如竹笋般拔地而起，漓江如绿色绸带蜿蜒其间。你的灵魂深处有着对自然和艺术的本能向往，这座充满诗意的城市是你内心的外在投射。在这里，山与水、人文与自然达成了最美妙的平衡。",
          "keywords": ["⛰️ 漓江", "🎋 阳朔", "🏞️ 龙脊梯田", "🚣 竹筏", "📜 摩崖石刻"] },
    ],
    "fire": [
        { "id": "shenzhen", "name": "深圳", "emoji": "🚀",
          "tagline": "来了就是深圳人",
          "subtitle": "创新引擎 · 科技先锋 · 梦想之城",
          "match_reason": "深圳的创业激情与「深圳速度」是火属性最极致的表达——敢闯敢试、从零到一。这座城市从一个小渔村到国际化大都市的蜕变，完美诠释了你内心那股不服输的火焰。这里有24小时不熄灯的科技园，有永远热血的创业者，这里属于每一个有梦就去追的人。",
          "keywords": ["💡 科技园", "🎨 华侨城", "🌊 大梅沙", "🏢 前海", "🎭 世界之窗"] },
        { "id": "guangzhou", "name": "广州", "emoji": "🦁",
          "tagline": "食在广州，商在广州",
          "subtitle": "千年商都 · 美食天堂 · 南国花城",
          "match_reason": "广州的热情与包容、敢为天下先的商业精神与火属性的感染力高度契合。这里是海上丝绸之路的起点，自古以来就是开放与活力的代名词。你有着广府人「叹世界」的乐观和「顶硬上」的坚韧——享受生活的同时从不畏惧挑战。",
          "keywords": ["🥟 早茶", "🦁 醒狮", "🏛️ 骑楼", "🌉 珠江夜游", "📦 广交会"] },
        { "id": "chongqing", "name": "重庆", "emoji": "🌶️",
          "tagline": "8D魔幻之都，热辣滚烫",
          "subtitle": "山城雾都 · 火锅江湖 · 立体魔幻",
          "match_reason": "重庆的热辣率真与火属性的直接和力度完美呼应。轻轨穿楼、长江索道，这座8D城市拒绝平庸，正如你的个性——不走寻常路，追求极致体验。重庆人的耿直和热情与你内心那份不畏惧表达真实的勇气如出一辙。",
          "keywords": ["🍲 火锅", "🚡 长江索道", "🏮 洪崖洞", "🚇 轻轨穿楼", "⛰️ 磁器口"] },
        { "id": "changsha", "name": "长沙", "emoji": "🎬",
          "tagline": "恰得苦、霸得蛮、耐得烦",
          "subtitle": "娱乐之都 · 敢为人先 · 湖湘精神",
          "match_reason": "长沙的娱乐基因和敢为人先的湖湘精神，是火属性最鲜活的当代写照。从湖南卫视到文和友，这座城市总在创造潮流。你和长沙人一样——不怕苦、不认输、不服周。在这里，你不需要隐藏自己的个性，越真实越受欢迎。",
          "keywords": ["📺 湖南卫视", "🦞 口味虾", "🏛️ 橘子洲", "🎢 世界之窗", "🍵 茶颜悦色"] },
        { "id": "xiamen", "name": "厦门", "emoji": "🏖️",
          "tagline": "城在海上，海在城中",
          "subtitle": "海上花园 · 文艺气息 · 慢生活美学",
          "match_reason": "厦门的温暖浪漫与火属性的热情似火形成了一种独特的平衡——不是灼人的烈焰，而是抚慰人心的篝火。鼓浪屿的琴声、环岛路的夕阳、沙坡尾的文创，这座城市将「热情」演绎为一种温柔而持久的生活方式。你像厦门的三角梅——在阳光下热烈绽放，在风雨中依然鲜艳。",
          "keywords": ["🎹 鼓浪屿", "🏫 厦门大学", "🌅 环岛路", "🎨 沙坡尾", "🛕 南普陀"] },
    ],
    "earth": [
        { "id": "xian", "name": "西安", "emoji": "🏛️",
          "tagline": "一座西安城，半部中国史",
          "subtitle": "十三朝古都 · 历史文脉 · 文化自信",
          "match_reason": "西安的厚重历史与土属性的沉稳可靠是最深沉的回响。站在明城墙上眺望钟楼，你能感受到千年的积淀在脚下。你和西安一样，不追求一时的夺目，而是用深厚的底蕴让人肃然起敬。这座城市的每一个角落都在诉说——真正的力量来自时间。",
          "keywords": ["⚔️ 兵马俑", "🏯 大雁塔", "🧱 明城墙", "🍜 回民街", "🎭 大唐不夜城"] },
        { "id": "zhengzhou", "name": "郑州", "emoji": "🚄",
          "tagline": "天地之中，通达八方",
          "subtitle": "中原腹地 · 米字枢纽 · 华夏之源",
          "match_reason": "郑州位于天地之中，是土属性最本真的地理表达。作为中国铁路的「心脏」，这座城市承载着四通八达的使命。你和郑州一样，天生具备连接与承载的力量——在你的世界里，你既是稳定的锚点，也是串联一切的枢纽。",
          "keywords": ["🚄 高铁枢纽", "🏛️ 河南博物院", "⛰️ 嵩山少林", "🏙️ CBD", "🌾 黄河"] },
        { "id": "luoyang", "name": "洛阳", "emoji": "🌸",
          "tagline": "唯有牡丹真国色",
          "subtitle": "神都洛阳 · 牡丹花城 · 千年帝都",
          "match_reason": "洛阳的牡丹是土属性最美的象征——深扎泥土、从容绽放。十三朝古都的底蕴赋予了这座城市不怒自威的沉稳。你和洛阳一样，内心有着丰富的层次和从容的节奏，不急于展示，但在恰当的时机一定会惊艳众人。",
          "keywords": ["🌺 牡丹", "🏯 龙门石窟", "⛩️ 白马寺", "🏮 洛邑古城", "🕍 应天门"] },
        { "id": "taiyuan", "name": "太原", "emoji": "⛏️",
          "tagline": "晋善晋美，诚信如山",
          "subtitle": "晋商故里 · 煤炭之都 · 三晋大地",
          "match_reason": "太原的朴实与诚信是土属性最宝贵的品质。晋商「一诺千金」的精神至今流淌在这座城市的血脉中。你和太原人一样——不善言辞但值得信赖，不追求浮华但内在充实。你的力量就像山西的煤，深沉而持久地发光发热。",
          "keywords": ["💰 晋商", "🏯 晋祠", "⛰️ 五台山", "🏛️ 平遥古城", "🍜 刀削面"] },
        { "id": "shijiazhuang", "name": "石家庄", "emoji": "🏭",
          "tagline": "脚踏实地，仰望星空",
          "subtitle": "华北重镇 · 红色热土 · 新兴之城",
          "match_reason": "石家庄的务实与低调是土属性最真诚的表达。它不是最闪耀的城市，却踏实地承载着千万人的生活与梦想。你像这座城市——也许不善于包装自己，但每一步都走得坚定扎实。正是这种脚踏实地的品质，让你走得比别人更远。",
          "keywords": ["⭐ 西柏坡", "🏔️ 苍岩山", "🌉 正定古城", "🏞️ 抱犊寨", "🎨 河北博物院"] },
    ],
    "metal": [
        { "id": "beijing", "name": "北京", "emoji": "🏛️",
          "tagline": "大气磅礴，方正规矩",
          "subtitle": "帝都气象 · 秩序井然 · 文化中心",
          "match_reason": "北京的方正格局与金属性的秩序感完美对应。从故宫的中轴线到长安街的笔直宽阔，这座城市的每一个毛孔都散发着规划与权威的美感。你像北京一样，内心有着清晰的原则和框架，在秩序中找到最大的自由与力量。",
          "keywords": ["🏯 故宫", "🧱 长城", "🎓 清华北大", "🎭 798艺术区", "🏮 胡同"] },
        { "id": "shanghai", "name": "上海", "emoji": "🌃",
          "tagline": "海纳百川，追求卓越",
          "subtitle": "东方魔都 · 国际金融 · 精致生活",
          "match_reason": "上海的精致高效与金属性的精准与锐利相得益彰。陆家嘴的天际线是理性与美学的完美结合，正如你追求的效率与品味从不矛盾。你身上有上海人的「腔调」——做事有标准，做人有格调，在规则中游刃有余。",
          "keywords": ["🏙️ 陆家嘴", "🛍️ 南京路", "🎭 外滩", "🏮 新天地", "🎨 西岸"] },
        { "id": "tianjin", "name": "天津", "emoji": "🚢",
          "tagline": "九河下梢天津卫",
          "subtitle": "北方大港 · 工业重镇 · 津味幽默",
          "match_reason": "天津的规矩与幽默是金属性最有趣的双面——一面是严谨的工业城市底蕴，一面是独特的津味乐天精神。你和天津人一样，在该认真时绝不含糊，在该放松时会心一笑。这种「规矩而不刻板」的平衡是你最大的魅力。",
          "keywords": ["🎡 天津之眼", "🏛️ 五大道", "🎭 相声", "🛕 古文化街", "🥟 狗不理"] },
        { "id": "shenyang", "name": "沈阳", "emoji": "⚙️",
          "tagline": "共和国长子的脊梁",
          "subtitle": "工业基石 · 东北心脏 · 铁骨柔情",
          "match_reason": "沈阳是中国工业的脊梁，这与金属性的坚毅与执行力一脉相承。作为「共和国长子」，沈阳支撑了中国现代化最初的梦想。你像这座城市——不追逐风口，但构筑了最坚实的基础。你的可靠与执行力，是团队中最不可或缺的钢铁骨架。",
          "keywords": ["🏭 工业博物馆", "🏯 沈阳故宫", "⛸️ 冰雪大世界", "🎭 中街", "🍖 烧烤"] },
        { "id": "dalian", "name": "大连", "emoji": "🌊",
          "tagline": "北方明珠，浪漫之都",
          "subtitle": "海滨城市 · 时尚气息 · 足球之城",
          "match_reason": "大连在金属性的理性框架下融入了海的浪漫，是你内外兼修的最佳体现。广场的对称美学与海岸线的自由曲线在这座城市完美共存。你像大连一样——面对外界展现的是秩序与专业，而内心的柔软与浪漫只留给最亲近的人。",
          "keywords": ["⛲ 星海广场", "🐯 老虎滩", "🏰 俄罗斯风情街", "🚃 有轨电车", "🌊 金石滩"] },
    ],
    "water": [
        { "id": "suzhou", "name": "苏州", "emoji": "🏡",
          "tagline": "上有天堂，下有苏杭",
          "subtitle": "园林之城 · 东方威尼斯 · 江南雅韵",
          "match_reason": "苏州的园林是水属性智慧的最高美学——以小见大、移步换景、曲径通幽。你像苏州一样，内心世界丰富而精巧，总能在有限的空间创造无限的意境。这种「以柔克刚」的东方智慧在你身上体现得淋漓尽致。",
          "keywords": ["🏯 拙政园", "🛶 平江路", "🎋 虎丘", "🏭 苏州工业园区", "🎭 昆曲"] },
        { "id": "nanjing", "name": "南京", "emoji": "🏯",
          "tagline": "江南佳丽地，金陵帝王州",
          "subtitle": "六朝古都 · 江水环绕 · 文化荟萃",
          "match_reason": "南京的深沉与包容是水属性最深邃的一面——秦淮河的灯火映照着千年兴衰，这座城市用江水般的胸怀容纳了所有历史的沧桑。你像南京一样，外表温润如水，内心却有着深厚的定力和不可动摇的底线。",
          "keywords": ["🏛️ 中山陵", "🛕 鸡鸣寺", "🎑 秦淮河", "🌳 梧桐大道", "🏯 夫子庙"] },
        { "id": "wuhan", "name": "武汉", "emoji": "🌉",
          "tagline": "大江大湖大武汉",
          "subtitle": "九省通衢 · 两江交汇 · 英雄之城",
          "match_reason": "武汉因水而生、因水而兴——长江与汉江在此交汇，赋予了这座城市「水」的流动与包容。你像武汉一样，有着「九省通衢」的通达与灵活，能在复杂多变的环境中找到最优路径。武汉人的「不服周」精神也在你身上——柔中带刚，坚忍不拔。",
          "keywords": ["🌉 长江大桥", "🌸 武大樱花", "🏛️ 黄鹤楼", "🍜 热干面", "🏞️ 东湖"] },
        { "id": "qingdao", "name": "青岛", "emoji": "⛵",
          "tagline": "红瓦绿树，碧海蓝天",
          "subtitle": "帆船之都 · 啤酒之城 · 欧韵海滨",
          "match_reason": "青岛的海洋气质与水的自由包容天然共鸣。帆船需要风与水才能远航，而你就像青岛——善于借助环境的力量，顺势而为却不失方向。这里有德国建筑群的优雅、有八大关的浪漫、有啤酒节的豪放，正如你丰富而立体的人格。",
          "keywords": ["🍺 啤酒节", "⛵ 奥帆中心", "🏖️ 金沙滩", "⛪ 八大关", "🌊 栈桥"] },
        { "id": "ningbo", "name": "宁波", "emoji": "🚢",
          "tagline": "书藏古今，港通天下",
          "subtitle": "东海之滨 · 商贸重镇 · 书香之城",
          "match_reason": "宁波兼具「书藏古今」的文化底蕴和「港通天下」的商业智慧，是水属性智慧与变通的完美结合。你像宁波港一样——表面平静，暗流涌动，蕴含着巨大的能量。你既有天一阁般的深厚内功，又能像宁波帮一样在广阔天地中把握机遇。",
          "keywords": ["📚 天一阁", "🚢 宁波港", "⛰️ 雪窦山", "🏮 老外滩", "🛕 天童寺"] },
    ],
}

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{city_name} - 城市匹配测验结果</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700;900&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Noto Sans SC', -apple-system, sans-serif;
            background: #FAF5F0;
            color: #3D2B1F;
            min-height: 100vh;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }}
        .container {{ max-width: 480px; margin: 0 auto; padding: 0 20px 32px; }}

        /* 品牌头部 */
        .brand-header {{
            display: flex; align-items: center; justify-content: center;
            gap: 8px; padding: 24px 0 8px;
        }}
        .brand-badge {{
            width: 28px; height: 28px; border-radius: 50%;
            background: #C97F7F; color: white;
            display: flex; align-items: center; justify-content: center;
            font-size: 13px; font-family: 'Noto Serif SC', serif;
        }}
        .brand-text {{ font-family: 'Noto Serif SC', serif; font-size: 14px; color: #6B5A4E; }}
        .brand-text-en {{ font-family: 'Noto Serif SC', serif; font-style: italic; font-size: 11px; color: #C9A96E; letter-spacing: 2px; }}

        /* 装饰标题 */
        .deco-title {{ text-align: center; margin-bottom: 20px; }}
        .deco-title .en {{ font-family: 'Noto Serif SC', serif; font-style: italic; font-size: 11px; color: #C9A96E; letter-spacing: 3px; display: block; margin-bottom: 6px; }}
        .deco-title .main {{ font-family: 'Noto Serif SC', serif; font-size: 22px; font-weight: 700; color: #3D2B1F; }}
        .deco-title .main .highlight {{ color: #C97F7F; }}
        .deco-title .sub {{ font-family: 'Noto Serif SC', serif; font-style: italic; font-size: 12px; color: #A89888; letter-spacing: 2px; margin-top: 6px; display: block; }}

        /* 城市展示区 */
        .city-showcase {{ text-align: center; padding: 8px 0 16px; }}
        .best-match-badge {{
            display: inline-block;
            background: linear-gradient(135deg, #D4837F 0%, #C4736F 100%);
            color: white; font-size: 11px; padding: 4px 14px;
            border-radius: 20px; margin-bottom: 14px; font-weight: 500; letter-spacing: 1px;
        }}
        .city-circle {{
            width: 160px; height: 160px; border-radius: 50%; margin: 0 auto 14px;
            display: flex; align-items: center; justify-content: center; font-size: 64px;
            position: relative; overflow: hidden;
            background: linear-gradient(135deg, {element_color}22 0%, {element_color}44 100%);
            box-shadow: 0 6px 24px rgba(61,43,31,0.08);
        }}
        .city-circle img {{
            width: 100%; height: 100%; object-fit: cover; border-radius: 50%;
        }}
        .city-circle::after {{
            content: ''; position: absolute; inset: -4px; border-radius: 50%;
            border: 2px solid rgba(201,169,110,0.3);
        }}
        .city-name-zh {{ font-family: 'Noto Serif SC', serif; font-size: 38px; font-weight: 900; color: #3D2B1F; letter-spacing: 6px; margin-bottom: 4px; }}
        .city-tagline {{ font-family: 'Noto Serif SC', serif; font-size: 14px; color: #C97F7F; letter-spacing: 2px; margin-bottom: 8px; }}
        .city-subtitle {{ font-size: 12px; color: #A89888; letter-spacing: 1px; }}

        /* 卡片 */
        .card {{
            background: #FFFFFF; border-radius: 20px; padding: 24px;
            margin-bottom: 14px; box-shadow: 0 2px 16px rgba(61,43,31,0.04);
            border: 1px solid rgba(185,160,130,0.1);
        }}
        .card-warm {{ background: #FFF9F4; }}
        .card-title {{
            font-family: 'Noto Serif SC', serif; font-size: 16px; font-weight: 700;
            margin-bottom: 14px; display: flex; align-items: center; gap: 8px;
        }}
        .card-desc {{ font-size: 14px; color: #6B5A4E; line-height: 2; }}

        /* 五行标签 */
        .element-badge {{
            display: inline-flex; align-items: center; gap: 6px;
            background: {element_bg}; color: {element_dark};
            font-size: 13px; font-weight: 600; padding: 6px 14px;
            border-radius: 12px; margin-bottom: 12px;
        }}

        /* 关键词 */
        .keywords {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }}
        .keyword {{
            background: {element_bg}; color: {element_dark};
            font-size: 12px; padding: 5px 12px; border-radius: 16px; font-weight: 500;
        }}

        /* 五行得分条 */
        .score-row {{ display: flex; align-items: center; gap: 10px; padding: 6px 0; }}
        .score-label {{ width: 52px; font-size: 12px; color: #A89888; text-align: right; flex-shrink: 0; }}
        .score-bar-wrap {{ flex: 1; height: 6px; background: #F3EDE6; border-radius: 3px; overflow: hidden; }}
        .score-bar {{ height: 100%; border-radius: 3px; transition: width 1s ease; }}
        .score-val {{ width: 32px; font-size: 12px; font-weight: 600; color: #3D2B1F; text-align: left; flex-shrink: 0; }}
        .score-row.active .score-val {{ color: {element_dark}; font-size: 14px; }}
        .score-row.active .score-label {{ font-weight: 600; color: {element_dark}; }}

        /* 竖线装饰引用 */
        .quote {{ position: relative; padding-left: 14px; border-left: 3px solid {element_color}; }}

        /* 按钮 */
        .btn {{
            width: 100%; padding: 16px 24px; border: none; border-radius: 16px;
            font-size: 15px; font-weight: 600; font-family: inherit;
            cursor: pointer; transition: all 0.25s ease;
            display: flex; align-items: center; justify-content: center; gap: 8px;
            text-decoration: none;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, #D4837F 0%, #C4736F 100%);
            color: white; box-shadow: 0 4px 16px rgba(196,115,111,0.25);
        }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 6px 24px rgba(196,115,111,0.35); }}
        .btn-secondary {{
            background: #FFFFFF; color: #6B5A4E; border: 1px solid rgba(185,160,130,0.15);
        }}
        .btn-secondary:hover {{ background: #FFF9F4; }}

        /* 底部分隔线 */
        .section-divider {{
            text-align: center; margin: 20px 0 16px;
            font-family: 'Noto Serif SC', serif; font-size: 13px; color: #A89888;
            letter-spacing: 2px;
        }}
        .section-divider .line {{
            display: inline-block; width: 40px; height: 1px;
            background: rgba(185,160,130,0.2); vertical-align: middle; margin: 0 10px;
        }}

        /* 底部 */
        .footer {{ text-align: center; padding: 16px 0; color: #C9B8A8; font-size: 11px; font-family: 'Noto Serif SC', serif; letter-spacing: 1px; }}

        @media (max-width: 380px) {{
            .city-name-zh {{ font-size: 32px; letter-spacing: 4px; }}
            .city-circle {{ width: 130px; height: 130px; }}
            .deco-title .main {{ font-size: 20px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="brand-header">
            <div class="brand-badge">五</div>
            <span class="brand-text">五行城市</span>
            <span class="brand-text-en">Five Elements City</span>
        </div>

        <div class="deco-title">
            <span class="en">your destiny city</span>
            <div class="main">你的五行<span class="highlight">城市</span></div>
            <span class="sub">based on your element & personality</span>
        </div>

        <div class="city-showcase">
            <div class="best-match-badge">⭐ 最佳匹配</div>
            <div class="city-circle"><img src="../images/{city_id}.jpg" alt="{city_name}"></div>
            <div class="city-name-zh">{city_name}</div>
            <div class="city-tagline">{city_tagline}</div>
            <div class="city-subtitle">{city_subtitle}</div>
        </div>

        <div class="card">
            <div class="element-badge">{element_emoji} {element_name}属性 · {element_en}</div>
            <div class="card-title">⚖️ 五行匹配度</div>
            {score_bars}
        </div>

        <div class="card card-warm">
            <div class="card-title">💫 为什么是{city_name}？</div>
            <div class="card-desc quote">{match_reason}</div>
            <div class="keywords">
                {keywords_html}
            </div>
        </div>

        <div class="section-divider"><span class="line"></span>性格解读<span class="line"></span></div>

        <div class="card">
            <div class="card-title">🧠 你的性格画像</div>
            <div class="card-desc">{personality}</div>
        </div>

        <div class="card card-warm">
            <div class="card-title">💡 给你的话</div>
            <div class="card-desc">{life_advice}</div>
            <div class="card-desc" style="margin-top:10px;">{work_style}</div>
        </div>

        <a href="../index.html" class="btn btn-primary" style="margin-bottom:10px;">
            🔄 再测一次
        </a>
        <a href="../results-index.html" class="btn btn-secondary">
            🏙️ 查看全部城市
        </a>

        <div class="footer">
            <p>五行城市 · 找到属于你的城</p>
        </div>
    </div>
</body>
</html>'''


def generate_scores(element_key):
    elements = ["wood", "fire", "earth", "metal", "water"]
    scores = {}
    random.seed(hash(element_key) * 31)
    for k in elements:
        if k == element_key:
            scores[k] = 92
        else:
            scores[k] = random.choice([38, 42, 45, 48, 52, 55, 58, 62, 65])
    return scores


def generate_html(city, element_key):
    e = element_config[element_key]
    scores = generate_scores(city["id"])
    elements = ["wood", "fire", "earth", "metal", "water"]
    emojis = {"wood": "🌲", "fire": "🔥", "earth": "🏔️", "metal": "⚙️", "water": "💧"}
    names = {"wood": "木", "fire": "火", "earth": "土", "metal": "金", "water": "水"}
    colors = {"wood": "#7CB342", "fire": "#E57373", "earth": "#BCAAA4", "metal": "#90A4AE", "water": "#64B5F6"}
    bgs = {
        "wood": "rgba(124,179,66,0.08)", "fire": "rgba(229,115,115,0.08)",
        "earth": "rgba(188,170,164,0.08)", "metal": "rgba(144,164,174,0.08)",
        "water": "rgba(100,181,246,0.08)"
    }
    darks = {"wood": "#558B2F", "fire": "#C62828", "earth": "#8D6E63", "metal": "#546E7A", "water": "#1E88E5"}

    score_bars = ""
    for k in elements:
        sc = scores[k]
        active = "active" if k == element_key else ""
        score_bars += f'''
                <div class="score-row {active}">
                    <div class="score-label">{emojis[k]} {names[k]}</div>
                    <div class="score-bar-wrap">
                        <div class="score-bar" style="width:{sc}%;background:{colors[k]};"></div>
                    </div>
                    <div class="score-val">{sc}%</div>
                </div>'''

    keywords_html = "\n".join(f'<span class="keyword">{kw}</span>' for kw in city["keywords"])

    return HTML_TEMPLATE.format(
        city_name=city["name"],
        city_id=city["id"],
        city_emoji=city["emoji"],
        city_tagline=city["tagline"],
        city_subtitle=city["subtitle"],
        match_reason=city["match_reason"],
        keywords_html=keywords_html,
        element_name=e["name"],
        element_emoji=e["emoji"],
        element_en=e["en"],
        element_color=e["color"],
        element_dark=e["color_dark"],
        element_bg=bgs[element_key],
        score_bars=score_bars,
        personality=e["personality"],
        life_advice=e["life_advice"],
        work_style=e["work_style"],
    )


# 生成25个城市页
generated = []
for element_key, city_list in cities.items():
    for city in city_list:
        filepath = os.path.join(output_dir, f"{city['id']}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(generate_html(city, element_key))
        generated.append({"name": city["name"], "element": element_config[element_key]["name"], "file": f"{city['id']}.html"})

# 生成导航索引页
index_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>五行城市 · 全部结果预览</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Noto Sans SC', -apple-system, sans-serif; background: #FAF5F0; color: #3D2B1F; min-height: 100vh; }
        .header { background: linear-gradient(135deg, #3D2B1F 0%, #5C4033 100%); color: white; padding: 40px 24px; text-align: center; }
        .header h1 { font-family: 'Noto Serif SC', serif; font-size: 26px; margin-bottom: 6px; }
        .header p { font-size: 13px; opacity: 0.7; font-family: 'Noto Serif SC', serif; font-style: italic; letter-spacing: 1px; }
        .container { max-width: 600px; margin: 0 auto; padding: 24px 20px 40px; }
        .section { margin-bottom: 32px; }
        .section-title { font-family: 'Noto Serif SC', serif; font-size: 16px; font-weight: 700; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; }
        .bar { width: 100%; height: 3px; border-radius: 2px; margin-bottom: 14px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; }
        .city-link { display: flex; align-items: center; gap: 10px; padding: 14px 14px; border-radius: 14px;
            background: white; border: 1px solid rgba(185,160,130,0.1); text-decoration: none; color: inherit;
            transition: transform 0.2s, box-shadow 0.2s; }
        .city-link:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(61,43,31,0.06); }
        .city-link .emoji {{ font-size: 22px; }}
        .city-link .thumbnail {{
            width: 56px; height: 56px; border-radius: 50%; object-fit: cover;
            margin-bottom: 6px; box-shadow: 0 2px 8px rgba(61,43,31,0.1);
        }}
        .city-link .name {{ font-size: 14px; font-weight: 600; }}
        .back-link { display: block; text-align: center; margin-top: 24px; color: #C97F7F; text-decoration: none; font-size: 14px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏙️ 五行城市 · 全部结果</h1>
        <p>5 种五行 × 5 个城市 = 25 个专属结果</p>
    </div>
    <div class="container">
'''

bar_colors = {"wood": "#7CB342", "fire": "#E57373", "earth": "#BCAAA4", "metal": "#90A4AE", "water": "#64B5F6"}
section_titles = {"wood": "🌲 木属性", "fire": "🔥 火属性", "earth": "🏔️ 土属性", "metal": "⚙️ 金属性", "water": "💧 水属性"}

for element_key, city_list in cities.items():
    index_html += f'''
    <div class="section">
        <div class="section-title">{section_titles[element_key]} · 5个城市</div>
        <div class="bar" style="background:{bar_colors[element_key]};"></div>
        <div class="grid">
'''
    for city in city_list:
        index_html += f'''
            <a href="results/{city['id']}.html" class="city-link">
                <img src="images/{city['id']}.jpg" alt="{city['name']}" class="thumbnail">
                <span class="name">{city['name']}</span>
            </a>'''
    index_html += '''
        </div>
    </div>'''

index_html += '''
        <a href="index.html" class="back-link">← 返回测验首页</a>
    </div>
</body>
</html>'''

with open(os.path.join(output_dir, '..', 'results-index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

print(f"✅ 已生成 {len(generated)} 个城市结果页")
print(f"✅ 已生成导航索引页 results-index.html")
