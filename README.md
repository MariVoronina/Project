# Проект по дисциплине "Языки и методы программирования"

Приложение анализа акций крупных мировых компаний и подбора наиболее выгодных предложений.

# Описание проекта

Данное приложение было создано нами для людей как экономической, так и любой другой специальности. Простой и удобный интерфейс подходит всем пользователям, которые хотели бы узнать поведение акций крупных мировых компаний и выяснить, покупка и продажа каких акций были бы наиболее выгодными.

### ***Описание приложения***

Наше приложение написано на языке программирования Python, так как мы изучаем его в рамках дисциплины. Наш проект представляет собой оконное приложение, позволяющее пользователю либо получить данные по акциям крупных компаний выбранного типа в выбранной стране в течении выбранного периода, которые будут представлены в виде графика, либо сравнить акции крупных компаний выбранного типа в двух выбранных странах за выбранный период времени. Кроме того, если пользователь захочет узнать, что за компании представлены в проекте, то приложение позволяет ему получить профиль (краткое описание) каждой компании. 

### ***Актуальность приложения***

Фондовый рынок - это неотъемлимая часть экономики любой страны. Есть три мотива, по которым компании выходят на фондовый рынок:
- привлечение финансирования для развития и масштабирования бизнеса;
- рыночная оценка бизнеса;
- возможность для основателей или инвесторов продать свою долю бизнеса по рыночной цене.

Таким образом, любой бизнесмен, который хочет достигнуть успеха, рано или поздно столкнётся с необходимостью приложения, которое позволяло бы узнавать текущую информацию по акциям крупных компаний, а так же имело бы возможность сравнивать рыночные цены акций, чтобы понять, какие выгоднее продаются, а какие покупаются. С помощью такого приложения бизнесмен сможет контролировать и анализировать поведение акций своей компании, а так же оценивать успех собственного дела.

Однако, тема акций актуальна не только для работников и руководителей компаний. Любой человек может стать акционером компаний, имеющих ОАО (Открытое Акционерное Общество). Так, владея 1 акцией — начинающий акционер получаете базовые права собственника компании: участие в управлении (участие в собраниях акционеров), право на дивиденды и на компенсацию в случае ликвидации АО. А владея 2%, он может уже выдвигать своего представителя в совет директоров. В итоге, упомянутое выше приложение будет актуально и для таких людей: оно позволит анализировать акции крупных компаний и выяснить, акции какой страны и какого типа компании выгоднее приобретать и продавать, чтобы получить прибыль. 

### ***Правила работы с приложением***

Наше приложение работает с информацией о рыночных ценах акций, с которыми они выходили с торгов. Причём данная информация возвращается, начиная только с 2012 года, так как раньше некоторых из представленных компаний просто не существовало.

При открытии приложения на экран выводится окно, на котором пользователь может увидеть две вкладки: "Price analysis" и "Price comparison", причём та вкладка, которая не закрашена, показывает в каком режиме находится пользователь.

Если открыта вкладка "Price analysis", то пользователь должен выполнять следующие действия:
- как указано на данной вкладке, ему следует ввести страну и тип компаний, информацию по акциям которых он хочет получить;
- затем вводится дата начала и конца периода, обязательно в формате дд/мм/гггг, причём если дата введена неправильно, то пользователю высветится окно с сообщением об ошибке;
- как только все необходимые данные корректно введены, то если пользователь нажмёт кнопку "Draw a graph", то ему соответственно выведется в отдельном окне график соотношения закрывающих цен акций компаний выбранного типа в выбранной стране с днями в выбранном периоде, а если будет нажата кнопка "Information about companies", то в отдельном окне появится краткий профиль для каждой компании выбранного типа в выбранной стране.

Если открыта вкладка "Price comparison", то пользователь должен выполнять следующие действия:
- как указано на данной вкладке, ему следует ввести страны, которые он хочет сравнить, и тип компаний, среднюю цену которых в долларах он хочет сравнить;
- затем вводится дата начала и конца периода, обязательно в формате дд/мм/гггг, причём если дата введена неправильно, то пользователю высветится окно с сообщением об ошибке;
-  как только все необходимые данные корректно введены, то при нажатии на кнопку "Draw a graph" выведутся в отдельных окнах графики соотношения закрывающих цен акций компаний выбранного типа в выбранных странах с днями в выбранном периоде, а после закрытия графиков выведется окно, где будет написано, акции каких стран выгоднее.

