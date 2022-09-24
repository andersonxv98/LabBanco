
CALL QtdProdutos(1, @increment);
SELECT  @increment;

set @data1 = '2021-07-22';
set @dataf =  '2022-06-01';
call ToTalVendas(@data1,@dataf, @totalvendas);
SELECT @totalvendas;