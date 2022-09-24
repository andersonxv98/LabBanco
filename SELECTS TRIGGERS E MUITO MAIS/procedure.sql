CREATE DEFINER=`root`@`localhost` PROCEDURE `QtdProdutos`(in NumVenda int, out QtdProd int)
begin
	select count(*) into QtdProd
    from produtod_da_venda
    where numero_ven = NumVenda;
end