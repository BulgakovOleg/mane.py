import random
def facts_of_trash():
    spisoc = ["Полиэтиленовые пакеты являются одним из самых опасных видов мусора и способны уничтожить целую экосистему. Брошенный в воду пакет может плавать в ней до 100 лет, а у каждой третьей морской птицы или рыбы в желудке находят пластик или полиэтилен. Пластиковые отходы, которые попадают в океан, убивают около 1 млн морских обитателей ежегодно","Мусор всегда играл главенствующую роль в человеческой культуре. Удивительно, что он оставил свой след и в религии. Например, участок земли под Иерусалимом, куда сбрасывали и периодически сжигали отходы, в Библии назван Геенной Огненной. Для христиан Геенна стала одним из обозначений Ада. Не менее известен один из 12-ти подвигов, которые совершил герой древнегреческих мифов Геракл - он решил проблему отходов, накопившихся в конюшнях царя Авгия","Изучением способов утилизации мусора занимается наука гарбология. Гарбология (от англ. garbage «мусор») или мусороведение, или мусорология — отдельное направление экологии, занимается изучением мусорных отходов и методов их утилизации. Так же гарбология - вид археологии, иначе говоря «мусорная археология», которая изучает мусорные отходы с целью изучения бытовой жизни людей","Каждую секунду в мире появляется 3,8 кг «экологически безвредного мусора»: объедки, яичная скорлупа, кожура от картофеля и прочее. Он составляет 29 % от среднестатистической мусорной корзины современного человека. Что же касается других составляющих, то 25% - это картон и бумага, 13% - стекло, 11% - пластик, 4% - металл и 18% - другие материалы"," Если в море бросить бумажную салфетку, то она исчезнет через три месяца, спички растворятся через шесть месяцев. Брошенный окурок проплавает в море от одного года до пяти лет, а пакет из полиэтилена – от десяти до двадцати лет. Изделия из нейлона растворятся через тридцать-сорок лет, а консервная банка через пятьсот! Пройдет тысяча лет, и только после этого исчезнет стандартная стеклянная бутылка!"]
    return random.choice(spisoc)
def things_of_trash():
    list1 = ["Использованные стеклянные бутылки могут стать сырьем для производства посуды, зеркал, оконных стекол и многих других вещей. Из них также производят стеклобетон и стекловату, которая является широко распространенным теплоизолирующим материалом.","Из древесных отходов можно изготавливать древесно-стружечные плиты, бумагу, топливные гранулы и брикеты","Из старых журналов, газет можно получить новую бумагу, которую могут использовать для новых книг и товаров"]
    return random.choice(list1)
def help_with_trash():
    list2 = ["Некоторые старые вещи могут найти новые применения - например, из них можно сделать новые поделки или восстановить их","Выкидывайте мусор разного типа в соответствующие контейнеры"]
    return random.choice(list2)
def place_for_trash():
    list3 = ["Специальные пункты приёма батареек, пункты в сетевых магазинах, контейнеры для батареек «Экобокс», пункты, организованные в рамках акций и волонтёрских проектов - лучшие места для использованных батареек"]
    return random.choice(list3)
