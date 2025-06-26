-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 29, 2025 at 03:46 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1loanverficationdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `loantb`
--

CREATE TABLE `loantb` (
  `id` int(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Aadhar` varchar(250) NOT NULL,
  `AccNo` varchar(250) NOT NULL,
  `LoanId` varchar(250) NOT NULL,
  `type` varchar(250) NOT NULL,
  `Amt` int(250) NOT NULL,
  `date` date NOT NULL,
  `Info` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Reason` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `loantb`
--

INSERT INTO `loantb` (`id`, `Name`, `Mobile`, `Email`, `Aadhar`, `AccNo`, `LoanId`, `type`, `Amt`, `date`, `Info`, `Status`, `Reason`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', '319494587101', '9486365535357', 'LoanID78819', 'CropLoan', 8000, '2025-04-18', 'nill', 'Close', 'Face');

-- --------------------------------------------------------

--
-- Table structure for table `multitb`
--

CREATE TABLE `multitb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Account` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `multitb`
--

INSERT INTO `multitb` (`id`, `Account`, `UserName`) VALUES
(1, '9486365535357', 'sangeeth123');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(50) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `AccountNo` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Pin` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Balance` decimal(20,2) NOT NULL,
  `AadharNo` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Age`, `Mobile`, `Email`, `Address`, `AccountNo`, `UserName`, `Password`, `Pin`, `Status`, `Balance`, `AadharNo`) VALUES
(1, 'sangeeth Kumar', '40', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', '9486365535357', 'sangeeth123', 'sangeeth123', 'nill', 'Active', '0.00', '319494587101');

-- --------------------------------------------------------

--
-- Table structure for table `temploantb`
--

CREATE TABLE `temploantb` (
  `id` int(10) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Aadhar` varchar(250) NOT NULL,
  `AccNo` varchar(250) NOT NULL,
  `LoanId` varchar(250) NOT NULL,
  `type` varchar(250) NOT NULL,
  `Amt` int(250) NOT NULL,
  `date` date NOT NULL,
  `Info` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Doc` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `temploantb`
--


-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `id` bigint(10) NOT NULL auto_increment,
  `AccountNo` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `OTP` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `temptb`
--

INSERT INTO `temptb` (`id`, `AccountNo`, `UserName`, `OTP`) VALUES
(1, '123', 'sangeeth123', '123');

-- --------------------------------------------------------

--
-- Table structure for table `waivertb`
--

CREATE TABLE `waivertb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Type` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `waivertb`
--

INSERT INTO `waivertb` (`id`, `Type`, `Amount`, `FileName`) VALUES
(1, 'CropLoan', '9000', '1372334.png');
