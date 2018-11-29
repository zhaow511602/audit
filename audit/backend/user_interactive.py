from django.contrib.auth import authenticate


class UserShell(object):
    def __init__(self,sys_argv):
        self.sys_argv = sys_argv
        self.user = None
    def auth(self):
        count = 0
        while count < 3:
            username = input("username:").strip()
            password = input("password:").strip()
            user = authenticate(username=username,password=password)
            if not user:
                count +=1
                print("Invalid username or password")
            else:
                self.user = user
                return True
        else:
            print("too many attempts")

    def start(self):
        if self.auth():
            host_group_list = self.user.account.host_group.all()
            while True:
                for id,group in enumerate(host_group_list):
                    count = group.host_user_binds.count()
                    print("%s\t%s[%s]"%(id,group,count))
                id = len(host_group_list)
                print("%s\t未分组[%s]" % (id,len(self.user.account.host.all())))
                choice_id = input("请输入组id:")
                if choice_id.isdigit():
                    choice_id = int(choice_id)
                    if choice_id >=0 and choice_id <len(host_group_list):
                        choice = host_group_list[choice_id]
                        host_list = choice.host_user_binds.all()
                    elif choice_id == len(host_group_list):
                        host_list = self.user.account.host.all()
                    else:
                        host_list = None
                        break
                    while True:
                        for id,host in enumerate(host_list):
                            print("%s\t%s:%s-%s" % (id,host.host.ip_addr,host.host_user.username,host.host_user.password))
                        choice_id = input("请输入host_id:")
                        if choice_id.isdigit():
                            choice_id = int(choice_id)
                            choice = host_list[choice_id]
                            print(choice)
                        elif choice_id == 'b':
                            break