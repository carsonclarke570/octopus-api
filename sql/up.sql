CREATE DATABASE octopus_db;
USE octopus_db;

CREATE TABLE `Party` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `queue_id` integer,
  `host_id` integer,
  `name` varchar(255),
  `code` varchar(255) UNIQUE,
  `access_token` varchar(255),
  `refresh_token` varchar(255),
  `created_on` datetime,
  `modified_on` datetime
);

CREATE TABLE `Queue` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `created_on` datetime,
  `modified_on` datetime
);

CREATE TABLE `Song` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `member_id` integer,
  `queue_id` integer,
  `spotify_id` varchar(255),
  `votes` integer,
  `created_on` datetime,
  `modified_on` datetime
);

CREATE TABLE `Member` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `party_id` integer,
  `name` varchar(255),
  `created_on` datetime,
  `modified_on` datetime
);

CREATE TABLE `Host` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `created_on` datetime,
  `modified_on` datetime
);

ALTER TABLE `Party` ADD FOREIGN KEY (`queue_id`) REFERENCES `Queue` (`id`);
ALTER TABLE `Party` ADD FOREIGN KEY (`host_id`) REFERENCES `Host` (`id`);
ALTER TABLE `Song` ADD FOREIGN KEY (`member_id`) REFERENCES `Member` (`id`);
ALTER TABLE `Song` ADD FOREIGN KEY (`queue_id`) REFERENCES `Queue` (`id`);
ALTER TABLE `Member` ADD FOREIGN KEY (`party_id`) REFERENCES `Party` (`id`);