# Список задач
При разработке приложения мы поставили перед собой следующие задачи:
- Выбрать крупные мировые компании с сайта [Investing.com](https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;1);
- На основе выбранных компаний создать базу данных с помощью компактной встраиваемой системы управления базами данных SQLite;
- Реализовать функционал нашего оконного приложения;
- Реализовать интерактивный модуль.

# Создание базы данных

Крупные мировые компании мы выбирали на сайте [Investing.com](https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;1), и для этого были следующие причины:
- во-первых, все данные на сайте находятся в свободном доступе;
- во-вторых, существует пакет Python **investpy** для получения данных с этого сайта.

Таким образом, данный сайт идеально подходит нам для решения поставленных задач и написания приложения.

С помощью компактной встраиваемой СУБД SQLite мы создаем нашу базу данных **Stocks.s3db**. Данная СУБД была выбрана, так как создан модуль **sqlite3**, который позволяет работать с базами данных в языке программирования Python.

Сначала, мы создаем две вспомогательных таблицы **Countries** и **Types**, которые будут содержать информацию про выбранные страны и типы компаний соответственно. Они необходимы для упрощения поиска нужных данных в нашей базе.

### ***Вспомогательная таблица Countries***

В данной таблице создано два поля для заполнения: ID и Name. Первое поле хранит коды каждой страны, на которые позже будет ссылаться наша основная таблица. Каждый код - это натуральное число от 1 до 5. Второе поле содержит наименования стран, каждое из которых соответствуют уникальному коду.

Для того, чтобы показать, как работает наше приложение, мы решили ограничиться 5 экономически развитыми странами: United States(США), Russia(Россия), China(Китай), France(Франция) и Japan(Япония). Им присвоены соответсвующие коды: 1, 2, 3, 4 и 5.

Поле ID сделано ключевым, так как каждый код уникален.

### ***Вспомогательная таблица Types***

В данной таблице создано два поля для заполнения: ID и Name. Первое поле хранит коды каждого типа компаний, на которые позже будет ссылаться наша основная таблица. Каждый код - это натуральное число от 1 до 8. Второе поле содержит наименования типов компаний, каждое из которых соответствуют уникальному коду.

Для того, чтобы показать, как работает наше приложение, мы решили ограничиться 8 распространёнными типами компаний: Banks(Банки), Biotechnology(Биотехнологии), Cars(Автомобили), Hotels(Отели и курортный бизнес), IT(Информационные технологии), Entertainments(Развлечения), Clothes(Бренды одежды и текстиль) и Food(Продовольственные компании). Им присвоены соответсвующие коды: 1, 2, 3, 4, 5, 6, 7 и 8.

Поле ID сделано ключевым, так как каждый код уникален.

Следующий шаг в создании базы данных - создание основной таблицы **Stocks**.

### ***Основная таблица Stocks***

В данной таблице создано пять полей для заполнения: Code, Name, Description, Country и Type. Первое поле хранит тикер акций определенной компании, который используется на фондовом рынке. Второе поле содержит полное название компании. Третье - это профиль компании, т.е. её краткое описание, которое будет выводить наше приложение. Четвёртое - это код страны компании, взятый из вспомогательной таблицы **Countries**. Наконец, пятое поле - это код типа компании, взятый из вспомогательной таблицы **Types**.

Всего в каждом типе компаний для каждой страны взято от 2 до 8 примеров, причём рассмотрены имено те, которое содержатся в пакете **investpy**.

Поле Code сделано ключевым, так как каждый тикер на фондовом рынке уникален.

# Реализация функционала оконного приложения

Для работы нашего приложения мы должны реализовать три основных функции:
- функция, которая выдает данные по акциям для графика;
- функция, которая сравнивает рыночные цены акций разных компаний из разных стран;
- функция, которая возвращает профиль компании (краткое описание).

Однако первым шагом в нашей работе будет импортирование необходимых пакетов и модулей.

### ***Импортирование*** 

Как уже говорилось ранее, данные по акциям для нашего приложения берутся из пакета **investpy**, который напрямую работает с сайтом [Investing.com](https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a%3Ceq_market_cap;1). Именно поэтому в самом начале написания функционала приложения мы устанавливаем данный пакет, а затем импортируем его.

Следующий шаг - это импорт модуля **sqlite3**, который позволит нам работать с созданной нами базой данных, выбирая из нее данные согласно заданным условиям.

На предпоследнем шаге мы должны импортировать модуль **json**, так как в дальнейшем мы будем получать данные из встроенных функций пакета **investpy** в формате json.

Завершающим шагом импортирования является импорт модуля **statistics**, который необходим нам для сравнения рыночных цен акций.

Следующий этап нашей работы - это создание глобальных переменных, которые будут необходимы для работы нашего приложения.

