# DBPG

> 組員
> 1. 鍾弘浩 411077033 軟工三 - E-R diagram and Relational Model
> 2. 林鈺祐 411031111 軟工三 - Populate Relations and Queries

###  ERD

<p align="center">
<img width="673" alt="image" src="https://github.com/CHUNG-HAO/DBPG/assets/67829896/96d82182-b43a-47ca-9ce7-ef07ec1c8076">
</p>

### Relational Model

<p align="center">
  <img width="717" alt="image" src="https://github.com/CHUNG-HAO/DBPG/assets/67829896/1405ff12-fd65-458d-bc1d-0e61c569a23c">

</p>

### Table Schema

```postgre
CREATE TABLE Brands (
    BrandID INT PRIMARY KEY,
    BrandName VARCHAR(255) NOT NULL
);

CREATE TABLE Dealers (
    DealerID INT PRIMARY KEY,
    DealerName VARCHAR(255) NOT NULL
);

CREATE TABLE DealerBrands (
    BrandID INT,
    DealerID INT,
    PRIMARY KEY (BrandID, DealerID),
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID),
    FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID)
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(50) NOT NULL,
    Gender VARCHAR(10),
    AnnualIncome VARCHAR(50)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    DealerID INT,
    CustomerID INT,
    CarVIN INT,
    SaleDate DATE,
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
    FOREIGN KEY (CarVIN) REFERENCES Cars(VIN)
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
    FOREIGN KEY (ModelID) REFERENCES Models(ModelID)
);

CREATE TABLE Factories (
    FactoryID INT PRIMARY KEY,
    FactoryName VARCHAR(255) NOT NULL
);

CREATE TABLE FactoryBrands (
    FactoryID INT,
    BrandID INT,
    PRIMARY KEY (FactoryID, BrandID),
    FOREIGN KEY (FactoryID) REFERENCES Factories(FactoryID),
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID)
);

CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255) NOT NULL
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
