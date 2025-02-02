'''
Bayes probability
'''






















"""
A. Срок задачи
Василий Иванович - тимлид команды разработки в компании RuCoding. К нему регулярно приходят менеджеры из других команд и просят сделать ту или иную задачу. И, конечно, они интересуются, успеет ли команда сделать задачу за N дней.

Василий Иванович перепробовал самые разные техники для оценки задач, и ни одна из них его так и не устроила.

Глава команды был уже близок к отчаянию, но он заметил интересный факт: на протяжении нескольких лет практически все задачи выполнялись не дольше 100 дней после начала разработки.

Василий Иванович понял, что теперь он может легко и быстро оценить любую новую задачу. Он смекнул, что если посчитать в процентах, сколько задач выполнилось за X дней, то он сможет называть этот процент менеджерам. Например, за 10 дней команда сделает задачу с вероятностью 11%, а за 41 день — с вероятностью 68%.

Чтобы не считать вероятность каждый раз, аналитики из команды подготовили специальную таблицу и теперь Василию Ивановичу достаточно посмотреть в неё, чтобы дать ответ.

Жизнь Василия Ивановича заиграла новыми красками. Оценка задач стала невероятно проста, а точность предсказаний повысилась в разы.

Однако сегодня к вашему начальнику пришёл топ-менеджер и поинтересовался, успеет ли команда сделать его задачу в оговоренные сроки? Команда уже начала разработку, но поскольку задача объёмная, в данный момент неизвестно, когда задачу точно закончат.

У тимлида нет времени, чтобы провести подробный анализ хода работ, поэтому он хочет воспользоваться своей таблицей. Вот только он пока не придумал как.

Помогите вашему начальнику справиться с данной задачей.

Формат ввода
Вы знаете, что Василий Иванович обещал справиться с задачей за 51 день, а с момента начала разработки прошло уже 7 дней.

Также вам известна таблица с процентом выполненных задач за X дней. Для краткости приведены только некоторые значения.

Количество прошедших дней	…	7	…	51	…	100	> 100
Процент выполненных задач	…	7%	…	72%	…	99.99%	100%
Формат вывода
Единственное число — процент уверенности, что задача будет выполнена в срок, с учётом прошедших 7 дней. При необходимости округлите ответ до целого.

Примечания
Вы можете воспринимать таблицу как функцию распределения дискретной случайной величины.
"""