### ***Глобальные переменные***

- **types** - это список, элементами которого являются строки, представляющие собой названия типа компаний, используемых в нашей базе данных (необходим для выпадающего списка в нашем интерфейсе);
- **countries** - это список, элементами которого являются строки, представляющие собой названия стран, используемых в нашей базе данных (необходим для выпадающего списка в нашем интерфейсе);
- **dict_types** - это словарь, где ключом является тип компании, а значением - его уникальный код, присвоенный в базе данных (используется в дальнейшем в функции);
- **dict_countries** - это словарь, где ключом является название страны, а значением - его уникальный код, присвоенный в базе данных (используется в дальнейшем в функции)
- **dict_currency** - это словарь, где ключом является название страны, а значением - название валюты данной страны (необходим для оформления графиков и используется в дальнейшем в функции)
- **dict_transfer** - это словарь, где ключом является название валюты, а значением - то, сколько долларов стоит 1 единица данной валюты (используется в дальнейшем в функции) 

Сейчас мы напишем первую нужную нам функцию

### ***Реализация функции info_stocks***

Это функция, которая возвращает нам данные по акциям выбранного типа компаний в выбранной стране в течении выбранного периода времени. Возвращает она информацию в виде словаря, где ключом является название компании, а значением либо список рыночных цен, со значением которых акции этой компании выходили с торгов каждый день в течении выбранного периода времени, либо словарь, где ключом является дата, а значением рыночная цена, со значением которой акции данной компании вышли с торгов в данный день. Причём стоит заметить, что список возвращается тогда, когда пользователь задал период, включающий неменьше двух месяцев или даже несколько лет, а словарь - тогда, когда пользователь ввёл период,включающий всего несколько дней или месяц. Данное различие было сделано, чтобы в дальнейшем при недолгом периоде времени выводить данные для красивого оформления графика.

**Первый шаг нашей реализации** - это создание соединения с нашей базой данных, для чего используется переменная **stocks** и метод **connect()** из модуля **sqlite3**. Строка нашего кода будет выглядеть так: **stocks = sqlite3.connect("")**, где в кавычках будет написан полный путь к нашей базе данных. А затем для перемещения по нашей базе данных и выбора из нее необходимых компаний по заданным условиям создаётся так называемый объект "курсор" с помощью переменной **cursor** и метода **cursor()** из модуля **sqlite3**. Строка кода выглядит так: **cursor = stocks.cursor()**. Всё, наше соединение с базой данных создано, и мы готовы работать с ней.

**Вторым шагом** является описание аргументов функции:
- **country** - строка, представляющая собой название страны, в которой мы хотим выбрать тип компании;
- **type** - строка, представляющая собой название типа компаний, данные по акциям которых мы хотим получить;
- **data_from** - строка, представляющая собой начало выбранного периода времени, в течении которого мы хотим получить информацию по акциям, и написанная соответственно правилам использования приложения;
- **data_to** - строка, представляющая собой конец выбранного периода времени, в течении которого мы хотим получить информацию по акциям, и написанная соответственно правилам использования приложения.

**Третий шаг** - это проверка на неправильно введённую дату, для чего были созданы локальные переменные **tos** и **fro**. Изначально введённые даты **data_from** и **data_to** мы разбиваем по критерию "/" с помощью метода **split()** и превращаем в списки, где три элемента: 0 - день, 1 - месяц, 2 - год, а затем соответственно сохраняем их в **fro** и **tos**. Потом мы проверяем на неправильные даты: если введены года до 2012, если в одинаковый год месяц начала периода превышает месяц конца периода, если в одинаковый год и месяц день начала периода превышает день конца периода. В любом из таких случаев функция возвращает строку "Date entered incorrectly"(Неправильно введена дата)

**Четвёртый шаг** случается, если на третьем шаге даты, введённые пользователем, прошли проверку. Этот этап является основным в работе нашей функции. Сначала создаётся переменная **result**, хранящая строки нашей базы данных, которые соответствуют условиям (выбираются те компании, страна и тип которых совпадают с заданными аргументами функции). Запрос для базы данных пишется с помощью метода **execute()** и код выглядит так: **result = cursor.execute("select Code from Stocks where country=:code_count and type=:code_type", {"code_count": dict_countries[country], "code_type": dict_types[type]})**. Важно заметить, что запрос написан на языке запросов SQLite, для чего мы использовали % - форматирование строк. Из основной  таблицы **Stocks** мы выбираем из поля **Code** те компании, где код страны совпадает с кодом выбранной страны и код типа компании совпадает с кодом выбранного типа компании. Вот для чего нужны были глобальные переменные **dict_types** и **dict_countries**, в них мы по ключам ищем код выбранного типа компаний и выбранной страны для поиска в базе данных.

