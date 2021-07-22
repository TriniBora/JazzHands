CREATE TABLE `jazz`.`usuarios` ( `id_usuario` INT(255) NOT NULL AUTO_INCREMENT , `username` VARCHAR(50) NOT NULL , `password` VARCHAR(10) NOT NULL , PRIMARY KEY (`id_usuario`)) ENGINE = InnoDB;

INSERT INTO `jazz`.`usuarios` (`id_usuario`, `username`, `password`) VALUES (NULL, 'admin', 'admin');