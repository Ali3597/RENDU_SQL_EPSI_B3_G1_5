CREATE TABLE `user` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `email` varchar(180) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `address_id` int NOT NULL
);

CREATE TABLE `info_payment` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `card_number` varchar(25) NOT NULL,
  `code` varchar(3) NOT NULL,
  `date_card` date NOT NULL,
  `user_id` int NOT NULL
);

CREATE TABLE `address` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  `town_id` int NOT NULL
);

CREATE TABLE `town` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  `zipCode` varchar(10) NOT NULL,
  `initials` varchar(5),
  `country_id` int NOT NULL
);

CREATE TABLE `country` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  `initials` varchar(5)
);

CREATE TABLE `category` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL
);

CREATE TABLE `order_product` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `number` int NOT NULL,
  `order_id` int NOT NULL,
  `product_id` int NOT NULL
);

CREATE TABLE `warehouse` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `address_id` int NOT NULL
);

CREATE TABLE `product` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal NOT NULL,
  `type` ENUM ('mixed', 'women', 'men', 'kid', 'baby') NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime,
  `category_id` int
);

CREATE TABLE `warehouse_product` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `warehouse_id` int NOT NULL,
  `product_id` int NOT NULL,
  `stock` int NOT NULL
);

CREATE TABLE `order` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `user_id` int NOT NULL,
  `status` ENUM ('delivered', 'in_delivery', 'in_preparation') NOT NULL
);

ALTER TABLE `user` ADD FOREIGN KEY (`address_id`) REFERENCES `address` (`id`);

ALTER TABLE `warehouse` ADD FOREIGN KEY (`address_id`) REFERENCES `address` (`id`);

ALTER TABLE `product` ADD FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

ALTER TABLE `info_payment` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `town` ADD FOREIGN KEY (`country_id`) REFERENCES `country` (`id`);

ALTER TABLE `address` ADD FOREIGN KEY (`town_id`) REFERENCES `town` (`id`);

ALTER TABLE `order_product` ADD FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

ALTER TABLE `order_product` ADD FOREIGN KEY (`order_id`) REFERENCES `order` (`id`);

ALTER TABLE `order` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `warehouse_product` ADD FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

ALTER TABLE `warehouse_product` ADD FOREIGN KEY (`warehouse_id`) REFERENCES `warehouse` (`id`);
