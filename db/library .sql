-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 14, 2021 at 08:12 PM
-- Server version: 5.7.32-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `topic` varchar(50) DEFAULT NULL,
  `available` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `title`, `author`, `topic`, `available`) VALUES
(1, 'Science', 'Manoj Shahi', 'Physics and Chemistry', 0),
(2, 'python for every one', 'Aaryan', 'python fundamentals', 1),
(3, 'Java Essencial', 'Kunal', 'Java programing for beginners', 1),
(4, 'Maths Magic', 'Rishi', 'probablity annd statistics', 1),
(5, 'Machine Learning', 'kunal', 'neural networks and pytorch', 1),
(6, 'Data Science', 'kunal', 'data science', 1);

-- --------------------------------------------------------

--
-- Table structure for table `issue_return`
--

CREATE TABLE `issue_return` (
  `id` int(11) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `book_title` varchar(50) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `member_name` varchar(50) DEFAULT NULL,
  `issue_date` datetime DEFAULT NULL,
  `return_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `issue_return`
--

INSERT INTO `issue_return` (`id`, `book_id`, `book_title`, `member_id`, `member_name`, `issue_date`, `return_date`) VALUES
(1, 1, 'Science', 1, 'kunal', '2021-02-14 19:19:40', '2021-02-14 19:26:30'),
(2, 2, 'python for every one', 1, 'kunal', '2021-02-14 19:21:44', '2021-02-14 19:34:13'),
(3, 1, 'Science', 1, 'kunal', '2021-02-14 19:36:46', '2021-02-14 19:36:59');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `joining` datetime DEFAULT NULL,
  `valid_till` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `name`, `address`, `phone`, `joining`, `valid_till`) VALUES
(1, 'kunal', 'lekha nagar patna', '9334397442', '2021-02-09 21:34:36', '2021-08-09 21:34:36'),
(2, 'Aaryan', 'Matri enclave patna', '989584985', '2021-02-14 19:40:31', '2021-08-14 19:40:31');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `issue_return`
--
ALTER TABLE `issue_return`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `issue_return`
--
ALTER TABLE `issue_return`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
