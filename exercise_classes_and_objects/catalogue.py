class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)


    def get_by_letter(self, first_letter):
        self.current_list = []
        for pr in self.products:
            if pr[0] == first_letter:
                self.current_list.append(pr)
        return self.current_list

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:\n"
        output += '\n'.join(sorted(self.products))
        return output

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
