-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: mobimeds
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `allopathic_medicines`
--

DROP TABLE IF EXISTS `allopathic_medicines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allopathic_medicines` (
  `Prdt_id` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Dosage` varchar(10) NOT NULL,
  `Price` float NOT NULL,
  `Discounted_price` float NOT NULL,
  `Discount_percent` int DEFAULT NULL,
  `Qty` varchar(15) NOT NULL,
  `Mfg_date` date NOT NULL,
  `Exp_date` date NOT NULL,
  PRIMARY KEY (`Prdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allopathic_medicines`
--

LOCK TABLES `allopathic_medicines` WRITE;
/*!40000 ALTER TABLE `allopathic_medicines` DISABLE KEYS */;
INSERT INTO `allopathic_medicines` VALUES (456,'Telmiride AM','40mg',60,51,15,'Strip of 10Tab','2020-09-21','2022-09-25'),(459,'Ampine AT','50mg',31.8,25.9,15,'Strip of 10Tab','2024-02-12','2027-01-11'),(460,'Volini Pain Relief','75g',245,208.25,15,'Tube of 75g','2024-04-03','2027-03-02'),(461,'Soframycin 1% Skin cream','100g',157.86,127.87,19,'Tube of 100g','2024-04-03','2027-03-02'),(464,'Rabemac DSR','50mg',119.79,98.23,18,'Strip of 10Tab','2023-02-10','2026-03-12'),(467,'Ourdaily Vitamin E cap','400mg',39,27.3,30,'Strip of 10Tab','2022-10-10','2024-09-08'),(468,'Phadox 100mg','100mg',79,63.2,20,'Strip of 10Tab','2022-10-10','2024-09-08'),(472,'Levecon 250mg','250mg each',59.4,48.71,18,'Box of 50tab','2023-10-23','2025-09-10'),(479,'Vicks Vaporub','50ml',145,145,0,'1 bottle','2020-10-10','2028-08-08');
/*!40000 ALTER TABLE `allopathic_medicines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ayurvedic_medicines`
--

DROP TABLE IF EXISTS `ayurvedic_medicines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ayurvedic_medicines` (
  `Prdt_id` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Dosage` varchar(10) NOT NULL,
  `Price` float NOT NULL,
  `Discounted_price` float NOT NULL,
  `Discount_percent` int DEFAULT NULL,
  `Qty` varchar(15) NOT NULL,
  `Mfg_date` date NOT NULL,
  `Exp_date` date DEFAULT NULL,
  PRIMARY KEY (`Prdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ayurvedic_medicines`
--

LOCK TABLES `ayurvedic_medicines` WRITE;
/*!40000 ALTER TABLE `ayurvedic_medicines` DISABLE KEYS */;
INSERT INTO `ayurvedic_medicines` VALUES (1002,'Patanjali Kayakalp Vati','20mg each',80,70,10,'Bottle of 80','2024-02-10','2027-01-09'),(1003,'Dabur Chawanprash','950g',349,349,0,'1 Bottle','2024-02-10',NULL),(1091,'Everherb Ashwagandha(Immunity and stress relief)','NA',599,299.5,50,'Bottle of 60','2023-10-10',NULL),(1200,'Patanjali Divya ShilajeetRasayan','20mg each',35,35,0,'Bottle of 60tab','2024-02-10','2027-01-09');
/*!40000 ALTER TABLE `ayurvedic_medicines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `Name` varchar(50) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` char(1) NOT NULL,
  `Salary` int DEFAULT NULL,
  `Shift_time` time NOT NULL,
  `Date_join` date NOT NULL,
  `City` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nutrition_fitness_supplements`
--

DROP TABLE IF EXISTS `nutrition_fitness_supplements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nutrition_fitness_supplements` (
  `Prdt_id` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Dosage` varchar(10) NOT NULL,
  `Price` float NOT NULL,
  `Discounted_price` float NOT NULL,
  `Discount_percent` int DEFAULT NULL,
  `Qty` varchar(15) NOT NULL,
  `Mfg_date` date NOT NULL,
  `Exp_date` date NOT NULL,
  PRIMARY KEY (`Prdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nutrition_fitness_supplements`
--

LOCK TABLES `nutrition_fitness_supplements` WRITE;
/*!40000 ALTER TABLE `nutrition_fitness_supplements` DISABLE KEYS */;
/*!40000 ALTER TABLE `nutrition_fitness_supplements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_care`
--

DROP TABLE IF EXISTS `personal_care`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_care` (
  `Prdt_id` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Dosage` varchar(10) NOT NULL,
  `Price` float NOT NULL,
  `Discounted_price` float NOT NULL,
  `Discount_percent` int DEFAULT NULL,
  `Qty` varchar(15) NOT NULL,
  `Mfg_date` date NOT NULL,
  `Exp_date` date NOT NULL,
  `Category` varchar(10) NOT NULL,
  PRIMARY KEY (`Prdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_care`
--

LOCK TABLES `personal_care` WRITE;
/*!40000 ALTER TABLE `personal_care` DISABLE KEYS */;
INSERT INTO `personal_care` VALUES (600,'Acmed Facewash','70g',199,155.22,22,'Pack of 1','2024-01-22','2027-02-21','Skin Care');
/*!40000 ALTER TABLE `personal_care` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shortterm_ailments`
--

DROP TABLE IF EXISTS `shortterm_ailments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shortterm_ailments` (
  `Prdt_id` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Dosage` varchar(10) NOT NULL,
  `Price` float NOT NULL,
  `Discounted_price` float NOT NULL,
  `Discount_percent` int DEFAULT NULL,
  `Qty` varchar(15) NOT NULL,
  `Mfg_date` date NOT NULL,
  `Exp_date` date NOT NULL,
  PRIMARY KEY (`Prdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shortterm_ailments`
--

LOCK TABLES `shortterm_ailments` WRITE;
/*!40000 ALTER TABLE `shortterm_ailments` DISABLE KEYS */;
INSERT INTO `shortterm_ailments` VALUES (5,'Acetal SP','600mg',65,53.3,18,'Strip of 10','2024-09-19','2027-09-20'),(10,'Amoxyclav 375mg','375mg',268.18,187.73,30,'Strip of 10','2023-10-23','2025-09-10'),(26,'Cefixime IP 200','200mg',107.74,75.42,30,'Strip of 10','2024-09-19','2027-09-20');
/*!40000 ALTER TABLE `shortterm_ailments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-11 22:47:09
