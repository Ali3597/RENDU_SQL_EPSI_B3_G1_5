## **Ma (première) DB** 

Ali Saleh , Steve Lezeau

Notre base de données représente celle d'un e-commerce , elle va permettre la gestions des produits et  des utilisateurs  de notre commerce et de leur commandes .

Le script que nous avons utilisé pour créer la base de donnée est dans le fichier  creation_bdd.sql .

Et le dump de notre base de donnée est aussi dans le fichier  sql_dump.sql.

Voila le schéma de la base de donnée :

![](C:\Users\ali_s\Documents\Ecole\sql\devoir photo\bdd.png)

Pour remplir notre base données  nous avons utilisé le langage python et la librairie faker. Le script utilisé pour la génération de données est dans le fichier  create_data.py

<div style="page-break-after: always;"></div>

### Les vues 

Nous avons créer cinq vues dans notre base de donnée:

La première vue  consiste a afficher les commandes qui ont  le montant le plus élevé.

Voici la commande utilisé pour la créer :

```sql
USE ali_steve;
CREATE VIEW meilleur_commande
AS SELECT order_product.id,order_product.order_id , SUM(order_product.number * product.price) AS prix_par_commande
FROM order_product 
JOIN product
ON order_product.product_id = product.id
GROUP BY order_id
order BY prix_par_commande DESC

```

La deuxième vue consiste a afficher les clients qui dépensent le plus d'argent chez nous .

Voici la commande utilisé pour la créer :

```sql
CREATE VIEW meilleur_client
AS SELECT user.id as userId,user.email, A.id as orderID,SUM(B.prix_par_commande) AS paye_par_client 
from ali_steve.order AS A
JOIN  
(SELECT order_product.id,order_product.order_id , SUM(order_product.number * product.price) AS prix_par_commande
FROM order_product 
JOIN product
ON order_product.product_id = product.id
GROUP BY order_id) AS B 
ON A.id = B.order_id
JOIN user
ON A.user_id = user.id
GROUP BY A.user_id
Order by paye_par_client DESC
```

<div style="page-break-after: always;"></div>

La troisième vue consiste a afficher les produits qui se vendent le plus 

Voici la commande utilisé pour la créer :

```sql
CREATE VIEW meilleur_vente  AS 
SELECT order_product.id AS orderProductId,order_product.product_id AS productId,product.name, SUM(order_product.number ) AS nombre_total_objet
FROM order_product 
JOIN product
ON order_product.product_id = product.id
GROUP BY order_product.product_id
Order BY nombre_total_objet DESC
```

La quatrième vue consiste a afficher les  produits pour femme .

Voici la commande utilisé pour la créer :

```sql
CREATE VIEW product_for_women AS
SELECT * 
FROM product
WHERE type="women"
```

La cinquième  vue consiste a afficher les warehouse dans une ville spécifique .

Voici la commande utilisé pour la créer :

```sql
CREATE VIEW warehouse_in_town_1 AS
SELECT warehouse.id,town.initials,address.label 
FROM warehouse
join address
ON warehouse.address_id = address.id
join town
ON address.town_id = town.id
where town.id = 1
```

<div style="page-break-after: always;"></div>

### Index 

Nous avons créer trois index:

Le premier index est sur la clé étrangère category_id présente dans la table product.

**Query avant la création de l'index :** 

![](C:\Users\ali_s\Documents\Ecole\sql\devoir\index_category_avant.png)

**Commande de création de l'index :**

```sql
CREATE INDEX idx_category  ON ali_steve.product(category_id)
```

**Query après création de l'index :**

![](C:\Users\ali_s\Documents\Ecole\sql\devoir\index_category_apres.png)

<div style="page-break-after: always;"></div>

Le deuxième  index est sur le champs status de la table product

**Query avant la  création de l'index :**

![](C:\Users\ali_s\Documents\Ecole\sql\devoir\index_status_avant.png)

**Commande de création de l'index :**

```sql
CREATE INDEX idx_status ON ali_steve.order(status)
```

**Query après la création de l'index :**

![](C:\Users\ali_s\Documents\Ecole\sql\devoir\index_status_apres.png)

<div style="page-break-after: always;"></div>

Le troisième index est sur le champs type de la table product .

**Query avant la création de l'index :**

![](C:\Users\ali_s\Documents\Ecole\sql\devoir\index_type_avant.png)



**Commande de création de l'index :**

```sql
CREATE INDEX idx_type  ON ali_steve.product(type)
```

**Query après la création de l'index:**

![](C:\Users\ali_s\Documents\Ecole\sql\devoir\index_type_apres.png)

<div style="page-break-after: always;"></div>

### Procédure Stocké:

```sql
USE `ali_steve`;
DROP procedure IF EXISTS `ali_steve`.`TopTenClientString`;
;

DELIMITER $$
USE `ali_steve`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `TopTenClientString`(INOUT emailList varchar(4000))
BEGIN
    DECLARE finished INTEGER DEFAULT 0;
    DECLARE thisEmail varchar(100) DEFAULT "";
    DECLARE paye integer default 0;
	DECLARE Cur_topTenClient Cursor for SELECT  email,paye_par_client  FROM meilleur_client limit 10;
    DECLARE CONTINUE HANDLER 
	FOR NOT FOUND SET finished = 1;
	open Cur_topTenClient;
	getEmail: LOOP
		FETCH Cur_topTenClient INTO thisEmail,paye ;
		IF finished = 1 THEN 
			LEAVE getEmail;
		END IF;
		SET emailList = CONCAT(thisEmail,"=",paye,";",emailList);
	END LOOP getEmail;
    CLOSE Cur_topTenClient;
	END$$

DELIMITER ;
;

```

 Pour exécuter la procédure stocké  :

```sql
SET @emailList = ""; 
CALL TopTenClientString(@emailList); 
SELECT @emailList;
```

