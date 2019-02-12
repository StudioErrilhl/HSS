init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    class Item(store.object):
        def __init__(self, name, displayname, weight, desc, amount=1):
            self.name = name
            self.displayname = displayname
            self.weight = weight
            self.amount = amount
            self.desc = desc

    class InvItem(store.object):
        def __init__(self, item, amount):
            self.item = item
            self.name = item.name
            self.displayname = item.displayname
            self.weight = item.weight
            self.amount = amount
            self.desc = item.desc

    class Container(store.object):
        def __init__(self, weight_max=75):
            self.inventory = []
            self.weight_max = weight_max

        def __iter__(self):
            return iter(self.inventory)

        def finditem(self, item):
            return(self.inventory[[i.item for i in self.inventory].index(item)])

        def add_item(self, item, amount=1): #remember to use the item-assignment, not anything else, to add to inventory
            if item.weight * amount > self.weight_max - sum(i.item.weight * i.amount for i in self.inventory):
                name = item.name.lower().replace('fs','').replace('fm','').replace('_',' ').title()
                name = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), name, 1)
                renpy.notify(name+' exceeds max weight you can carry')
            else:
                if self.has_item(item):
                    self.finditem(item).amount += amount
                else:
                    self.inventory.append(InvItem(item, amount))
                if 'fsp' in item.name.lower():
                    name = item.name.lower().replace('fsp','panties - ').replace('fm','').replace('_','').title()
                else:
                    name = item.name.lower().replace('fs','').replace('fm','').replace('_',' ').title()
                name = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), name, 1)
                renpy.notify(name+' added successfully')

        def has_item(self, item, a=1,returnname=False): #remember to use the Item-assignment, not a string to check for items
            if item in [i.item for i in self.inventory]:
                if self.finditem(item).amount >= a and returnname:
                    return(self.finditem(item).name.capitalize())
                elif self.finditem(item).amount >= a:
                    return(self.finditem(item).amount)
                else:
                    return(False)
            else:
                return(False)

        def remove_item(self,item,amount=1,sec_reply=False): #remember to use the Item-assignment, not a string, to remove items
            if self.has_item(item):
                self.finditem(item).amount -= amount
                if self.finditem(item).amount <= 0:
                    self.inventory.pop(self.inventory.index(self.finditem(item)))
                    if sec_reply and item == phone_item:
                        renpy.notify("You put the "+item.name+" on charge")
                    elif sec_reply:
                        name = name = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), item.name, 1)
                        renpy.notify("You returned the "+name)
                    else:
                        name = name = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), item.name, 1)
                        renpy.notify(name+" has been deleted")
                else:
                    renpy.notify("There are "+str(self.finditem(item).amount)+" "+str(item.name)+" left")
            else:
                renpy.notify("Couldn't find the item you were trying to delete")

init -1 python:
    def updateInventory():
        for file in renpy.list_files():
            if file.startswith('images/inventory/') and file.endswith('.webp'):
                if 'hover' in file:
                    name = file.replace('images/inventory/','').replace('_hover','').replace('.webp','')
                    if not hasattr( store, ""+name+"_item" ):
                        weight = item_weights[name]
                        desc = item_desc[name]
                        if 'fsp_' in name:
                            ptmp = name.replace('fsp_','panties_').replace('_',' ').split(' ')
                            if len(ptmp) == 2:
                                pname = ptmp[0]+' - '+ptmp[1]
                            elif len(ptmp) == 3:
                                pname = str(ptmp[0]+' - '+ptmp[1]+' '+ptmp[2])
                            else:
                                pname = str(ptmp[0])
                            displayname = pname.capitalize()
                        else:
                            displayname = name.capitalize()
                        setattr(store,""+name+"_item",Item(name,displayname,weight,desc))