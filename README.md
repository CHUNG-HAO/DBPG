# DBPG

> 組員
> 1. 鍾弘浩 411077033 軟工三 - E-R diagram and Relational Model
> 2. 林鈺祐 411031111 軟工三 - Populate Relations and Queries

## 搜尋

<p align="center">
<img width="717" alt="image" src="https://github.com/CHUNG-HAO/DBPG/assets/67829896/563e01d1-0283-4c60-a80a-0a697373429a"
/p>


###  ERD

<p align="center">
<img width="717" alt="image" src="https://github.com/CHUNG-HAO/DBPG/assets/67829896/608b57c3-7d25-4258-afdd-c4054626bf76">

</p>

### Relational Model

<p align="center">
  <img width="717" alt="image" src="https://github.com/CHUNG-HAO/DBPG/assets/67829896/1405ff12-fd65-458d-bc1d-0e61c569a23c">

</p>

### Table Schema

```MariaDB
CREATE TABLE Brands (
    BrandID INT PRIMARY KEY,
    BrandName VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Dealers (
    DealerID INT PRIMARY KEY,
    DealerName VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE DealerBrands (
    id INT PRIMARY KEY,
    BrandID INT,
    DealerID INT,
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID),
    FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID)
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(80) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Gender VARCHAR(20),
    AnnualIncome DECIMAL(10, 2)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    DealerID INT,
    CustomerID INT,
    CarVIN INT,
    SaleDate DATETIME,
    FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (CarVIN) REFERENCES Cars(VIN)
);

CREATE TABLE Options (
    OptionID INT PRIMARY KEY,
    CarVIN INT,
    Color VARCHAR(50),
    Engine VARCHAR(50),
    Transmission VARCHAR(50),
    OptionPrice DECIMAL(10, 2) NOT NULL,
    SupplierID INT,
    ProduceTime DATETIME,
    FOREIGN KEY (CarVIN) REFERENCES Cars(VIN),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

CREATE TABLE Models (
    ModelID INT PRIMARY KEY,
    BrandID INT,
    ModelName VARCHAR(255) NOT NULL,
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID)
);

CREATE TABLE Cars (
    VIN INT PRIMARY KEY,
    ModelID INT,
    Status VARCHAR(1) DEFAULT(1) NOT NULL,
    FOREIGN KEY (ModelID) REFERENCES Models(ModelID)
);

CREATE TABLE Factories (
    FactoryID INT PRIMARY KEY,
    FactoryName VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE FactoryBrands (
    id INT PRIMARY KEY,
    FactoryID INT,
    BrandID INT,
    FOREIGN KEY (FactoryID) REFERENCES Factories(FactoryID),
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID)
);

CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255) NOT NULL UNIQUE
);

```


> 1. Brands 和 Models：一個品牌 (Brands) 可以有多個型號 (Models)，所以這是一對多的關係。
> 2. Models 和 Cars：一個型號 (Models) 可以有多輛車 (Cars)，所以這也是一對多的關係。
> 3. Cars 和 Options：一輛車 (Cars) 可以有多種選項 (Options)，所以這是一對多的關係。
> 4. Dealers 和 DealerBrands：一個經銷商 (Dealers) 可以銷售多個品牌 (DealerBrands)，所以這是一對多的關係。
> 5. Brands 和 DealerBrands：一個品牌 (Brands) 可以在多個經銷商 (DealerBrands) 處銷售，所以這是一對多的關係。
> 6. Dealers 和 Sales：一個經銷商 (Dealers) 可以有多筆銷售 (Sales)，所以這是一對多的關係。
> 7. Customers 和 Sales：一個客戶 (Customers) 可以有多筆銷售 (Sales)，所以這是一對多的關係。
> 8. Cars 和 Sales：一輛車 (Cars) 可以有多筆銷售 (Sales)，但通常情況下，一輛車只會被銷售一次，所以這可能是一對一或一對多的關係，取決於業務邏輯，而我取用一對多邏輯。
> 9. Factories 和 FactoryBrands：一個工廠 (Factories) 可以生產多個品牌 (FactoryBrands)，所以這是一對多的關係。
> 10. Brands 和 FactoryBrands：一個品牌 (Brands) 可以在多個工廠 (FactoryBrands) 中生產，所以這是一對多的關係。
