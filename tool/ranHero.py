from tool.mysql import MysqlTool
import random

mage = []
support = []
fighter = []
tank = []
marksman = []
assassin = []
mage_a = []
support_a = []
fighter_a = []
tank_a = []
marksman_a = []
assassin_a = []
mage_b = []
support_b = []
fighter_b = []
tank_b = []
marksman_b = []
assassin_b = []
team_a = []
team_b = []
class RandHero:

    def randomhero(num: int):
        with MysqlTool() as db:
            data = db.execute('select * from herodata;')
            # print(len(data))
            for x in range(len(data)):
                roles = data[x][4]
                if 'mage' in roles:
                    mage.append(data[x])
                if 'support' in roles:
                    support.append(data[x])
                if 'fighter' in roles:
                    fighter.append(data[x])
                if 'tank' in roles:
                    tank.append(data[x])
                if 'marksman' in roles:
                    marksman.append(data[x])
                if 'assassin' in roles:
                    assassin.append(data[x])
                # print(len(mage), len(support), len(fighter), len(tank), len(marksman), len(assassin))
        total = []
        mage_new = random.sample(mage, 2 * num)
        support_new = random.sample(support, 2 * num)
        fighter_new = random.sample(fighter, 2 * num)
        tank_new = random.sample(tank, 2 * num)
        marksman_new = random.sample(marksman, 2 * num)
        assassin_new = random.sample(assassin, 2 * num)
        total = total + mage_new + support_new + fighter_new + tank_new + marksman_new + assassin_new
        count = 0
        while len(total) != len(set(total)):
            total = []
            mage_new = random.sample(mage, 2 * num)
            support_new = random.sample(support, 2 * num)
            fighter_new = random.sample(fighter, 2 * num)
            tank_new = random.sample(tank, 2 * num)
            marksman_new = random.sample(marksman, 2 * num)
            assassin_new = random.sample(assassin, 2 * num)
            total = total + mage_new + support_new + fighter_new + tank_new + marksman_new + assassin_new
            # print(len(total), len(set(total)))
            count = count + 1
            if len(total) == len(set(total)):
                # print(len(mage_new))
                # print(count)
                break
        for x in range(len(mage_new)):
            if x < num:
                mage_a.append(mage_new[x])
                support_a.append(support_new[x])
                fighter_a.append(fighter_new[x])
                tank_a.append(tank_new[x])
                marksman_a.append(marksman_new[x])
                assassin_a.append(assassin_new[x])
            else:
                mage_b.append(mage_new[x])
                support_b.append(support_new[x])
                fighter_b.append(fighter_new[x])
                tank_b.append(tank_new[x])
                marksman_b.append(marksman_new[x])
                assassin_b.append(assassin_new[x])
        team_a = mage_a+support_a+fighter_a+tank_a+marksman_a+assassin_a
        team_b = mage_b+support_b+fighter_b+tank_b+marksman_b+assassin_b
        return team_a,team_b
            # for x in range(len(mage_b)):
            #     print(mage_a[x], mage_b[x])
            #     print(support_a[x], support_b[x])
            #     print(fighter_a[x], fighter_b[x])
            #     print(tank_a[x], tank_b[x])
            #     print(marksman_a[x], marksman_b[x])
            #     print(assassin_a[x], assassin_b[x])
