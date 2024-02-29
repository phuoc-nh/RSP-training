import math

reqArea = int(input().strip())

area_count = int(input().strip())

area = []
dupAreaPriceMap = {}
for _ in range(area_count):
    area_item = int(input().strip())
    area.append(area_item)
    dupAreaPriceMap[area_item] = []

price_count = int(input().strip())

price = []

for i in range(price_count):
    price_item = int(input().strip())
    price.append(price_item)
    dupAreaPriceMap[area[i]].append(price_item)


class Area:
    def __init__(self, area, price, compList):
        self.area = area
        self.price = price
        self.compList = compList
        self.sums = []
        
    def isOutliner(self):
        if len(self.compList) == 0:
            return False
        
        mean = sum(self.compList) / len(self.compList)
        var  = sum(pow(x-mean,2) for x in self.compList) / len(self.compList)
        standDeviation  = math.sqrt(var)
        
        # print('price',self.price)
        # print('mean',mean)
        # print('devi',standDeviation)
        # print('3devi',3 * standDeviation)
        # print('outliner', abs(self.price - mean) > 3 * standDeviation)
        # print('--------------')
        return abs(self.price - mean) > 3 * standDeviation
    
    def __eq__(self, other):
        return self.area == other.area

    def __hash__(self):
        return self.area
        
    def print(self):
        print('area', self.area)
        print('price', self.price)
        print('comList', self.compList)
        print('isOutliner', self.isOutliner())
        print('==============')
        

def valuation(reqArea, area, price, dupAreaPriceMap):
    areaPriceList = []
    for i in range(len(area)):
        compList = dupAreaPriceMap[area[i]].copy()
        compList.remove(price[i])
        # print('compList', compList)
        entity = Area(area[i], price[i], compList)
        areaPriceList.append(entity)

    notOutlinersArea = filter(lambda x: not x.isOutliner(), areaPriceList)
    remainArea = set()
    areaPriceMap = {}
    for a in notOutlinersArea:
        remainArea.add(a)
        
        if a.area not in areaPriceMap:
            areaPriceMap[a.area] = [a.price]
        else:
            
            areaPriceMap[a.area].append(a.price)
            
    # print(areaPriceMap)
    remainArea = list(remainArea)
    
    

    res = None
    if len(remainArea) == 0:
        res = reqArea * 1000

    elif len(remainArea) == 1:
        leftArea = remainArea[0]
        # print('leftArea', leftArea)
        mean = sum(areaPriceMap[leftArea.area]) / len(areaPriceMap[leftArea.area])
        res = (reqArea * remainArea[0].price) / remainArea[0].area 

    elif len(remainArea) > 1:
        remainArea.sort(key=lambda x: x.area)
        lowClosest = None
        upClosest = None
        i = 0
        
        # for a in remainArea:
        #     a.print()
        # for a in remainArea:
        #     a.print()
        while i < len(remainArea) and reqArea >= remainArea[i].area :
            i += 1
        
        
        # print('remainArea[0]', remainArea[0].print())
        # print('remainArea[1]', remainArea[1].print())
        if i == 0:
            lowClosest = remainArea[0]
            upClosest = remainArea[1]
        elif i >= len(remainArea):
            lowClosest = remainArea[-2]
            upClosest = remainArea[-1]
        else:
            lowClosest = remainArea[i-1]
            upClosest = remainArea[i]
        # print('lowest')
        # print(lowClosest.print())
        # print('up')
        # print(upClosest.print())
        # print('req', reqArea)
        meanLowPrice = sum(areaPriceMap[lowClosest.area]) / len(areaPriceMap[lowClosest.area])
        meanUpPrice = sum(areaPriceMap[upClosest.area]) / len(areaPriceMap[upClosest.area])
        # print(meanLowPrice)
        # print(meanUpPrice)
        # print(upClosest.area)
        # print(lowClosest.area)
        meanBase = meanLowPrice
        base = lowClosest
        if i >= len(remainArea):
            meanBase = meanUpPrice
            base = upClosest
            
        # print('meanBase', meanBase)
        # print('meanUpPrice', meanUpPrice)
        # print('meanLowPrice', meanLowPrice)
        # print('lowClosest.area', lowClosest.area)
        # print('upClosest.area', upClosest.area)
        
        res = meanBase + (meanUpPrice - meanLowPrice) * (reqArea - base.area) / (upClosest.area - lowClosest.area)


    res = max(1e3, res)
    res = min(1e6, res)

    print('>>>>>>',round(res))
    return round(res)
        # for r in remainArea:
        #     if r
    
valuation(reqArea, area, price, dupAreaPriceMap)
