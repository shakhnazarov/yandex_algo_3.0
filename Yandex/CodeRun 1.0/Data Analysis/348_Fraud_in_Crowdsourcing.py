import random

def flip(prob=0.5):
    return random.random() < prob

def check_ans(k, N, trials):
    if flip(k/N):
        trials.append(True)
    else:
        trials.append(False)


def simulation(k):
    N = 100
    trials = []
    for i in range(10):
        check_ans(k, N, trials)
        if trials[-1] == True:
            k -= 1
        N -= 1
    if sum(trials) < 7:
        return True

    for j in range(3):
        for i in range(5):
            check_ans(k, N, trials)
            if trials[-1] == True:
                k -= 1
            N -= 1
        if sum(trials[-10:]) < 7:
            return True
    return False


num_sim = 10000
draws = [0 for _ in range(101)]
for i in range(num_sim):
    for k in range(101):
        draws[k] += simulation(k)

for i in range(101):
    print(i, draws[i]/num_sim)
# ans: 68




"""
Одним из популярных способов разметки данных является краудсорсинг. Краудсорсинговые платформы, такие как Toloka, позволяют заказчикам размещать задания по разметке данных, а исполнителям выполнять эти задания за вознаграждение от заказчика.

Довольно распространенный тип краудсорсинговых заданий — бинарная классификация изображений, где исполнителю нужно выбрать один из двух вариантов, например, указать, есть ли на картинке котик.

Один из заказчиков решил использовать для борьбы с недобросовестными исполнителями (фродерами) механизм контрольных заданий. На каждую страницу с заданиями добавляется одно контрольное задание, для которого известен правильный ответ. Ответы исполнителя на такие задания сравниваются с эталонными, после чего исполнитель может быть заблокирован, если его ответы не будут соответствовать правилу контроля качества.

Заказчик настроил следующее правило контроля качества:

Если среди первых 10 ответов на контрольные задания более 30% неверных, исполнитель блокируется.
Далее после каждых новых 5 контрольных ответов выбираются 10 последних контрольных ответов исполнителя, и если среди них более 30% неверных, исполнитель блокируется.
В каждом задании заказчика можно дать один из двух ответов: «Да» или «Нет». Заказчик готовит набор из 100 контрольных заданий. Каждый раз, когда исполнителю нужно будет показать контрольное задание, оно будет случайно равновероятно выбираться из тех контрольных заданий, которые исполнитель еще не выполнял.

Какое наибольшее число контрольных заданий с эталонным ответом «Да» может быть в подготовленном наборе контрольных заданий, чтобы фродер, всегда отвечающий «Да», с вероятностью не менее 80% был заблокирован после выполнения не более 25 контрольных заданий?"""