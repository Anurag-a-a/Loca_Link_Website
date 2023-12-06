/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80034
Source Host           : localhost:3306
Source Database       : team20

Target Server Type    : MYSQL
Target Server Version : 80034
File Encoding         : 65001

Date: 2023-12-05 17:59:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `content` text,
  `postId` int(10) unsigned zerofill NOT NULL,
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `postOfCom` (`postId`),
  KEY `userWhoCom` (`author`),
  CONSTRAINT `postOfCom` FOREIGN KEY (`postId`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `userWhoCom` FOREIGN KEY (`author`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('0000000001', 'This is the content of this example of comment. ', '0000000002', 'UserName', '2023-11-20 19:02:52');
INSERT INTO `comment` VALUES ('0000000002', 'This is the second example of comment. ', '0000000002', 'UserName1', '2023-11-20 19:07:12');
INSERT INTO `comment` VALUES ('0000000003', 'This is test of adding a new comment', '0000000002', 'UserName', '2023-11-25 14:08:56');
INSERT INTO `comment` VALUES ('0000000004', 'This is test of adding a new comment', '0000000002', 'UserName', '2023-11-25 14:08:59');
INSERT INTO `comment` VALUES ('0000000005', 'This is test of adding a new comment', '0000000002', 'UserName', '2023-11-25 14:09:17');
INSERT INTO `comment` VALUES ('0000000006', 'This is test of adding a new comment.', '0000000002', 'UserName', '2023-11-25 14:10:25');

-- ----------------------------
-- Table structure for community
-- ----------------------------
DROP TABLE IF EXISTS `community`;
CREATE TABLE `community` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `userId` int unsigned NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `communityCreater` (`userId`),
  CONSTRAINT `communityCreater` FOREIGN KEY (`userId`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of community
-- ----------------------------
INSERT INTO `community` VALUES ('0000000001', 'Hoboken', '1', 'Here you can find posts related to Hoboken', 'https://assets.online.berklee.edu/catalog-site-heroes/careers-illustration-v2.png');
INSERT INTO `community` VALUES ('0000000002', 'Weehawken', '1', 'Here you can find posts related to Weehawken', 'https://c8.alamy.com/comp/2JWN0J8/hands-up-group-of-people-of-diverse-culture-or-friends-holding-musical-notes-community-of-fans-musicians-collaborators-who-share-or-exchange-music-2JWN0J8.jpg');
INSERT INTO `community` VALUES ('0000000003', 'Union City', '1', 'Here you can find posts related to Union City', 'https://dancedentampa.com/wp-content/uploads/2023/02/industry-hip-hop-transformed.jpg');
INSERT INTO `community` VALUES ('0000000004', 'Jersey City', '1', 'Here you can find posts related to Jersey City', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqOJQE2AsHIEAqZOGdH_Q_yr41jy9SSrK54Q&usqp=CAU.');
INSERT INTO `community` VALUES ('0000000005', 'Manhattan', '1', 'Here you can find posts related to Manhattan', 'https://assets.online.berklee.edu/catalog-site-heroes/careers-illustration-v2.png');
INSERT INTO `community` VALUES ('0000000006', 'New York', '1', 'Here you can find posts related to New York', 'https://assets.online.berklee.edu/catalog-site-heroes/careers-illustration-v2.png');

-- ----------------------------
-- Table structure for event
-- ----------------------------
DROP TABLE IF EXISTS `event`;
CREATE TABLE `event` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `communityId` int unsigned NOT NULL,
  `title` varchar(255) NOT NULL,
  `edate` date NOT NULL,
  `eventDesc` text,
  `eventType` varchar(255) NOT NULL,
  `regURL` varchar(255) DEFAULT '',
  `imgURL` varchar(255) DEFAULT '',
  `interestedNum` int NOT NULL DEFAULT '0',
  `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ecommunity` (`communityId`),
  KEY `eventCreater` (`userId`),
  CONSTRAINT `ecommunity` FOREIGN KEY (`communityId`) REFERENCES `community` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `eventCreater` FOREIGN KEY (`userId`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of event
-- ----------------------------
INSERT INTO `event` VALUES ('0000000016', '6', '1', 'Event test', '2023-12-05', 'This is a test of creating an event', 'Promotions', '', '../uploads/kaggle_pets2.png', '1', '2023-12-05 17:23:30');

-- ----------------------------
-- Table structure for interested
-- ----------------------------
DROP TABLE IF EXISTS `interested`;
CREATE TABLE `interested` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userId` int(10) unsigned zerofill NOT NULL,
  `eventId` int(10) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userInter` (`userId`),
  KEY `eventInter` (`eventId`),
  CONSTRAINT `eventInter` FOREIGN KEY (`eventId`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `userInter` FOREIGN KEY (`userId`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of interested
-- ----------------------------
INSERT INTO `interested` VALUES ('0000000002', '0000000006', '0000000016');

-- ----------------------------
-- Table structure for likestate
-- ----------------------------
DROP TABLE IF EXISTS `likestate`;
CREATE TABLE `likestate` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userId` int(10) unsigned zerofill NOT NULL,
  `postId` int(10) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userWhoLike` (`userId`),
  KEY `postLiked` (`postId`),
  CONSTRAINT `postLiked` FOREIGN KEY (`postId`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `userWhoLike` FOREIGN KEY (`userId`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of likestate
-- ----------------------------
INSERT INTO `likestate` VALUES ('0000000003', '0000000001', '0000000002');
INSERT INTO `likestate` VALUES ('0000000004', '0000000006', '0000000002');

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `communityId` int unsigned NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text,
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('0000000002', '1', '1', 'Exploring the Beauty of Oil Painting', 'Hey, fellow art enthusiasts! I\'ve been diving into the world of oil painting lately. Here\'s my latest creation, a serene landscape inspired by the countryside. What do you think?.', '', '2', '0', '0', '2023-12-05 17:19:27');
INSERT INTO `post` VALUES ('0000000003', '1', '1', 'Discovering Street Art in Barcelona', 'Street art has always fascinated me. During my recent trip to Barcelona, I stumbled upon some amazing street art. Here\'s a photo diary of my findings.', '', '0', '0', '0', '2023-11-04 20:01:42');
INSERT INTO `post` VALUES ('0000000004', '1', '1', 'Sculpting Dreams: My Journey with Clay', 'I\'ve recently taken up sculpting with clay. It\'s been a therapeutic and creative journey. Here\'s one of my latest clay sculptures, inspired by nature.', '', '0', '0', '0', '2023-11-04 20:02:20');
INSERT INTO `post` VALUES ('0000000005', '1', '2', 'Exploring Jazz: The Soulful Rhythms', 'Hey music lovers! Let\'s delve into the world of Jazz. I\'ve been captivated by its soulful rhythms. What are your favorite Jazz tunes?', '', '0', '0', '0', '2023-11-04 20:06:06');
INSERT INTO `post` VALUES ('0000000006', '1', '2', 'Rock Legends: A Nostalgic Journey', 'Rock music has a special place in my heart. Join me in celebrating the rock legends. Who\'s your ultimate rock icon?', '', '0', '0', '0', '2023-11-04 20:05:23');
INSERT INTO `post` VALUES ('0000000007', '1', '2', 'Classical Melodies: Timeless Beauty', 'Let\'s discuss the mesmerizing world of classical music. Do you have any favorite classical compositions?', '', '0', '0', '0', '2023-11-04 20:05:49');
INSERT INTO `post` VALUES ('0000000008', '1', '3', 'Contemporary Dance: Expressive Movements', 'Let\'s talk about contemporary dance forms. I find the expressive movements captivating. Share your thoughts!', '', '0', '0', '0', '2023-11-04 20:06:48');
INSERT INTO `post` VALUES ('0000000009', '1', '3', 'Traditional Dance Styles Around the World', 'Exploring traditional dance styles has been a fascinating journey. Which traditional dance forms do you admire?', '', '0', '0', '0', '2023-11-04 20:07:30');
INSERT INTO `post` VALUES ('0000000010', '1', '3', 'Hip-Hop Culture: The Beat and Dance', 'Hip-hop culture is more than just dance; it\'s a lifestyle. What aspects of hip-hop dance intrigue you the most?', '', '0', '0', '0', '2023-11-04 20:07:53');
INSERT INTO `post` VALUES ('0000000011', '1', '4', 'Basketball Fever: The Game & Strategies', 'Let\'s discuss the latest in basketball. What strategies do you find most effective on the court?', '', '0', '0', '0', '2023-11-04 20:08:24');
INSERT INTO `post` VALUES ('0000000012', '1', '4', 'Football Frenzy: Legendary Matches', 'Football has seen some epic matches. Which one do you think is the most legendary, and why?', '', '0', '0', '0', '2023-11-04 20:08:48');
INSERT INTO `post` VALUES ('0000000013', '1', '4', 'Thrilling Sports Moments: Your Favorites', 'Share some of the most thrilling sports moments that have left a lasting impact on you.', '', '0', '0', '0', '2023-11-04 20:09:27');
INSERT INTO `post` VALUES ('0000000014', '1', '1', 'Creating Post Test 1', 'This is test 1 of creating post. This post is in arts community. ', '', '0', '0', '0', '2023-11-16 21:33:59');
INSERT INTO `post` VALUES ('0000000015', '1', '1', 'Creating Post Test 2', 'This is test 2 of creating post. This post is in arts community. ', '', '0', '0', '0', '2023-11-16 21:35:28');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('0000000001', 'UserName', '$2b$12$PUrlmbRTStKgR/FQAOsyIuhyB9ARvSuRZKshWfpgqO9ROf.X8sCvm', 'mail@mail.com','', 'Hoboken','','','');
INSERT INTO `user` VALUES ('0000000005', 'UserName1', '$2b$12$PUrlmbRTStKgR/FQAOsyIuhyB9ARvSuRZKshWfpgqO9ROf.X8sCvm', 'mail1@mail1.com','', 'Union City','','','' );
INSERT INTO `user` VALUES ('0000000006', 'UserName2', '$2b$12$DIfnDYwol2RJwsJ67wn2rO.TsUvaQwVBEsTUD3V.0WraSzgp0z2qy', 'mail2@mail2.com','', 'Jersey City','','','');
