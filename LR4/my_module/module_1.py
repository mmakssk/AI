def first_function(x):
        index_first = -1
        index_last = -1
        length = 0
        max_len = 0
        end_index_first = -1
        end_index_last = -1
        target = False

        for i in range(len(x)):
            if x[i] == 0:
                if not target:
                    target = True
                    length = 1
                    index_first = i
                else:
                    length += 1
            else:
                target = False
                index_last = i
                if max_len < length:
                    max_len = length
                    end_index_first = index_first
                    end_index_last = index_last

        print('\nДовжина серії:',max_len, '\nІндекс першого елементу серії:' ,end_index_first, '\nІндекс останього елементу серії:' ,end_index_last)