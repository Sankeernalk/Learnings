def first_run():
    import re
    f_part_out = open("C:\\Users\\611419222\\Documents\\project\\SRAP_performance_tuning\\sprint4\\57_box\\inbox_fttc_up_a_out.xml", 'a')
    with open('C:\\Users\\611419222\\Documents\\project\\SRAP_performance_tuning\\sprint4\\57_box\\inbox_fttc_up_a.xml') as f:
        f_read = f.readlines()
        for i in f_read:
            if re.match(r'^.*\btitle\b.*$', i):
                pass
            else:
                f_part_out.write(i)


def second_run():
    import re
    f_out = open("C:\\Users\\611419222\\Documents\\project\\SRAP_performance_tuning\\sprint4\\57_box\\inbox_fttc_up_a_rep_out.xml", 'a')
    with open("C:\\Users\\611419222\\Documents\\project\\SRAP_performance_tuning\\sprint4\\57_box\\inbox_fttc_up_a_out.xml") as f:
        f_read = f.readlines()
        for i in f_read:
            if re.match(r'^.*\balias\b.*$',i):
                f_out.write(i)
                f_out.write((re.sub("[\(\[].*?[\)\]]", "",(i.replace('alias','title')).replace('Fttc Up A ',''))))
            else:
                f_out.write(i)
    f_out.close()


first_run()
second_run()