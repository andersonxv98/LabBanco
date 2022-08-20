create view view_nome_qtd
as 
select produto.nome, produtos_da_venda.qtd_ven, produtos_da_venda.valor_uni
from produto inner join produtos_da_venda 
on produto.codigo = produtos_da_venda.codigo_pro

select * from view_nome_qtd