
create database VentaCobroMovil;

use VentaCobroMovil;
create table Vendedor(
idVendedor int primary key not null AUTO_INCREMENT ,
numVentas int not null
 );
 create table Rol(
idRol int primary key not null AUTO_INCREMENT ,
nombre varchar(50) not null
 );
  create table Categoria(
idCategoria int primary key not null AUTO_INCREMENT ,
nombre varchar(50) not null
 );
  create table Empaque(
idEmpaque int primary key not null AUTO_INCREMENT ,
nombre varchar(50) not null
 );
  create table Unidad_Medida(
idUnidad int primary key not null AUTO_INCREMENT ,
nombre varchar(50) not null,
valor double
 );
create table usuario(
 idUsuario int  primary key not null AUTO_INCREMENT ,
 nombres varchar (50)not null,
 apellidos varchar (50)not null,
 ruc varchar (13)not null,
 cedula varchar (10)not null,
 direccion varchar (50)not null,
 telefono varchar (10)not null,
 correo varchar (50)not null,
 estado boolean not null,
 fechaRegistro datetime not null,
 usuario varchar (50) not null,
 contrasena varchar (50)not null,
 idRol int not null,
 idVendedor int not null,
 FOREIGN KEY (idRol) REFERENCES Rol(idRol),
 FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
 );
 create table Cliente(
idCliente int primary key not null AUTO_INCREMENT ,
 nombres varchar (50)not null,
 apellidos varchar (50)not null,
 cedula varchar (10)not null,
 tienda varchar (50)not null,
 telefono varchar (10)not null,
 correo varchar (50)not null,
 estado boolean not null,
 fechaRegistro datetime not null,
 ciudad varchar (50) not null
 
);
 create table Pedido(
idPedido int primary key not null AUTO_INCREMENT ,
estado varchar(10)not null,
fechaPedido datetime not null,
ahorro double not null,
subtotal double not null,
ivatotal double,
total double,
comentario varchar (100),
idVendedor int not null,
idCliente int not null,
FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
 FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
 );

 create table Producto(
 idProducto int primary key not null AUTO_INCREMENT ,
 nombre varchar (50)not null,
 descripcion varchar (50)not null,
 marca varchar (30)not null,
 precio double,
 fechaIngreso datetime,
 iva double,
 idUnidad int not null,
 idEmpaque int not null,
 idCategoria int not null,
 FOREIGN KEY (idUnidad) REFERENCES Unidad_Medida(idUnidad),
 FOREIGN KEY (idEmpaque) REFERENCES Empaque(idEmpaque),
FOREIGN KEY (idCategoria) REFERENCES Categoria(idCategoria)

 );
 
 create table DetallePedido(
 idDetalle int primary key not null AUTO_INCREMENT ,
 cantidad int not null,
 precio double,
 iva double,
 descuento double,
 idPedido int not null,
 idProducto int not null,
 FOREIGN KEY (idPedido) REFERENCES Pedido(idPedido),
FOREIGN KEY (idProducto) REFERENCES Producto(idProducto)

 );
 
INSERT INTO `ventacobromovil`.`vendedor` (`idVendedor`, `numVentas`) VALUES ('1', '12');
INSERT INTO `ventacobromovil`.`vendedor` (`idVendedor`, `numVentas`) VALUES ('2', '43');
INSERT INTO `ventacobromovil`.`vendedor` (`idVendedor`, `numVentas`) VALUES ('3', '5');
INSERT INTO `ventacobromovil`.`rol` (`idRol`, `nombre`) VALUES ('1', 'Administrador');
INSERT INTO `ventacobromovil`.`rol` (`idRol`, `nombre`) VALUES ('2', 'Vendedor');
INSERT INTO `ventacobromovil`.`rol` (`idRol`, `nombre`) VALUES ('3', 'Despachador');
INSERT INTO `ventacobromovil`.`usuario` (`idUsuario`, `nombres`, `apellidos`, `ruc`, `cedula`, `direccion`, `telefono`, `correo`, `estado`, `fechaRegistro`, `usuario`, `contrasena`, `idRol`, `idVendedor`) VALUES ('1', 'Wesley', 'Briones', '0986757438001', '0948573475', 'Esmeraldas y los Rios', '0948374564', 'wesbrio@hotmail.com', '1', '11/8/21', 'wesbrio', 'wesbrio', '1', '1');
INSERT INTO `ventacobromovil`.`usuario` (`idUsuario`, `nombres`, `apellidos`, `ruc`, `cedula`, `direccion`, `telefono`, `correo`, `estado`, `fechaRegistro`, `usuario`, `contrasena`, `idRol`, `idVendedor`) VALUES ('2', 'Katiuska', 'Marin', '095847534001', '0923845721', 'portete y la 11', '0948374572', 'katiuska@hotmail.com', '1', '10/8/21', 'katmarin', 'katmarin', '1', '2');
INSERT INTO `ventacobromovil`.`empaque` (`idEmpaque`, `nombre`) VALUES ('1', 'empaque1');
INSERT INTO `ventacobromovil`.`empaque` (`idEmpaque`, `nombre`) VALUES ('2', 'empaque2');
INSERT INTO `ventacobromovil`.`empaque` (`idEmpaque`, `nombre`) VALUES ('3', 'empaque3');
INSERT INTO `ventacobromovil`.`categoria` (`idCategoria`, `nombre`) VALUES ('1', 'categoria1');
INSERT INTO `ventacobromovil`.`categoria` (`idCategoria`, `nombre`) VALUES ('2', 'categoria2');
INSERT INTO `ventacobromovil`.`categoria` (`idCategoria`, `nombre`) VALUES ('3', 'categoria3');
INSERT INTO `ventacobromovil`.`Unidad_Medida` (`idUnidad`, `nombre`, `valor`) VALUES ('1', 'kg', '1.2');
INSERT INTO `ventacobromovil`.`Unidad_Medida` (`idUnidad`, `nombre`, `valor`) VALUES ('2', 'L', '2.1');
INSERT INTO `ventacobromovil`.`producto` (`idProducto`, `nombre`, `descripcion`, `marca`, `precio`, `fechaIngreso`, `iva`, `idUnidad`, `idEmpaque`, `idCategoria`) VALUES ('1', 'Toni mix', 'Yogurt', 'Toni', '12.3', '12/1/21', '12', '1', '2', '3');
INSERT INTO `ventacobromovil`.`producto` (`idProducto`, `nombre`, `descripcion`, `marca`, `precio`, `fechaIngreso`, `iva`, `idUnidad`, `idEmpaque`, `idCategoria`) VALUES ('2', 'Fideos tallerin', 'fideos', 'Sumesa', '32.1', '14/2/21', '12', '2', '1', '2');
INSERT INTO `ventacobromovil`.`cliente` (`idCliente`, `nombres`, `apellidos`, `cedula`, `tienda`, `telefono`, `correo`, `estado`, `fechaRegistro`, `ciudad`) VALUES ('1', 'Juam', 'Marcet', '0968475345', 'Los 3 Hermanos', '20495863', 'cliente@gmail.com', '1', '3/4/21', 'guayaquil');
INSERT INTO `ventacobromovil`.`pedido` (`idPedido`, `estado`, `fechaPedido`, `ahorro`, `subtotal`, `ivatotal`, `total`, `comentario`,`idVendedor`, `idCliente`) VALUES ('1', 'true', '12/5/21', '12.3', '45.32', '13.4', '58.72', 'comentario1', '1', '1');

