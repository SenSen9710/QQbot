import json
import logging
import requests

from tool.mysql import MysqlTool


class UpdateHero:
    """更新数据库中英雄表的数据"""

    @staticmethod
    def updatedate():
        res = requests.get("https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js")
        res = res.text

        # 把获取的数据转换成列表
        hero_data = json.loads(res)

        with MysqlTool() as db:
            # 获取最新英雄数量
            hero_num = len(hero_data['hero'])
            # 查询库中英雄数量
            sel_count = db.execute('SELECT COUNT(id) from herodata;')
            # 作比较
            if hero_num != sel_count[0][0]:
                # 清空再重新插入
                db.execute('TRUNCATE TABLE herodata;')
                logging.info("清空表数据完成")
                for x in range(len(hero_data['hero'])):
                    hero_id = hero_data['hero'][x]['heroId']
                    name = hero_data['hero'][x]['title']
                    roles = hero_data['hero'][x]['roles']
                    roles = ','.join(map(str, roles))
                    sql = 'INSERT INTO herodata (heroId, name, roles) VALUES (%s, %s, %s);'
                    values = (hero_id, name, roles)
                    db.execute(sql, args=values, commit=True)
                logging.info("已获取英雄最新数据")


