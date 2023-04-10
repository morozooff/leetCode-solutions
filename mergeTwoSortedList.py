
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    #создаем два листа
    # пустышка ссылактся на начало списка
    # с помощью tail будем редактировать элементы списка
    dummy = tail = ListNode(0)
    # пока не дошли до конца хотя бы одного листа выполняем цикл
    while list1 and list2:
        #если знчение первого больше
        if list1.val < list2.val:
            #в выходной список сохраняем элемент первого листа
            tail.next = list1
            # передвигаем указатель на элемент первого листа следующий
            list1 = list1.next
        # иначе
        else:
            # в выходной список сохраняем элемент второго листа
            tail.next = list2
            # передвигаем указатель на элемент второго листа следующий
            list2 = list2.next
        # передвигаем указатель на выходной жлемент вперед
        tail = tail.next
    # заканчиваем заполнение выходного списка
    tail.next = list1 or list2

    return dummy.next

print(mergeTwoLists(list1, list2))