Затем создаётся пустой словарь **dict_result**, который и будет нашим итоговым результатом. Потом мы начинаем передвигаться по строкам нашей базы данных (каждая из которых представляет собой кортеж, состоящий из пяти элементов, идущих в следующем порядке: тикер компании, название компании, профиль компании, код страны и код типа компании), сохранённых в **result**, и для каждой из них выполняем следующие действия:
- с помощью функции **get_stock_historical_data** из пакета **investpy** мы получаем информацию по рыночным ценам данной компании в течении выбранного периода времени в формате **json**, затем с помощью метода **loads()** из модуля **json** мы преобразуем полученную информацию в словарь, где есть два ключа: name и historical, причем в первом хранится название компании, а во втором - список словарей. Словари в данном списке состоят из семи ключей: date, open, high, low, close, volume и currency, каждый из которых содержит соответствующую информацию. Однако нас интересуют только ключи date и close. Основной словарь, полученный с помощью метода **loads()** мы сохраняем в переменную **info**;
- дальше заполнение **dict_result** зависит от выбранного периода: если задан один год, месяц и несколько дней, если задан один год и разница в один месяц, если задана разница между годами один год и разница между месяцами тоже один. В первой ситуации мы в **dict_result** сохраняем название компании как ключ, а значением делаем словарь, где ключ - это день, в который акция вышла с торгов, а значение - это цена, с которой акция вышла с торгов. Во второй ситуации в **dict_result** сохраняется все тоже самое, вот только в словарях, соответствующих названиям компаний, ключом является день и месяц. И наконец в третьем случае все сохраняется в **dict_result** точно так же, как и во втором случае, но его нужно было рассмотреть отдельно из-за особенности поведения. Во всех остальных ситуациях, не соответствующих данным случаям, в **dict_result** сохраняется название компании как ключ, и список всех закрывающих цен за выбранный период как значение.

И наконец мы проверяем, если наш получившийся **dict_result** является пустым, то функция возвращает строку "Unfortunately there are no companies of this type" (К сожалению, таких компаний нет). В остальных случаях, наша функция возвращает **dict_result**.

Перейдём ко второй функции.

### ***Реализация функции compare_stocks***

Функция, которая сравнивает рыночные цены акций выбранного типа компаний, с которыми они вышли с торгов, в двух выбранных странах в течении выбранного периода времени. Причём возвращает она строку, в которой указано, чьи акции наиболее выгодны. Сравниваем мы рыночные цены акций, используя среднее арифметическое: для каждой компании данного вида мы запоминаем рыночные цены акций за весь период, а затем высчитываем их среднее арифметическое и прибавляем к общему результату. 

**Первым шагом нашей реализации** является описание аргументов функции:
- **country_1** - строка, представляющая собой название первой страны, которую мы хотим сравнивать;
- **country_2** - строка, представляющая собой название второй страны, которую мы хотим сравнивать;
- **typen** - строка, представляющая собой название типа компаний, по которому мы сравниваем компании в этих двух странах;
- **data_from** - строка, представляющая собой начало выбранного периода времени, в течении которого мы хотим сравнить информацию по акциям, и написанная соответственно правилам использования приложения;
- **data_to** - строка, представляющая собой конец выбранного периода времени, в течении которого мы хотим сравнить информацию по акциям, и написанная соответственно правилам использования приложения.

**Вторым шагом** является проверка на неправильно введённую дату и отсутствие информации об акциях компаний выбранного типа в какой-либо из двух стран. Для работы нашей функции создаём две локалных переменных **info_1** и **info_2**, каждая из которых содержит информацию по рыночным ценам акций выбранного типа компаний в течении выбранного периода времени в первой и второй сравниваемых странах соответственно. Данную информацию мы получаем, используя написанную нами функцию **info_stocks**. Если дата введена неправильно, то функция возвращает строку "Date entered incorrectly". Если же компаний выбранного типа нет в какой-нибудь из стран, то наша функция автоматически признаёт более выгодными акции той страны, в которой они есть, и возвращает строку, в которой написано, какая страна победила. А если таких компаний нет в обоих странах, то функция возвращает строку "Unfortunately there are no companies of this type".

**Третий шаг** происходит, если все данные введены корректно и такие компании есть в обоих странах. Это основной этап нашей работы. Создаем две локальных переменных **comp_1** и **comp_2**, которые хранят общий результат по всем средним арифметическим для каждой компании выбранного типа в первой и второй странах соответственно. В переменных **info_1** и **info_2** хранится словарь с нашими результатами.

