from django.db import models
from django.contrib import admin

# Create your models here.
class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=80, blank=False, unique=True)
        
    def __str__(self):
        return self.SupplierName
    
class Brand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=80, blank=False, unique=True)
    
    def __str__(self):
        return self.BrandName
    
class Dealer(models.Model):
    DealerID = models.AutoField(primary_key=True)
    DealerName = models.CharField(max_length=80, blank=False, unique=True)
    
    def __str__(self):
        return self.DealerName
    
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=80, blank=False)
    Address = models.CharField(max_length=100, blank=False)
    Phone = models.CharField(max_length=15, blank=False)
    Gender = models.CharField(max_length=20, blank=False)
    AnnualIncome = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    
    def __str__(self):
        return self.Name
    
class Factory(models.Model):
    FactoryID = models.AutoField(primary_key=True)
    FactoryName = models.CharField(max_length=80, blank=False, unique=True)
    
    def __str__(self):
        return self.FactoryName
  
class Model(models.Model):
    ModelID = models.AutoField(primary_key=True)
    BrandID = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models', blank=False)
    ModelName = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.ModelName
    
class Car(models.Model):
    STATUS_CHOICE = (
        ('1', 'ForSale'),
        ('0', 'Sold'),
    )
    
    VIN = models.AutoField(primary_key=True)
    ModelID = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars', blank=False)
    Status = models.CharField(max_length=1, blank=False, default='1', choices=STATUS_CHOICE)
    
    def __str__(self):
        return str(self.VIN)
    
class Option(models.Model):
    OptionID = models.AutoField(primary_key=True)
    CarVIN = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='options', blank=False)
    Color = models.CharField(max_length=80, blank=False)
    Engine = models.CharField(max_length=80, blank=False)
    Transmission = models.CharField(max_length=80, blank=False)
    OptionPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
    SupplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='options', blank=False, default=2)
    ProduceTime = models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return f'{self.Color} {self.Engine} {self.Transmission} {self.OptionPrice} {self.SupplierID}'
    
class FactoryBrand(models.Model):
    BrandID = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='factory_brands')
    FactoryID = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='factory_brands')
    
    class Meta:
        unique_together = ('BrandID' , 'FactoryID')
    
    def __str__(self):
        return f'BrandID: {self.BrandID.BrandName}, FactoryID: {self.FactoryID.FactoryName}'

class DealerBrand(models.Model):
    BrandID = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='dealer_brands')
    DealerID = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_brands')
    
    class Meta:
        unique_together = ('BrandID', 'DealerID')
    
    def __str__(self):
        return f'BrandID: {self.BrandID.BrandName}, DealerID: {self.DealerID.DealerName}'

class Sale(models.Model):
    SaleID = models.AutoField(primary_key=True)
    DealerID = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='sales', blank=False)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales', blank=False)
    CarVIN = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales', blank=False)
    SaleDate = models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return f'Sale: {self.SaleID} for car {self.CarVIN}'
    
@admin.register(Supplier)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Supplier._meta.fields]
    
@admin.register(Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dealer._meta.fields]

@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]

@admin.register(Factory)
class FactoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Factory._meta.fields]
    
@admin.register(Model)
class ModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Model._meta.fields]
    
@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
    
@admin.register(Option)
class OptionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Option._meta.fields]

@admin.register(FactoryBrand)
class FactoryBrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FactoryBrand._meta.fields]
    
@admin.register(DealerBrand)
class DealerBrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DealerBrand._meta.fields]
    
@admin.register(Sale)
class SalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sale._meta.fields]