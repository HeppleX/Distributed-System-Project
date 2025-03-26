/*
 Navicat Premium Dump SQL

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80404 (8.4.4)
 Source Host           : localhost:3306
 Source Schema         : course_selection_db

 Target Server Type    : MySQL
 Target Server Version : 80404 (8.4.4)
 File Encoding         : 65001

 Date: 26/03/2025 14:46:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course_id` bigint NOT NULL,
  `course_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `start_time` date NOT NULL COMMENT 'Course start time',
  `end_time` date NOT NULL COMMENT 'Course completion time',
  `current_enrollment` int NULL DEFAULT NULL COMMENT 'Current enrollment',
  `total_seats` int NULL DEFAULT NULL COMMENT 'Total capacity',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `course_id`(`course_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, 4510, 'Distributed System', '2025-01-02', '2025-03-30', 34, 40);
INSERT INTO `course` VALUES (2, 9035, 'Datebase', '2025-01-28', '2025-04-10', 2, 10);
INSERT INTO `course` VALUES (3, 4510, 'Distributed System', '2025-01-02', '2025-03-30', 35, 40);
INSERT INTO `course` VALUES (4, 9035, 'Datebase', '2025-01-28', '2025-04-10', 2, 10);
INSERT INTO `course` VALUES (5, 4520, 'Cloud Computing', '2025-01-05', '2025-03-25', 20, 35);
INSERT INTO `course` VALUES (6, 6010, 'Machine Learning', '2025-01-08', '2025-04-05', 15, 30);
INSERT INTO `course` VALUES (7, 7025, 'Computer Vision', '2025-01-12', '2025-03-28', 10, 25);
INSERT INTO `course` VALUES (8, 8040, 'Natural Language Processing', '2025-01-15', '2025-04-02', 12, 20);
INSERT INTO `course` VALUES (9, 3505, 'Operating Systems', '2025-01-10', '2025-03-31', 30, 50);
INSERT INTO `course` VALUES (10, 4780, 'Cybersecurity', '2025-01-18', '2025-04-08', 18, 40);
INSERT INTO `course` VALUES (11, 5215, 'Blockchain Technology', '2025-01-20', '2025-03-29', 8, 15);
INSERT INTO `course` VALUES (12, 6305, 'Software Engineering', '2025-01-07', '2025-03-27', 25, 45);
INSERT INTO `course` VALUES (13, 7350, 'Deep Learning', '2025-01-22', '2025-04-09', 10, 20);
INSERT INTO `course` VALUES (14, 8420, 'Big Data Analytics', '2025-01-25', '2025-04-03', 14, 30);
INSERT INTO `course` VALUES (15, 9135, 'Internet of Things', '2025-01-17', '2025-03-26', 22, 40);
INSERT INTO `course` VALUES (16, 6520, 'Artificial Intelligence', '2025-01-09', '2025-04-06', 28, 50);
INSERT INTO `course` VALUES (17, 4875, 'Computer Networks', '2025-01-14', '2025-03-30', 35, 55);
INSERT INTO `course` VALUES (18, 7050, 'Software Testing', '2025-01-19', '2025-04-07', 16, 30);
INSERT INTO `course` VALUES (19, 3890, 'Human-Computer Interaction', '2025-01-23', '2025-03-28', 12, 25);
INSERT INTO `course` VALUES (20, 5605, 'Embedded Systems', '2025-01-26', '2025-04-04', 11, 20);
INSERT INTO `course` VALUES (21, 6145, 'Quantum Computing', '2025-01-11', '2025-03-29', 5, 15);
INSERT INTO `course` VALUES (22, 8230, 'Autonomous Systems', '2025-01-16', '2025-04-10', 8, 18);
INSERT INTO `course` VALUES (23, 4900, 'Mobile App Development', '2025-01-27', '2025-03-31', 20, 40);
INSERT INTO `course` VALUES (24, 3650, 'Game Development', '2025-01-06', '2025-04-05', 30, 50);
INSERT INTO `course` VALUES (25, 9805, 'Parallel Computing', '2025-01-13', '2025-03-26', 18, 35);
INSERT INTO `course` VALUES (26, 5015, 'Wireless Networks', '2025-01-21', '2025-04-08', 22, 45);
INSERT INTO `course` VALUES (27, 7455, 'Database Administration', '2025-01-28', '2025-03-29', 14, 30);
INSERT INTO `course` VALUES (28, 5910, 'Robotics', '2025-01-09', '2025-04-03', 25, 50);
INSERT INTO `course` VALUES (29, 8835, 'Computer Graphics', '2025-01-15', '2025-03-27', 19, 40);
INSERT INTO `course` VALUES (30, 7750, 'Cloud Security', '2025-01-12', '2025-04-09', 10, 20);
INSERT INTO `course` VALUES (31, 9625, 'Computational Biology', '2025-01-20', '2025-03-30', 12, 28);
INSERT INTO `course` VALUES (32, 3500, 'VR & AR Development', '2025-01-07', '2025-04-07', 14, 35);
INSERT INTO `course` VALUES (33, 4960, 'Algorithm Design', '2025-01-23', '2025-03-28', 25, 45);
INSERT INTO `course` VALUES (34, 7320, 'Pattern Recognition', '2025-01-17', '2025-04-04', 18, 30);
INSERT INTO `course` VALUES (35, 8755, 'High-Performance Computing', '2025-01-05', '2025-03-29', 20, 38);
INSERT INTO `course` VALUES (36, 6015, 'DevOps', '2025-01-08', '2025-04-06', 22, 50);
INSERT INTO `course` VALUES (37, 4530, 'IT Project Management', '2025-01-14', '2025-03-31', 28, 60);
INSERT INTO `course` VALUES (38, 7820, 'Software Architecture', '2025-01-11', '2025-04-02', 18, 40);
INSERT INTO `course` VALUES (39, 9205, 'Smart Grid Technologies', '2025-01-18', '2025-03-26', 12, 25);
INSERT INTO `course` VALUES (40, 6330, 'Multimedia Processing', '2025-01-22', '2025-04-08', 15, 35);
INSERT INTO `course` VALUES (41, 7060, 'Knowledge Engineering', '2025-01-25', '2025-03-30', 10, 22);
INSERT INTO `course` VALUES (42, 5170, 'Cryptography', '2025-01-10', '2025-04-05', 16, 30);
INSERT INTO `course` VALUES (43, 8900, 'Full Stack Development', '2025-01-16', '2025-03-29', 22, 45);
INSERT INTO `course` VALUES (44, 3750, 'AI Ethics', '2025-01-13', '2025-04-07', 8, 15);
INSERT INTO `course` VALUES (45, 9525, 'Distributed Databases', '2025-01-28', '2025-03-28', 10, 20);
INSERT INTO `course` VALUES (46, 5400, 'Business Analytics', '2025-01-09', '2025-04-03', 30, 50);
INSERT INTO `course` VALUES (47, 4605, 'Biometric Security', '2025-01-21', '2025-03-31', 18, 40);
INSERT INTO `course` VALUES (48, 8710, 'Cloud-Native Computing', '2025-01-26', '2025-04-06', 20, 45);
INSERT INTO `course` VALUES (49, 7055, 'Digital Signal Processing', '2025-01-06', '2025-03-27', 14, 30);
INSERT INTO `course` VALUES (50, 6215, 'Data Mining', '2025-01-15', '2025-04-09', 22, 50);
INSERT INTO `course` VALUES (51, 3895, 'Hardware Security', '2025-01-19', '2025-03-26', 12, 25);
INSERT INTO `course` VALUES (52, 7250, 'AI for Healthcare', '2025-01-23', '2025-04-10', 10, 20);

-- ----------------------------
-- Table structure for enrollment
-- ----------------------------
DROP TABLE IF EXISTS `enrollment`;
CREATE TABLE `enrollment`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `student_id` bigint NOT NULL,
  `student_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `course_id` bigint NOT NULL,
  `course_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `enroll_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of enrollment
-- ----------------------------
INSERT INTO `enrollment` VALUES (2, 251445867, 'Test', 9035, 'Datebase', '2025-02-02 01:00:09');
INSERT INTO `enrollment` VALUES (15, 251430000, 'Donald Trump', 8835, 'Computer Graphics', '2025-03-26 00:44:19');
INSERT INTO `enrollment` VALUES (23, 251430000, 'Donald Trump', 5605, 'Embedded Systems', '2025-03-26 01:02:00');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `student_id` bigint NOT NULL,
  `student_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `password_hash` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `student_id`(`student_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, 251430000, 'Donald Trump', '3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d');
INSERT INTO `student` VALUES (2, 251445867, 'Test', '3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d');

SET FOREIGN_KEY_CHECKS = 1;
