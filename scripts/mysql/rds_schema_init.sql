-- database initialization

Create database IF NOT EXISTS `gemmapp_prod`
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE `gemmapp_prod`;

CREATE TABLE IF NOT EXISTS `accomz` (
    `name` varchar(255) NOT NULL,
    `location` varchar(255), 
    `email` varchar(255) NOT NULL UNIQUE,
    `tel` varchar(255), 
    `type` varchar(255),
    `style` varchar(255),
    `descrip` text,
    `stars` varchar(5),
    `gpspoint` varchar(255),
    `source` varchar(255),
    `image` varchar(255) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `activities` (
    `bizname` varchar(255) NOT NULL,
    `type` varchar(255),
    `email` varchar(255) NOT NULL UNIQUE,
    `socials` varchar(255),
    `tel` varchar(10),
    `reviews` text,
    `descrip` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `city` (
    `name` varchar(255) NOT NULL,
    `country` varchar(255),
    `attractions` varchar(255),
    `events` varchar(255),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `country` (
    `name` varchar(255) NOT NULL,
    `email` varchar(255),
    `telcode` varchar(5),
    `advisories` varchar(text)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `eats` (
    `name` varchar(255),
    `address` varchar(255),
    `email` varchar(255) NOT NULL UNIQUE,
    `tel` varchar(10),
    `type` varchar(255),
    `style` varchar(255),
    `descrip` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `events` (
    `evntname` varchar(255) NOT NULL,
    `venue` varchar(255),
    `type` varchar(255),
    `artist` varchar(255) NOT NULL,
    `descrip` text,
    `evntdate` varchar(255),
    `city` varchar(255),
    `address` varchar(255),
    `gps_point` varchar(255),
    `country` varchar(255),
    `startdate` varchar(255),
    `end_date` varchar(255),
    `evnt_charge` varchar(255),
    `rel_evnt` varchar(255),
    `publish` boolean
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `transport` (
    `name` varchar(255),
    `type` varchar(255),
    `hireType` varchar(255),
    `email` varchar(255),
    `tel` varchar(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `users` (
    `username` varchar(255) NOT NULL UNIQUE,
    `email` varchar(255) NOT NULL UNIQUE,
    `password` varchar(255) NOT NULL,
    `prefs` text,
    `userID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `venue` (
    `name` varchar(255),
    `address` varchar(255),
    `type` varchar(255),
    `style` varchar(255),
    `descrip` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;