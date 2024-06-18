from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Avg, Count, F, ExpressionWrapper, DurationField
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from datetime import timedelta
from .models import (
    Option, Car, Model, Factory, FactoryBrand, Supplier,
    Brand, Dealer, DealerBrand, Sale, Customer
)

# Create your views here.
def index(request):
    
    return HttpResponse('<h1> Hi! This is index page! </h1>')

def get_queries(request):
    # 假設有缺陷的變速箱來自供應商Getrag
    defective_transmission_supplier = Supplier.objects.get(SupplierName="Getrag")
    print(defective_transmission_supplier)
    start_date = timezone.now() - timedelta(days=30)  # 設定查詢日期範圍
    print(start_date)
    end_date = timezone.now()
    print(end_date)
    # 找到變速箱有缺陷且由Getrag供應的所有選項
    defective_options = Option.objects.filter(
        SupplierID__SupplierName='Getrag',
        Transmission__icontains="defective"
    )
    print(defective_options)
    
    # 找到這些選項對應的所有汽車
    defective_cars = Car.objects.filter(options__in=defective_options)
    print(defective_cars)
    
    # 找到在指定日期範圍內銷售的這些汽車的銷售信息
    defective_car_vins_and_customers = Sale.objects.filter(
        CarVIN__in=defective_cars,
        SaleDate__range=(start_date, end_date)
    ).values('CarVIN__ModelID__ModelName', 'CustomerID__Name', 'CarVIN__options__SupplierID__SupplierName')
    
    print(defective_car_vins_and_customers)

    # 過去一年銷售最多（以美元金額）的經銷商
    one_year_ago = timezone.now() - timedelta(days=365)
    print(one_year_ago)
    top_dealer = Sale.objects.filter(SaleDate__gte=one_year_ago).values('DealerID__DealerName').annotate(total_sales=Sum('CarVIN__options__OptionPrice')).order_by('total_sales').first()
    print(top_dealer)

    # 過去一年銷售排名前2的品牌
    top_brands = Sale.objects.filter(SaleDate__gte=one_year_ago).values('CarVIN__ModelID__BrandID__BrandName').annotate(total_sales=Sum('CarVIN__options__OptionPrice')).order_by('total_sales')[:2]
    print(top_brands)
    
    # SUV在哪個月份銷售最佳
    selling = Sale.objects.filter(CarVIN__ModelID__ModelName__icontains='SUV')
    print(selling)
    selling_month = Sale.objects.annotate(month=ExtractMonth('SaleDate')).values('month')
    print(selling_month)
    best_selling_month = Sale.objects.filter(CarVIN__ModelID__ModelName__icontains="SUV").annotate(month=ExtractMonth('SaleDate')).values('month').annotate(total_sales=Count('SaleID')).order_by('-total_sales').first()
    print(best_selling_month)
    
    # 按照平均庫存時間降序排列經銷商
    dealers_with_avg_inventory_time = Dealer.objects.annotate(
        avg_inventory_time=Avg(
            ExpressionWrapper(
                F('dealer_brands__BrandID__models__cars__sales__SaleDate') - F('dealer_brands__BrandID__models__cars__options__ProduceTime'),
                output_field=DurationField()
            )
        )
    ).order_by('-avg_inventory_time')
    
    print(dealers_with_avg_inventory_time)
    
    context = {
        'defective_car_vins_and_customers': defective_car_vins_and_customers,
        'top_dealer': top_dealer,
        'top_brands': top_brands,
        'best_selling_month': best_selling_month,
        'dealers_with_avg_inventory_time': dealers_with_avg_inventory_time,
    }
    return render(request, 'queries.html', context)