

def prepare_disconnect(strategy, user, name, user_storage,
                       association_id=None, *args, **kwargs):
    print("I'm fine with disconnecting user {}".format(user))


def cleanup_after_disconnect(strategy, user, name, user_storage,
                       association_id=None, *args, **kwargs):
    if user and user.social_auth.count() == 0:
        print("I'm deleting user {} as he can't log in with us".format(user))
        user.delete()
