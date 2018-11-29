from audit.backend import user_interactive
import sys,os



if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s4baoleiji.settings")
    import django
    django.setup() #手动注册app
    obj = user_interactive.UserShell(sys.argv)
    obj.start()