class ShoppingCart:
    # write your code here
    def __init__(self, _employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = _employee_discount
        
    @property
    def total(self):
        return self._total
        
    @total.setter
    def total(self, _t):
        self._total = _t
        return self._total
        
    @property
    def items(self):
        return self._items
        
    @total.setter
    def items(self, _i):
        self._items = _i
        return self._items
            
    @property
    def employee_discount(self):
        return self._employee_discount
        
    @employee_discount.setter
    def employee_discount(self, _ed):
        self._employee_discount = _ed
        return self._employee_discount
         
    def add_item(self, name, price, n=1):
        for i in list(range(n)):
            self._items.append({"name": name, "price": price})
            self._total += price
        return self._total
    
    def mean_item_price(self):
        price_lst = []
        for x in self._items:
            price_lst.append(x["price"])
        return sum(price_lst)/len(price_lst)    
        
    def median_item_price(self):
        price_lst = []   
        for x in self._items:
            price_lst.append(x["price"])            
        lgth = float(len(price_lst))
        if lgth%2==0:
            return (price_lst[int(lgth/2)]+price_lst[int((lgth/2)-1)])/2
        else:
            return price_lst[int((lgth-1)/2)]
            
    def apply_discount(self):
        if self._employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("        
        else:
            d = self._employee_discount/100
            return self._total-(self._total*d)
            
    def item_names(self):
        i_n = []
        for item in self._items:
            i_n.append(item["name"])
        return i_n
        
    def void_last_item(self):
        if self._items == []:
            return "There are no items in your cart!"
        else:
            self._total -=self._items[-1]["price"]
            self._items.pop()
            