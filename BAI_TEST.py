class Product:
    def __init__(self, id, name, price, quantity_sold, discount=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        

    @property
    def total_revenue(self):
        return self.quantity_sold * self.price

    @property
    def revenue_type(self):
        revenue = self.total_revenue 
        if revenue < 5_000_000: return "Thấp"
        if revenue < 20_000_000: return "Trung bình"
        if revenue <= 50_000_000: return "Khá"
        return "Cao"

    def display_info(self):
        print(f"MA  : {self.id} | Ten : {self.name} | Gia : {self.price:,} | DT : {self.total_revenue:,} | Status : {self.revenue_type}")

    @property
    def calculate_revenue(self):
        self.total_revenue = self.quantity_sold * self.price
        return self.quantity_sold * self.price

    def check_revenue_type(self):
        revenue = self.total_revenue
        if revenue < 5_000_000:
            self.revenue_type = "Thấp"
            
        elif revenue >= 5_000_000 and revenue < 20_000_000:
            self.revenue_type = "Trung bình"
            
        elif revenue >= 20_000_00 and revenue <= 50_000_000:
            self.revenue_type = "Khá"
            
        else:
            self.revenue_type = "Cao"
            

    def display_info(self):
        print(f"MA  : {self.id} | Ten : {self.name} | Gia ban : {self.price} | Doanh thu : {self.total_revenue:,.0f} VND | Status : {self.revenue_type}")
        
    
    

class ProductManager:
    def __init__(self):
        self.products = [
                Product("SP001","Laptop Dell", 15_000_000 , 17 , 2_000_000),
                Product("SP002","Chuột Logitech", 350_000 , 20 , 2_000_000),
                Product("SP003","Bàn phím cơ AKKO", 1_200_000 , 10 , 1_000_000),
                Product("SP004","Màn hình Samsung", 500_000 , 5 , 0),
                Product("SP005","Tai nghe sony", 2_500_000 , 1 , 0),
                Product("SP006","Laptop lenlovo", 2_500_000 , 1 , 0),
                Product("SP007","Laptop asus", 2_500_000 , 1 , 0),
        ]

    def display_all_products(self):
        if len(self.products) == 0:
            print("Danh sách đang trống")
            return
        for product in self.products:
            product.display_info()
            


    def check_id_in_list(self , id_check):
        found = None
        for products in self.products:
            if products.id == id_check:
                # print(f"Đã tìm thấy {products.id}")
                return products
        if found == None:
            return None

        
    def add_new_product(self):
        new_product_id = input("Nhập mã sản phẩm mới ").upper().strip()
        if new_product_id == "":
            print("Mã sản phẩm không được để trống")
            return
        
        if ProductManager.check_id_in_list(self, new_product_id) !=  None :
            print(f"{new_product_id} đã tồn tại trong danh sách này !")
            return
        
        new_product_name = input("Nhập tên sản phẩm : ").title().strip()
        if new_product_name == "":
            print("Tên sản phẩm không được đẻ trống")
            return
        
        try:
            new_price_input = float(input("Nhập giá bán sản phẩm mới : "))
        except ValueError:
            print("Sai định dạng vừa nhập vào")
            return

        if new_price_input < 0:
            print("Giá bán không được âm")
            return
        
        try:
            new_quantity_sold = int(input("Nhập số lượng đã bán : "))
        except ValueError:
            print("Sai định dạng")
            return
        
        if not new_quantity_sold >= 0 and not new_quantity_sold <= 10_000:
            print("Số lượng đã bán chỉ có thể trong khoản 0 - 10.000!")
            return
        
        try:
            new_discount = int(input("Nhập số phần trăm giảm giá : "))

        except ValueError:
            print("Nhập sai định dạng ")
            return

        if not new_discount >= 0:
            print("Giảm giá phải >= 0 !")   
            return
        
        new_product = Product(new_product_id,new_product_name,new_price_input,new_quantity_sold,new_discount)
        self.products.append(new_product)
        print(f"Đã thêm sản phẩm {new_product_id} !")

    def update_product(self):
         update_product_id = input("Nhập mã sản phẩm cập nhật ").upper().strip()
         if update_product_id == "":
            print("Mã sản phẩm không được để trống")
            return
            
         if ProductManager.check_id_in_list(self, update_product_id) !=  None :
            print(f"{update_product_id} đã tồn tại trong danh sách này !")
            current_editing_product = ProductManager.check_id_in_list(self, update_product_id)
            print(current_editing_product)

            try:
                update_price_input = float(input("Nhập giá bán sản phẩm mới : "))
            except ValueError:
                print("Sai định dạng vừa nhập vào")
                return

            if update_price_input < 0:
                print("Giá bán không được âm")
                return
            
            try:
                update_quantity = int(input("Nhập số lượng đã bán : "))
            except ValueError:
                print("Sai định dạng")
                return
            
            if not update_quantity >= 0 and not update_quantity <= 10_000:
                print("Số lượng đã bán chỉ có thể trong khoản 0 - 10.000!")
                return
            
            try:
                update_discount = int(input("Nhập số phần trăm giảm giá : "))

            except ValueError:
                print("Nhập sai định dạng ")
                return

            if not update_discount >= 0:
                print("Giảm giá phải >= 0 !")   
                return
            
            current_editing_product.price = update_price_input
            current_editing_product.quantity_sold = update_quantity
            current_editing_product.discount = update_discount

            current_editing_product.calculate_revenue()
            current_editing_product.check_revenue_type()

            print(f"Đã cập nhật thành công  cho {update_product_id}")
            
            
         else:
             print(f"{update_product_id} không tồn tại trong danh sách")
             return
           
    def delete_product(self):
        delete_product_id = input("Nhập sản phẩm mà bạn muốn xóa : ").upper().strip()
        if ProductManager.check_id_in_list(self, delete_product_id) !=  None :
            print(f"Đã tìm thấy {delete_product_id} trong danh sách này!")
            about_delete_product = ProductManager.check_id_in_list(self, delete_product_id)
            while True:
                delete_choice = input(f"Bạn có muốn xóa sp {about_delete_product.name} \nY.có\nN.Không").strip().lower()
                match delete_choice:
                    case "y":
                        self.products.remove(about_delete_product)
                        break
                    case "n":
                        print("Đã hủy xóa ..")
                        break
                    case _:
                        print("Vui lòng chỉ chọn y - n")
        else:
            print(f"{delete_product_id} không có trong danh sách!")

    def find_product(self):
        find_input = input("Nhập sản phẩm bạn tìm kiếm : ").lower().strip()
        count = 0
        for product in self.products:
            if product.name.lower().startswith(find_input) or product.name.lower().count(find_input):
                count = count + 1            
                print(f"{product.id} - {product.name}")

        if count != 0:
            print(f"Đã tìm được {count} kết quả")
        else:
            print("Không có kết quả nào phù hợp")


    def stats_display(self):
       for product in self.products:
           print(product.revenue_type)
           

    
manager = ProductManager()

while True:
    choice = input("""
================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
Nhập lựa chọn của bạn: 
""")
    
    match choice:
        case "1":
            manager.display_all_products()
        case "2":
            manager.add_new_product()
        case "3":
            manager.update_product()
        case "4":
            manager.delete_product()
        case "5":
            manager.find_product()
        case "6":
            manager.stats_display()
        case "7":
            print("Thoát chương trình..")
            break
        case _:
            print("Vui lòng nhập từ 1 - 7")
