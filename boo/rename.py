#
# Описания полей отчетности можно посмотреть например в:
# http://info.avtovaz.ru/files/avtovaz_ras_fs_2012_rus_secured.pdf
#
# Более подробно:
# http://www.consultant.ru/document/cons_doc_LAW_103394/b990bf4a13bd23fda86e0bba50c462a174c0d123/#dst100515
#

# TODO: проставить названия полей
FIELDS = [
    ('1150', 'of', 'Основные фонды'),
    ('1100', 'ta_fix', ''),
    ('1200', 'ta_nonfix', ''),
    ('1250', 'cash', 'Денежные средства и денежные эквиваленты'), 
    ('1600', 'ta', ''),
    ('1300', 'tp_capital', ''),
    ('1400', 'tp_long', ''),
    ('1410', 'debt_long', ''),
    ('1500', 'tp_short', ''),
    ('1510', 'debt_short', ''),
    ('1700', 'tp'                  ''),


    ('2110', 'sales', ''),
    ('2200', 'profit_oper', ''),
    ('2330', 'exp_interest', ''),
    ('2300', 'profit_before_tax', ''),
    ('2400', 'profit_after_tax', ''),    


    ('4100', 'cf_oper', ''),
    ('4200', 'cf_inv', ''),
    ('4300', 'cf_fin', ''),
    ('4400', 'cf', ''),
    ('4110', 'cash_in_oper_total', ''),
    ('4111', 'cash_in_oper_sales', ''),
    ('4121', 'paid_to_supplier', ''),
    ('4122', 'paid_to_worker', ''),
    ('4123', 'paid_interest', ''),
    ('4124', 'paid_profit_tax', ''),
    ('4129', 'paid_other_costs', ''),
    ('4221', 'paid_fa_investment', '')]

DEFAULT_LOOKUP_DICT = {t[0]: t[1] for t in FIELDS}

doc = """БУХГАЛТЕРСКИЙ БАЛАНС	1000
Итого внеоборотных активов	1100
Нематериальные активы	1110
Результаты исследований и разработок	1120
Нематериальные поисковые активы	1130
Материальные поисковые активы	1140
Основные средства	1150
Доходные вложения в материальные ценности	1160
Финансовые вложения	1170
Отложенные налоговые активы	1180
Прочие внеоборотные активы	1190
Итого оборотных активов	1200
Запасы	1210
Налог на добавленную стоимость по приобретенным ценностям	1220
Дебиторская задолженность	1230
Финансовые вложения (за исключением денежных эквивалентов)	1240
Денежные средства и денежные эквиваленты	1250
Прочие оборотные активы	1260
БАЛАНС (актив)	1600
ИТОГО капитал	1300
Уставный капитал (складочный капитал, уставный фонд, вклады товарищей)	1310
Собственные акции, выкупленные у акционеров	1320
Переоценка внеоборотных активов	1340
Добавочный капитал (без переоценки)	1350
Резервный капитал	1360
Нераспределенная прибыль (непокрытый убыток)	1370
Долгосрочные заемные средства	1410
Отложенные налоговые обязательства	1420
Оценочные обязательства	1430
Прочие долгосрочные обязательства	1450
ИТОГО долгосрочных обязательств	1400
Краткосрочные заемные обязательства	1510
Краткосрочная кредиторская задолженность	1520
Доходы будущих периодов	1530
Оценочные обязательства	1540
Прочие краткосрочные обязательства	1550
ИТОГО краткосрочных обязательств	1500
БАЛАНС (пассив)	1700"""
pairs = [x.split('\t') for x in doc.split('\n')]

pairs_dict = {x[1]:x[0] for x in pairs}


WHO_IS_IT= {a:dict(text=pairs_dict.get(z, ""), code=z) for z, a in DEFAULT_LOOKUP_DICT.items()}
