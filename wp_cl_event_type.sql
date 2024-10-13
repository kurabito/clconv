-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: pod-140517.wpengine.com:13306
-- Generation Time: Oct 12, 2024 at 01:21 AM
-- Server version: 8.0.37-29
-- PHP Version: 7.2.24-0ubuntu0.18.04.17+esm3

-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
-- START TRANSACTION;
-- SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wp_commloaves`
--

-- --------------------------------------------------------

--
-- Table structure for table `wp_cl_event_type`
--

-- CREATE TABLE `wp_cl_event_type` (
--   `event_type_id` int NOT NULL,
--   `event_name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
--   `business_rule` text COLLATE utf8mb4_unicode_520_ci,
--   `event_category` enum('person','hub','pantry') COLLATE utf8mb4_unicode_520_ci NOT NULL,
--   `query` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
--   `event_type_status` enum('active','inactive') COLLATE utf8mb4_unicode_520_ci NOT NULL,
--   `extra_info_descr` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `wp_cl_event_type`
--

-- INSERT INTO `wp_cl_event_type` (`event_type_id`, `event_name`, `business_rule`, `event_category`, `query`, `event_type_status`, `extra_info_descr`) VALUES
-- (1, 'accept terms', 'User accepts terms', 'person', NULL, 'active', NULL),
-- (2, 'create profile', 'User creates profile', 'person', NULL, 'active', NULL),
-- (3, 'update profile', 'User updates profile', 'person', NULL, 'active', NULL),
-- (4, 'set hub', 'User selects hub', 'person', NULL, 'active', NULL),
-- (5, 'set assignments', 'Any combination of patron, baker, and time; or retail', 'person', NULL, 'active', NULL),
-- (6, 'set roles', 'Admin updates user roles', 'person', NULL, 'active', NULL),
-- (7, 'set person status', 'Active or inactive', 'person', NULL, 'active', NULL),
-- (8, 'set hub owners', 'Hub owner added or changed', 'hub', NULL, 'active', NULL),
-- (9, 'set hub delegates', 'Hub delegates added or changed', 'hub', NULL, 'active', NULL),
-- (10, 'set pantries', 'Pantries added or removed from hub', 'hub', NULL, 'active', NULL),
-- (11, 'set hub data', 'Change to any tracked data for a hub', 'hub', NULL, 'active', NULL),
-- (12, 'set pantry liaison', 'Pantry liaison added or changed', 'pantry', NULL, 'active', NULL),
-- (13, 'set pantry data', 'Change to any tracked data for a pantry', 'pantry', NULL, 'active', NULL);


UPDATE wp_cl_event_type
SET event_name = 'create profile', business_rule = 'User creates profile'
WHERE event_type_id = 1;

UPDATE wp_cl_event_type
SET event_name = 'update profile', business_rule = 'User updates profile'
WHERE event_type_id = 2;

UPDATE wp_cl_event_type
SET event_name = 'set hub', business_rule = 'User selects hub'
WHERE event_type_id = 3;

UPDATE wp_cl_event_type
SET event_name = 'set assignments', business_rule = 'Any combination of patron, baker, and time; or retail'
WHERE event_type_id = 4;

UPDATE wp_cl_event_type
SET event_name = 'set roles', business_rule = 'Admin updates user roles'
WHERE event_type_id = 5;

UPDATE wp_cl_event_type
SET event_name = 'set person status', business_rule = 'Active or inactive'
WHERE event_type_id = 6;

UPDATE wp_cl_event_type
SET event_name = 'set hub owners', business_rule = 'Hub owner added, changed, or removed', event_category = 'hub'
WHERE event_type_id = 7;

UPDATE wp_cl_event_type
SET event_name = 'set hub delegates', business_rule = 'Hub delegates added, changed, or removed'
WHERE event_type_id = 8;

UPDATE wp_cl_event_type
SET event_name = 'set pantries', business_rule = 'Pantries added or removed from hub'
WHERE event_type_id = 9;

UPDATE wp_cl_event_type
SET event_name = 'set hub data', business_rule = 'Change to any tracked data for a hub'
WHERE event_type_id = 10;

UPDATE wp_cl_event_type
SET event_name = 'set pantry liaison', business_rule = 'Pantry liaison added or changed'
WHERE event_type_id = 11;

UPDATE wp_cl_event_type
SET event_name = 'set hubs', business_rule = 'Changes to hubs assigned to a pantry'
WHERE event_type_id = 12;

UPDATE wp_cl_event_type
SET event_name = 'set pantry data', business_rule = 'Change to any tracked data for a pantry'
WHERE event_type_id = 13;


-- INSERT INTO wp_cl_event_type (event_type_id, event_name, business_rule, event_category, query, event_type_status, extra_info_descr) VALUES
-- (14, 'set person hub owner', 'Person is added or deleted as hub owner', 'person', NULL, 'active', NULL),
-- (15, 'set person hub delegate', 'Person is added or deleted as hub delegate', 'person', NULL, 'active', NULL),
-- (16, 'set person pantry liaison', 'Person is added or deleted as pantry liaison', 'person', NULL, 'active', NULL);


INSERT INTO wp_cl_event_type (event_name, business_rule, event_category, query, event_type_status, extra_info_descr) VALUES
('set person hub owner', 'Person is added or deleted as hub owner', 'person', NULL, 'active', NULL),
('set person hub delegate', 'Person is added or deleted as hub delegate', 'person', NULL, 'active', NULL),
('set person pantry liaison', 'Person is added or deleted as pantry liaison', 'person', NULL, 'active', NULL);


-- (1, 'accept terms', 'User accepts terms', 'person', NULL, 'active', NULL),
-- (2, 'create profile', 'User creates profile', 'person', NULL, 'active', NULL),
-- (3, 'update profile', 'User updates profile', 'person', NULL, 'active', NULL),
-- (4, 'set hub', 'User selects hub', 'person', NULL, 'active', NULL),
-- (5, 'set assignments', 'Any combination of patron, baker, and time; or retail', 'person', NULL, 'active', NULL),
-- (6, 'set roles', 'Admin updates user roles', 'person', NULL, 'active', NULL),
-- (7, 'set person status', 'Active or inactive', 'person', NULL, 'active', NULL),
-- (8, 'set hub owners', 'Hub owner added or changed', 'hub', NULL, 'active', NULL),
-- (9, 'set hub delegates', 'Hub delegates added or changed', 'hub', NULL, 'active', NULL),
-- (10, 'set pantries', 'Pantries added or removed from hub', 'hub', NULL, 'active', NULL),
-- (11, 'set hub data', 'Change to any tracked data for a hub', 'hub', NULL, 'active', NULL),
-- (12, 'set pantry liaison', 'Pantry liaison added or changed', 'pantry', NULL, 'active', NULL),
-- (13, 'set pantry data', 'Change to any tracked data for a pantry', 'pantry', NULL, 'active', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `wp_cl_event_type`
--
-- ALTER TABLE `wp_cl_event_type`
--   ADD PRIMARY KEY (`event_type_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `wp_cl_event_type`
--
-- ALTER TABLE `wp_cl_event_type`
--   MODIFY `event_type_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
-- COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
