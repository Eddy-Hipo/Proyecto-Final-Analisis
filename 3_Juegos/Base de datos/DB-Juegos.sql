-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-03-2021 a las 03:21:53
-- Versión del servidor: 10.4.16-MariaDB
-- Versión de PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `examen2-juegos2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `table_name`
--

CREATE TABLE `table_name` (
  `Game` varchar(100) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  `Genre` varchar(100) DEFAULT NULL,
  `Publisher` varchar(100) DEFAULT NULL,
  `NorthAmerica` decimal(10,2) DEFAULT NULL,
  `Europe` decimal(10,2) DEFAULT NULL,
  `Japan` decimal(10,2) DEFAULT NULL,
  `RestofWorld` decimal(10,2) DEFAULT NULL,
  `Global` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `table_name`
--

INSERT INTO `table_name` (`Game`, `Year`, `Genre`, `Publisher`, `NorthAmerica`, `Europe`, `Japan`, `RestofWorld`, `Global`) VALUES
('Grand Theft Auto V', 2014, 'Action', 'Rockstar Games', '6.06', '9.71', '0.60', '3.02', '19.39'),
('Call of Duty: Black Ops 3', 2015, 'Shooter', 'Activision', '6.18', '6.05', '0.41', '2.44', '15.09'),
('Red Dead Redemption 2', 2018, 'Action-Adventure', 'Rockstar Games', '5.26', '6.21', '0.21', '2.26', '13.94'),
('Call of Duty: WWII', 2017, 'Shooter', 'Activision', '4.67', '6.21', '0.40', '2.12', '13.40'),
('FIFA 18', 2017, 'Sports', 'EA Sports', '1.27', '8.64', '0.15', '1.73', '11.80'),
('FIFA 17', 2016, 'Sports', 'Electronic Arts', '1.26', '7.95', '0.12', '1.61', '10.94'),
('Uncharted (PS4)', 2016, 'Action', 'Sony Interactive Entertainment', '4.49', '3.93', '0.21', '1.70', '10.33'),
('Spider-Man (PS4)', 2018, 'Action-Adventure', 'Sony Interactive Entertainment', '3.64', '3.39', '0.32', '1.41', '8.76'),
('Call of Duty: Infinite Warfare', 2016, 'Shooter', 'Activision', '3.11', '3.83', '0.19', '1.36', '8.48'),
('Fallout 4', 2015, 'Role-Playing', 'Bethesda Softworks', '2.91', '3.97', '0.27', '1.34', '8.48'),
('FIFA 16', 2015, 'Sports', 'EA Sports', '1.15', '5.77', '0.07', '1.23', '8.22'),
('Star Wars Battlefront 2015', 2015, 'Shooter', 'Electronic Arts', '3.31', '3.19', '0.23', '1.30', '8.03'),
('Call of Duty: Advanced Warfare', 2014, 'Shooter', 'Activision', '2.84', '3.34', '0.14', '1.22', '7.53'),
('Battlefield 1', 2016, 'Shooter', 'Electronic Arts', '2.20', '3.65', '0.29', '1.12', '7.26'),
('The Last of Us', 2014, 'Action-Adventure', 'Sony Computer Entertainment', '2.70', '2.86', '0.11', '1.10', '6.77'),
('MineCraft', 2014, 'Misc', 'Sony Computer Entertainment', '1.89', '3.13', '0.35', '0.96', '6.33'),
('FIFA 15', 2014, 'Sports', 'EA Sports', '0.83', '4.49', '0.05', '0.94', '6.32'),
('God of War (PS4)', 2018, 'Action', 'Sony Interactive Entertainment', '2.83', '2.17', '0.13', '1.02', '6.15'),
('Horizon: Zero Dawn', 2017, 'Action', 'Sony Interactive Entertainment', '2.20', '2.43', '0.28', '0.92', '5.82'),
('Destiny', 2014, 'Shooter', 'Activision', '2.53', '2.13', '0.16', '0.94', '5.76'),
('Uncharted: The Nathan Drake Collection', 2015, 'Action', 'Sony Computer Entertainment', '2.55', '2.11', '0.10', '0.94', '5.70'),
('The Witcher 3: Wild Hunt', 2015, 'Role-Playing', 'Namco Bandai Games', '1.48', '2.82', '0.28', '0.81', '5.39'),
('Final Fantasy XV', 2016, 'Role-Playing', 'Square Enix', '1.81', '1.53', '1.05', '0.68', '5.07'),
('Crash Bandicoot N. Sane Trilogy', 2017, 'Platform', 'Activision', '1.09', '2.92', '0.07', '0.74', '4.83'),
('Monster Hunter: World', 2018, 'Action', 'Capcom', '1.03', '1.06', '2.17', '0.42', '4.67'),
('Overwatch', 2016, 'Shooter', 'Blizzard Entertainment', '1.84', '1.80', '0.17', '0.73', '4.54'),
('Star Wars Battlefront II (2017)', 2017, 'Shooter', 'Electronic Arts', '1.70', '1.99', '0.12', '0.73', '4.53'),
('Watch Dogs', 2014, 'Action-Adventure', 'Ubisoft', '1.40', '2.13', '0.11', '0.68', '4.32'),
('Call of Duty: Ghosts', 2013, 'Shooter', 'Activision', '1.79', '1.64', '0.05', '0.69', '4.17'),
('Far Cry 4', 2014, 'Shooter', 'Ubisoft', '1.18', '2.14', '0.11', '0.63', '4.06'),
('NBA 2K16', 2015, 'Sports', '2K Sports', '2.56', '0.66', '0.05', '0.71', '3.98'),
('Far Cry 5', 2018, 'Action', 'Ubisoft', '1.44', '1.73', '0.15', '0.62', '3.95'),
('Battlefield 4', 2013, 'Shooter', 'Electronic Arts', '1.40', '1.74', '0.19', '0.62', '3.94'),
('Gran Turismo Sport', 2017, 'Racing', 'Sony Interactive Entertainment', '0.63', '2.35', '0.24', '0.54', '3.77'),
('Madden NFL 15', 2014, 'Sports', 'EA Sports', '1.58', '0.25', '0.00', '0.41', '2.25'),
('Need for Speed: Payback', 2017, 'Racing', 'Electronic Arts', '0.62', '1.18', '0.04', '0.34', '2.18'),
('Destiny: The Taken King', 2015, 'Shooter', 'Activision', '0.97', '0.80', '0.05', '0.36', '2.18'),
('Need for Speed Rivals', 2013, 'Racing', 'Electronic Arts', '0.75', '1.04', '0.03', '0.35', '2.17'),
('PlayStation VR Worlds', 2016, 'Misc', 'Sony Interactive Entertainment', '0.36', '1.40', '0.09', '0.32', '2.16'),
('Battlefield: Hardline', 2015, 'Shooter', 'Electronic Arts', '0.72', '0.97', '0.14', '0.33', '2.15'),
('Rise of the Tomb Raider', 2016, 'Adventure', 'Square Enix', '0.61', '1.08', '0.05', '0.32', '2.07'),
('LittleBigPlanet 3', 2014, 'Platform', 'Sony Computer Entertainment', '0.78', '0.93', '0.01', '0.34', '2.06'),
('The Elder Scrolls Online', 2015, 'MMO', 'Bethesda Softworks', '0.74', '0.98', '0.00', '0.33', '2.05'),
('Middle-Earth: Shadow of War', 2017, 'Action', 'Warner Bros. Interactive Entertainment', '0.82', '0.84', '0.06', '0.33', '2.04'),
('Dragon Quest XI', 2017, 'Role-Playing', 'Square Enix', '0.29', '0.22', '1.43', '0.10', '2.04'),
('Rocket League', 2016, 'Sports', '505 Games', '0.37', '1.34', '0.00', '0.31', '2.02');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
