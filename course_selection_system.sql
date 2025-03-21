/*
 Navicat Premium Dump SQL

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50744 (5.7.44-log)
 Source Host           : localhost:3306
 Source Schema         : course_selection_system

 Target Server Type    : MySQL
 Target Server Version : 50744 (5.7.44-log)
 File Encoding         : 65001

 Date: 20/03/2025 16:23:42
*/

SET NAMES utf8mb4;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `course_id` bigint(20) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `start_time` date NOT NULL COMMENT 'Course start time',
  `end_time` date NOT NULL COMMENT 'Course completion time',
  `current_enrollment` int(11) NULL DEFAULT NULL COMMENT 'Current enrollment',
  `total_seats` int(11) NULL DEFAULT NULL COMMENT 'Total capacity',
  PRIMARY KEY (`id`) USING BTREE,
  KEY (`course_id`) USING BTREE
) ENGINE = InnoDB;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1,4510, 'Distributed System', '2025-01-02', '2025-03-30', 35, 40);
INSERT INTO `course` VALUES (2,9035, 'Datebase', '2025-01-28', '2025-04-10', 2, 10);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `student_id` bigint(20) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY (`student_id`) USING BTREE
) ENGINE = InnoDB;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1,251430000, 'Donald Trump','3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d');
INSERT INTO `student` VALUES (2,251445867, 'Test','3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d');

-- ----------------------------
-- Table structure for enrollment
-- ----------------------------
DROP TABLE IF EXISTS `enrollment`;
CREATE TABLE `enrollment`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `student_id` bigint(20) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `enroll_time` DATETIME NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB ;

-- ----------------------------
-- Records of enrollment
-- ----------------------------
INSERT INTO `enrollment` VALUES (1, 251430000, 'Donald Trump', 4510, 'Distributed System', '2025-01-02 01:00:09');
INSERT INTO `enrollment` VALUES (2, 251445867, 'Test', 9035, 'Datebase', '2025-02-02 01:00:09');

