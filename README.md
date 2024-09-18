# Friendship with Benefits 2

改动生成脚本时应当先后运行 convert 和 reconvert 检查是否能无损的互转

目前的生成脚本会漏掉形如下方所示的对话

```rpy

# game/3 - World Map.rpy:131
translate chinese moxmenu_ca71130c:

    # mox "Hey stud!" nointeract
    mox "" nointeract

```
