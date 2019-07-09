# 贪吃蛇游戏
> <b>实现规则</b>：
1. 贪吃蛇、食物
2. 能控制蛇上下移动来获取食物
3. 贪吃蛇在吃取食物后，自身长度增加，同时食物消失并随机生成新的食物
4. 如果贪吃蛇触碰到四周墙壁 或者 触碰到自己身体时，则游戏结束

> <b>术语注释：</b>：
* SDL（Simple DirectMedia Layer）:是一个跨平台库，支持访问计算机多媒体硬件（声音、视频、输入等），SDL非常强大，但美中不足的是它是基于 C的。
* PyGame:是 SDL 库的 Python 包装器（wrapper），Pygame 在SDL库的基础上提供了各种接口，从而使用用户能够使用python语言创建各种各样的游戏或多媒体程序。

## Pygame用法：
* <b>pygame.locals</b>: 从pygame模块导入常用的函数和常量
* <b>pygame.display.set_mode</b>: 初始化一个游戏界面窗口，包括分辨率、标志位、色深
* pygame.display.set_caption: 设置窗口标题
* pygame.font.SysFont: 初始化游戏界面内使用的字体
* pygame.Color: 定义颜色变量
* pygame.event.get: 检测按键等Pygame事件
* pygame.draw.rect: 绘制位置
* pygame.display.flip: 刷新Pygame的显示层，贪吃蛇与食物的每一次移动，都会进行刷新显示层的操作来显示