Дальше мы для каждого результата в **info_1** и **info_2** выполняем следующие действия:
- циклом **for** пробегаемся по всем ключам данного словаря. Берём ключ и соответствующее ему значение. Если это значение тоже является словарем, то мы берем список его значений и высчитываем для него среднее арифметическое с помощью метода **mean** из модуля **statistics**. Затем в словаре **dict_currency** мы смотрим, какая валюта соответствует данной стране, а затем ищем сколько долларов в 1 единице данной валюты в словаре **dict_transfer**. Полученный результат с помощью **mean** мы умножаем на значение, полученной в словаре **dict_transfer** и округляем до 2 знаков после запятой с помощью метода **round**, а затем прибавляем к общему результату.  То есть мы получили сумму всех средних арифметических компаний выбранного типа в выбранной стране, переведённые из валюты этой страны в доллары;
- если же ключу соответствует список, то мы проделываем все то же самое для данного списка.

В конце, мы сравниваем значения, полученные в **comp_1** и **comp_2** и как итог, выводим строку, в которой написано, акции какой страны выгоднее по результатам сравнения.

И наконец наша последняя функция

### ***Реализация функции company_description***

Данная функция возвращает профиль компании по ее названию.

Аргументом данной функции является **company** - строка, представляющая собой название компании, профиль которой мы можем получить.

Сама она очень простая: с помощью объекта для работы с базой данных **cursor** и метода **execute()** из модуля **sqlite3** мы формируем запрос на выбор из нашей базы данных и ищем строки, где значение поля Name совпадает с названием компании, которую мы ищем. Запрос формируется с помощью % - форматирования строк.

А дальше передвигаясь по выбранным строкам, в самой первой выбирается поле Description и функция его возвращает, то есть возвращает описание данной компании.

Всё, функционал для нашего оконного приложения реализован.

# Интерфейс
А теперь немного об интерфейсе.

Здесь мы использовали следующие библиотеки: 
- tkinter;
- matplotlib.pyplot;
- pandas.

### ***Окно window***
![image](https://user-images.githubusercontent.com/99398012/170889332-ce221409-bca6-4872-8f45-8cf7982a3f3d.png)
Это основное окно, в котором осуществляется получение данных от пользователя. В нем есть две кладки - анализ акций и сравнение акций двух стран. На первой вкладке пользователь из выпадающего списка выбирает страну и тип, хранящиеся в списках **country** и **types** соответственно, и задает временной промежуток, за который изменяются акции. Кнокпа **Draw a grag** вызывает функцию **clicked1**, кнопка **Information abount companies** - **clicked3**. На следующей вкладке есть поле ввода для еще одной страны и ещё одна кнопка **Draw a grag**, которая, однако, вызывает функцию **clicked2**.

### ***Реализация функции clicked1***
В этой функции мы создаем табличную структуру данных **df**, по которой строим график. Суть в том, что мы вызваем функцию **info_stocks**, и по введенным пользователем данным получаем нужные нам компании для построения графика: 

![image](https://user-images.githubusercontent.com/99398012/170888646-ba309a36-62f4-47e3-8404-209eee363e61.png)

### ***Реализация функции clicked2***
Эта функция делает то же самое, что и предыдущая, с той разницей, что на ввод требуется две страны для дальнейшего сравнения их акций:

![image](https://user-images.githubusercontent.com/99398012/170888868-1f3349cc-5db5-4d7c-ac6e-fbe278071d5f.png)

Получив данные, мы строим графики: 

![image](https://user-images.githubusercontent.com/99398012/170888935-12838a05-38b7-4467-a72a-ed2e41ee896b.png)

И в заключение выпадает сообщение о том, акции какой страны выгоднее:
![image](https://user-images.githubusercontent.com/99398012/170888998-567786ce-c59f-42c3-a74f-46d3289b115a.png)

Для этого мы использовали функцию **compare_stocks**

### ***Реализация функции clicked3***
Данная функция выводит данные о компаниях, параметры которых задал пользователь. Здесь мы создаем окно, в котором благодаря **company_description** получаем информацию об интересующих пользователя компаниях: 

![image](https://user-images.githubusercontent.com/99398012/170889216-e0006e04-6035-4105-b44a-dc1a34cc2230.png)

Если пользователь неккоректно ввел дату, всплывает следующее сообщение с ошибкой:

![image](https://user-images.githubusercontent.com/99398012/170889284-07c19557-b156-4128-8fa8-72689ad13058.png)
