def email_post(dep_list,email_list):
    all_room = sum(dep_list)
    room_dict = {i+1:[j for j in range(dep_list(i))] for i in range(len(dep_list))}
    for i in email_list:
        pass