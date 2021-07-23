CREATE TABLE `servicios` (
 `id` int(10) NOT NULL AUTO_INCREMENT,
 `spa` varchar(10) NOT NULL,
 `nombre` varchar(100) NOT NULL,
 `proceso` varchar(20) NOT NULL,
 `duracion` varchar(20) NOT NULL,
 `precio` decimal(6,2) NOT NULL,
 `foto` varchar(255) NOT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4