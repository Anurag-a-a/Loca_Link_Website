CREATE DATABASE  IF NOT EXISTS `team20` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `team20`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: team20
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `communityId` int unsigned NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` varchar(255) DEFAULT '',
  `imgURL` varchar(255) DEFAULT '',
  `likeNum` int NOT NULL DEFAULT '0',
  `isTop` tinyint NOT NULL DEFAULT '0',
  `isDeleted` int NOT NULL DEFAULT '0',
  `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `community` (`communityId`),
  KEY `postCreater` (`userId`),
  CONSTRAINT `community` FOREIGN KEY (`communityId`) REFERENCES `community` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `postCreater` FOREIGN KEY (`userId`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (0000000002,1,1,'Exploring the Beauty of Oil Painting','Hey, fellow art enthusiasts! I\'ve been diving into the world of oil painting lately. Here\'s my latest creation, a serene landscape inspired by the countryside. What do you think?.','',0,0,0,'2023-11-05 00:00:54'),(0000000003,1,1,'Discovering Street Art in Barcelona','Street art has always fascinated me. During my recent trip to Barcelona, I stumbled upon some amazing street art. Here\'s a photo diary of my findings.','',0,0,0,'2023-11-05 00:01:42'),(0000000004,1,1,'Sculpting Dreams: My Journey with Clay','I\'ve recently taken up sculpting with clay. It\'s been a therapeutic and creative journey. Here\'s one of my latest clay sculptures, inspired by nature.','',0,0,0,'2023-11-05 00:02:20'),(0000000005,1,2,'Exploring Jazz: The Soulful Rhythms','Hey music lovers! Let\'s delve into the world of Jazz. I\'ve been captivated by its soulful rhythms. What are your favorite Jazz tunes?','',0,0,0,'2023-11-05 00:06:06'),(0000000006,1,2,'Rock Legends: A Nostalgic Journey','Rock music has a special place in my heart. Join me in celebrating the rock legends. Who\'s your ultimate rock icon?','',0,0,0,'2023-11-05 00:05:23'),(0000000007,1,2,'Classical Melodies: Timeless Beauty','Let\'s discuss the mesmerizing world of classical music. Do you have any favorite classical compositions?','',0,0,0,'2023-11-05 00:05:49'),(0000000008,1,3,'Contemporary Dance: Expressive Movements','Let\'s talk about contemporary dance forms. I find the expressive movements captivating. Share your thoughts!','',0,0,0,'2023-11-05 00:06:48'),(0000000009,1,3,'Traditional Dance Styles Around the World','Exploring traditional dance styles has been a fascinating journey. Which traditional dance forms do you admire?','',0,0,0,'2023-11-05 00:07:30'),(0000000010,1,3,'Hip-Hop Culture: The Beat and Dance','Hip-hop culture is more than just dance; it\'s a lifestyle. What aspects of hip-hop dance intrigue you the most?','',0,0,0,'2023-11-05 00:07:53'),(0000000011,1,4,'Basketball Fever: The Game & Strategies','Let\'s discuss the latest in basketball. What strategies do you find most effective on the court?','',0,0,0,'2023-11-05 00:08:24'),(0000000012,1,4,'Football Frenzy: Legendary Matches','Football has seen some epic matches. Which one do you think is the most legendary, and why?','',0,0,0,'2023-11-05 00:08:48'),(0000000013,1,4,'Thrilling Sports Moments: Your Favorites','Share some of the most thrilling sports moments that have left a lasting impact on you.','',0,0,0,'2023-11-05 00:09:27'),(0000000014,1,1,'Creating Post Test 1','This is test 1 of creating post. This post is in arts community. ','',0,0,0,'2023-11-17 02:33:59'),(0000000015,1,1,'Creating Post Test 2','This is test 2 of creating post. This post is in arts community. ','',0,0,0,'2023-11-17 02:35:28'),(0000000016,1,1,'asda','asdasd','../uploads/diwali.png',0,0,1,'2023-12-01 20:19:50'),(0000000017,1,1,' Embrace the joy of the day!','Share a smile with someone and brighten their world. Happiness is contagious! ? #SpreadJoy #HappyVibes','../uploads/download.jpeg',0,0,0,'2023-12-01 20:22:02');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 14:11:10
