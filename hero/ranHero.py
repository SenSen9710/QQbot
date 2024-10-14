from tool.mysql import MysqlTool

with MysqlTool() as db:
    data = db.execute('select * from herodata;')
    print(len(data))
    mage = []
    support = []
    fighter = []
    tank = []
    marksman = []
    assassin = []
    for x in range(len(data)):
        roles = data[x][3]
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
    print(len(mage),len(support),len(fighter),len(tank),len(marksman),len(assassin))


