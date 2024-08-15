/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - blood_donation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`blood_donation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `blood_donation`;

/*Table structure for table `bloodbanks` */

DROP TABLE IF EXISTS `bloodbanks`;

CREATE TABLE `bloodbanks` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `phone` varchar(1111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`bank_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bloodbanks` */

insert  into `bloodbanks`(`bank_id`,`login_id`,`name`,`place`,`pincode`,`phone`,`email`) values 
(1,3,'blood','bloodplace','873838','7736253394','bank04@gmail.com');

/*Table structure for table `bloodgroups` */

DROP TABLE IF EXISTS `bloodgroups`;

CREATE TABLE `bloodgroups` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(100) DEFAULT NULL,
  `group_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `bloodgroups` */

insert  into `bloodgroups`(`group_id`,`group_name`,`group_description`) values 
(1,'a','eya postive'),
(2,'0+ve','nothing');

/*Table structure for table `collection` */

DROP TABLE IF EXISTS `collection`;

CREATE TABLE `collection` (
  `collection_id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `unit_collected` varchar(111) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`collection_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `collection` */

insert  into `collection`(`collection_id`,`bank_id`,`group_id`,`date_time`,`unit_collected`,`user_id`) values 
(1,1,1,'21','2',2),
(7,1,1,'7667','1',2),
(8,1,2,'2024-02-17','80ml',2);

/*Table structure for table `distribution` */

DROP TABLE IF EXISTS `distribution`;

CREATE TABLE `distribution` (
  `distribution_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `unit_distributed` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`distribution_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `distribution` */

insert  into `distribution`(`distribution_id`,`user_id`,`group_id`,`unit_distributed`,`date_time`) values 
(2,1,5,'878','2024-02-10'),
(3,1,5,'77','2024-02-10'),
(4,1,5,'35','2024-02-10'),
(9,2,1,'90ml','2024-02-17');

/*Table structure for table `donors` */

DROP TABLE IF EXISTS `donors`;

CREATE TABLE `donors` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `gender` varchar(111) DEFAULT NULL,
  `age` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `donors` */

insert  into `donors`(`user_id`,`login_id`,`first_name`,`last_name`,`group_id`,`gender`,`age`,`place`,`pincode`,`phone`,`email`) values 
(2,5,'donor','d',1,'male','19','palakkad','59949','7736253394','vjsparrow04@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(3,'bank','bank','bank'),
(5,'donor','donor123','donor');

/*Table structure for table `requests` */

DROP TABLE IF EXISTS `requests`;

CREATE TABLE `requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `unit_required` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `requests` */

insert  into `requests`(`request_id`,`user_id`,`group_id`,`date_time`,`unit_required`,`pincode`,`status`) values 
(4,2,2,'2024-02-17','80ml','7667','pending');

/*Table structure for table `requrement_message` */

DROP TABLE IF EXISTS `requrement_message`;

CREATE TABLE `requrement_message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `unit_requried` varchar(222) DEFAULT NULL,
  `description` varchar(222) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `requrement_message` */

insert  into `requrement_message`(`message_id`,`bank_id`,`user_id`,`group_id`,`unit_requried`,`description`) values 
(1,1,2,1,'245ml','ok thee'),
(2,1,2,1,'350ml','check'),
(3,1,2,1,'290ml','blood'),
(4,1,2,1,'280ml','urgent'),
(5,1,2,2,'200ml','u');

/*Table structure for table `status` */

DROP TABLE IF EXISTS `status`;

CREATE TABLE `status` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `donation_availability_status` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `message_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `status` */

insert  into `status`(`status_id`,`user_id`,`donation_availability_status`,`date_time`,`message_id`) values 
(1,2,'pending','2024-02-14',2),
(2,2,'pending','2024-02-14',3),
(3,2,'pending','2024-02-17',4),
(4,2,'okey','2024-02-26',5);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
