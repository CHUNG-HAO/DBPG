# DBPG

> 組員
> 1. 鍾弘浩 411077033 軟工三 - E-R diagram and Relational Model
> 2. 林鈺佑 411031111 軟工三 - Populate Relations and Queries

### E-R diagram and Relational Model

<p align="center">
  <img width="762" alt="image" src="https://github.com/CHUNG-HAO/DBPG/assets/67829896/0da24537-6491-4c64-a59d-043dc2a61f16">
</p>

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
