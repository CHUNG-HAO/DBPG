from django.db import models
from django.contrib import admin

# Create your models here.
class Suppliers(models.Model):
    SupplierID = models.IntegerField(primary_key=True)
    SupplierName = models.CharField(max_length=80, blank=False)
        
    def __str__(self):
        return self.SupplierID
    
class Brands(models.Model):
    BrandID = models.IntegerField(primary_key=True)
    BrandName = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.BrandID
    
class Dealers(models.Model):
    DealerID = models.IntegerField(primary_key=True)
    DealerName = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.DealerID
    
class Customers(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=80, blank=False)
    Address = models.CharField(max_length=100, blank=False)
    Phone = models.CharField(max_length=80, blank=False)
    Gender = models.CharField(max_length=20, blank=False)
    AnnualIncome = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.CustomerID
    
class Factories(models.Model):
    FactoryID = models.IntegerField(primary_key=True)
    FactoryName = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.FactoryID
  
class Models(models.Model):
    ModelID = models.IntegerField(primary_key=True)
    BrandID = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=False)
    ModelName = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.ModelID
    
class Cars(models.Model):
    VIN = models.IntegerField(primary_key=True)
    ModelID = models.ForeignKey(Models, on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return self.VIN
    
class Options(models.Model):
    OptionID = models.IntegerField(primary_key=True)
    CarVIN = models.ForeignKey(Cars, on_delete=models.CASCADE, blank=False)
    Color = models.CharField(max_length=80, blank=False)
    Engine = models.CharField(max_length=80, blank=False)
    Transmission = models.CharField(max_length=80, blank=False)
    
    def __str__(self):
        return self.OptionID   
    
class FactoryBrands(models.Model):
    FactoryID = models.ForeignKey(Factories, on_delete=models.CASCADE)
    DealerID = models.ForeignKey(Dealers, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<FactoryID: {self.FactoryID}, DealerID: {self.DealerID}>'

class DealerBrands(models.Model):
    BrandID = models.ForeignKey(Brands, on_delete=models.CASCADE)
    DealerID = models.ForeignKey(Dealers, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<BrandID: {self.BrandID}, DealerID: {self.DealerID}>'

class Sales(models.Model):
    SaleID = models.IntegerField(primary_key=True)
    DaelerID = models.ForeignKey(Dealers, on_delete=models.CASCADE, blank=False)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=False)
    CarVIN = models.ForeignKey(Cars, on_delete=models.CASCADE, blank=False)
    SaleDate = models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return self.SaleID
    
@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Suppliers._meta.fields]
    
@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brands._meta.fields]

@admin.register(Dealers)
class DealerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dealers._meta.fields]

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customers._meta.fields]

@admin.register(Factories)
class FactoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Factories._meta.fields]
    
@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Models._meta.fields]
    
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cars._meta.fields]
    
@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Options._meta.fields]

@admin.register(FactoryBrands)
class FactoryBrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FactoryBrands._meta.fields]
    
@admin.register(DealerBrands)
class DealerBrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DealerBrands._meta.fields]
    
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sales._meta.fields]